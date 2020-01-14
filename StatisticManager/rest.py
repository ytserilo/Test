from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import UserManager
import json

class SearchRest(APIView, UserManager):
    def get(self, request):
        search_query = request.GET.get("search_query")
        page = request.GET.get("page")

        paginator = self.search(search_query, page)

        return Response(paginator)
