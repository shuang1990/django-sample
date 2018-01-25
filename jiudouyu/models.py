from django.db import models

# Create your models here.

class AuthCard(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID', default=0)
    bank_id = models.SmallIntegerField(verbose_name='银行ID', default=0)
    card_number = models.CharField(verbose_name='银行卡号', max_length=30, default='', unique=True)
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'core_auth_card'
        verbose_name = '绑定银行卡'
        verbose_name_plural = verbose_name
        app_label = 'jiudouyu'
        indexes = [
            models.Index(fields=['user_id'], name='idx_user_id')
        ]



class Bank(models.Model):
    name = models.CharField(verbose_name='银行名称', max_length=30, default='', unique=True)
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'core_bank'
        verbose_name = '银行信息'
        verbose_name_plural = verbose_name


class BankCard(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID', default=0)
    bank_id = models.SmallIntegerField(verbose_name='银行ID', default=0)
    card_number = models.CharField(verbose_name='银行卡号', max_length=30, default='', unique=True)
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'core_bank_card'
        verbose_name = '提现银行卡'
        verbose_name_plural = verbose_name

        indexes = [
            models.Index(fields=['user_id'], name='idx_user_id')
        ]


class CreditAssignProject(models.Model):
    project_id = models.IntegerField(verbose_name='原项目ID', default=0)
    invest_id = models.IntegerField(verbose_name='投资ID', default=0)
    user_id = models.IntegerField(verbose_name='用户ID', default=0)
    total_amount = models.DecimalField(verbose_name='总金额', max_digits=20, decimal_places=2, default=0)
    invested_amount = models.DecimalField(verbose_name='已投金额', max_digits=20, decimal_places=2, default=0)
    end_at = models.DateField(verbose_name='项目完结日', auto_now_add=True)
    status = models.SmallIntegerField(verbose_name='项目状态', default=100)
    serial_number = models.IntegerField(verbose_name='每天不重复的编号', default=0)
    app_type = models.SmallIntegerField(verbose_name='App来源')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'core_credit_assign_project'
        verbose_name = '债权项目'
        verbose_name_plural = verbose_name

        indexes = [
            models.Index(fields=['project_id'], name='idx_project_id'),
            models.Index(fields=['invest_id'], name='idx_invest_id'),
            models.Index(fields=['user_id'], name='idx_user_id'),
        ]


class CurrentAccount(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID', default=0)
    cash = models.DecimalField(verbose_name='账户总金额', max_digits=20, decimal_places=2, default=0)
    interest = models.DecimalField(verbose_name='总利息', max_digits=20, decimal_places=2, default=0)
    yesterday_interest = models.DecimalField(verbose_name='昨日利息', max_digits=10, decimal_places=2, default=0)
    interested_at = models.DateTimeField(verbose_name='计算日期', auto_now_add=True)
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'core_current_account'
        verbose_name = '活期账户'
        verbose_name_plural = verbose_name

        indexes = [
            models.Index(fields=['user_id'], name='idx_user_id'),
        ]


class CurrentInterestHistory(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID', default=0)
    rate = models.DecimalField(verbose_name='利率', max_digits=5, decimal_places=2, default=0)
    interest = models.DecimalField(verbose_name='利息', max_digits=10, decimal_places=2, default=0)
    principal = models.DecimalField(verbose_name='本息', max_digits=20, decimal_places=2, default=0)
    interest_date = models.DateField(verbose_name='计算日期', auto_now_add=True)
    type = models.SmallIntegerField(verbose_name='利息来源', default=1)
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'core_current_interest_history'
        verbose_name = '活期收益记录'
        verbose_name_plural = verbose_name

        indexes = [
            models.Index(fields=['user_id', 'interest_date', 'type'], name='idx_user_date_type'),
            models.Index(fields=['created_at'], name='idx_created_at'),
        ]


class CurrentPrincipal(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID', default=0, unique=True)
    principal = models.DecimalField(verbose_name='截止今日0点的活期账户金额', max_digits=20, decimal_places=2, default=0)
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'core_current_principal'
        verbose_name = '活期待收'
        verbose_name_plural = verbose_name


class TermPrincipal(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID', default=0, unique=True)
    principal = models.DecimalField(verbose_name='截止今日0点的定期待收本金', max_digits=20, decimal_places=2, default=0)
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'core_term_principal'
        verbose_name = '定期待收'
        verbose_name_plural = verbose_name


class FundHistory(models.Model):
    user_id = models.IntegerField(verbose_name='用户ID', default=0)
    balance_before = models.DecimalField(verbose_name='变更前金额', max_digits=20, decimal_places=2, default=0)
    balance_change = models.DecimalField(verbose_name='变更额', max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(verbose_name='变更后金额', max_digits=20, decimal_places=2, default=0)
    event_id = models.SmallIntegerField(verbose_name='事件id', default=1)
    note = models.CharField(verbose_name='备注', max_length=100, default='')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'core_fund_history'
        verbose_name = '资金流水'
        verbose_name_plural = verbose_name

        indexes = [
            models.Index(fields=['user_id', 'event_id'], name='idx_user_event'),
            models.Index(fields=['created_at'], name='idx_created_at'),
        ]


class Invest(models.Model):
    project_id = models.IntegerField(verbose_name='项目ID', default=0)
    assign_project_id = models.IntegerField(verbose_name='债转项目ID', default=0)
    user_id = models.IntegerField(verbose_name='用户ID', default=0)
    cash = models.DecimalField(verbose_name='投资金额', max_digits=20, decimal_places=2, default=0)
    invested_amount = models.DecimalField(verbose_name='已投金额', max_digits=20, decimal_places=2, default=0)
    is_match = models.SmallIntegerField(verbose_name='是否匹配', default=100)
    invest_type = models.SmallIntegerField(verbose_name='投资来源', default=0)
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'core_invest'
        verbose_name = '投资记录'
        verbose_name_plural = verbose_name

        indexes = [
            models.Index(fields=['project_id'], name='idx_project_id'),
            models.Index(fields=['created_at'], name='idx_created_at'),
            models.Index(fields=['user_id'], name='idx_user_id'),
            models.Index(fields=['assign_project_id'], name='idx_assign_project_id'),
        ]

class Order(models.Model):
    order_id = models.CharField(verbose_name='订单编号', max_length=32, unique=True, default='')
    user_id = models.IntegerField(verbose_name='用户ID', default=0)
    cash = models.DecimalField(verbose_name='金额', max_digits=20, decimal_places=2, default=0)
    handling_fee = models.DecimalField(verbose_name='手续费', max_digits=10, decimal_places=2, default=0)
    status = models.SmallIntegerField(verbose_name='订单状态', default=300)
    success_time = models.DateTimeField(verbose_name='处理成功时间')
    type = models.SmallIntegerField(verbose_name='订单状态', default=1)
    random = models.CharField(max_length=8, default='0')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'core_order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name

        indexes = [
            models.Index(fields=['created_at'], name='idx_created_at'),
            models.Index(fields=['user_id'], name='idx_user_id'),
        ]


class OrderExtend(models.Model):
    order_id = models.CharField(verbose_name='订单编号', max_length=32, unique=True, default='')
    bank_id = models.SmallIntegerField(verbose_name='银行ID', default=0)
    card_number = models.CharField(verbose_name='银行卡号', max_length=30, default='', unique=True)
    trade_no = models.CharField(verbose_name='交易流水号', max_length=30, default='', unique=True)
    type = models.SmallIntegerField(verbose_name='支付渠道', default=0)
    note = models.CharField(verbose_name='订单备信息', max_length=200, default='')
    app_request = models.SmallIntegerField(verbose_name='三端来源', default='')
    abnormal = models.BooleanField(verbose_name='账户资金流水是否异', default=0)
    app_type = models.SmallIntegerField(verbose_name='App来源')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'core_order_extend'
        verbose_name = '订单扩展表'
        verbose_name_plural = verbose_name

        indexes = [
            models.Index(fields=['created_at'], name='idx_created_at'),
        ]

class RefundRecord(models.Model):
    project_id = models.IntegerField(verbose_name='项目ID', default=0)
    invest_id = models.IntegerField(verbose_name='投资ID', default=0)
    user_id = models.IntegerField(verbose_name='用户ID', default=0)
    principal = models.DecimalField(verbose_name='本金', max_digits=20, decimal_places=2, default=0)
    interest = models.DecimalField(verbose_name='总利息', max_digits=20, decimal_places=2, default=0)
    cash = models.DecimalField(verbose_name='本息', max_digits=20, decimal_places=2, default=0)
    times = models.DateField(verbose_name='还款日')
    status = models.SmallIntegerField(verbose_name='还款状态', default=300)
    before_refund = models.SmallIntegerField(verbose_name='是否提前还款', default=0)
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'core_refund_record'
        verbose_name = '用户回款记录表'
        verbose_name_plural = verbose_name

        indexes = [
            models.Index(fields=['created_at'], name='idx_created_at'),
            models.Index(fields=['user_id'], name='idx_user_id'),
            models.Index(fields=['times'], name='idx_times'),
            models.Index(fields=['project_id'], name='idx_project_id'),
        ]

class User(models.Model):
    phone = models.CharField(verbose_name='手机号', max_length=11, unique=True, default='')
    password_hash = models.CharField(verbose_name='密码', max_length=65, default='')
    trading_password = models.CharField(verbose_name='交易密码', max_length=65, default='')
    balance = models.DecimalField(verbose_name='账户余额', max_digits=20, decimal_places=2, default=0)
    status_code = models.SmallIntegerField(verbose_name='用户状态', default=200)
    real_name = models.CharField(verbose_name='姓名', max_length=30, default='')
    identity_card = models.CharField(verbose_name='身份证号', max_length=25, default='')
    note = models.CharField(verbose_name='备注', max_length=50, default='')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'core_user'
        verbose_name = '用户列表'
        verbose_name_plural = verbose_name

        indexes = [
            models.Index(fields=['created_at'], name='idx_created_at'),
            models.Index(fields=['identity_card'], name='idx_identity_card'),
        ]