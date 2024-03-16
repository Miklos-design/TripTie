from django.urls import path
from . import views

app_name = 'tripapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('edit_profile/<username>/', views.EditProfileView.as_view(), name='edit_profile'),
    path('my_trip_plans/<username>/', views.MyTripPlansView.as_view(), name='my_trip_plans'),
    path('my_likes/<username>/', views.MyLikesView.as_view(), name='my_likes'),
    path('add_plan/<username>', views.AddPlan.as_view(), name='add_plan'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('trip_plan_search/', views.TripPlanSearch.as_view(), name='trip_plan_search'),
    path('add_comment/<int:trip_plan_id>', views.AddCommentView.as_view(), name='add_comment'),
    path('like_trip_plan/<int:trip_plan_id>', views.LikeTripPlan.as_view(), name='like_trip_plan'),
    path('delete_trip_plan/<int:trip_plan_id>', views.DeleteTripPlan.as_view(), name='delete_trip_plan'),
    path('explore/', views.explore, name='explore'),
    path('search_youtube/', views.search_youtube_for_city, name='search_youtube'),
    path('weather/', views.WeatherView.as_view(), name='weather'),
]
