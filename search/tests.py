from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from datetime import datetime
from .models import Search
from .views import *

class SearchViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_do_search_view_post(self):
        url = 'example.com'
        response = self.client.post(reverse('do_search'), {'search': url}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_done.html')

        # Check if the Search object is created with the correct values
        search = Search.objects.latest('id')
        self.assertEqual(search.link, url)
        self.assertEqual(search.date, datetime.now().date())



    def test_search_done_view(self):
        link_list = ['example.com', 'example.com']
        search = Search.objects.create(link='example.com', date=datetime.now(), links_list=link_list)

        response = self.client.get(reverse('search_done'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_done.html')

        # Check if the context contains the correct data
        self.assertEqual(response.context['link_list'], link_list)

    def test_history_view(self):
        link_list = ['example.com', 'example.com']
        # Criação de objetos Search para testar o histórico
        search1 = Search.objects.create(link='example.com', date='2023-07-14', links_list=link_list)
        search2 = Search.objects.create(link='example.org', date='2023-07-14', links_list=link_list)

        # Criação de uma requisição GET para a view history com date_filter='all'
        client = Client()
        response = client.get('/search/history/', {'date_filter': 'all'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'history.html')

        # Verifica se a lista de resultados contém todos os objetos Search, ordenados pela data
        search_results = response.context['search_results']
        search_results_repr = [repr(search) for search in search_results]
        self.assertListEqual(search_results_repr, [repr(search1), repr(search2)])

        # Verifica se a lista de datas contém todas as datas distintas dos objetos Search, ordenadas pela data
        dates = response.context['dates']
        expected_dates = ['2023-07-14']
        self.assertListEqual([str(date) for date in dates], expected_dates)

    def test_delete_history_view(self):
        link_list = ['example.com', 'example.com']
        search = Search.objects.create(link='example.com', date=datetime.now(), links_list=link_list)

        response = self.client.post(reverse('delete_history', args=[search.id]))

        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertRedirects(response, '/search/history/?date_filter=all')

        # Check if the Search object is deleted
        self.assertFalse(Search.objects.filter(id=search.id).exists())

    def test_access_search_view(self):
        link_list = ['example.com', 'example.com']
        search = Search.objects.create(link='example.com', date=datetime.now(), links_list=link_list)

        response = self.client.get(reverse('access_search', args=[search.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'access_search.html')

        # Check if the context contains the correct data
        self.assertEqual(response.context['link'], search.link)
        self.assertEqual(response.context['links_list'], search.links_list)
