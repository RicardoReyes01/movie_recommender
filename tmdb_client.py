import requests
from config import API_KEY, BASE_URL

# Function to search for a movie by title
def search_movie(title):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": title
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Return the first movie if results exist
    if data["results"]:
        return data["results"][0]  # returns dict of movie info
    else:
        return None

# Function to get details about a movie using its ID
def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

# Quick test to make sure it works
if __name__ == "__main__":
    movie = search_movie("Inception")
    if movie:
        print(f"Found: {movie['title']} (ID: {movie['id']})")
        details = get_movie_details(movie["id"])
        print(f"Overview: {details['overview']}")
    else:
        print("Movie not found.")

