# Generated by Django 4.2.7 on 2023-11-30 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_post_slug_post_introducao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='introducao',
            field=models.TextField(blank=True),
        ),
    ]