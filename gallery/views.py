from django.shortcuts import render, get_object_or_404


# Необхідно додати до аплікації gallery дві views.
#  - призначення: відображає зображення, які були створені в останній місяць.
#  - назва view: gallery_view
#  - шаблон: gallery.html

#  Add views.gallery_view
#  Add views.image_detail

def gallery_view(request):
    return render(request, 'gallery.html')

def image_detail(request, pk):
    return render(request, 'image_detail.html')

