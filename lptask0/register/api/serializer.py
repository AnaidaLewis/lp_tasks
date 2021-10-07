from rest_framework import serializers
from task0.models import Item
from register.models import MyUser


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style = {'input_type': 'password'},write_only = True)
    class Meta:
        model = MyUser
        fields = ["username","email","password","password2"]
        extra_kwargs = {
            'password' : {'write_only' : True},
        }

    def save(self):
        my_user = MyUser(
            username = self.validated_data['username'],
            email = self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match!'})
        my_user.set_password(password)
        my_user.save()
        return my_user