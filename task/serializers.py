# coding: utf-8


from .models import Task
from rest_framework import routers, serializers, viewsets
from rest_framework import exceptions

# Serializers define the API representation.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #read_only_fields = ( 'date',)
        # fields = '__all__' 输出所有模型
        # exclude = ('image',) 排除模型
        fields = ('q','a',"link","myfile","choice","myimg")
        extra_kwargs = {                    #额外参数 指定最大最小值
            'q': { 'required': True,'label':u"问题"},      #可使用的额外参数 label='阅读量', max_value=2147483647, min_value=0, required=True
            'a': { 'required': True,'max_length':5,'help_text': u'帮助介绍'},       #read_only=True   max_length=20
        }

    def validate_q(self, attrs):  ##validate+字段名进行序列验证
        if 's' not in attrs:
            raise serializers.ValidationError(u'必须包含s')
        return attrs
