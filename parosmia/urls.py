from django.urls import path
from parosmia import views
from parosmia.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:50],  
    context_object_name="message_list",
    template_name="parosmia/log.html",
)

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("resources/", views.resources, name="resources"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("chat/", views.log, name="chat"),
    path("track/", views.track, name="track"),
    path("auth/", views.auth, name="auth"),
    path("register/", views.register, name="register"),
]

