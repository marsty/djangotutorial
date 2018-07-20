from rest_framework import serializers
from .models import Server,NetworkDevice,IP
from manufacturer.models import Manufacturer,ProductModel
class ServerAutoReportSerializer(serializers.Serializer):
    """
    服务器信息同步序列化
    """
    ip = serializers.IPAddressField(required=True)
    hostname = serializers.CharField(required=True,max_length=20)
    cpu = serializers.CharField(required=True,max_length=50)
    mem = serializers.CharField(required=True,max_length=20)
    disk = serializers.CharField(required=True,max_length=200)
    os = serializers.CharField(required=True,max_length=50)
    sn = serializers.CharField(required=True,max_length=50)
    manufacturer = serializers.CharField(required=True)
    model_name = serializers.CharField(required=True)
    uuid = serializers.CharField(required=True,max_length=50)
    network = serializers.JSONField(required=True)


    def validate_manufacturer(self,value):
        try:
            return Manufacturer.objects.get(vendor_name = value)
        except Manufacturer.DoesNotExist:
            return self.create_manufacturer(value)

    def validate(self, attrs):
        #network = attrs['network']
        manufacturer_obj = attrs['manufacturer']
        try:
            attrs['model_name'] = manufacturer_obj.productmodel_set.get(model_name = attrs['model_name'])
        except ProductModel.DoesNotExist:
            self.create_productmodel(manufacturer_obj,attrs['model_name'])
        return attrs


    def create(self, validated_data):
        network = validated_data.pop('network')
        obj = Server.objects.create(**validated_data)
        self.check_server_network_device(network,obj)
        return obj

    def update(self, instance, validated_data):
        instance.cpu = validated_data.get('cpu', instance.cpu)
        instance.mem = validated_data.get('mem', instance.mem)
        instance.disk = validated_data.get('disk', instance.disk)
        instance.os = validated_data.get('os', instance.os)
        instance.sn = validated_data.get('sn', instance.sn)
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.model_name = validated_data.get('model_name', instance.model_name)
        instance.uuid = validated_data.get('uuid', instance.uuid)
        instance.save()
        return  instance

    def check_server_network_device(self,network,obj):
        network_device_queryset = obj.networkdevice_set.all()
        for device in network:
            try:
                network_device_obj = network_device_queryset.get(name = device['name'])
            except NetworkDevice.DoesNotExist:
                self.create_network_device(obj,device)


    def check_ip(self,network_device_obj,ifnets):
        ip_queryset = network_device_obj.ip_set.all()
        for ifnet in ifnets:
            try:
                ip_obj = ip_queryset.get(ip_addr = ifnet['ip_addr'])
            except IP.DoesNotExist:
                self.create_ip(network_device_obj,ifnet)

    def create_ip(self,network_device_obj,ifnet):
        ifnet['device'] = network_device_obj
        return IP.objects.create(**ifnet)

    def create_network_device(self,obj,device):
        ips = device.pop('ips')
        device['host'] = obj
        network_device_obj = NetworkDevice.objects.create(**device)
        self.check_ip(network_device_obj,ips)
        return network_device_obj

    def create_productmodel(self,manufacturer_obj,model_name):
        return ProductModel.objects.create(model_name = model_name,vendor=manufacturer_obj)

    def create_manufacturer(self,vendor_name):
        return Manufacturer.objects.create(vendor_name= vendor_name)

    def to_representation(self, instance):
        ret = {
            "ip": instance.ip,
            "hostname": instance.hostname,
        }
        return ret
    class Meta:
      model = Server
      fields = ["ip","hostname","cpu","mem","disk","os","sn","manufacturer","model_name","uuid"]


class ServerSerializer(serializers.ModelSerializer):
    """
    服务器序列化
    """
    class Meta:
        model = Server
        fields = "__all__"

class NetworkDeviceSerializer(serializers.ModelSerializer):
    """
    网卡序列化
    """
    class Meta:
        model = NetworkDevice
        fields = "__all__"


class IPSerializer(serializers.ModelSerializer):
    """
    IP序列化
    """
    class Meta:
        model = IP
        fields = "__all__"