from django.urls import path
import users.views as users
from users.views import login, registration, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),

    path('veryfy/<str:email>/<str:activate_key>/', users.verify, name='verify'),
]
