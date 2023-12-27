# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime

from django.utils import timezone
from django.db import models


class AscendexMarket(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ascendex_markets'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BilaxyMarket(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'bilaxy_markets'


class BitrueMarket(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitrue_markets'


class BitgetMarket(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitget_markets'


class BkexMarket(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bkex_markets'


class GateMarket(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gate_markets'


class KucoinMarket(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kucoin_markets'


class MexcMarket(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mexc_markets'


class ComparePair(models.Model):
    token = models.CharField(unique=True, max_length=20)
    contract = models.CharField(max_length=100)
    decimals = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField()
    tsymbol = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compare_pairs'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HitbtcMarket(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'hitbtc_markets'


class HotbitMarket(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'hotbit_markets'


class IdexMarket(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'idex_markets'


class PoolsSushi(models.Model):
    pool_contract = models.CharField(max_length=500)
    token0_contract = models.CharField(max_length=500)
    token0_symbol = models.CharField(max_length=500)
    token0_decimals = models.CharField(max_length=500)
    token1_contract = models.CharField(max_length=500)
    token1_symbol = models.CharField(max_length=500)
    token1_decimals = models.CharField(max_length=500)
    is_active = models.BooleanField()
    tsymbol = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'pools_sushi'


class ProfitExchange(models.Model):
    pair = models.CharField(max_length=100)
    buy_name = models.CharField(max_length=100)
    buy = models.FloatField()
    sell_name = models.CharField(max_length=100)
    sell = models.FloatField()
    percent = models.FloatField()
    tokenid = models.CharField(max_length=100)
    buyurl = models.CharField(max_length=200)
    sellurl = models.CharField(max_length=200)
    buy_ask = models.FloatField()
    sell_bid = models.FloatField()
    sell_symbol = models.CharField(max_length=100, blank=True, null=True)
    contract = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profit_exchanges'


class RestFrameworkApiKeyApikey(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    created = models.DateTimeField()
    name = models.CharField(max_length=50)
    revoked = models.BooleanField()
    expiry_date = models.DateTimeField(blank=True, null=True)
    hashed_key = models.CharField(max_length=100)
    prefix = models.CharField(unique=True, max_length=8)

    class Meta:
        managed = False
        db_table = 'rest_framework_api_key_apikey'


class SendMailContacts(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'send_mail_contacts'


class Setting(models.Model):
    currency = models.FloatField(blank=True, null=True)
    gas_fast = models.IntegerField()
    gas_normal = models.IntegerField()
    currency_usd = models.FloatField(blank=True, null=True)
    min_profit = models.FloatField(help_text='минимальный профит в USDC')
    hide_volume_usd = models.FloatField(help_text='сумма порога спрятанных профитов в USDC')
    max_volume_usd = models.FloatField(help_text='максимальный объем в USDC')
    alert_profit_usd = models.IntegerField(help_text='мин профит для звука')
    alert_time = models.IntegerField(help_text='время на которое запоминает в сек')
    alert_usdt = models.FloatField(help_text='объем в USDT для сравнения')
    amm_percent = models.FloatField(help_text='процент биржи')
    uni_percent = models.FloatField(help_text='процент uniswap')
    candle_timer = models.FloatField(help_text='время заморозки показа свечи в секундах')
    fee = models.BooleanField(help_text='комиссия', default=False)

    class Meta:
        managed = False
        db_table = 'settings'


class SettingsModule(models.Model):
    module_name = models.CharField(max_length=200)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'settings_modules'


class TrustedPair(models.Model):
    token = models.CharField(max_length=20)
    contract = models.CharField(unique=True, max_length=100, blank=True, null=True)
    decimals = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField()
    tsymbol = models.CharField(unique=True, max_length=100, blank=True, null=True)
    token_name = models.CharField(max_length=255, blank=True, null=True)
    strong_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'trusted_pairs'


class TrustedTokensBSC(models.Model):
    token = models.CharField(max_length=20)
    contract = models.CharField(unique=True, max_length=100, blank=True, null=True)
    tsymbol = models.CharField(unique=True, max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=False, default=False)
    strong_active = models.BooleanField(blank=False, default=False)

    class Meta:
        managed = False
        db_table = 'trusted_tokens_bsc'


class PoolsUniV2(models.Model):
    pool_contract = models.CharField(max_length=500, null=False, blank=False)
    token0_contract = models.CharField(max_length=500, null=False, blank=False)
    token0_symbol = models.CharField(max_length=500, null=False, blank=False)
    token0_decimals = models.CharField(max_length=500)
    token1_contract = models.CharField(max_length=500, null=False, blank=False)
    token1_symbol = models.CharField(max_length=500, null=False, blank=False)
    token1_decimals = models.CharField(max_length=500, null=False, blank=False)
    is_active = models.BooleanField(default=False)
    datatime = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        managed = False
        db_table = 'pools_uni_v2'


class PoolsUniV3(models.Model):
    pool_contract = models.CharField(max_length=500, null=False, blank=False)
    token0_contract = models.CharField(max_length=500, null=False, blank=False)
    token0_symbol = models.CharField(max_length=500, null=False, blank=False)
    token0_decimals = models.CharField(max_length=500)
    token0_name = models.CharField(max_length=500)
    token1_contract = models.CharField(max_length=500, null=False, blank=False)
    token1_symbol = models.CharField(max_length=500, null=False, blank=False)
    token1_decimals = models.CharField(max_length=500, null=False, blank=False)
    token1_name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        managed = False
        db_table = 'pools_uni_v3'


class V3PoolsContract(models.Model):
    contract = models.CharField(unique=True, max_length=100, blank=False, null=False)
    checked = models.BooleanField(blank=True, default=False)

    class Meta:
        managed = False
        db_table = 'v3_pools_contracts'


class TickersAscendex(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickers_ascendex'


class TickersBitrue(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickers_bitrue'


class TickersBitget(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickers_bitget'


class TickersGate(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickers_gate'


class TickersHitbtc(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickers_hitbtc'


class TickersMexc(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickers_mexc'


class TransferCheck(models.Model):
    contract = models.CharField(max_length=100, blank=False, null=False)
    label = models.CharField(max_length=100, blank=False, null=False)
    exchanger = models.BooleanField(blank=False, null=False, default=False)

    class Meta:
        managed = False
        db_table = 'transfer_check'
