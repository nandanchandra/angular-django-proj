from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from api.app.models import Imageaws
from api.app.serializers import ImageawsSerializer

class AwsImageViewSet(viewsets.ModelViewSet):
    queryset = Imageaws.objects.all()
    serializer_class = ImageawsSerializer
    parser_classes = (MultiPartParser, FormParser)


    # def get_queryset(self):
    #     qs=Imageaws.objects.all()
    #     title =self.request.query_params.get('title')
    #     if title:
    #         qs = qs.filter(title__icontains=title)
    #     return qs