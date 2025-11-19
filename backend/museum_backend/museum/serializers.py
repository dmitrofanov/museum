from rest_framework import serializers
import datetime
from .models import Person, PersonPhoto, Group

class GroupSerializer(serializers.ModelSerializer):
    key = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'key', 'title', 'description']

class PersonPhotoSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    key = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = PersonPhoto
        fields = ['id', 'key', 'photo_url', 'caption', 'is_main']

    def get_photo_url(self, obj):
        if obj.photo:
            return obj.photo.url
        return None

class PersonListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка людей (только основные данные)"""
    groups = GroupSerializer(many=True, read_only=True)
    key = serializers.IntegerField(source='id', read_only=True)
    
    class Meta:
        model = Person
        fields = ['id', 'key', 'first_name', 'middle_name', 'last_name', 'rank', 'gender', 'groups']

class GroupWithPersonsSerializer(serializers.ModelSerializer):
    """Сериализатор для группы с людьми"""
    children = PersonListSerializer(many=True, read_only=True, source='persons')
    key = serializers.IntegerField(source='id', read_only=True)
    
    class Meta:
        model = Group
        fields = ['id', 'key', 'title', 'description', 'children']

class PersonDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной информации о человеке"""
    photos = PersonPhotoSerializer(many=True, read_only=True)
    groups = GroupSerializer(many=True, read_only=True)
    # age = serializers.SerializerMethodField()
    key = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Person
        fields = [
            'id', 'key', 'rank', 'first_name', 'middle_name', 'last_name', 'birth_year', 'death_year',
            'job_title', 'work_start_year', 'work_end_year', 'gender', 'description', 'photos', 'groups'
        ]
    
    # def get_age(self, obj):
    #     if obj.birth_year:
    #         today = datetime.date.today()
    #         return today.year - obj.birth_year
    #     return None