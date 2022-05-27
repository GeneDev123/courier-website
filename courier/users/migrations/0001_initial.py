# Generated by Django 3.2.13 on 2022-05-27 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('account_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Account ID')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('user_address', models.CharField(max_length=150, verbose_name='Address')),
                ('user_contact', models.CharField(max_length=11, verbose_name='Contact Number')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('hide_email', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CourierPartner',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Company ID')),
                ('company_name', models.CharField(max_length=100, verbose_name='Company Name')),
                ('company_address', models.CharField(max_length=150, verbose_name='Company Address')),
                ('company_contact', models.CharField(max_length=11, verbose_name='Contact Number')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryPartner',
            fields=[
                ('partner_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Partner ID')),
                ('partner_name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('partner_email', models.EmailField(max_length=50, unique=True, verbose_name='Email')),
                ('partner_address', models.CharField(max_length=150, verbose_name='Address')),
                ('partner_contact', models.CharField(max_length=11, verbose_name='Contact Number')),
                ('partner_birthday', models.DateField(verbose_name='Birth Date')),
                ('partner_vehicle', models.CharField(max_length=50, verbose_name='Vehicle')),
                ('partner_gcash', models.CharField(max_length=11, verbose_name='GCash Number')),
                ('partner_license', models.CharField(max_length=20, unique=True, verbose_name="Driver's License")),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publication Date')),
            ],
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Update Price ID')),
                ('provincial_price_small', models.CharField(max_length=30, verbose_name='Provincial Price Small')),
                ('provincial_price_medium', models.CharField(max_length=30, verbose_name='Provincial Price Medium')),
                ('provincial_price_large', models.CharField(max_length=30, verbose_name='Provincial Price Large')),
                ('provincial_price_extra_large', models.CharField(max_length=30, verbose_name='Provincial Price Extra Large')),
                ('provincial_price_box', models.CharField(max_length=30, verbose_name='Provincial Price Box')),
                ('metro_manila_price_small', models.CharField(max_length=30, verbose_name='Metro Manila Price Small')),
                ('metro_manila_price_medium', models.CharField(max_length=30, verbose_name='Metro Manila Price Medium')),
                ('metro_manila_price_large', models.CharField(max_length=30, verbose_name='Metro Manila Price Large')),
                ('metro_manila_price_extra_large', models.CharField(max_length=30, verbose_name='Metro Manila Price Extra Large')),
                ('metro_manila_price_box', models.CharField(max_length=30, verbose_name='Metro Manila Price Box')),
                ('mega_manila_price_small', models.CharField(max_length=30, verbose_name='Mega Manila Price Small')),
                ('mega_manila_price_medium', models.CharField(max_length=30, verbose_name='Mega Manila Price Medium')),
                ('mega_manila_price_large', models.CharField(max_length=30, verbose_name='Mega Manila Price Large')),
                ('mega_manila_price_extra_large', models.CharField(max_length=30, verbose_name='Mega Manila Price Extra Large')),
                ('mega_manila_price_box', models.CharField(max_length=30, verbose_name='Mega Manila Price Box')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published Date')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('receiver_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Receiver ID')),
                ('receiver_name', models.CharField(blank=True, max_length=100, verbose_name='Receiver Full Name')),
                ('receiver_email', models.EmailField(blank=True, max_length=100, verbose_name='Receiver Email')),
                ('receiver_address', models.CharField(max_length=150, verbose_name='Receiver Address')),
                ('receiver_contact', models.CharField(max_length=11, verbose_name='Contact Number')),
                ('item_desc', models.TextField(max_length=250, verbose_name='Item Description')),
                ('item_value', models.CharField(max_length=30, verbose_name='Item Value')),
                ('item_size', models.CharField(choices=[('Small', 'SMALL'), ('Medium', 'MEDIUM'), ('Large', 'LARGE'), ('Extra Large', 'EXTRA LARGE'), ('Box', 'BOX')], default='SMALL', max_length=30, verbose_name='Pouch Size')),
                ('item_payment', models.CharField(choices=[('Paid by Sender', 'Paid by Sender'), ('COD (All Not Paid)', 'COD (All Not Paid)'), ('Paid by Receiver', 'Paid by Receiver'), ('COD (Items Not Paid)', 'COD (Items Not Paid)'), ('GCash', 'GCash'), ('Bank Transfer', 'Bank Transfer')], default='Cash on delivery', max_length=50, verbose_name='Payment method')),
                ('delivery_select', models.CharField(choices=[('Metro Manila', 'METRO MANILA'), ('Provincial', 'PROVINCIAL'), ('Mega Manila', 'MEGA MANILA')], default='METRO MANILA', max_length=50, verbose_name='Delivery Selection')),
                ('requested_pickup', models.DateField(verbose_name='Requested Date Pickup')),
                ('admin_approved', models.BooleanField(default=False, verbose_name='Admin Approved')),
                ('delivery_status', models.CharField(choices=[('On process', 'ON PROCESS'), ('Picked Up', 'PICKED UP'), ('Dispatched', 'DISPATCHED'), ('Delivered', 'DELIVERED'), ('Cancelled', 'CANCELLED'), ('Not Delivered', 'NOT DELIVERED'), ('Reschedule', 'RESCHEDULE'), ('Return to Sender', 'RETURN TO SENDER')], default='On process', max_length=100, verbose_name='Delivery Status')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publication Date')),
                ('tracking_number', models.CharField(default='05282022', max_length=50, verbose_name='Tracking Number')),
                ('courier_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courier_partner', to='users.courierpartner', verbose_name='Courier Partner')),
                ('delivery_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_partner', to='users.deliverypartner', verbose_name='Delivery Partner')),
                ('transactor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to=settings.AUTH_USER_MODEL, verbose_name='Account ID')),
            ],
        ),
    ]
