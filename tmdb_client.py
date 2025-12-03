#imports requests module and api key and base url from config.py
import requests
from config import API_KEY, BASE_URL


class TMDBClient:
    """Client wrapper around the TMDB API."""

    #dictonaries for genre names 
    GENRE_DICT = {
        "action": 28,
        "adventure": 12,
        "animation": 16,
        "comedy": 35,
        "crime": 80,
        "documentary": 99,
        "drama": 18,
        "family": 10751,
        "fantasy": 14,
        "history": 36,
        "horror": 27,
        "music": 10402,
        "mystery": 9648,
        "romance": 10749,
        "science fiction": 878,
        "tv movie": 10770,
        "thriller": 53,
        "war": 10752,
        "western": 37,
    }

    #intializes the api key and base url within class
    def __init__(self, api_key=API_KEY, base_url=BASE_URL):
        self.api_key = api_key
        self.base_url = base_url

    #searches for a movie by title the user inputs
    def search_movie(self, title: str):
        """Search for a movie by title and return the result"""
        url = f"{self.base_url}/search/movie"
        params = {
            "api_key": self.api_key,
            "query": title,
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            results = data.get("results", [])
            return results[0] if results else None
        except requests.RequestException as e:
            print(f"Error searching movie: {e}")
            return None

    #searches for similar movies based on movie id
    def get_similar_movies(self, movie_id: int):
        """Return a list of movies similar to the given movie id."""
        url = f"{self.base_url}/movie/{movie_id}/similar"
        params = {"api_key": self.api_key}

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("results", [])
        except requests.RequestException as e:
            print(f"Error getting similar movies: {e}")
            return []
    

    
    #searches for movies based on genre
    def get_genre_id(self, genre_name: str):
        """Convert a genre name that the user typed into a TMDB genre id."""
        if not genre_name:
            return None
        return self.GENRE_DICT.get(genre_name.strip().lower())

    def discover_by_genre(self, genre_name: str):
        """Return a list of movies for a given genre"""
        genre_id = self.get_genre_id(genre_name)
        if not genre_id:
            print("invalid genre name.")
            return []  

        url = f"{self.base_url}/discover/movie"
        params = {
            "api_key": self.api_key,
            "with_genres": genre_id,
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("results", [])
        except requests.RequestException as e:
            print(f"Error discovering movies by genre: {e}")
            return []

    #searches for movies based on age rating
    def discover_by_age_rating(self, rating_name: str):
        """Return a list of movies for a given age rating"""
        if not rating_name:
            return []

        rating = rating_name.strip().upper()

        url = f"{self.base_url}/discover/movie"
        params = {
            "api_key": self.api_key,
            "certification_country": "US",
            "certification": rating,
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("results", [])
        except requests.RequestException as e:
            print(f"Error discovering movies by age rating: {e}")
            return []

