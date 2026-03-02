import requests

from adapters.base import QuoteProvider


class OllamaProvider(QuoteProvider):
    def generate_quote(self, prompt: str, config: dict) -> str:
        base_url = config.get("ollama_base_url", "http://localhost:11434")
        payload = {
            "model": config.get("model", "llama3.1"),
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": config.get("temperature", 0)},
        }

        response = requests.post(f"{base_url}/api/generate", json=payload, timeout=120)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")
