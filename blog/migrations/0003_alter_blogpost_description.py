# Generated by Django 5.0.2 on 2024-02-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_language_blogpost_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
