from rest_framework.routers import DefaultRouter
from fjfundo.api.views import FundoViewSet

router = DefaultRouter()
router.register(r'fundo', FundoViewSet)
