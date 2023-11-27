import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions


openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    model_name="text-embedding-ada-002", api_key='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'
)

client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet",
                                  persist_directory="db/"
                                  ))


def create_collection(id):
    client.create_collection(name=id)
    client.persist()


def insert_data(id, content, metadata):
    collection = client.get_collection(
        name=id, embedding_function=openai_ef)
    print(collection.count())
    collection.add(documents=[content], metadatas=[
                   {'source': metadata}], ids=[str(collection.count() + 1)])
    client.persist()


def query_data(id, query_text):
    collection = client.get_collection(name=id, embedding_function=openai_ef)
    results = collection.query(query_texts=[query_text], n_results=1)
    return results
