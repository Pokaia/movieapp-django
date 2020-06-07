from django.core.urlresolvers import reverse, resolve
from django.test import TestCase


class TestMovieURLs(TestCase):
    """Test URL patterns for movies app api."""

    def test_urls(self):
        self.assertEqual(reverse('api:list'), '/api/movies/')
        self.assertEqual(reverse('api:movie-detail', kwargs={'pk': '1'}), '/api/movies/1/')
        self.assertEqual(reverse('api:rating'), '/api/rating/')
        self.assertEqual(reverse('api:get', kwargs={'movie_id': '1'}), '/api/rating/1/')
