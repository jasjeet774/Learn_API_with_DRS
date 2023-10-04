from rest_framework import serializers
from api.models import Company, Employee

# Serializer is used to convert the complex data type into json or xml for API refrences
# serializers.HyperlinkedModelSerializer is used to working with model instances and creating hyperlinks to related resources.
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model = Company  
        fields = "__all__"


class EmployeeSerialzer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"        