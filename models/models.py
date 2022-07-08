# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AscendexMarkets(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ascendex_markets'


class MarketAscendexTest(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_ascendex_test'


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


class BilaxyMarkets(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'bilaxy_markets'


class MarketBilaxyTest(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'market_bilaxy_test'


class GateMarkets(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gate_markets'


class KucoinMarkets(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kucoin_markets'


class MarketGateTest(models.Model):
    market = models.CharField(max_length=30, blank=True, null=True)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_gate_test'


class MexcMarkets(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mexc_markets'


class MarketMexcTest(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'market_mexc_test'


class ComparePairs(models.Model):
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


class ExchangePairs(models.Model):
    exch_direction = models.CharField(max_length=20)
    bancor_direction = models.ForeignKey('ModuleBancor', models.DO_NOTHING, blank=True, null=True)
    idex_direction = models.ForeignKey('ModuleIdex', models.DO_NOTHING, blank=True, null=True)
    kyber_direction = models.ForeignKey('ModuleKyber', models.DO_NOTHING, blank=True, null=True)
    uniswap_direction = models.ForeignKey('ModuleUniswap', models.DO_NOTHING, blank=True, null=True)
    uniswap_one_direction = models.ForeignKey('ModuleUniswapOne', models.DO_NOTHING, blank=True, null=True)
    hotbit = models.ForeignKey('ModuleHotbit', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exchange_pairs'


class HitbtcMarkets(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'hitbtc_markets'


class MarketHitbtcTest(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'market_hitbtc_test'


class HotbitMarkets(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'hotbit_markets'


class MarketHotbitTest(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'market_hotbit_test'


class IdexMarkets(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'idex_markets'


class MarketIdexTest(models.Model):
    market = models.CharField(unique=True, max_length=30)
    token = models.CharField(max_length=30, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'market_idex_test'


class IdexSocketLog(models.Model):
    log = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idex_socket_log'


class ModuleBancor(models.Model):
    exch_direction = models.CharField(max_length=20)
    highest_bid = models.FloatField()
    lowest_ask = models.FloatField()
    name = models.CharField(max_length=100)
    link_id = models.CharField(max_length=100)
    is_active = models.BooleanField()
    volume = models.FloatField()
    tsymbol = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_bancor'


class ModuleHitbtc(models.Model):
    exch_direction = models.CharField(max_length=30)
    buy = models.FloatField(blank=True, null=True)
    sell = models.FloatField(blank=True, null=True)
    symbol = models.CharField(unique=True, max_length=30)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    contract = models.CharField(max_length=100, blank=True, null=True)
    decimals = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'module_hitbtc'


class ModuleHotbit(models.Model):
    exch_direction = models.CharField(max_length=30)
    buy = models.FloatField(blank=True, null=True)
    sell = models.FloatField(blank=True, null=True)
    symbol = models.CharField(unique=True, max_length=30)
    is_active = models.BooleanField()
    volume = models.FloatField(blank=True, null=True)
    contract = models.CharField(max_length=100, blank=True, null=True)
    decimals = models.IntegerField(blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_hotbit'


class ModuleIdex(models.Model):
    exch_direction = models.CharField(max_length=20)
    lowest_ask = models.FloatField()
    highest_bid = models.FloatField()
    is_active = models.BooleanField()
    token_id = models.CharField(max_length=50, blank=True, null=True)
    volume = models.FloatField()
    tsymbol = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_idex'


class ModuleKyber(models.Model):
    exch_direction = models.CharField(max_length=20)
    highest_bid = models.FloatField()
    lowest_ask = models.FloatField()
    is_active = models.BooleanField()
    volume = models.FloatField()
    token_id = models.CharField(max_length=50, blank=True, null=True)
    tsymbol = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_kyber'


class ModuleUniswap(models.Model):
    exch_direction = models.CharField(max_length=256)
    highest_bid = models.FloatField(blank=True, null=True)
    lowest_ask = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField()
    tokenid = models.CharField(max_length=500)
    volume = models.FloatField(blank=True, null=True)
    tsymbol = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_uniswap'


class ModuleUniswapOne(models.Model):
    exch_direction = models.CharField(max_length=256)
    highest_bid = models.FloatField()
    lowest_ask = models.FloatField()
    is_active = models.BooleanField()
    tokenid = models.CharField(max_length=500)
    volume = models.FloatField()
    tsymbol = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_uniswap_one'


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


class ProfitExchanges(models.Model):
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


class Settings(models.Model):
    timeout_refresh_data = models.IntegerField()
    timeout_notice = models.IntegerField()
    koef_top = models.FloatField()
    koef_low = models.FloatField()
    koef_push = models.FloatField()
    freeze_percent = models.FloatField()
    api_keys = models.JSONField(blank=True, null=True)
    market_koef = models.FloatField(blank=True, null=True)
    market_percent = models.FloatField(blank=True, null=True)
    currency = models.FloatField(blank=True, null=True)
    gas_fast = models.IntegerField()
    gas_normal = models.IntegerField()
    currency_usd = models.FloatField(blank=True, null=True)
    min_profit = models.FloatField(help_text='минимальный профит в USDC')
    min_volume_eth = models.FloatField(help_text='минимальный порог парсера в ETH')
    hide_volume_usd = models.FloatField(help_text='сумма порога спрятанных профитов в USDC')
    max_volume_usd = models.FloatField(help_text='максимальный объем в USDC')

    class Meta:
        managed = False
        db_table = 'settings'


class SettingsModules(models.Model):
    module_name = models.CharField(max_length=200)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'settings_modules'


class TrustedPairs(models.Model):
    token = models.CharField(max_length=20)
    contract = models.CharField(unique=True, max_length=100, blank=True, null=True)
    decimals = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField()
    tsymbol = models.CharField(unique=True, max_length=100, blank=True, null=True)
    token_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trusted_pairs'


class UniswapMarkets(models.Model):
    market = models.CharField(unique=True, max_length=100)
    token = models.CharField(max_length=256, blank=True, null=True)
    tokenid = models.CharField(max_length=256, blank=True, null=True)
    tsymbol = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'uniswap_markets'


class WebsocketLog(models.Model):
    datetime = models.DateTimeField()
    log = models.TextField(unique=True)
    buy_url = models.CharField(max_length=255, blank=True, null=True)
    sell_url = models.CharField(max_length=255, blank=True, null=True)
    percent = models.CharField(max_length=255, blank=True, null=True)
    site = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    sprice = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'websocket_log'
