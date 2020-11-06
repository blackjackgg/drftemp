# coding: utf-8


from .models import {a}
from rest_framework import routers, serializers, viewsets
from rest_framework import exceptions

# Serializers define the API representation.
class {a}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {a}
        #read_only_fields = ( 'date',)
        fields = '__all__' #输出所有模型
        # exclude = ('image',) 排除模型


    # def validate_q(self, attrs):  ##validate+字段名进行序列验证
    #     if 's' not in attrs:
    #         raise serializers.ValidationError(u'必须包含s')
    #     return attrs
