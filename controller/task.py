import os
from PIL import Image

from src.agent.classification import ObjectClassificator
from src.agent.detection import ObjectDectector, annotate
from src.agent.text_ocr import OCRAgent
from src.agent.llm import GroqAgent, GeminiAgent

from src.agent.constants import keywords, CONTEXT

GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

groq_agent = GroqAgent(api_key=GroqAgent)
gemini_agent = GeminiAgent(api_key=GEMINI_API_KEY)

detector = ObjectDectector()
classificator = ObjectClassificator()
ocr_agent = OCRAgent()

def get_annotate_image(images): 
    imgs = Image.fromarray(images)
    return imgs

def analyze_image_information(model, 
                              image_context, 
                              image_detection, 
                              image_ocr):
    prompt = f"""
    You are given information that are extracted from a party or a place in which 
    people consume their meal. The information consists of the following parts:

    Image OCR: 
    {image_ocr}

    Image Detection: 
    {image_detection}

    Image Context: 
    {image_context}

    The answer must follow these question: 
    1. Counting Heineken Drinkers: Distinguish between those drinking Heineken and other beer brands.
    2. Heineken Event Success Evaluation: Count the number of participants attending the Heineken event at the restaurant in the images.
    3. Heineken Sales Rep Tracking: Analyze the extracted information from the image to identify objects or features consistent with Heineken sales representatives (keywords like uniform,logo,name tag).
    4. Heineken In-Store Presence Evaluation: Count the number of Heineken beer cases in stock and confirm there are at least 10. Analyze the extracted information from the image to identify objects consistent with Heineken branding (keywords like signboard,standee,beer case, presence of the Heineken logo)

    Try to answer it in the most creative and friendly way. You must give some insights based on those information and give a solution to improve Heineken marketing campaign.
    Answers: 
    """
    chat_completion = model.chat(prompt)
    return chat_completion

def ses_pipeline(image, 
             context=CONTEXT,
             keywords=keywords): 
    
    # Extract text from Image via OCR
    image_ocr = ocr_agent.invoke(image, keywords)

    # Extract context of 
    (max_value, max_index, img_context) = classificator.invoke(image, context, return_max_context=True)

    detections = detector.invoke(image=image)
    
    detected_obj = list(set([dt_res.label for dt_res in detections]))

    insight = analyze_image_information(model=gemini_agent, 
                                    image_context=img_context,
                                    image_detection = detected_obj, 
                                    image_ocr=image_ocr)
    return {'detections': detections, 
            'detected_obj': detected_obj, 
            'image_ocr': image_ocr, 
            'image_context': img_context,
            'insight': insight}