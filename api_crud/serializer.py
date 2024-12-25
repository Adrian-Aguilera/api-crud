from rest_framework import serializers
from .models import usuario

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ['nombre', 'apellido', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.get('password')
        instancia = usuario(**validated_data)
        instancia.set_password(password)
        instancia.save()
        return instancia

class usuarioSerializerList(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ['id','nombre', 'apellido', 'email', 'password']