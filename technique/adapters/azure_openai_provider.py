from openai import AzureOpenAI

from adapters.base import QuoteProvider


class AzureOpenAIProvider(QuoteProvider):
    def generate_quote(self, prompt: str, config: dict) -> str:
        api_key = config.get("azure_api_key")
        endpoint = config.get("azure_endpoint")
        if not api_key or not endpoint:
            raise ValueError(
                "AZURE_OPENAI_API_KEY ou AZURE_OPENAI_ENDPOINT manquante pour Azure OpenAI."
            )

        client = AzureOpenAI(
            api_key=api_key,
            azure_endpoint=endpoint,
            api_version=config.get("azure_api_version", "2024-10-21"),
        )
        response = client.chat.completions.create(
            model=config.get("model", "gpt-4o-mini"),
            messages=[{"role": "user", "content": prompt}],
            temperature=config.get("temperature", 0),
        )
        return response.choices[0].message.content or ""
