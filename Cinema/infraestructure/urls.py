from django.urls import path
from Cinema.views import bulk_views, main_views, template_view

urlpatterns = [
    path('', main_views.home, name='home'),
    path('movies/', bulk_views.MoviesListView.as_view(), name='movies'),
    path('projections/', bulk_views.projections, name='projections'),
    path('reserves/<int:hall>', main_views.Reserves.as_view(), name='reserves'),
    path('movies_details/', bulk_views.details, name='movies_details'),
    path('active_discounts/', template_view.DiscountView.as_view(), name='active_discounts'),
    path('select_discounts/', template_view.SelectDiscountView.as_view(), name='select_discounts'),

]
