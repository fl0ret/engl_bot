from openai import OpenAI
from config import AI_TOKEN

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=AI_TOKEN
)

def chat_with_ai(prompt: str) -> str:
    completion = client.chat.completions.create(
        model="deepseek/deepseek-chat:free",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content.strip()

async def ask_ai(message: str, system_prompt: str) -> str:
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat:free",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content.strip()



