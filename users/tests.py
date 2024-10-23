from django.test import SimpleTestCase

class TemplatesTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_solution_page_status_code(self):
        response = self.client.get('/solutions/')
        self.assertEqual(response.status_code, 200)
    
    def test_contact_page_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
    
    def test_resources_page_status_code(self):
        response = self.client.get('/resources/')
        self.assertEqual(response.status_code, 200)
    
    def test_careers_page_status_code(self):
        response = self.client.get('/careers/')
        self.assertEqual(response.status_code, 200)
