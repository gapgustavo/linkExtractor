from rest_framework.views import APIView
from rest_framework.response import Response
from search.models import Search
from datetime import datetime
from search.useful import *
from .serializers import SearchSerializer
from django.shortcuts import render
import json

def searchApiDoc(request):
    return render(request, 'scanapi.html')

class SearchView(APIView):
    def post(self, request):
        url = request.data.get('link')

        page_count = 40
        urls = bing_search(url, page_count)
        relevant_urls = get_relevant_links(urls)

        date = datetime.now()

        links_search = Search(
            link=url,
            links_list=relevant_urls,
            date=date,
        )

        links_search.save()
        return Response({"result": relevant_urls}, status=200)
    
    def get(self, request):
        search_results = Search.objects.all()

        # Serializar os resultados para retornar em formato JSON
        data = []
        for result in search_results:
            result_data = {
                'id': result.id,
                'link': result.link,
                'date': result.date,
                'links_list': result.links_list,
            }
            data.append(result_data)

        return Response(data, status=200)

