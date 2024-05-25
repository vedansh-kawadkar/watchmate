from django.urls import path
from watchlist_app.api.views import ContentDetailsAPIView, ContentListAPIView

urlpatterns = [
    path('list/', view=ContentListAPIView.as_view(), name='content-list'),
    path('<int:pk>/', view=ContentDetailsAPIView.as_view(), name='content-details'),
]

