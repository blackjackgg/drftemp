# coding: utf-8


from .models import Ask
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class AskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ask
        #read_only_fields = ( 'date',)
        # fields = '__all__' 输出所有模型
        # exclude = ('image',) 排除模型
        fields = ('q','a',"link")
        extra_kwargs = {                    #额外参数 指定最大最小值
            'q': { 'required': True,'label':u"问题"},      #可使用的额外参数 label='阅读量', max_value=2147483647, min_value=0, required=True
            'a': { 'required': True,'max_length':5},       #read_only=True   max_length=20
            'link':{'read_only':True}
        }
