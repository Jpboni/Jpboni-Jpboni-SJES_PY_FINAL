# Generated by Django 4.1.1 on 2022-12-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_course_facultykey_remove_course_studentkey'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
