from django.urls import path
from .views import news_detail,HomePageView,news_list,ContactView,error_404_view,SinglePageView
from .views import SearchResultList
from .views import LocalNewsView, ForiegnNewsView, TechnologyNewsView, SportNewsView, NewsCreateView, NewsEditView, NewsDeleteView
from .views import  admin_page
from django.conf.urls import handler404



urlpatterns = [
    path("", HomePageView, name="home_page"),
    path("all/", news_list, name="all_news_list"),
    path('<int:id>/', news_detail, name="news_detail_page"),
    path("contact/", ContactView, name='contact'),
    path("404/", error_404_view, name='404'),
    path("single_page/", SinglePageView, name="single_page"),
    path('searchresult/', SearchResultList.as_view(), name='search_result'),
    path('local-news/', LocalNewsView.as_view(), name='local_news_page'),
    path('foriegn-news/', ForiegnNewsView.as_view(), name='foriegn_news_page'),
    path('technology-news/', TechnologyNewsView.as_view(), name='technology_news_page'),
    path('sport-news/', SportNewsView.as_view(), name='sport_news_page'),
    path("news_create/", NewsCreateView.as_view(), name="news_create_page"),
    path("news_edit/<int:pk>/", NewsEditView.as_view(), name="news_edit_page"),
    path("news_delete/<int:pk>/", NewsDeleteView.as_view(), name="news_delete_page"),
    path('admin_page', admin_page, name="admin_page"),

   

]






