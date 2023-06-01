# Generated by Django 4.1.7 on 2023-03-05 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='id',
            field=models.BigAutoField(auto_created=True, default=12, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vital_signs',
            name='date',
            field=models.DateTimeField(default='12', null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='vital_signs',
            field=models.ForeignKey(default='12', null=True, on_delete=django.db.models.deletion.CASCADE, to='management.vital_signs'),
        ),
    ]