from tmdb_client import TMDBClient
from recommender import RecommenderFactory


def main():
    """Simple CLI to choose a recommendation mode and display TMDB results."""
    client = TMDBClient()

    while True:
        print("\nChoose recommendation mode:")
        print("1. Movies by age rating (G, PG, PG-13, R)")
        print("2. Movies by genre name")
        print("q. Quit")

        choice = input("Enter choice: ").strip().lower()

        if choice == "q":
            break

        movies = []  # ensure it's always defined

        if choice == "1":
            mode = "rating"
            rating = input("Enter an age rating (G, PG, PG-13, R, NC-17): ").strip().lower()
            recommender = RecommenderFactory.create(mode, client)
            movies = recommender.recommend(rating=rating)

        elif choice == "2":
            mode = "genre"
            genre_name = input("Enter a genre (e.g., action, comedy, horror): ").strip().lower()
            recommender = RecommenderFactory.create(mode, client)
            movies = recommender.recommend(genre_name=genre_name)

        else:
            print("Invalid choice.")
            continue

        if not movies:
            print("No results found or invalid input.")
            continue

        print("\n Top 10 Recommendations:")
        for m in movies[:10]:
            print("-", m.get("title", "Unknown title"))


if __name__ == "__main__":
    main()

