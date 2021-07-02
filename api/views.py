from django.conf import settings
from rest_framework.authentication import BaseAuthentication

from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.models import EntryPoint
from api.serializers import EntryPointSerializer
from api.tasks import fetch_data


class EntryPointPaginator(PageNumberPagination):
    page_size = 100


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        params = {k.lower(): v.lower() for k, v in request.GET.items()}
        if params.get("api_key") != settings.API_KEY:
            raise PermissionDenied("No or invalid key provided.")


class RetrieveExchangeRateApiEndpoint(ListAPIView):

    queryset = EntryPoint.objects.order_by("-created_at")
    serializer_class = EntryPointSerializer
    pagination_class = EntryPointPaginator
    authentication_classes = (APIKeyAuthentication,)

    def post(self, request, *args, **kwargs):
        fetch_data.delay()
        return Response({"success": True})
