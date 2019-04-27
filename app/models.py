from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=64,verbose_name='名前')



    def __str__(self):
        return self.name



class CodeModel(models.Model):
    date = models.DateTimeField(auto_now_add=True,verbose_name='投稿時間')
    title = models.CharField(max_length=128,verbose_name='タイトル')
    text = models.TextField(max_length=1024,verbose_name='テキスト')
    tags = models.ManyToManyField(Tag,blank=True,related_name='tag')
    name = models.CharField(max_length=64,)

    class Meta:
        ordering = ('-date',)


    def __str__(self):
        return self.title
