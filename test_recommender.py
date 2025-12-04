import unittest
from unittest.mock import MagicMock
from recommender import AgeRatingRecommender, GenreRecommender, RecommenderFactory, BaseRecommender

# Test the Age Rating functionality
class TestAgeRatingRecommender(unittest.TestCase):
    def test_recommend_calls_client(self):
        # Creates a fake client with the expected method
        mock_client = MagicMock()
        mock_client.discover_by_age_rating.return_value = ["Mock Movie PG"]

        recommender = AgeRatingRecommender(mock_client)
        result = recommender.recommend(rating="PG")

        # Verifies if the method is called correctly
        mock_client.discover_by_age_rating.assert_called_once_with("PG")
        self.assertEqual(result, ["Mock Movie PG"])

# Test the Genre functionality
class TestGenreRecommender(unittest.TestCase):
    def test_recommend_calls_client(self):
        # Creates a fake client with the expected method
        mock_client = MagicMock()
        mock_client.discover_by_genre.return_value = ["Mock Movie Action"]

        recommender = GenreRecommender(mock_client)
        result = recommender.recommend(genre_name="Action")

        # Verifies if the method is called correctly
        mock_client.discover_by_genre.assert_called_once_with("Action")
        self.assertEqual(result, ["Mock Movie Action"])


class TestRecommenderFactory(unittest.TestCase):
    # Creates a fake client and makes sure that rating recommender returns the correct response
    def test_create_rating_recommender(self):
        mock_client = MagicMock()
        recommender = RecommenderFactory.create("rating", mock_client)
        self.assertIsInstance(recommender, AgeRatingRecommender)

    # Creates a fake client and makes sure that genre recommender returns the correct response
    def test_create_genre_recommender(self):
        mock_client = MagicMock()
        recommender = RecommenderFactory.create("genre", mock_client)
        self.assertIsInstance(recommender, GenreRecommender)

class TestBaseRecommender(unittest.TestCase):
    # Creates a fake client 
    def test_cannot_instantiate(self):
        mock_client = MagicMock()
        # BaseRecommender is abstract, so instantiating it would give TypeError
        with self.assertRaises(TypeError):
            BaseRecommender(mock_client)

if __name__ == "__main__":
    unittest.main()
