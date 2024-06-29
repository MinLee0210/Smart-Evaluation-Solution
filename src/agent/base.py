from abc import ABC
from typing import Union, Any
from PIL import Image

class BaseAgent(ABC): 
    def __init__(self, api_key:str, model_name:str, temperature:Union[float, None]=None, max_token:Union[int, None]=1024, system_prompt:Union[str, None]=None, **kwargs): 
        ...

    def set_model(self, model_name: str): 
        ...

    def get_model(self, model_name: str) -> str: 
        ...

    def invoke(self, prompt:str, image:Image=None, stream:bool=False, **kwargs): 
        ...