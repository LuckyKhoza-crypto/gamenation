from django.shortcuts import render, redirect
from .models import visit_count

# Create your views here.


def home(request):

    # get the current URL
    current_url = request.build_absolute_uri()

    # get the object or create it if it doesn't exist
    count_value, created = visit_count.objects.get_or_create(url=current_url)

    if not created:
        count_value.count += 1
        count_value.save()

    return render(request, 'home.html', {'count_value': count_value.count})
