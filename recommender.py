from abc import ABC, abstractmethod
from tmdb_client import TMDBClient


class BaseRecommender(ABC):
    """Abstract base class for all recommenders."""

    def __init__(self, client: TMDBClient):
        self.client = client

    @abstractmethod
    def recommend(self, **kwargs):
        """Return a list of recommended movies."""
        raise NotImplementedError


class AgeRatingRecommender(BaseRecommender):
    """Recommender that suggests movies based on age rating (G, PG, PG-13, R, NC-17)."""

    def recommend(self, **kwargs):
        rating = kwargs.get("rating")
        if not rating:
            raise ValueError("AgeRatingRecommender requires a 'rating' argument")

        movies = self.client.discover_by_age_rating(rating)
        return movies


class GenreRecommender(BaseRecommender):
    """Recommender that suggests movies based on a genre name."""

    def recommend(self, **kwargs):
        genre_name = kwargs.get("genre_name")
        if not genre_name:
            raise ValueError("GenreRecommender requires a 'genre_name' argument")

        movies = self.client.discover_by_genre(genre_name)
        return movies


class RecommenderFactory:
    """Factory class responsible for creating recommender instances."""

    @staticmethod
    def create(mode: str, client: TMDBClient) -> BaseRecommender:
        """
        Create and return an appropriate recommender object for the given mode.
        """
        mode = mode.lower()

        if mode == "rating":
            return AgeRatingRecommender(client)
        elif mode == "genre":
            return GenreRecommender(client)
        else:
            raise ValueError(f"Unknown recommendation mode: {mode}")
