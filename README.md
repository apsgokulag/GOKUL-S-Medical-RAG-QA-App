# GOKUL-S-Medical-RAG-QA-App
fast.ai students

1. PubMedBERT Embeddings: Discover how this fined-tuned model, using sentence transformers, enhances the app's ability to understand complex medical text, offering superior performance in clustering and semantic search.
2. Orchestration Framework: I'll show you how long-chain simplifies prompts, preprocessing, and more, making your experience seamless.
3. Qdrant Vector Database: Learn about the integration of qdrant in a Docker container for efficient embedding storage and retrieval.
 🖥️ Everything runs locally on your CPU and is completely open source.
The LLM App uses [Pathway](https://pathway.com/), An awesome package to handle real-time data streaming.

## Demo
Follow these steps to immerse yourself into Generative AI Storytelling

https://github.com/user-attachments/assets/056588e5-99f8-4db2-bfca-b1a01f7e6f90


## Technologies Used
*OpenAI

*Docker

*meditron-7B-GGUF

*Python 3.12.4  

## Features
OpenAI Modules: Enhances natural language understanding and generation capabilities.
User-Friendly Interface: Designed for intuitive interaction. The interface is created using HTML,CSS,Javascripts tools and integarted with these modules.
Docker:improving datasets api configuration and support for localhost server.



## How to run the tool
1. **Clone the repository:**
https://github.com/apsgokulag/GOKUL-S-Medical-RAG-QA-App/tree/main/MEDrag
cd MEDrag;

3. **Install dependencies:**
   install all requirments packages using this command.
   
    ```bash
   py -m pip install -r .\requirements.txt
   ```
4. **download the docker**

      ```bash
   https://www.docker.com/products/docker-desktop/
      ```
create an account and sign-in
check docker is downloaded successfully

```bash
   docker --version 
 ```

activate image section and create qdrant using this command.

   ```bash
     docker pull qdrant/qdrant
   ```
   or
   
      ```bash
    docker build -t qdrant/qdrant
       ```
    
5. **Install the package**
   
  ```bash
     py -m pip install -U langchain-huggingface 
  ```

Similarly, update to the new langchain-qdrant package:

    ```bash
pip install -U langchain-qdrant
    ```


6. **How to Use It**

The command docker run -p 6333:6333 qdrant/qdrant is used to run the Qdrant vector database inside a Docker container. Here's a breakdown of what each part of the command does:

docker run -p 6333:6333 qdrant/qdrant

docker run: This is the command to create and start a new Docker container.
-p 6333:6333: This option maps port 6333 on your local machine (host) to port 6333 on the Docker container. It allows you to access the Qdrant service running inside the container via port 6333 on your host machine.
qdrant/qdrant: This specifies the Docker image to use for the container. In this case, it is the official Qdrant image.
also you must run the docker host for 
 firstly,you must be run this package of code
 
     ```bash
 python ingest.py
     ```

 then,it have some database is downloaded into your docker env collection.To check that collection database 

     ```bash
      http://localhost:6333/dashboard
     ```

you can check the vector_db in that docker collection.so you must run another code of commands,
python .\retriever.py 

then you will get some metadata and page_content.after that, you can run the last code command for activating the chatbot,
(https://huggingface.co/TheBloke/meditron-7B-GGUF)

uvicorn rag:app 

this will download the basic repo contains GGUF format model files for EPFL LLM Team's Meditron 7B.llama.cpp. The source project for GGUF. Offers a CLI and a server option.
The following clients/libraries will automatically download models for you, providing a list of available models to choose from:
LM Studio
LoLLMS Web UI
Faraday.dev

use it to see your chatbot:

http://localhost:8000
or
http://127.0.0.1:8000/


**Benefits:**
- Unlock the transformative capabilities of generative AI.
- Seamlessly generate medical health care ideas based on user-provided prompts.
- Ask any kind of question related on medical health questions used on the 2024 data will shown perfectly by using this predefined idea.

  ## Acknowledgments

First and foremost, I extend my heartfelt gratitude to Mulearn and Pathway for providing me with this invaluable opportunity to delve into the fascinating realm of Generative AI and LLM model



 





   
   

