"""A search module to load encoder model and get search results using embeddings.

"""

from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
import pandas as pd


class ElasticSearchEngine:
    """A  class to load model and get output"""

    def __init__(self) -> None:

        self.tokenizer = SentenceTransformer("all-MiniLM-L6-v2")
        self.elastic_client = Elasticsearch("http://localhost:9200")

    def get_model_output(self, input_data, search_results_limit=5):
        """A method to get model output from given text input
        Args:
            input_data (text):input text data

        Returns:
            output: model prediction
        """

        input_vector = self.tokenizer.encode(input_data)

        es_query = {
            "size": search_results_limit,
            "knn": {
                "field": "embeddings",
                "query_vector": input_vector,
                "k": 10,
                "num_candidates": 100,
            },
        }
        results = pd.DataFrame(
            columns=["similarity_score", "article_url", "article_text"]
        )
        for result in self.elastic_client.search(
            index="articles", body=es_query
        )["hits"]["hits"]:
            new_row = pd.Series(
                {
                    "similarity_score": result["_score"],
                    "article_url": result["_source"]["url"],
                    "article_text": result["_source"]["paragraph"],
                }
            )
            results = pd.concat(
                [results, new_row.to_frame().T], ignore_index=True
            )
        return results
