from dotenv import load_dotenv
from haystack import Pipeline, PredefinedPipeline
import urllib.request

load_dotenv()

# When you use `dotenv` to load your environment variables, 
# it automatically loads all the variables defined in your `.env`` file into the environment, 
# making them accessible via `os.getenv()` or directly through `os.environ`

# import os
# os.environ["OPENAI_API_KEY"]

urllib.request.urlretrieve("https://www.gutenberg.org/cache/epub/7785/pg7785.txt", "davinci.txt")  

indexing_pipeline =  Pipeline.from_template(PredefinedPipeline.INDEXING)
indexing_pipeline.run(data={"sources": ["data/davinci.txt"]})

rag_pipeline =  Pipeline.from_template(PredefinedPipeline.RAG)

query = "Did he invent flying machines?"
result = rag_pipeline.run(data={"prompt_builder": {"query":query}, "text_embedder": {"text": query}})
print(result["llm"]["replies"][0])