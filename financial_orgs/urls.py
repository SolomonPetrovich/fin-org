from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (FinancialOrganizationNewsViewSet,
                    FinancialOrganizationViewSet, index, news_detail,
                    organization_detail)

router = DefaultRouter()
router.register(r'organizations', FinancialOrganizationViewSet)
router.register(r'news', FinancialOrganizationNewsViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('<uuid:organization_id>/', organization_detail,
         name='organization_detail'),
    path('news/<uuid:news_id>/', news_detail, name='news_detail'),
    path('api/', include(router.urls)),
]
