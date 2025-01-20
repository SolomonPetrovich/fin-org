from celery import shared_task
from .models import FinancialOrganizationNews, FinancialOrganization
import requests

@shared_task
def fetch_and_update_news():
    response = requests.get('https://api.example.com/financial-news')
    news_data = response.json()
    print('News fetched')
    # for item in news_data:
        # organization = FinancialOrganization.objects.filter(name=item['organization_name']).first()
        # if organization:
            # FinancialOrganizationNews.objects.create(
            #     title=item['title'],
            #     content=item['content'],
            #     organization=organization
            # )