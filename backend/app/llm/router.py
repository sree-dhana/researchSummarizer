from app.llm.mistral import MistralLLM
from app.llm.ollama import OllamaLLM

class LLMRouter:
    def __init__(self):
        self.mistral=MistralLLM()
        self.Ollama=OllamaLLM()

    def get_reasoning_llm(self):
        return self.mistral
    
    def get_utility_llm(self):
        return self.ollamapy