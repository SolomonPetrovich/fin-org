from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import FinancialOrganization, FinancialOrganizationNews
from .serializers import (FinancialOrganizationNewsSerializer,
                          FinancialOrganizationSerializer)


def index(request):
    organizations = cache.get('organizations')
    news = cache.get('news')

    if not organizations:
        organizations = FinancialOrganization.objects.all()
        cache.set('organizations', organizations, timeout=60*15)

    if not news:
        news = FinancialOrganizationNews.objects.all()
        cache.set('news', news, timeout=60*15)

    return render(request, 'index.html', {'organizations': organizations, 'news': news})


def news_detail(request, news_id):
    try:
        news = FinancialOrganizationNews.objects.get(id=news_id)
    except FinancialOrganizationNews.DoesNotExist:
        return HttpResponse("News not found", status=404)

    return render(request, 'news-detail.html', {'news': news})


def organization_detail(request, organization_id):
    try:
        organization = FinancialOrganization.objects.get(id=organization_id)
        news = FinancialOrganizationNews.objects.filter(organization=organization)
    except FinancialOrganization.DoesNotExist:
        return HttpResponse("Organization not found", status=404)

    return render(request, 'detail.html', {'organization': organization, 'news': news})


class FinancialOrganizationViewSet(viewsets.ModelViewSet):
    queryset = FinancialOrganization.objects.all()
    serializer_class = FinancialOrganizationSerializer


class FinancialOrganizationNewsViewSet(viewsets.ModelViewSet):
    queryset = FinancialOrganizationNews.objects.all()
    serializer_class = FinancialOrganizationNewsSerializer
