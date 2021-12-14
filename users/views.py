from rest_framework import viewsets
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from api_practice.utils import success_response
from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def create(self, request, *args, **kwargs):
        data = request.data
        # create user
        user_serializer = self.serializer_class(
            data=data, context=self.get_serializer_context())
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        # update user profile
        serializer = UserProfileSerializer(
            user.profile, data=request.data, context={'user': user})
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
        else:
            raise exceptions.ParseError(detail=serializer.errors)


        headers = self.get_success_headers(serializer.data)
        return success_response(detail="User Profile created successfully.", code=201, **serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            serializer = UserProfileSerializer(
                instance.profile, context={'request': self.request})
            return success_response(detail='Successfully fetched user profile', **serializer.data)
        except UserProfile.DoesNotExist:
            raise exceptions.NotFound(
                detail='User Profile does not exist for this user')

    @action(detail=False, permission_classes=[AllowAny], methods=['get', 'put'])
    def me(self, request):
        if request.method == 'GET':
            try:
                serializer = UserProfileSerializer(request.user.profile)
                return success_response(detail="User data fetched successfully", **serializer.data)
            except UserProfile.DoesNotExist:
                raise exceptions.NotFound(detail="User profile does not exist")
        elif request.method == 'PUT':
            try:
                serializer = UserProfileSerializer(
                    request.user.profile, data=request.data, context={'user': request.user})
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return success_response(detail="User profile updated successfully", **serializer.data)
            except UserProfile.DoesNotExist:
                raise exceptions.NotFound(detail="User profile does not exist")

    @action(detail=True, permission_classes=[AllowAny], methods=['get'])
    def profile(self, request, pk=None):
        instance = self.get_object()
        serializer = UserProfileSerializer(instance.profile)
        return success_response(detail="Profile data fetched successfully", **serializer.data)


