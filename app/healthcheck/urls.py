from django.urls import path

from healthcheck.views import HealthcheckView

app_name = "healthcheck"

urlpatterns = [
    path(r"", HealthcheckView.as_view(), name="healthcheck"),
]
