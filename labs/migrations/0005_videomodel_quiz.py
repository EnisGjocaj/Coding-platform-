# Generated by Django 4.1.7 on 2023-12-20 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
        ('labs', '0004_videomodel_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='videomodel',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='challenges.quiz'),
        ),
    ]
