from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.Thank_YouView.as_view()),
    path("reviews", views.ReviewsListViews.as_view()),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.ReviewDetailsView.as_view(), name="review-details")
]
