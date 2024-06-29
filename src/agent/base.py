from abc import ABC

class BaseAgent(ABC): 
    def __init__(self, api_key, model_name, temperature, system_prompt, kwargs): 
        ...