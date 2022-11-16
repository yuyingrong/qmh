# Generated by Django 2.2.24 on 2021-06-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qmh', '0010_auto_20210625_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Present Age.'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ageAtFirstAttack',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Age at First Attack.'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dateOfDischargeOrDeath',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Date of Discharge or Death.'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='numPreviousAttacks',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Number of Previous Attacks.'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='numberInOrderOfAdmission',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Number in Order of Admission'),
        ),
    ]
