from django.urls import path
from chewy.views.index import IndexTemplateView
from django.contrib.auth import views as auth_views

# from .views.filmsViews import filmsViews

# views.app_name = "chewy"

urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    # path('accounts/login/', auth_views.LoginView.as_view()),
    #  path("films/", filmsViews, name="search")
]
