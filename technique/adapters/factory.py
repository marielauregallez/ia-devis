from adapters.azure_openai_provider import AzureOpenAIProvider
from adapters.mistral_provider import MistralProvider
from adapters.ollama_provider import OllamaProvider
from adapters.openai_provider import OpenAIProvider


def build_provider(provider_name: str):
    normalized = (provider_name or "").strip().lower()
    providers = {
        "openai": OpenAIProvider,
        "azure": AzureOpenAIProvider,
        "mistral": MistralProvider,
        "ollama": OllamaProvider,
    }
    if normalized not in providers:
        allowed = ", ".join(sorted(providers.keys()))
        raise ValueError(f"Provider inconnu '{provider_name}'. Choisir parmi: {allowed}.")
    return providers[normalized]()
