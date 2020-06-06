from rest_framework import serializers

from moviesapp.movies.models import Movie, Rating

class MovieListSerializer(serializers.HyperlinkedModelSerializer):
    avg_rating = serializers.DecimalField(max_digits=None, decimal_places=2, read_only=True)
    class Meta:
        model = Movie
        view_name = 'movie-list'
        fields = [
            'id',
            'title',
            'year',
            'rated',
            'released_on',
            'genre',
            'director',
            'plot',
            'avg_rating',
        ]

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    avg_rating = serializers.DecimalField(max_digits=None, decimal_places=2)
    class Meta:
        model = Movie
        view_name = 'movie-detail'
        fields = [
            'id',
            'title',
            'year',
            'rated',
            'released_on',
            'genre',
            'director',
            'plot',
            'avg_rating',
        ]

class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(max_value=5, min_value=0)
    class Meta:
        model = Rating
        view_name = 'rating'
        fields = '__all__'
        lookup_field = 'movie_id'
