# coding: utf-8


from account.models import MyUser,Role,Permission
from rest_framework import routers, serializers, viewsets
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError


# Serializers define the API representation.
class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        #read_only_fields = ( 'date',)
        # exclude = ('image',) 排除模型
        fields = '__all__'



class RoleListSerializer(serializers.ModelSerializer):
    """角色序列化"""
    class Meta:
        model = Role
        fields ="__all__"




class PermissionListSerializer(serializers.ModelSerializer):
    '''
    权限列表序列化
    '''

    class Meta:
        model = Permission
        fields = "__all__"


#登录序列器
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, error_messages={'blank': u'用户名不能为空'})
    password = serializers.CharField(
        style={'input_type': 'password'}, required=True, error_messages={'blank': u'密码不能为空'})

    def validate(self, attrs):
        username, password= attrs['username'], attrs['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError(u'用户名或者密码错误')
        attrs['user'] = user
        return attrs