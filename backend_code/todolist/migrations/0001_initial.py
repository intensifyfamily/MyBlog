# Generated by Django 2.2 on 2020-04-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('content', models.CharField(max_length=255)),
                ('is_done', models.IntegerField(choices=[(0, '未完成'), (1, '已完成')], default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('finish_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '待办事项',
                'verbose_name_plural': '待办事项',
                'db_table': 'todolist',
            },
        ),
    ]
