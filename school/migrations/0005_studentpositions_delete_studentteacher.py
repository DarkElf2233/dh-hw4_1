# Generated by Django 4.2.3 on 2023-07-11 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_remove_student_teachers'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPositions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='school.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='school.teacher')),
            ],
        ),
        migrations.DeleteModel(
            name='StudentTeacher',
        ),
    ]
