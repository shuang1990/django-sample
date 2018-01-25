# Generated by Django 2.0.1 on 2018-01-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jiudouyu', '0002_delete_authcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, verbose_name='用户ID')),
                ('bank_id', models.SmallIntegerField(default=0, verbose_name='银行ID')),
                ('card_number', models.CharField(default='', max_length=30, unique=True, verbose_name='银行卡号')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '绑定银行卡',
                'verbose_name_plural': '绑定银行卡',
                'db_table': 'core_auth_card',
            },
        ),
        migrations.AddIndex(
            model_name='authcard',
            index=models.Index(fields=['user_id'], name='idx_user_id'),
        ),
    ]