from django.db import models

# Create your models here.
class Warrior(models.Model):
    """
    Описание война
    """

    race_types = (
        ('s', 'student'),
        ('d', 'developer'),
        ('t', 'teamlead'),
    )
    race = models.CharField(max_length=1, choices=race_types, verbose_name='Расса')
    name = models.CharField(max_length=120, verbose_name='Имя')
    level = models.IntegerField(verbose_name='Уровень', default=0)
    skill = models.ManyToManyField('Skill', verbose_name='Умения', through='SkillOfWarrior')
    profession = models.ForeignKey('Profession', on_delete=models.SET_NULL, verbose_name='Профессия',
                                   blank=True, null=True)


class Profession(models.Model):
    """
    Описание профессии
    """

    title = models.CharField(max_length=120, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')


class Skill(models.Model):
    """
    Описание умений
    """

    title = models.CharField(max_length=120, verbose_name='Наименование', unique=True)

    def __str__(self):
        return self.title


class SkillOfWarrior(models.Model):
    """
    Описание умений война
    """

    skill = models.ForeignKey('Skill', verbose_name='Умение', on_delete=models.CASCADE, related_name="warriors")
    warrior = models.ForeignKey('Warrior', verbose_name='Воин', on_delete=models.CASCADE, related_name="skills")
    level = models.IntegerField(verbose_name='Уровень освоения умения')