# Generated by Django 3.2.7 on 2021-11-06 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recordapp', '0006_patient_info_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Command', models.CharField(blank=True, max_length=120, null=True)),
                ('presentUnit', models.TextField(blank=True, null=True)),
                ('personal_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordapp.patient_info')),
            ],
            options={
                'verbose_name_plural': 'Unit',
            },
        ),
    ]
