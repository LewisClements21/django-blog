# Generated by Django 4.2.14 on 2024-07-24 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_post_excerpt_post_updated_on_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]