from rest_framework import serializers
from map.models import House, Company

class HouseSerializer(serializers.ModelSerializer):
    # comp_name = serializers.CharField(source='Company.comp_name', read_only=True)
    class Meta:
        model = House
        # fields = ('id','house_addr', 'geo_lat', 'geo_lon', 'comp_id')
        fields = all
    # house_addr = serializers.CharField(max_length=120)
    # comp_id = serializers.CharField()
    # geo_lat = serializers.FloatField()
    # geo_lon = serializers.FloatField()

class CompanySerializer(serializers.ModelSerializer):
    # comp_name = serializers.CharField()
    # comp_house_count=IntegerField()
    # Houses = HouseSerializer(many=True)
    class Meta:
        model=Company
        fields = ('id','comp_name', 'comp_house_count')
        # fields = ('id','comp_name', 'comp_house_count', 'Houses')
