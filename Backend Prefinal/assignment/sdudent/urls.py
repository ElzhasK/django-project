from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('sdudent/', views.sdudent, name='sdudent'),
    path('result/', views.result, name='result'),
    path('all_members/', views.members, name='all_members'),
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('show_result/<int:pk>/', views.show_result, name='show_result'),


    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

    path('registration/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  

    path('profile/', views.profile, name='profile'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)