#imports abstract base class and abstractmethod decorator and TMDBClient class
from abc import ABC, abstractmethod
from tmdb_client import TMDBClient

# base recommender class that other recommender classes will inherit from
class BaseRecommender(ABC):
    """Abstract base class for all recommenders."""

    def __init__(self, client: TMDBClient):
        self.client = client

    @abstractmethod
    def recommend(self, **kwargs): #Note: kwargs (key word arguments) to allow different params such as title, genre_name, rating
        """Return a list of recommended movies."""
        raise NotImplementedError


class SimilarTitleRecommender(BaseRecommender):
    """Recommender that suggests movies similar to a given title."""

    def recommend(self, **kwargs):
        title = kwargs.get("title")
        if not title:
            raise ValueError("SimilarTitleRecommender requires a 'title' argument")

        #finds the movie by title
        movie = self.client.search_movie(title)
        if not movie:
            print("No movie found matching that title.")
            return []

        #finds movie id from the movie found by title
        movie_id = movie.get("id")
        if not movie_id:
            print("Movie ID missing from TMDB response.")
            return []

        print(f"Using '{movie.get('title', 'Unknown')}' (id={movie_id}) as the base movie.")

        #finds similar movies based on movie id
        similar_list = self.client.get_similar_movies(movie_id)
        if not similar_list:
            print("TMDB did not return any similar movies for this title.")
        return similar_list


class GenreRecommender(BaseRecommender):
    """Recommender that suggests movies based on a genre name."""
    
    def recommend(self, **kwargs):
        genre_name = kwargs.get("genre_name")
        if not genre_name:
            raise ValueError("GenreRecommender requires a 'genre_name' argument")
        
        #uses the discover_by_genre method from tmdb_client.py to find movies by genre
        movies = self.client.discover_by_genre(genre_name)
        if not movies:
            print("Invalid genre name or no movies found for that genre.")
        return movies


class AgeRatingRecommender(BaseRecommender):
    """Recommender that suggests movies based on age rating (G, PG, PG-13, R, NC-17)."""

    def recommend(self, **kwargs):
        rating = kwargs.get("rating")
        if not rating:
            raise ValueError("AgeRatingRecommender requires a 'rating' argument")

        #uses the discover_by_age_rating method to find movies by age rating
        movies = self.client.discover_by_age_rating(rating)
        if not movies:
            print("Invalid rating or no movies found for that rating.")
        return movies


class RecommenderFactory:
    """Factory class responsible for creating recommender instances."""

    @staticmethod
    def create(mode: str, client: TMDBClient) -> BaseRecommender:
        """Create and return an appropriate recommender object for the 
        given mode using Python's swtich cases"""

        match mode.lower():

            case "similar":
                return SimilarTitleRecommender(client)

            case "genre":
                return GenreRecommender(client)

            case "rating":
                return AgeRatingRecommender(client)

            case _:
                raise ValueError(f"Unknown recommendation mode: {mode}")

