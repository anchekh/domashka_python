from django.urls import path
# from .views import home_page_view

# urlpatterns = [
#     path("", home_page_view, name="home"),
# ]

from django.urls import path
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="resume"),
]
