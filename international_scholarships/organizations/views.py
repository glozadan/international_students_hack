from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from organizations.models import Organization
from organizations.serializers import OrganizationSerializer, OrgScholarshipListSerializer

# Create your views here.

class OrganizationView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)  

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)   

class OrganizationSingleView(APIView):
    def get(self, request, id):
        organization = Organization.objects.filter(id = id).first()
        if organization is None:
            return Response({'error': 'Bad Request'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = OrgScholarshipListSerializer(organization)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def patch(self, request, id):
        organization = Organization.objects.filter(id = id).first()
        if Organization is None:
            return Response({'error': 'Bad Request.'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = OrganizationSerializer(organization, data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)

    def delete(self, request, id):
        organization = Organization.objects.get(id = id)
        organization.delete()
        return Response({"msg": "Organización eliminada correctamente."}, status = status.HTTP_204_NO_CONTENT)
    