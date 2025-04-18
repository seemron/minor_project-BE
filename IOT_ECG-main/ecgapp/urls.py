from django.urls import path
from .views import PostHealthDataView, DisplayDataView,get_latest_data

urlpatterns = [
    path('post_data/', PostHealthDataView.as_view(), name='post_data'),
    path('display_data/', DisplayDataView.as_view(), name='display_data'),
    path('get_latest_data/', get_latest_data, name='get_latest_data'),
]