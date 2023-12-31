# Generated by Django 3.2 on 2023-12-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_total'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Тапсырыс', 'verbose_name_plural': 'Тапсырыстар'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Тапсырыс тауары', 'verbose_name_plural': 'Тапсырыс тауарлары'},
        ),
        migrations.AddField(
            model_name='order',
            name='card_cvv',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Карта cvv'),
        ),
        migrations.AddField(
            model_name='order',
            name='card_date',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Карта мерзімі'),
        ),
        migrations.AddField(
            model_name='order',
            name='card_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Карта нөмірі'),
        ),
        migrations.AddField(
            model_name='order',
            name='card_payment',
            field=models.BooleanField(default=False, verbose_name='Картамен төлем'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment12',
            field=models.BooleanField(default=False, verbose_name='Рассрочка 0:0:12'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=120, verbose_name='Мекен-жайы'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=30, verbose_name='Қала'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=40, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=75, verbose_name='Толық аты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Телефон'),
        ),
    ]
