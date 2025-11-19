from tmdb_client import search_movie, get_movie_details

def main():
    print("🎬 Welcome to the Movie Recommender!")
    while True:
        title = input("\nEnter a movie title (or 'q' to quit): ")

        if title.lower() == 'q':
            print("Goodbye!")
            break

        movie = search_movie(title)

        if movie:
            print(f"\nFound: {movie['title']} (ID: {movie['id']})")
            details = get_movie_details(movie["id"])
            print(f"Overview:\n{details['overview']}")
        else:
            print("No results found. Try another title.")

if __name__ == "__main__":
    main()
