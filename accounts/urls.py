from .views import NoteListCreateAPI, NoteRetrieveUpdateDestroyAPI, RegisterAPI, LoginAPI, UserListAPI, UserRetrieveUpdateDestroyAPI
from django.urls import path
from rest_framework_simplejwt import views as jwt_views




urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    
    path('api/users/', UserListAPI.as_view()), #name mund te hiqet
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyAPI.as_view(), name='users'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('api/notes/', NoteListCreateAPI.as_view(), name='notes'),
    path('api/notes/<int:pk>/', NoteRetrieveUpdateDestroyAPI.as_view(), name='note_detail'),
]