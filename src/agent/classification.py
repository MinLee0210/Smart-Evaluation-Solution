import clip
import torch

from constants import CONTEXT

device = 'cuda' if torch.cuda.is_available() else 'cpu'

class ObjectClassificator: 
    def __init__(self, model_id: str="ViT-B/32", device=device): 
        self.clip_model, self.clip_preprocessor = self.__set_model(model_id=model_id, 
                                                                   device=device)
        

    def __set_model(self, model_id, device): 
        clip_model, clip_preprocessor = clip.load(model_id, device=device)
        return  clip_model, clip_preprocessor
    
    def __get_model(self): 
        return f"We servce {clip.available_models()}.\nMore details refers to https://github.com/openai/CLIP.git"
    
    def __call__(self, image): 
        self.invoke(image=image)

    def invoke(self, image, context:list[str]=CONTEXT, return_max_context:bool=True): 
        img = self.clip_preprocessor(image).unsqueeze(0).to(device)
        text = clip.tokenize(context).to(device)
        with torch.no_grad():
            image_features = self.clip_model.encode_image(img)
            text_features = self.clip_model.encode_text(text)
            
            logits_per_image, logits_per_text = self.clip_model(img, text)
            probs = logits_per_image.softmax(dim=-1).cpu().numpy()

        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)
        similarity = text_features.cpu().numpy() @ image_features.cpu().numpy().T

        text_probs = (100.0 * image_features @ text_features.T).softmax(dim=-1)
        max_value, max_index = torch.max(text_probs, dim=1)
        if return_max_context: 
            return max_value, max_index, context[max_index]
        else: 
            return max_value, max_index, 