from django.urls import path
from Cinema.views import bulk_views, main_views

urlpatterns = [
    path('', main_views.home , name='home'),

    path('movies/', bulk_views.MoviesListView.as_view(), name='movies'),

]
