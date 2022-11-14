"""A factory module to get predictor class based on type"""
from src.inference.elasticsearch_engine import ElasticSearchEngine


def get_predictor(model_type):
    """A method to retun Predictor class object

    Args:
        model_type (str): Model type

    Returns:
        Predictor: A predictor class
    """
    if model_type is None:
        return None
    elif model_type == "elastic_search":
        return ElasticSearchEngine()
