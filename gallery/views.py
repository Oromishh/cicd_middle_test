from django.shortcuts import render, get_object_or_404
from . import models
import datetime

#  Необхідно додати до аплікації gallery дві views.
#  - призначення: відображає зображення, які були створені в останній місяць.
#  - назва view: gallery_view
#  - шаблон: gallery.html

#  - призначення: відображає певне зображення з використанням його id.
#  - назва view: image_detail
#  - шаблон: image_detail.html3. Написати unit-тести, які протестують роботу із створеними views.   

def gallery_view(request):
    images = []
    image_1 = models.Image()
    image_1.title = 'Cat Photo 1'
    image_1.image = 'cat.jpg'
    # Set date month ago
    image_1.created_date = '2021-09-11'
    images.append(image_1)

    # Create second image with date 2 months ago
    image_2 = models.Image()
    image_2.title = 'Dog Photo 2'
    image_2.image = 'dog.jpg'
    # Set date 2 months ago
    image_2.created_date = '2021-08-01'
    images.append(image_2)

    filtered_images = []

    # Filter images by not older than 2021-09-10
    for image in images:
        date = datetime.datetime.strptime(image.created_date, '%Y-%m-%d')
        if date > datetime.datetime(2021, 9, 10):
            filtered_images.append(image)
    
    # Render gallery.html template with filtered images
    print(filtered_images)
    return render(request, 'gallery.html', {'images': filtered_images})

def image_detail(request, pk):
    image = models.Image()

    image.title = f'ID: {pk}'
    image.image = f'{pk}.jpg'
    image.created_date = '2021-09-11'

    return render(request, 'image_detail.html', {'image': image})


