from dataclasses import dataclass
from typing import Any, List, Dict, Optional, Union, Tuple
from PIL import Image

import cv2
import numpy as np
import matplotlib.pyplot as plt
import torch
from transformers import (AutoProcessor, AutoModelForZeroShotObjectDetection, 
                          pipeline)

from src.agent.constants import PREDEFINED_CLASS

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model_id = "IDEA-Research/grounding-dino-tiny"

@dataclass
class BoundingBox:
    xmin: int
    ymin: int
    xmax: int
    ymax: int

    @property
    def xyxy(self) -> List[float]:
        return [self.xmin, self.ymin, self.xmax, self.ymax]

@dataclass
class DetectionResult:
    score: float
    label: str
    box: BoundingBox
    mask: Optional[np.array] = None

    @classmethod
    def from_dict(cls, detection_dict: Dict) -> 'DetectionResult':
        return cls(score=detection_dict['score'],
                   label=detection_dict['label'],
                   box=BoundingBox(xmin=detection_dict['box']['xmin'],
                                   ymin=detection_dict['box']['ymin'],
                                   xmax=detection_dict['box']['xmax'],
                                   ymax=detection_dict['box']['ymax']))
    
def annotate(image: Union[Image.Image, np.ndarray], detection_results: List[DetectionResult]) -> np.ndarray:
    # Convert PIL Image to OpenCV format
    image_cv2 = np.array(image) if isinstance(image, Image.Image) else image
    image_cv2 = cv2.cvtColor(image_cv2, cv2.COLOR_RGB2BGR)

    # Iterate over detections and add bounding boxes and masks
    for detection in detection_results:
        label = detection.label
        score = detection.score
        box = detection.box
        mask = detection.mask

        # Sample a random color for each detection
        color = np.random.randint(0, 256, size=3)

        # Draw bounding box
        cv2.rectangle(image_cv2, (box.xmin, box.ymin), (box.xmax, box.ymax), color.tolist(), 2)
        cv2.putText(image_cv2, f'{label}: {score:.2f}', (box.xmin, box.ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color.tolist(), 2)

        # If mask is available, apply it
        if mask is not None:
            # Convert mask to uint8
            mask_uint8 = (mask * 255).astype(np.uint8)
            contours, _ = cv2.findContours(mask_uint8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(image_cv2, contours, -1, color.tolist(), 2)

    return cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)

def plot_detections(
    image: Union[Image.Image, np.ndarray],
    detections: List[DetectionResult],
    save_name: Optional[str] = None
) -> None:
    annotated_image = annotate(image, detections)
    plt.imshow(annotated_image)
    plt.axis('off')
    if save_name:
        plt.savefig(save_name, bbox_inches='tight')
    plt.show()

class ObjectDectector: 
    def __init__(self, model_id, device:Union[str, None]=device, **kwargs): 
        self.model, self.processor = self.__set_model(model_id=model_id, 
                                                      device=device)

    def __set_model(self, model_id, device, **kwargs):
        dn_processor = AutoProcessor.from_pretrained(model_id)
        dn_model = AutoModelForZeroShotObjectDetection.from_pretrained(model_id).to(device)
        return dn_model, dn_processor
    
    def __get_model(self): 
        return f"More details refer to https://github.com/IDEA-Research/GroundingDINO.git"

    def __call__(self, image): 
        self.invoke(image=image)

    def invoke(self, 
        image: Image.Image,
        labels: List[str]=PREDEFINED_CLASS.strip().split(),
        threshold: float = 0.42,
        detector_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Use Grounding DINO to detect a set of labels in an image in a zero-shot fashion.
        """
        device = "cuda" if torch.cuda.is_available() else "cpu"
        detector_id = detector_id if detector_id is not None else "IDEA-Research/grounding-dino-tiny"
        object_detector = pipeline(model=detector_id, task="zero-shot-object-detection", device=device)

        labels = [label if label.endswith(".") else label+"." for label in labels]

        results = object_detector(image,
                                candidate_labels=labels,
                                threshold=threshold)
        results = [DetectionResult.from_dict(result) for result in results]

        return results