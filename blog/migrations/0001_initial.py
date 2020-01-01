# Generated by Django 2.2.6 on 2020-01-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('date_pub', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
