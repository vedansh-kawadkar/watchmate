from django.urls import path
from watchlist_app.api.views import MovieDetailsAPIView, MovieListAPIView

urlpatterns = [
    path('list/', view=MovieListAPIView.as_view(), name='movie-list'),
    path('<int:pk>/', view=MovieDetailsAPIView.as_view(), name='movie-details'),
]

