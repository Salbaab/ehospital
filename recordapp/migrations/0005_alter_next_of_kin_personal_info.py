# Generated by Django 3.2.7 on 2021-11-05 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recordapp', '0004_alter_patient_info_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='next_of_kin',
            name='personal_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recordapp.patient_info'),
        ),
    ]
