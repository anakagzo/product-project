# Generated by Django 4.2 on 2023-04-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='images/')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=225)),
                ('pub_date', models.DateTimeField()),
                ('body', models.CharField()),
            ],
        ),
    ]