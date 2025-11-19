import requests
from config import API_KEY, BASE_URL

def search_movie(title):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": title
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # raises an error for bad status codes
        data = response.json()

        # Return the first result if results exist
        if "results" in data and data["results"]:
            return data["results"][0]
        else:
            print("No results found for that title.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Network or API error: {e}")
        return None
    except ValueError:
        print("Failed to decode JSON (check API key or connection).")
        return None


def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": API_KEY}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Network or API error: {e}")
        return None
    except ValueError:
        print("Failed to decode JSON (check API key or connection).")
        return None
    
def get_similar_movies(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/similar"
    params = {"api_key": API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("results", [])

