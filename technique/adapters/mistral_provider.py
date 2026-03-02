from mistralai import Mistral

from adapters.base import QuoteProvider


class MistralProvider(QuoteProvider):
    def generate_quote(self, prompt: str, config: dict) -> str:
        api_key = config.get("mistral_api_key")
        if not api_key:
            raise ValueError("MISTRAL_API_KEY manquante pour le provider Mistral.")

        client = Mistral(api_key=api_key)
        response = client.chat.complete(
            model=config.get("model", "mistral-small-latest"),
            messages=[{"role": "user", "content": prompt}],
            temperature=config.get("temperature", 0),
        )
        return response.choices[0].message.content or ""
