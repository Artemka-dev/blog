# Generated by Django 2.2.6 on 2020-01-02 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_comment_is_liked'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_pub']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_pub']},
        ),
    ]