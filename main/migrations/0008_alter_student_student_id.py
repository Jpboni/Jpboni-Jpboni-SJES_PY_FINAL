# Generated by Django 3.2.4 on 2022-12-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_faculty_password_alter_faculty_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]