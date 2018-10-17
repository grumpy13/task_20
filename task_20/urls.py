
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from restaurants import views
from api.views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantUpdateView,
    RestaurantDeleteView,
    RestaurantCreateView,
    SignUpView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('restaurants/list/',views.restaurant_list ,name='restaurant-list'),
    path('restaurants/favorite/',views.favorite_restaurants ,name='favorite-restaurant'),
    path('restaurants/<int:restaurant_id>/detail/',views.restaurant_detail ,name='restaurant-detail'),
    path('restaurants/create/',views.restaurant_create ,name='restaurant-create'),
    path('restaurants/<int:restaurant_id>/update/',views.restaurant_update ,name='restaurant-update'),
    path('restaurants/<int:restaurant_id>/delete/',views.restaurant_delete ,name='restaurant-delete'),
    path('restaurants/<int:restaurant_id>/favorite/',views.restaurant_favorite ,name='restaurant-favorite'),
    path('restaurants/<int:restaurant_id>/item/add/',views.item_create ,name='item-create'),
    path('signup/',views.signup ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),
    path('no-access/',views.no_access ,name='no-access'),

    path('api/list/', RestaurantListView.as_view(), name='api-list'),
    path('api/create/', RestaurantCreateView.as_view(), name='api-create'),
    path('api/<int:restaurant_id>/detail/', RestaurantDetailView.as_view(), name='api-detail'),
    path('api/<int:restaurant_id>/update/', RestaurantUpdateView.as_view(), name='api-update'),
    path('api/<int:restaurant_id>/delete/', RestaurantDeleteView.as_view(), name='api-delete'),
    path('api/signup/', SignUpView.as_view(),name='api-signup'),

    path('api/login/', obtain_jwt_token, name= 'api-login'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)