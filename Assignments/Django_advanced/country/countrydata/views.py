from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
import json

from .models import Continent, Country


def continent_json(request, continent_code):
    all_continents = Continent.objects.all()
    my_dictionary = {}
    for continent in all_continents:
        if continent.code == continent_code:
            for country in continent.countries.all():
                my_dictionary[country.code] = country.name
            response = JsonResponse(my_dictionary)
            response.status_code = 200
            callback = request.GET.get('callback')
            if not callback:
                return HttpResponse(response, content_type="application/json")
            response =  '{0}({1})'.format(callback, response)
            return HttpResponse(response, content_type="application/javascript")

    raise Http404("Not implemented")

def country_json(request, continent_code, country_code):
    all_countries = Country.objects.all()
    for country in all_countries:
        if country.code == country_code:
            if country.continent.code == continent_code:
                area = country.area
                population = country.population
                capital = country.capital
                dictionary = dict([('area', area), ('population', population), ('capital', capital)])
                obj = json.dumps(dictionary, indent=4)
                response = JsonResponse(dictionary)
                response.status_code = 200
                callback = request.GET.get('callback')
                if not callback:
                    return HttpResponse(response, content_type="application/json")
                response =  '{0}({1})'.format(callback, response)
                return HttpResponse(response, content_type="application/javascript")

    raise Http404()
