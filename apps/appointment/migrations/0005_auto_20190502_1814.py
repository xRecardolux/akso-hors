# Generated by Django 2.0.3 on 2019-05-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_appointment_order_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='order_no',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='订单号'),
        ),
    ]
