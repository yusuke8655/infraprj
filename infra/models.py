from django.db import models

# Create your models here.
class Computer(models.Model):
    name = models.CharField('コンピューター名', max_length=20)
    cpu = models.CharField('CPU', max_length=20)
    memory_cap = models.IntegerField('メモリ容量', blank=True, null=True, default=0)
    strage_cap = models.IntegerField('ストレージ容量', blank=True, null=True, default=0)
    os = models.CharField('OS', max_length=20)
    created_at = models.DateTimeField('登録日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.name