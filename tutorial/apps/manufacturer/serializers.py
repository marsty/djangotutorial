from rest_framework import serializers
from .models import Manufacturer,ProductModel
class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = "__all__"


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = "__all__"

    def validate(self, attrs):
        print(attrs)
        m_obj= attrs["vendor"]
        try:
            m_obj.productmodel_set.get(model_name = attrs["model_name"])
            raise serializers.ValidationError("该型号已经存在")
        except ProductModel.DoesNotExist:
            return attrs

    def to_representation(self, instance):
        obj_ven = instance.vendor
        ret = super(ProductModelSerializer,self).to_representation(instance)
        ret['vendor'] = {
            "id" : obj_ven.id,
            "name": obj_ven.vendor_name
        }
        return ret