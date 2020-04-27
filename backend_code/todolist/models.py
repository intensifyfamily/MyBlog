from django.db import models

class ToDo(models.Model):

    CHOICES = (
        (0, '未完成'),
        (1, '已完成')
    )
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=255)
    is_done = models.IntegerField(choices=CHOICES, default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table='todolist'
        verbose_name='待办事项'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title
