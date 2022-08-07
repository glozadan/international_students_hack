from rest_framework import serializers
from organizations.models import Organization
from scholarships.models import Scholarship
from scholarships.serializers import ScholarshipOrgListSerializer


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


class OrgScholarshipListSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = (
            'id',
            'name_org',
            'name'  #Scholarshipname
        )
    
    def get_name(self, obj):
        selected_name = Scholarship.objects.filter(place__id = obj.id)
        return ScholarshipOrgListSerializer(selected_name, many = True).data

