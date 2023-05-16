"""social_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from social import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register", views.SignUpView.as_view(), name="register"),
    path("", views.LoginView.as_view(), name="signin"),
    path("home", views.IndexView.as_view(), name="home"),
    path("logout",views.signout,name="signout"),
    path("posts/all",views.MyPostsView.as_view(),name="my-posts"),
    path("posts/<int:id>/comments/add",views.add_comment,name="add-comment"),
    path("ansers/<int:id>/upvote",views.upvote_view,name="upvote"),
    path('posts/detail/<int:id>',views.PostDetailView.as_view(),name="post-detail"),

    path("profile/detail",views.ProfiledetailView.as_view(),name="profile-detail"),
    path("posts/remove/<int:id>", views.PostDeleteView.as_view(), name="post-delete"),
    

    path("posts/change/<int:id>", views.PostEditView.as_view(), name="post-change"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
