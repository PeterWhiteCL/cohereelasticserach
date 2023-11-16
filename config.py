import os

import cohere



cohere_vector_size_lookup = {"embed-english-light-v2.0": 1024}

COHERE_API_KEY = "eReng5vKo29t825i3mYu7A8dMPezrk8y6kqNHB1c"#os.environ["COHERE_API_KEY"]
COHERE_MODEL = "embed-english-light-v2.0"
VECTOR_NAME = "cohere_vector"
VECTOR_SIZE = cohere_vector_size_lookup[COHERE_MODEL]
DATA_PATH = "data/arxiv_5000.csv"
DATA_COLUMNS = ["title", "abstract"]
EMBED_COLUMN = ["abstract"]
ELASTICSEARCH_NODE_NAME="my-es-node"
ELASTICSEARCH_CLUSTER_NAME="my-es-cluster"
ES_PASSWORD = "<es_pw>"
ES_USER = "<es_user>"


def get_cohere_client(api_key: str):
    return cohere.Client(api_key)


# init your clients
co = get_cohere_client(COHERE_API_KEY)
#client = get_opensearch_client()
