from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название группы')
    description = models.TextField(verbose_name='Описание', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['name']

    def __str__(self):
        return self.name

class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    rank = models.CharField(max_length=100, verbose_name='Сан')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    birth_year = models.IntegerField(verbose_name='Дата рождения')
    death_year = models.IntegerField(verbose_name='Дата смерти', null=True, blank=True)
    job_title = models.CharField(max_length=100, verbose_name='Должность')
    work_start_year = models.IntegerField(verbose_name='Дата начала работы', null=True, blank=True)
    work_end_year = models.IntegerField(verbose_name='Дата окончания работы', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    description = models.TextField(verbose_name='Описание', blank=True)
    groups = models.ManyToManyField(Group, related_name='persons', verbose_name='Группы', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['last_name', 'first_name', 'middle_name']

    def __str__(self):
        return f"{self.rank} {self.last_name} {self.first_name} {self.middle_name}"

class PersonPhoto(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='people_photos/', verbose_name='Фотография')
    caption = models.CharField(max_length=200, verbose_name='Подпись', blank=True)
    is_main = models.BooleanField(default=False, verbose_name='Основная фотография')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['-is_main', 'uploaded_at']

    def __str__(self):
        return f"Фото {self.person.last_name}"