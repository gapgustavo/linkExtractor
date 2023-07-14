from rest_framework import serializers
from search.models import Search

class DateTimeFieldWithTZ(serializers.DateTimeField):
    def to_representation(self, value):
        value = self.enforce_timezone(value)
        return super().to_representation(value)

class SearchSerializer(serializers.ModelSerializer):
    date = DateTimeFieldWithTZ(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Search
        fields = '__all__'
