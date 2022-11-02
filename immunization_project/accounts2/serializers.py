from rest_framework import serializers
from accounts2.models import User, UserImmunization

        
class UserImmunizationSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False) #user id i.e. 1
    class Meta:
        model = UserImmunization
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    # tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    immunizations = UserImmunizationSerializer(read_only=True,many=True)
    class Meta:
        model = User
        fields='__all__'