# Generated by Django 4.1.4 on 2022-12-22 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0007_noticia_autor_noticia_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='comentario',
        ),
    ]
