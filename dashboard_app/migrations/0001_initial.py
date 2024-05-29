# Generated by Django 5.0.4 on 2024-05-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(max_length=100)),
                ('intensity', models.FloatField()),
                ('sector', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('insight', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('start_year', models.CharField(max_length=100)),
                ('impact', models.CharField(max_length=100)),
                ('added', models.CharField(max_length=100)),
                ('published', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('relevance', models.FloatField(max_length=100)),
                ('pestle', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('likelihood', models.FloatField(max_length=100)),
            ],
        ),
    ]
