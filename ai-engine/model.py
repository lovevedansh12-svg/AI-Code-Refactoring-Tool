import os
from openai import OpenAI


class AIModel:

    def generate(self, prompt):
        raise NotImplementedError


class OpenAIModel(AIModel):

    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY")
        )

    def generate(self, prompt):

        response = self.client.responses.create(
            model=os.environ.get("OPENAI_MODEL", "gpt-5.6-luna"),
            input=prompt
        )

        return response.output_text
