from .models import MyUser, UserManager, Profile
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import pysnooper

UserModel = get_user_model()

class UserSerializer (serializers.ModelSerializer):

    #profile = ProfileSerializer(required=True)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data.get('password'):
            validated_data['password'] = make_password(
                validated_data['password']
            )

        user = get_user_model().objects.create(**validated_data)
        Token.objects.create(user=user)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    #extra_kwargs = {'password': {'write_only': True}}

class LogoutSerializer(serializers.Serializer):
    logout = serializers.BooleanField()

@pysnooper.snoop('/home/lisa/otus/StaryProfil.log')
class ProfileSerializer (serializers.ModelSerializer):


    #user = serializers.CharField()
    name = serializers.CharField(source='user.username')# dla geta ostavit
    image = serializers.ImageField(use_url=True, required=False)


    # def get_image(self, obj):
    #     request = self.context.get('request')
    #     image_url = obj.image.url
    #     return request.build_absolute_uri(image_url)

    def update(self, instance, validated_data):
        #profile = instance
        #myuser = UserSerializer(required=True)
        #profile_data = self.validated_data.pop('profile')

        #new_name = validated_data.get('name')
        #mauser = instance.u
        myuser = instance.user
        myusername = validated_data.get('user', instance.user)
        #id = MyUser.objects.filter(myuser.email)
        myuser.username = myusername.get('username', myuser.username)
        #myuser.username = validated_data.get('name', myuser.username)
        #myuser_username = validated_data.get('name', myuser.username)
        # myuser.objects.update ('username', myuser_username)
        #MyUser.objects.myuser.update()

        myuser.save()
        # instance.email = validated_data.get('email', instance.email)
        # # instance.first_name = validated_data.get('first_name', instance.first_name)
        # # instance.last_name = validated_data.get('last_name', instance.last_name)
        # instance.save()

        instance.bio = validated_data.get('bio', instance.bio)
        #instance.image = validated_data.get('image', profile.image)
        instance.save()

        return instance

    class Meta:
        model = Profile
        fields = ('name', 'bio', 'image')




@pysnooper.snoop('/home/lisa/otus/Updateprofile1.log')
class AddProfileSerializer(serializers.ModelSerializer):
    #tam ego netusername = serializers.CharField()
    profile = ProfileSerializer(required=True)

    def update(self, instance, validated_data):


        #v viewsvalidated_data = self.check(request, ProfileSerializer)
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        print(instance.email)
        instance.username = validated_data.get('username', instance.username)

        # instance.first_name = validated_data.get('first_name', instance.first_name)
        # instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        profile.bio = profile_data.get('bio', profile.bio)
        # profile.location = profile_data.get('location', profile.location)
        profile.image = profile_data.get('image', profile.image)
        profile.save()

        return instance

    class Meta():
        model = MyUser
        fields = (
            'username', 'email', 'profile'

        )


