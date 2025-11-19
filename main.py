from tmdb_client import search_movie, get_movie_details, get_similar_movies

def main():
    print("Welcome to the Movie Recommender!")
    while True:
        title = input("\nEnter a movie title (or 'q' to quit): ")

        if title.lower() == 'q':
            print("Goodbye!")
            break

        movie = search_movie(title)

        if movie:
            print(f"\nFound: {movie['title']} (ID: {movie['id']})")
            details = get_movie_details(movie["id"])
            print(f"Overview:\n{details['overview']}\n")

            print("Recommended similar movies:")
            similar_movies = get_similar_movies(movie["id"])

            if similar_movies:
                for m in similar_movies[:5]:  # show top 5
                    title = m.get("title", "Unknown Title")
                    release = m.get("release_date", "N/A")[:4] if m.get("release_date") else "N/A"
                    print(f" - {title} ({release})")
            else:
                print("No similar movies found.")

        else:
            print("No results found. Try another title.")

if __name__ == "__main__":
    main()
