# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class UserInfo(BaseModel):
    CHOICES = (
        (0, '男'),
        (1, '女')
    )

    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    sex = models.IntegerField(choices=CHOICES, default=0)
    email = models.EmailField(null=True)
    motto = models.CharField(max_length=64, null=True, default='博主很懒~~~ 什么也没写')
    avatar = models.ImageField(upload_to='img',default='img/default.jpg')
    github = models.URLField()
    addTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='user_info'
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username

