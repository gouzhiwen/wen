# Generated by Django 2.0.1 on 2020-02-22 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('ord', models.IntegerField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'sys_menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True, unique=True)),
            ],
            options={
                'db_table': 'sys_role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysRoleMenus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.IntegerField(blank=True, null=True)),
                ('menu_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_role_menus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('auth_string', models.CharField(max_length=32)),
                ('nick_name', models.CharField(blank=True, max_length=20, null=True)),
                ('role_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_user',
                'managed': False,
            },
        ),
    ]
