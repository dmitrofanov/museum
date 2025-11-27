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
    # groups = GroupSerializer(many=True, read_only=True)
    key = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    
    class Meta:
        model = Person
        fields = ['id', 'key', 'title']

    def get_title(self, obj):
        return f"{obj.rank} {obj.first_name}{' ' + obj.middle_name if obj.middle_name else ''} {obj.last_name}"

    def get_key(self, obj):
        group_id = self.context.get('group_id')
        if group_id is None:
            return obj.id
        return f"{group_id}-{obj.id}"

class GroupWithPersonsSerializer(serializers.ModelSerializer):
    """Сериализатор для группы с людьми"""
    children = serializers.SerializerMethodField()
    key = serializers.IntegerField(source='id', read_only=True)
    
    class Meta:
        model = Group
        fields = ['id', 'key', 'title', 'description', 'children']

    def get_children(self, obj):
        serializer = PersonListSerializer(
            obj.persons.all(),
            many=True,
            context={**self.context, 'group_id': obj.id}
        )
        return serializer.data

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