from django.urls import path
from .views import UserCreateView, UserDetailView, UserListView, UserUpdateView, UserDeleteView, UserLoginView,login_view

app_name = 'accounts'

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create'),
    path('login/', login_view, name='login'),
    path('list/', UserListView.as_view(), name='list'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('<int:pk>/update', UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', UserDeleteView.as_view(), name='delete'),
]
