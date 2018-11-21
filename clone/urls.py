from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    path("", include("quena.urls", namespace="quena")),
    path("user/", include("user.urls", namespace="user")),
]