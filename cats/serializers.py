import datetime as dt
import webcolors
from rest_framework import serializers

from cats.models import Cat, Owner, Achivment, AchivmentCat, CHOICES


class Hex2name(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        try:
            data = webcolors.hex_to_name(data)
        except ValueError:
            raise serializers.ValidationError('НЕТ ТАКОГО ЦВЕТА!')
        return data


class AchivmentSerialaizer(serializers.ModelSerializer):
    achivment_name = serializers.CharField(source='name')

    class Meta:
        model = Achivment
        fields = ('achivment_name',)


class CatSerializer(serializers.ModelSerializer):
    achivments = AchivmentSerialaizer(many=True, required=False)
    age = serializers.SerializerMethodField()
    color = serializers.ChoiceField(choices=CHOICES)

    def create(self, validated_data):
        if 'achivments' not in self.initial_data:
            cat = Cat.objects.create(**validated_data)
            return cat
        achivments = validated_data.pop('achivments')
        cat = Cat.objects.create(**validated_data)
        for achivment in achivments:
            temp_achivment, status = Achivment.objects.get_or_create(
                **achivment
            )
            AchivmentCat.objects.create(
                achivment=temp_achivment,
                cat=cat
            )
        return cat

    def get_age(self, obj):
        return dt.datetime.now().year - obj.birth_year

    class Meta:
        model = Cat
        fields = ('name', 'color', 'birth_year', 'owner', 'achivments', 'age')


class OwnerSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'cats')
