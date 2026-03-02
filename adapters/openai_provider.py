from openai import OpenAI

from adapters.base import QuoteProvider


class OpenAIProvider(QuoteProvider):
    def generate_quote(self, prompt: str, config: dict) -> str:
        api_key = config.get("api_key")
        if not api_key:
            raise ValueError("OPENAI_API_KEY manquante pour le provider OpenAI.")

        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=config.get("model", "gpt-4o-mini"),
            messages=[{"role": "user", "content": prompt}],
            temperature=config.get("temperature", 0),
        )
        return response.choices[0].message.content or ""
