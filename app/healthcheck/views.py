from rest_framework.response import Response
from rest_framework.views import APIView


class HealthcheckView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        content = {"status": "ok"}
        return Response(content)
