from django.db import models

# Create your models here.
class Announce(models.Model):
    doc_no = models.CharField(max_length=20, primary_key=True, null=False)
    writer = models.CharField(max_length=50, null=False)
    write_date = models.DateField(null=False)
    viewer = models.IntegerField(default=0, null=False)
    desc = models.CharField(max_length=255)
    insert_date = models.DateField(auto_now_add=True)
    insert_user = models.CharField(max_length=50)
    deleted = models.CharField(max_length=1)
    insert_std = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.doc_no


class Comment(models.Model):
    reply_no = models.IntegerField(primary_key=True, null=False)
    writer = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=255, null=False)
    date = models.DateTimeField
    insert_date = models.DateTimeField(auto_now_add=True)
    insert_user = models.CharField(max_length=50)
    type = models.CharField(max_length=10, null=False)
    deleted = models.CharField(max_length=1)

    def __str__(self):
        return self.reply_no


class Commu(models.Model):
    doc_no = models.IntegerField(primary_key=True, null=False)
    writer = models.CharField(max_length=255, null=False)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    viewer = models.IntegerField(null=False, default=0)
    write_date = models.DateTimeField(null=False)
    reply_count = models.IntegerField(null=False, default=0)
    like = models.IntegerField(null=False, default=0)
    scrap = models.IntegerField(null=False, default=0)
    insert_date = models.DateTimeField(auto_now_add=True)
    insert_user = models.CharField(max_length=50)
    deleted = models.CharField(max_length=1)

    def __str__(self):
        return self.doc_no


class Comp(models.Model):
    doc_no = models.IntegerField(primary_key=True, null=False)
    writer = models.CharField(max_length=255, null=False)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    viewer = models.IntegerField(null=False, default=0)
    write_date = models.DateTimeField(null=False)
    reply_count = models.IntegerField(null=False, default=0)
    insert_date = models.DateTimeField(auto_now_add=True)
    insert_user = models.CharField(max_length=50)
    deleted = models.CharField(max_length=1)

    def __str__(self):
        return self.doc_no
