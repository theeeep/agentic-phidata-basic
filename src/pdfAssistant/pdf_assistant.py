import typer
from typing import Optional, List
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
db_url = os.getenv("DATABASE_URL")

# Create a knowledge base with the PDF documents
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector2(
        db_url=db_url,
        collection="pdf_documents",
    ),
)

# Load the knowledge base
knowledge_base.load(recreate=True, upsert=True)

storage = PgAssistantStorage(table_name="pdf_assistant", db_url=db_url)


def create_pdf_assistant(new: bool = False, user: str = "user"):
    run_id: Optional[str] = None
    if not new:
        existing_run_ids: List[str] = storage.get_all_run_ids(user)
        if len(existing_run_ids) > 0:
            run_id = existing_run_ids[0]
    assistant = Assistant(
        run_id=run_id,
        user_id=user,
        knowledge_base=knowledge_base,
        storage=storage,
        show_tool_calls=True,  # show tool calls in the response
        # Enable the assistant to search the knowledge base and read chat history
        search_knowledge=True,
        read_chat_history=True,
    )
    if run_id is None:
        run_id = assistant.run_id
        print(f"Starting new run id: {run_id}")
    else:
        print(f"Resuming run id: {run_id}")
    assistant.cli_app(markdown=True)


if __name__ == "__main__":
    typer.run(create_pdf_assistant)
