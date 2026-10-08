import requests

from bs4 import BeautifulSoup

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


CHROMA_DIR = "./chroma_db"

EMBEDDING_MODEL = "nomic-embed-text"


URLS = [
    "https://www.gov.uk/skilled-worker-visa",
    "https://www.gov.uk/health-care-worker-visa",
    "https://www.gov.uk/global-talent",
    "https://www.gov.uk/youth-mobility",
]


def download_page(url):
    response = requests.get(
        url,
        timeout=30,
        headers={
            "User-Agent": "VisaPath/1.0"
        },
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    main = soup.find("main")

    if main:
        text = main.get_text(
            separator="\n",
            strip=True
        )
    else:
        text = soup.get_text(
            separator="\n",
            strip=True
        )

    return text


def build_documents():
    documents = []

    for url in URLS:
        print(f"Downloading: {url}")

        try:
            text = download_page(url)

            document = Document(
                page_content=text,
                metadata={
                    "source": url
                }
            )

            documents.append(document)

            print("Downloaded successfully.")

        except Exception as e:
            print(f"Failed to download {url}")
            print(e)

    return documents


def create_vector_database():
    documents = build_documents()

    if not documents:
        print("No documents were downloaded.")
        return

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)

    print()
    print(f"Created {len(chunks)} document chunks.")
    print()

    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )

    print("Creating vector database...")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
        collection_name="visapath"
    )

    print()
    print("===================================")
    print("      RAG Database Created")
    print("===================================")
    print()
    print(f"Documents: {len(documents)}")
    print(f"Chunks: {len(chunks)}")
    print(f"Database: {CHROMA_DIR}")
    print()


if __name__ == "__main__":
    create_vector_database()

