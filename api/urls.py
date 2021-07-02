from django.urls import path

from api.views import RetrieveExchangeRateApiEndpoint

app_name = "api"
urlpatterns = [
    path("quotes/", RetrieveExchangeRateApiEndpoint.as_view(), name="quotes"),
]
