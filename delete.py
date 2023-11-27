
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions


openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    model_name="text-embedding-ada-002", api_key='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'
)

client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet",
                                  persist_directory="db/"
                                  ))


collection = client.get_collection(name='researcher')

# Assume you have a Chroma instance `chroma_instance` and the source document `source_doc

ids = collection.get(where={'source': 'researcher'})['ids']
collection.delete(ids=ids)
client.persist()

collection = client.get_collection(name='student1')

# Assume you have a Chroma instance `chroma_instance` and the source document `source_doc

ids = collection.get(where={'source': 'student1'})['ids']
collection.delete(ids=ids)
client.persist()

collection = client.get_collection(name='student2')

# Assume you have a Chroma instance `chroma_instance` and the source document `source_doc

ids = collection.get(where={'source': 'student2'})['ids']
collection.delete(ids=ids)
client.persist()
