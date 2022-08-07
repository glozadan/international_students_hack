from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scholarships.models import Scholarship
from scholarships.serializers import ScholarshipSerializer

# Create your views here.

class ScholarshipView(APIView):
    def get(self, request):
        scholarships = Scholarship.objects.all()
        serializer = ScholarshipSerializer(scholarships, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)  

    def post(self, request):
        serializer = ScholarshipSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)   

class ScholarshipSingleView(APIView):
    def get(self, request, id):
        scholarship = Scholarship.objects.filter(id = id).first()
        if scholarship is None:
            return Response({'error': 'Bad Request'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = ScholarshipSerializer(scholarship)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def patch(self, request, id):
        scholarship = Scholarship.objects.filter(id = id).first()
        if Scholarship is None:
            return Response({'error': 'Bad Request.'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = ScholarshipSerializer(scholarship, data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)

    def delete(self, request, id):
        scholarship = Scholarship.objects.get(id = id)
        scholarship.delete()
        return Response({"msg": "Beca eliminada satisfactoriamente."}, status = status.HTTP_204_NO_CONTENT)
    