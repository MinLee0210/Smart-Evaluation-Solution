from PIL import Image

from paddleocr import PaddleOCR, draw_ocr
from fuzzywuzzy import fuzz, process

import numpy as np

from constants import keywords

class OCRAgent: 
    def __init__(self): 
        self.model = self.__set_model()

    def __set_model(self): 
        model = ocr = PaddleOCR(use_angle_cls=True, lang='en')  # Need to run only once to download and load model into memory
        return model
    
    def __get_model(self): 
        return f"Details refer to https://github.com/PaddlePaddle/PaddleOCR.git"
    
    def __call__(self, image): 
        self.invoke(image=image)

    def invoke(self, image, keywords=keywords): 
        if not isinstance(image, (np.ndarray, list, str, bytes)) and isinstance(image, Image.Image):
            image = np.asarray(image)

        # Run OCR on the image
        result = self.model.ocr(image, cls=True)
        text = {}
        if result and result[0]:
            extracted_text = ' '.join([line[1][0] for line in result[0]])
            # print(f"Extracted Text from {image_path}:", extracted_text)
            text['extracted-text'] = extracted_text
            # Map the extracted text to closest keywords
            mapped_text = self._map_to_closest_keyword(extracted_text, keywords)
            # print(f"Mapped Text from {image_path}:", mapped_text)
            text['closest-words'] = mapped_text
            # Count keywords in the mapped text
            keyword_counts = self._count_keywords(mapped_text, keywords)
            # print(f"Keyword Counts from {image_path}:", keyword_counts)
            text['word-counts'] = keyword_counts
            # Append the counts to the results list
        return result, text
    
    # Function to map extracted text to closest keywords using fuzzy matching

    def _map_to_closest_keyword(self, text, keywords):
        words = text.split()
        mapped_words = []
        for word in words:
            match, score = process.extractOne(word.lower(), keywords, scorer=fuzz.token_sort_ratio)
            if score > 80:  # Threshold to consider a match (adjustable)
                mapped_words.append(match)
        return ' '.join(mapped_words)

    # Function to count keyword occurrences
    def _count_keywords(self, text, keywords):
        keyword_counts = {keyword: text.lower().split().count(keyword) for keyword in keywords}
        return keyword_counts