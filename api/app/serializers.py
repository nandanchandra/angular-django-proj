from rest_framework import serializers
from api.app.models import Imageaws

class ImageawsSerializer(serializers.ModelSerializer):

    document = serializers.ImageField(required=False)

    class Meta:
        model = Imageaws
        fields = ['title','description','document']
