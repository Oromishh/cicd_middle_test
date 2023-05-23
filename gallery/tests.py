from django.test import TestCase

# Create your tests here.

#  Create tests for views.gallery_view and views.image_detail


class GalleryViewTest(TestCase):
    def test_gallery_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')
        self.assertContains(response, 'Cat Photo 1')
        self.assertNotContains(response, 'Dog Photo 2')
        self.assertNotContains(response, 'Cat Photo 3')
        self.assertNotContains(response, 'Dog Photo 4')


class ImageDetailViewTest(TestCase):
    def test_image_detail_view(self):
        response = self.client.get('/image/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'image_detail.html')
        self.assertContains(response, 'ID: 1')
        self.assertContains(response, '1.jpg')
        self.assertNotContains(response, 'ID: 2')
        self.assertNotContains(response, '2.jpg')
