import unittest
import photosort


class TestExists(unittest.TestCase):

    def test_exists(self):
        path = "C:\Program Files"
        result = photosort.exists(path)
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()