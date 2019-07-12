from django.urls import path
from chewy.views.index import IndexTemplateView
from chewy.views.filmsViews import SearchTemplateView

# from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("search/", SearchTemplateView.as_view(), name="search_list")
    # path('accounts/login/', auth_views.LoginView.as_view()),
]
