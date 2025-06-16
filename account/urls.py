from django.urls import path, re_path
from account.views import login, myAccount, logout, activate

urlpatterns = [
    path('login/', login, name = 'login'),
    path('myAccount/', myAccount, name = 'myAccount'),
    path('logout/', logout, name = 'logout'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        activate, name='activate'),
]