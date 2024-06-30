import os
from PIL import Image

from src.agent.classification import ObjectClassificator
from src.agent.detection import ObjectDectector, annotate
from src.agent.text_ocr import OCRAgent
from src.agent.llm import GroqAgent, GeminiAgent

from src.agent.constants import keywords, CONTEXT,  PREDEFINED_CLASSES_BY_GROUP

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
                              image_ocr):
    prompt = f"""
    You are given information that are extracted from a party or a place in which
    people consume their meal. The information consists of context, the predefined label by us, the ocr infomation (only use words relating the beer branch: heineken, tiger, bia viet, larue, biniva, strongbow, edelweiss, ...):

    Image Context:
    {image_context}

    The Object could be appearend:
    {PREDEFINED_CLASSES_BY_GROUP[image_context]}

    Image OCR:
    {image_ocr}


    The answer must follow these question:
    1. Summary of product appearances for each brand as a table and review them
    2. Rate the frequency of heineken's appearance in that context.
    Answer:
    """
    chat_completion = model.chat(prompt)
    return chat_completion


def ses_pipeline(image,
                 context=CONTEXT,
                 keywords=keywords):

    # Extract text from Image via OCR
    image_ocr, ocr_text = ocr_agent.invoke(image, keywords)
    count_text = ocr_text['word-counts']

    # Extract context of
    (max_value, max_index, img_context) = classificator.invoke(
        image, context, return_max_context=True)

    # detections = detector.invoke(image=image, context=img_context)

    # detected_obj = list(set([dt_res.label for dt_res in detections]))

    insight = analyze_image_information(model=gemini_agent,
                                        image_context=img_context,
                                        image_ocr=image_ocr)
    return {'detections': 'detections',
            'detected_obj': 'detected_obj',
            'image_ocr': count_text,
            'image_context': img_context,
            'insight': insight}
