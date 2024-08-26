# Generated by Django 5.0.6 on 2024-08-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('reply_no', models.IntegerField(primary_key=True, serialize=False)),
                ('writer', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('insert_date', models.DateTimeField(auto_now_add=True)),
                ('insert_user', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=10)),
                ('deleted', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Commu',
            fields=[
                ('doc_no', models.IntegerField(primary_key=True, serialize=False)),
                ('writer', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=255)),
                ('viewer', models.IntegerField(default=0)),
                ('write_date', models.DateTimeField()),
                ('reply_count', models.IntegerField(default=0)),
                ('like', models.IntegerField(default=0)),
                ('scrap', models.IntegerField(default=0)),
                ('insert_date', models.DateTimeField(auto_now_add=True)),
                ('insert_user', models.CharField(max_length=50)),
                ('deleted', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Comp',
            fields=[
                ('doc_no', models.IntegerField(primary_key=True, serialize=False)),
                ('writer', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=255)),
                ('viewer', models.IntegerField(default=0)),
                ('write_date', models.DateTimeField()),
                ('reply_count', models.IntegerField(default=0)),
                ('insert_date', models.DateTimeField(auto_now_add=True)),
                ('insert_user', models.CharField(max_length=50)),
                ('deleted', models.CharField(max_length=1)),
            ],
        ),
    ]
