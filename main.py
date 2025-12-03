from tmdb_client import TMDBClient

def main():
    client = TMDBClient()

    print("Welcome to the Movie Recommender!")
    while True:
        title = input("\nEnter a movie title (or 'q' to quit): ")

        if title.lower() == 'q':
            print("Goodbye!")
            break

        movie = client.search_movie(title)

        if not movie:
            print("No results found. Try another title.")
            continue

        print(f"\nFound: {movie['title']} (ID: {movie['id']})")

        details = client.get_movie_details(movie["id"])
        if details:
            print(f"Overview:\n{details.get('overview', 'No overview available.')}\n")
        else:
            print("Couldn't load movie details.\n")

        print("Recommended similar movies:")
        similar_movies = client.get_similar_movies(movie["id"])

        if similar_movies:
            for m in similar_movies[:5]:  # show top 5
                sim_title = m.get("title", "Unknown Title")
                release = m.get("release_date", "N/A")
                year = release[:4] if release and len(release) >= 4 else "N/A"
                print(f" - {sim_title} ({year})")
        else:
            print("No similar movies found.")

if __name__ == "__main__":
    main()

