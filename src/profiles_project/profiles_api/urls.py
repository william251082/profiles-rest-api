from django.conf.urls import url

from . import views


urlpatters = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
]
