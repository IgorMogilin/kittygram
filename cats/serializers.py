from rest_framework import serializers

from cats.models import Cat, Owner, Achivment, AchievementCat


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achivment
        fields = ('id', 'name')


class CatSerializer(serializers.ModelSerializer):
    # owner = serializers.StringRelatedField(read_only=True)
    achievements = AchievementSerializer(many=True)

    def create(self, validated_data):
        achievements = validated_data.pop('achievements')
        cat = Cat.objects.create(**validated_data)
        for achievement in achievements:
            current_achievement, status = Achivment.objects.get_or_create(
                **achievement
            )
            AchievementCat.objects.create(
                achievement=current_achievement,
                cat=cat
            )
        return cat

    class Meta:
        model = Cat
        fields = ('name', 'color', 'birth_year', 'owner', 'achievements')


class OwnerSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'cats')
