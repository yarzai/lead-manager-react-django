from rest_framework import viewsets, permissions
from .models import Lead
from .serializers import LeadSerializer

# Lead Viewsets


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = LeadSerializer
