from rest_framework import serializers
from scholarships.models import Scholarship


class ScholarshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scholarship
        fields = (
            'id',
            'organization',
            'name'
        )
    
    def to_representation(self, instance):
        return {
            'id':  instance.id,
            'organization': {
                'id': instance.organization.id,
                'name_org': instance.organization.name_org
                },
            'name': instance.name,
        }


class ScholarshipOrgListSerializer(serializers.Serializer):
    class Meta:
        model = Scholarship
        fields = (
            'id',
            'name'
        )
