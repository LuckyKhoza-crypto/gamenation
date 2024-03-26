from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse

from .models import visit_count


from .models import TrafficSource, TrafficSourceResource

from .serializer import TrafficSourceSerializer

import pandas as pd

from rest_framework.response import Response
from rest_framework import generics
from django.views.generic import View
from rest_framework.views import APIView


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


class ImportTrafficSource(generics.GenericAPIView):

    # overrides the serializer class
    serializer_class = TrafficSourceSerializer

    def post(self, request):

        # get the file from the request
        file = request.FILES['excel']

        # read the file using pandas
        df = pd.read_excel(file, engine='openpyxl')

        # rename the columns to match the model fields
        df.rename(
            columns={
                'Traffic source': 'traffic_source',
                'Views': 'views',
                'Watch time (hours)': 'watch_time',
                'Average view duration': 'average_view_duration',
                'Impressions': 'impressions',
                'Impressions click-through rate (%)': 'impressions_clicks',
            }, inplace=True
        )

        for index, row in df.iterrows():

            # get the default values
            default = row.to_dict()

            # get the object or create it if it doesn't exist, ensure that the traffic_source is unique
            traffic_source = default.pop('traffic_source', None)

            TrafficSource.objects.update_or_create(
                traffic_source=traffic_source, defaults=default)

        return Response({"status": "success"})

# query the data from the api and prepare it for pie chart display


class traffic_source_visual(View):

    def get(self, request):

        traffic_data = {}

        api_url = 'https://gamenation-production.up.railway.app/api/'

        response = requests.get(api_url)

        if response.status_code == 200:

            # x elements for graph
            x_elements = []

            # y elements for graph
            y_elements = []

            # the data returned from the api
            traffic_data = response.json()

            # iterate over the data and append the values to the x and y elements
            for source, data in traffic_data.items():

                # append the y and x elements to their arrays
                x_elements.append(source)
                y_elements.append(data['views'])  # only views are considered
            x_elements.pop(0)
            y_elements.pop(0)

        else:
            traffic_data = {'error': 'An error occurred'}

        return render(request, 'traffic_source_visual.html', {'x_elements': x_elements, 'y_elements': y_elements})


# returns the data from the api using django rest framework
class traffic_source_api(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):

        data = {}

        for source in TrafficSource.objects.all():

            data[source.traffic_source] = {
                'views': source.views,
                'watch_time': source.watch_time,
                'average_view_duration': source.average_view_duration,
                'impressions': source.impressions,
                'impressions_clicks': source.impressions_clicks
            }

        return Response(data)
