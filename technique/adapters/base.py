from abc import ABC, abstractmethod


class QuoteProvider(ABC):
    @abstractmethod
    def generate_quote(self, prompt: str, config: dict) -> str:
        """Generate a quote JSON string from prompt/config."""
