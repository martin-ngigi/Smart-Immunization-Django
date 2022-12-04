from rest_framework import serializers
from accounts2.models import User, UserImmunization

        
class UserImmunizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImmunization
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    immunizations = UserImmunizationSerializer(read_only=True,many=True)
    class Meta:
        model = User
        fields='__all__'