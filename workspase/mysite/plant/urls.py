from django.urls import path
from . import views

app_name = 'plant'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('signup/', views.Create_account.as_view(), name='user_create'),
    path('top/', views.Top.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    # path('user_create/', views.UserCreate.as_view(), name='user_create'),
    # path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    # path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
    
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)