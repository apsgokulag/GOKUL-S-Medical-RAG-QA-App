from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader, PyPDFLoader

# Initialize SentenceTransformerEmbeddings
embeddings = SentenceTransformerEmbeddings(model_name="NeuML/pubmedbert-base-embeddings")

# Setup Qdrant
url = "http://localhost:6333"
client = QdrantClient(url=url, prefer_grpc=False)
db = Qdrant(client=client, embeddings=embeddings, collection_name="vector_db")

# Load and process documents
loader = DirectoryLoader('data/', glob="**/*.pdf", show_progress=True, loader_cls=PyPDFLoader)
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

# Create Qdrant vector store
db.add_documents(texts)
print("Vector DB Successfully Created!")
