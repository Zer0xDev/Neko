from openai import OpenAI

class chat:
    def create(prompt: str, key: str, model: str) -> str:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=key
        )

        completion = client.chat.completions.create(
            model="google/gemini-2.0-flash-001",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )

        return completion.choices[0].message.content
