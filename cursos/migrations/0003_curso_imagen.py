# Generated by Django 4.1.13 on 2023-12-04 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_alter_curso_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='cursos/'),
        ),
    ]
