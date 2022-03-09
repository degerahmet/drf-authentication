from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate
from django.contrib.auth.password_validation import validate_password



UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','first_name','last_name','email','username')
        extra_kwargs = {'email': {'read_only': True},'username': {'read_only': True}}


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3,required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = UserModel
        fields = ('username','password')

    def validate(self,data):

        username = data.get('username', None)
        password = data.get('password', None)
        
        if username is None:
            raise serializers.ValidationError(
                'An username is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=username, password=password)
        

        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return user

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=3, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = UserModel
        fields = ('first_name','last_name','email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self,email):
        user = UserModel.objects.filter(email=email).first()
        if user:
            raise serializers.ValidationError({"email":"Email already signed up."})
        return email
        
    def validate_username(self,username):
        user = UserModel.objects.filter(username=username).first()
        if user:
            raise serializers.ValidationError({"email":"Email already signed up."})
        return username

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True,required=True)
    password = serializers.CharField(write_only=True,required=True)
    password2 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = UserModel
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"Password fields didn't match."})
        return attrs
    
    def validate_password(self,value):
        validate_password(value)
        return value
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
