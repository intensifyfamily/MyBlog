# Generated by Django 2.2 on 2020-04-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('sex', models.IntegerField(choices=[(0, '男'), (1, '女')], default=0)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('motto', models.CharField(default='博主很懒~~~ 什么也没写', max_length=64, null=True)),
                ('avatar', models.ImageField(default='default.jpg', upload_to='img')),
                ('github', models.URLField()),
                ('addTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user_info',
            },
        ),
    ]
