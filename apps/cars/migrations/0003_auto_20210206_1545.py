# Generated by Django 3.1.6 on 2021-02-06 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_remove_car_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating_car',
            field=models.ForeignKey(help_text='Car model that is rated by a user', on_delete=django.db.models.deletion.CASCADE, related_name='car_rating', to='cars.car', verbose_name='Car'),
        ),
        migrations.AlterUniqueTogether(
            name='car',
            unique_together={('car_make', 'car_model')},
        ),
    ]
