# Haystack

Haystack is a framework for building custom RAG pipelines with LLMs. 

### What is RAG?

RAG, or Retrieval-Augmented Generation, integrates retrieval-based models, which search large datasets to extract relevant information, and generation-based models, which use this information to produce coherent and contextually accurate text.

This approach is especially valuable in scenarios requiring access to extensive external information, such as customer support, knowledge-based systems, and other applications where precise and accurate information retrieval is essential.

The RAG process consists of four stages:

1. **Indexing**: Data to be referenced is first transformed into LLM embeddings—numerical representations in the form of large vectors. These embeddings are then stored in a vector database, enabling efficient document retrieval.

2. **Retrieval**: Given a user query, a document retriever is employed to select the most relevant documents. This process typically utilizes models like _BM25_, _dense retrievers_, or other retrieval techniques to find documents or passages related to the query, providing the necessary information for the next steps.

3. **Augmentation**: The relevant information retrieved is fed into the LLM through prompt engineering, augmenting the user’s original query. This augmented data serves as additional context, helping the model generate more informed and accurate responses.

4. **Generation**: The LLM generates output based on both the user query and the retrieved documents. Models like GPT process this combined input to produce a coherent and contextually appropriate response.

### Haystack Concepts

- **Pipelines**: Directed multigraphs of different Haystack components and integrations to design and scale your interactions with LLMs
    - The `Pipeline` class in Haystack allows you to construct a sequence of components, each performing a specific task in a data processing pipeline. This modular approach makes it easy to build complex pipelines by chaining together different components.
- **Document Stores**: an object that stores your documents in Haystack, like an interface to a storage database
- **Data Classes**
- **Components**: Building Blocks of a pipeline that can be connected to each other
    - Generators: responsible for generating text responses after you give them a prompt using a specific llm technology (two types: chat and non-chat)
    - Retrievers: go through all the documents in a Document Store, select the ones that match the user query, and pass it on to the next componen
