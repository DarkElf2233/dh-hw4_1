# Generated by Django 4.2.3 on 2023-07-11 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_studentteacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teachers',
        ),
    ]
