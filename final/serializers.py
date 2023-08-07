from rest_framework import serializers
from finalapp.models import sample
class sample_data(serializers.ModelSerializer):
         class Meta:
                  model=sample
                  fields=['name','age','gender']