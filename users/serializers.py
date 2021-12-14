from rest_framework import serializers

from .models import User, UserProfile

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)


    class Meta(object):
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password',
                  'is_active', 'is_superuser', 'is_staff', 'date_joined', 'last_login')
        read_only_fields = ('id', 'date_joined', 'last_login',
                            'is_active', 'is_superuser', 'is_staff')
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        # set password
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'first_name', 'last_name', 'email', 'phone', 'avatar', 'bio', 'gender']
        read_only_fields = ['id']