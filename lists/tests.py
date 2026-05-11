from calendar import firstweekday
from hmac import new
import html
from multiprocessing import set_forkserver_preload
from urllib import response
from django.urls import resolve
from django.test import TestCase
from lists.views import home_page # (1) 从我们的视图里导入主页函数
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item


class ItemModelTest(TestCase):
    def test_save_and_retrieve_items(self):
        first_item=Item()
        first_item.text='The first list item'
        first_item.save()

        second_item=Item()
        second_item.text='Item the second'
        second_item.save()

        saved_items=Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item=saved_items[0]
        second_saved_item=saved_items[1]
        self.assertEqual(first_saved_item.text, first_item.text)
        self.assertEqual(second_saved_item.text, second_item.text)

    def test_uses_home_template(self):
        response=self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_can_save_a_POST_request(self):
        response=self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
        
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
      
        


