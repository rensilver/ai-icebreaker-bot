"""Module for interfacing with IBM watsonx.ai LLMs."""

import logging

from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

from ai_icebreaker_bot.config import settings

logger = logging.getLogger(__name__)

def create_nomic_embedding() -> OllamaEmbedding:
    """Creates an Ollama Nomic Embedding model for vector representation.
    
    Returns:
        OllamaEmbedding model.
    """
    embed_model = OllamaEmbedding(
        model_name=settings.EMBEDDING_MODEL,
        base_url=settings.OLLAMA_BASE_URL
    )
    logger.info(f"Created Nomic Embedding model: {settings.EMBEDDING_MODEL}")
    return embed_model

def create_llama_llm(
    temperature: float = settings.TEMPERATURE,
    num_predict: int = settings.MAX_NEW_TOKENS
) -> Ollama:
    """Creates an Ollama Llama 3.2 LLM for generating responses.
    
    Args:
        temperature: Temperature for controlling randomness in generation (0.0 to 1.0).
        max_new_tokens: Maximum number of new tokens to generate.
        decoding_method: Decoding method to use (sample, greedy).
        
    Returns:
        Llama 3.2 model.
    """
    additional_params = {
        "top_k": settings.TOP_K,
        "top_p": settings.TOP_P,
        "options": {"num_ctx": 4096}
    }

    llama_llm = Ollama(
        model=settings.LLM_MODEL,
        base_url=settings.OLLAMA_BASE_URL,
        temperature=temperature,
        num_predict=num_predict,
        request_timeout=120.0,
        context_window=4096,
        additional_kwargs=additional_params
    )
    logger.info(f"Created Llama 3.2 LLM model: {settings.LLM_MODEL}")
    return llama_llm

def change_llm_model(new_model_id: str) -> None:
    """Change the LLM model to use.
    
    Args:
        new_model_id: New LLM model ID to use.
    """
    global config
    config.LLM_MODEL_ID = new_model_id
    logger.info(f"Changed LLM model to: {new_model_id}")