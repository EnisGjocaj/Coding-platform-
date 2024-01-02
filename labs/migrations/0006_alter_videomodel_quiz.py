# Generated by Django 4.1.7 on 2023-12-20 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
        ('labs', '0005_videomodel_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videomodel',
            name='quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='challenges.quiz'),
        ),
    ]
