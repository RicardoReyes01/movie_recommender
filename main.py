#imports TMDBClient and RecommenderFactory
from tmdb_client import TMDBClient
from recommender import RecommenderFactory


def main():
    """Simple CLI to choose a recommendation mode and display TMDB results."""
    #initialize TMDB client instance
    client = TMDBClient()

    #shows menu continually until user quits
    while True:
        print("\nChoose recommendation mode:")
        print("1. Similar movies by title")
        print("2. Movies by genre name")
        print("3. Movies by age rating (G, PG, PG-13, R)")
        print("q. Quit")

        choice = input("Enter choice: ").strip().lower()

        if choice == "q":
            break

        movies = []  # make sure it's always defined

        #handles user choices and creates appropriate recommender 
        if choice == "1":
            mode = "similar"
            title = input("Enter a movie title: ").strip()
            recommender = RecommenderFactory.create(mode, client)
            movies = recommender.recommend(title=title)

        elif choice == "2":
            mode = "genre"
            genre_name = input("Enter a genre (e.g., action, comedy, horror): ").strip().lower()
            recommender = RecommenderFactory.create(mode, client)
            movies = recommender.recommend(genre_name=genre_name)

        elif choice == "3":
            mode = "rating"
            rating = input("Enter an age rating (G, PG, PG-13, R, NC-17): ").strip().lower()
            recommender = RecommenderFactory.create(mode, client)
            movies = recommender.recommend(rating=rating)

        #prevents invalid choices from user
        else:
            print("Invalid choice.")
            continue
        
        #checks if any movies were found
        if not movies:
            print("No results found or invalid input.")
            continue

        #prints the first 5 recommended movies
        print("\nRecommendations:")
        for m in movies[:5]:
            print("-", m.get("title", "Unknown title"))


if __name__ == "__main__":
    main()

