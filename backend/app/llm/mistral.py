from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from app.llm.base import BaseLLM
from app.core.config import settings

class MistralLLM(BaseLLM):
    def __init__(self):
        self.client=MistralClient(api_key=settings.MISTRAL_API_KEY)
        self.model=settings.MODEL_NAME

    def generate(self,prompt:str)->str:
        messages=[ChatMessage(role="user",content=prompt)]

        response=self.client.chat(
            model=self.model,
            messages=messages
        )
        return response.choices[0].message.content
    
