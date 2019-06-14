# Generated by Django 2.2.1 on 2019-06-12 17:36

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('government_id', models.CharField(max_length=20, verbose_name='Government ID')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('address1', models.CharField(max_length=100, verbose_name='Address 1')),
                ('address2', models.CharField(max_length=100, verbose_name='Address 2')),
                ('address_city', models.CharField(max_length=100, verbose_name='City')),
                ('address_zip_code', models.CharField(max_length=100, verbose_name='ZIP Code')),
                ('address_country', django_countries.fields.CountryField(max_length=2, verbose_name='Country')),
                ('country_of_citizenship', django_countries.fields.CountryField(max_length=2)),
                ('company', models.CharField(max_length=20, verbose_name='Company')),
                ('company_field_of_business', models.CharField(max_length=20, verbose_name='Company Field of Business')),
                ('company_state', models.CharField(max_length=20, verbose_name='State')),
                ('company_country', django_countries.fields.CountryField(max_length=2)),
                ('sns_facebook', models.CharField(max_length=20, verbose_name='Facebook ID')),
                ('sns_instagram', models.CharField(max_length=20, verbose_name='Instagram ID')),
                ('sns_twitter', models.CharField(max_length=20, verbose_name='Twitter ID')),
                ('sns_google', models.CharField(max_length=20, verbose_name='Google ID')),
                ('sns_linkedin', models.CharField(max_length=20, verbose_name='Linkedin ID')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
