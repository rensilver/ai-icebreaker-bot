import os
from dataclasses import dataclass

@dataclass
class Settings:
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "llama3.2:3b")
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
    MOCK_DATA_URL: str = os.getenv("MOCK_DATA_URL", "https://raw.githubusercontent.com/rensilver/datasets/69a11fcf8e5381f7c428f66abd58c98f80e8eb53/linkedin_profile_data.json")
    PROXYCURL_API_KEY: str = os.getenv("PROXYCURL_API_KEY", "")
    SIMILARITY_TOP_K: int = int(os.getenv("SIMILARITY_TOP_K", 5))
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", 0.0))
    MAX_NEW_TOKENS: int = int(os.getenv("MAX_NEW_TOKENS", 500))
    MIN_NEW_TOKENS: int = int(os.getenv("MIN_NEW_TOKENS", 1))
    TOP_K: int = int(os.getenv("TOP_K", 50))
    TOP_P: int = int(os.getenv("TOP_P", 1))
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", 400))
    INITIAL_FACTS_TEMPLATE: str = os.getenv("INITIAL_FACTS_TEMPLATE", """
        You are an AI assistant that provides detailed answers based on the provided context.

        Context information is below:

        {context_str}

        Based on the context provided, list 3 interesting facts about this person's career or education.

        Answer in detail, using only the information provided in the context.
    """)
    USER_QUESTION_TEMPLATE: str = os.getenv("USER_QUESTION_TEMPLATE", """
        You are an AI assistant that provides detailed answers to questions based on the provided context.

        Context information is below:

        {context_str}

        Question: {query_str}

        Answer in full details, using only the information provided in the context. If the answer is not available in the context, say "I don't know. The information is not available on the LinkedIn page."
    """)

settings = Settings()