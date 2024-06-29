import os
from typing import Any, Dict, List

try:
    import google.generativeai as genai
except ImportError:
    raise ValueError(
        "Gemini is not installed. Please install it with "
        "`pip install 'google-generativeai'`."
    )
from google.generativeai.types import HarmCategory, HarmBlockThreshold


from src.agent.constants import DEFAULT_CANDIDATE_COUNT, DEFAULT_NUM_OUTPUTS, DEFAULT_TEMPERATURE, DEFAULT_TOP_K, DEFAULT_TOP_P, VisionAnswer
from src.agent.base import BaseAgent

#    "max_output_tokens": DEFAULT_NUM_OUTPUTS, 

_generation_config = {
    "candidate_count": DEFAULT_CANDIDATE_COUNT, 
    "temperature": DEFAULT_TEMPERATURE, 
    "top_k": DEFAULT_TOP_K, 
    "top_p": DEFAULT_TOP_P, 
    "response_mime_type": "application/json"
}

# https://ai.google.dev/api/python/google/generativeai/protos/HarmCategory
_safety_setting = {
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
}

GEMINI_MODELS = {
        "gemini-1.0-pro": "models/gemini-1.0-pro", 
        "gemini-1.0-pro-001": "models/gemini-1.0-pro-001", 
        "gemini-1.0-pro-latest": "models/gemini-1.0-pro-latest", 
        "gemini-1.5-pro": "models/gemini-1.5-pro", 
        "gemini-1.5-pro-001": "models/gemini-1.5-pro-001", 
        "gemini-1.5-pro-latest": "models/gemini-1.5-pro-latest", 
        "gemini-1.5-flash": "models/gemini-1.5-flash", 
        "gemini-1.5-flash-001": "models/gemini-1.5-flash-001", 
        "gemini-1.5-flash-latest": "models/gemini-1.5-flash-latest", 
        "gemini-pro": "models/gemini-pro", 
    }

class GeminiAgent(BaseAgent):

    def __init__(self, 
                api_key,
                model_name="gemini-1.5-flash",
                system_prompt=None,
                ): 
        super().__init__(api_key, model_name, system_prompt)
        self.config_params: Dict[str, Any] = {
            "api_key": api_key or os.getenv("GOOGLE_API_KEY"),
        }
        self.model = self.set_model(model_name=model_name)
        self._model_meta = genai.get_model(self.get_model(model_name))

        if system_prompt: 
            self.system_prompt = {"role": "system", 
                                  "parts": [system_prompt]}
            
        supported_methods = self._model_meta.supported_generation_methods
        if "generateContent" not in supported_methods:
            raise ValueError(
                f"Model {model_name} does not support content generation, only "
                f"{supported_methods}."
            )

    def set_model(self, model_name):
        model_name = self.get_model(model_name)
        genai.configure(**self.config_params)
        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=_generation_config,
            safety_settings=_safety_setting,
        )
        return model
    
    def get_model(self, model_name):
        return GEMINI_MODELS[model_name]

    def list_model(self) -> dict: 
        return GEMINI_MODELS
    
    def model_meta(self): 
        return self._model_meta
    
    def invoke(self, prompt, image, stream=False): 
        messages = []
        user_msg = {
            "role": "user", 
            "parts": [prompt, image]
        }
        if hasattr(self, "system_prompt"): 
            messages.append(self.system_prompt)
        else: 
            messages.append(user_msg)

        try: 
            response = self.model.generate_content(messages, stream=stream)
            return response
        except: 
            raise Exception("Failed to send request to Gemini")