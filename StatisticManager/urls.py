from django.urls import path
from .views import *
from .rest import *


urlpatterns = [
    path('api/', SearchRest.as_view()), #get params 'page' and 'search_query'
    path('get_user/<int:id>/', GetUserInfo.as_view()),
    path('', Search.as_view()),
]
