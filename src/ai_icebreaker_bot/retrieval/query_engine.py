"""Module for querying indexed LinkedIn profile data."""

import logging
from typing import Any, Dict, Optional

from llama_index.core import VectorStoreIndex, PromptTemplate

from ai_icebreaker_bot.llm.llm_interface import create_llama_llm
from ai_icebreaker_bot.config import settings

logger = logging.getLogger(__name__)

def generate_initial_facts(index: VectorStoreIndex) -> str:
    """Generates interesting facts about the person's career or education.
    
    Args:
        index: VectorStoreIndex containing the LinkedIn profile data.
        
    Returns:
        String containing interesting facts about the person.
    """
    try:
        # Creating LLM for generating facts
        llama_llm = create_llama_llm(
            temperature=0.0,
            num_predict=500
        )

        # Create prompt template
        facts_prompt = PromptTemplate(template=settings.INITIAL_FACTS_TEMPLATE)

        # Create query engine
        query_engine = index.as_query_engine(
            streaming=False,
            similarity_top_k=settings.SIMILARITY_TOP_K,
            llm=llama_llm,
            text_qa_template=facts_prompt
        )

        # Execute the query
        query = "Provide three interesting facts about this person\'s career or education"
        response = query_engine.query(query)

        return response.response
    except Exception as e:
        logger.error(f"Error in generate_initial_facts: {e}")
        return "Failed to generate initial facts."

def answer_user_query(index: VectorStoreIndex, user_query: str) -> Any:
    """Answers the user's question using the vector database and the LLM.
    
    Args:
        index: VectorStoreIndex containing the LinkedIn profile data.
        user_query: The user's question.
        
    Returns:
        Response object containing the answer to the user's question.
    """
    try:
        # Create LLM for answering questions
        llama_llm = create_llama_llm(
            temperature=0.0,
            num_predict=250
        )

        # Create prompt template
        question_prompt = PromptTemplate(template=settings.USER_QUESTION_TEMPLATE)

        # Create query engine
        query_engine = index.as_query_engine(
            streaming=False,
            similarity_top_k=settings.SIMILARITY_TOP_K,
            llm=llama_llm,
            text_qa_template=question_prompt
        )

        # Execute the query
        answer = query_engine.query(user_query)
        return answer
    except Exception as e:
        logger.error(f"Error in answer_user_query: {e}")
        return "Failed to get an answer."