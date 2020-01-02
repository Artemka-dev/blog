# Generated by Django 2.2.6 on 2020-01-02 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название комментария')),
                ('desc', models.TextField(verbose_name='Описание комментария')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, db_index=True, verbose_name='Тело поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Название поста'),
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.Comment'),
        ),
    ]
