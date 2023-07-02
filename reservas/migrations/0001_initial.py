# Generated by Django 4.0 on 2023-06-30 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admins', '0002_alter_habitacion_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('duracion', models.IntegerField()),
                ('estado', models.CharField(default='Activo', max_length=10)),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.habitacion')),
                ('huesped', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.huesped')),
            ],
            options={
                'ordering': ['estado', 'fecha'],
            },
        ),
    ]
