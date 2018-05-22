from django.conf.urls import include, url
from .import views

app_name='administration'
urlpatterns = [
    url(r'^signup/',views.signup_view, name="signup"),
]