from rest_framework.routers import DefaultRouter
from fjfundo.mensalidades.views import FundoViewSet

router = DefaultRouter()
router.register(r'fundo', FundoViewSet)
