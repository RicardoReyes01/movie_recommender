import requests
from config import API_KEY, BASE_URL

class TMDBClient:
    """Client wrapper around the TMDB API."""

    def __init__(self, api_key=API_KEY, base_url=BASE_URL):
        self.api_key = api_key
        self.base_url = base_url

    def search_movie(self, title):
        """Search for a movie by title and return the first result (or None)."""
        url = f"{self.base_url}/search/movie"
        params = {
            "api_key": self.api_key,
            "query": title
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
    def get_movie_details(self, movie_id):
        """Get detailed information for a specific movie id."""
        url = f"{self.base_url}/movie/{movie_id}"
        params = {"api_key": self.api_key}

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error getting movie details: {e}")
            return None

    def get_similar_movies(self, movie_id):
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

