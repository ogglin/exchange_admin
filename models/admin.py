from django.contrib import admin
# from django.conf.urls import url
from django.urls import include, re_path
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html

from .models import *
from .admin_utils import activate, deactivate


@admin.register(AscendexMarket)
class AscendexMarketsAdmin(admin.ModelAdmin):
    list_display = (
        'market', 'token', 'tsymbol', 'is_active', 'currency', 'chain_name', 'withdraw_fee', 'allow_deposit',
        'allow_withdraw', 'min_deposit_amt', 'min_withdrawal', 'num_confirmations')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(BitrueMarket)
class GateMarketsAdmin(admin.ModelAdmin):
    list_display = (
        'market', 'token', 'tsymbol', 'is_active', 'chains', 'status', 'coin_ful_name', 'enable_withdraw',
        'enable_deposit')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(GateMarket)
class GateMarketsAdmin(admin.ModelAdmin):
    list_display = (
        'market', 'token', 'tsymbol', 'is_active', 'currency', 'delisted', 'withdraw_disabled', 'withdraw_delayed',
        'deposit_disabled', 'trade_disabled', 'fixed_rate', 'chain')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(KucoinMarket)
class GateMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active', 'markets', 'is_margin_enabled', 'enable_trading')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(BilaxyMarket)
class BilaxyMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(MexcMarket)
class MexcMarketsAdmin(admin.ModelAdmin):
    list_display = (
        'market', 'token', 'tsymbol', 'is_active', 'currency', 'chain', 'fee', 'is_withdraw_enabled',
        'is_deposit_enabled')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(Setting)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('timeout_refresh_data', 'timeout_notice', 'koef_top', 'koef_low', 'koef_push', 'hide_volume_usd',
                    'max_volume_usd', 'alert_profit_usd', 'alert_time')


@admin.register(SettingsModule)
class SettingsModulesAdmin(admin.ModelAdmin):
    list_display = ('module_name', 'is_active')


@admin.register(TrustedPair)
class TrustedPairsAdmin(admin.ModelAdmin):
    list_display = ('token', 'contract', 'tsymbol', 'decimals', 'is_active', 'strong_active')
    list_filter = ('is_active',)
    search_fields = ('token', 'tsymbol', 'contract',)

    # def get_urls(self):
    #     urls = super().get_urls()
    #     custom_urls = [
    #         re_path(r'^(?P<token_id>.+)/uniswap/$', self.process_uniswap, name='token-uniswap'),
    #         # url(
    #         #     r'^(?P<token_id>.+)/withdraw/$',
    #         #     self.admin_site.admin_view(self.process_withdraw),
    #         #     name='account-withdraw',
    #         # ),
    #     ]
    #     return custom_urls + urls
    #
    # def token_actions(self, obj):
    #     return format_html(
    #         '<a class="button" href="{}">Uniswap</a> ',
    #         # '<a class="button" href="{}">Withdraw</a>',
    #         # reverse('admin:account-deposit', args=[obj.pk]),
    #         reverse('admin:token-uniswap', args=[obj.pk]),
    #     )
    #
    # token_actions.short_description = 'Token Actions'
    # token_actions.allow_tags = True

    # def process_uniswap(self, request, token_id, *args, **kwargs):
    #     obj = TrustedPairs.objects.get(id=token_id)
    #     try:
    #         uniObj = ModuleUniswap.objects.get(tokenid__icontains=obj.contract)
    #         uniObj.tsymbol = obj.tsymbol
    #         uniObj.is_active = True
    #         uniObj.save()
    #     except:
    #         obj = ModuleUniswap(tokenid=obj.contract, highest_bid=0, lowest_ask=0, volume=0, tsymbol=obj.tsymbol,
    #                             exch_direction=obj.token, is_active=True)
    #         obj.save()
    #     return HttpResponseRedirect("/admin/exchange_pairs/trustedpairs/")
    #
    # def process_withdraw(self):
    #     pass


@admin.register(HitbtcMarket)
class HitbtcMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active', 'payin_enabled', 'payout_enabled', 'transfer_enabled')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(HotbitMarket)
class HotbitMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active', 'chain')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(IdexMarket)
class IdexMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(PoolsSushi)
class PoolsSushiAdmin(admin.ModelAdmin):
    list_display = ('pool_contract', 'token0_contract', 'token0_symbol', 'token0_decimals',
                    'token1_contract', 'token1_symbol', 'token1_decimals', 'is_active',)
    search_fields = ('pool_contract', 'token0_contract', 'token0_symbol', 'token1_contract', 'token1_symbol',)


@admin.register(PoolsUniV2)
class V3PollsContractsAdmin(admin.ModelAdmin):
    list_display = ('pool_contract', 'token0_contract', 'token0_symbol', 'token0_decimals',
                    'token1_contract', 'token1_symbol', 'token1_decimals', 'is_active',)
    search_fields = ('pool_contract', 'token0_contract', 'token0_symbol', 'token1_contract', 'token1_symbol',)


@admin.register(PoolsUniV3)
class V3PollsContractsAdmin(admin.ModelAdmin):
    list_display = ('pool_contract', 'token0_contract', 'token0_symbol', 'token0_decimals', 'token0_name',
                    'token1_contract', 'token1_symbol', 'token1_decimals', 'token1_name', 'is_active',)
    search_fields = ('pool_contract', 'token0_contract', 'token0_symbol', 'token1_contract', 'token1_symbol',)


@admin.register(V3PoolsContract)
class V3PollsContractsAdmin(admin.ModelAdmin):
    list_display = ('contract', 'checked')
    search_fields = ('contract',)
