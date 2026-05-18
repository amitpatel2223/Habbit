from fastapi import APIRouter, Depends, HTTPException
from schemas.chat import ChatRequest
from ai.embeddings import create_embedding
from ai.vector_store import collection
from ai.chatbot import generate_response

router = APIRouter(prefix="/assistant", tags=["Assistant"])


@router.post("/chat")
def chat(request: ChatRequest):

    question = request.question

    query_embedding = create_embedding(
        question
    )

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=3
    )
    #print(f"Results: {results}")
    documents = results["documents"][0]
    #print(f"Documents: {documents}")

    context = "\n".join(documents)

    answer = generate_response(
        question,
        context
    )

    return {
        "question": question,
        "context": context,
        "answer": answer
    }