import html
from urllib import response
from django.urls import resolve
from django.test import TestCase
from lists.views import home_page # (1) 从我们的视图里导入主页函数
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # (2) 解析根路径 URL
        self.assertEqual(found.func, home_page) # (3) 检查解析到的函数是否是 home_page
    
    def test_home_page_return_correct_html(self):
        response=self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
      




