import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatGPT:
    def generate(self, question, context):
        prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{question}
"""

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content
