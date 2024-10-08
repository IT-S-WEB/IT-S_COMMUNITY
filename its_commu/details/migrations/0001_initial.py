# Generated by Django 5.0.6 on 2024-08-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Its_plan',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('schedule', models.CharField(max_length=100)),
                ('insert_date', models.DateField(auto_now_add=True)),
                ('insert_user', models.CharField(max_length=50)),
                ('deleted', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Its_prj',
            fields=[
                ('prj_no', models.IntegerField(primary_key=True, serialize=False)),
                ('member', models.CharField(max_length=255)),
                ('team', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('keyword', models.CharField(max_length=50)),
                ('viewer', models.IntegerField(default=0)),
                ('img', models.CharField(max_length=50)),
                ('insert_date', models.DateTimeField(auto_now_add=True)),
                ('insert_user', models.CharField(max_length=50)),
                ('deleted', models.CharField(max_length=1)),
            ],
        ),
    ]
