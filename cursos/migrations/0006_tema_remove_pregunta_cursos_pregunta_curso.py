# Generated by Django 4.1.13 on 2023-12-05 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_alter_curso_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='temas/')),
            ],
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='cursos',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cursos.curso'),
        ),
    ]
