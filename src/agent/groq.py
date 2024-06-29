import os
from typing import Optional

try:
    from groq import Groq
except ImportError:
    raise ValueError(
        "Groq is not installed. Please install it with "
        "`pip install 'groq'`."
    )

from pydantic import Field


class GroqAgent: 
    model_name: str = Field(
        default="llama3-8b-8192", description="You can choose any LLMs that the Groq supports."
    )

    def __init__(self, 
                api_key: Optional[str]=None, 
                model_name: Optional[str]="llama3-8b-8192"): 
        self.model_name = model_name
        self._model = Groq(api_key=api_key or os.environ["GROQ_API_KEY"],
                        max_retries=5)        

    def chat(self, prompt): 
        usr_msg = {"role": "user", 
                   "content": prompt}
        messages = [usr_msg]
        try: 
            chat_completion = self._model.chat.completions.create(messages=messages, 
                                                                  model=self.model_name)
            return chat_completion.choices[0].message.content
        except: 
            raise Exception("Failed to send request to Groq.")