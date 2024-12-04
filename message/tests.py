from django.test import SimpleTestCase
from django.urls import reverse


class MessagePageTests(SimpleTestCase):
    
    #test for url existance
    def test_url_exist_at_correct_location(self):
        response=self.client.get("/message/")
        self.assertEqual(response.status_code,200)
        
    #test for url name is available
    def test_url_available_by_name(self):
        response=self.client.get(reverse('message'))
        self.assertEqual(response.status_code,200)
        
    #test for template name is available in url that name : "message"
    def test_template_name(self):
        response=self.client.get(reverse('message'))
        self.assertTemplateUsed(response,'home.html')
        
    #test that our content has contain this text in it
    def test_template_content(self):
        response=self.client.get("/message/")
        self.assertContains(response,"<h1>this is first block template </h1>")
