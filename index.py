import os

os.environ['OPENAI_API_KEY'] = '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'

import langchain
from langchain.indexes import VectorstoreIndexCreator
from langchain.globals import set_debug

set_debug(True)

loader = langchain.document_loaders.TextLoader("./article.txt")

index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query("What do LangChain help?"))