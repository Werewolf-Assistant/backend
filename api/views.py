from rest_framework import viewsets

from .models import Uratha
from .serializers import UrathaSerializer


class UrathaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Urathas to be viewed or edited.
    """
    queryset = Uratha.objects.all()
    serializer_class = UrathaSerializer
