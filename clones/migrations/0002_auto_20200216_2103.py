# Generated by Django 3.0.3 on 2020-02-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardlist',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='card',
            name='Attachment',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(blank=True, max_length=10),
        ),
    ]
