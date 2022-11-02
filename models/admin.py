from django.contrib import admin
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html

from .models import *
from .admin_utils import activate, deactivate


@admin.register(ModuleBancor)
class BancorAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'tsymbol', 'is_active')
    search_fields = ('exch_direction', 'tsymbol',)


@admin.register(AscendexMarkets)
class AscendexMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(GateMarkets)
class GateMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(KucoinMarkets)
class GateMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(BilaxyMarkets)
class BilaxyMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(MexcMarkets)
class MexcMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(ExchangePairs)
class ExchangePairAdmin(admin.ModelAdmin):
    list_display = (
        'exch_direction', 'idex_direction', 'uniswap_direction', 'bancor_direction', 'kyber_direction', 'hotbit')
    search_fields = ('exch_direction',)


@admin.register(PoolsSushi)
class PoolsSushiAdmin(admin.ModelAdmin):
    list_display = (
        'pool_contract', 'token0_contract', 'token0_symbol', 'token1_contract', 'token1_symbol', 'tsymbol', 'is_active')
    search_fields = ('polls_sushi',)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('timeout_refresh_data', 'timeout_notice', 'koef_top', 'koef_low', 'koef_push', 'hide_volume_usd',
                    'max_volume_usd')


@admin.register(SettingsModules)
class SettingsModulesAdmin(admin.ModelAdmin):
    list_display = ('module_name', 'is_active')


@admin.register(TrustedPairs)
class TrustedPairsAdmin(admin.ModelAdmin):
    list_display = ('token', 'contract', 'tsymbol', 'decimals', 'is_active', 'token_actions', 'strong_active')
    list_filter = ('is_active',)
    search_fields = ('token', 'tsymbol', 'contract',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(r'^(?P<token_id>.+)/uniswap/$', self.process_uniswap, kwargs=[], name='token-uniswap'),
            # url(
            #     r'^(?P<token_id>.+)/withdraw/$',
            #     self.admin_site.admin_view(self.process_withdraw),
            #     name='account-withdraw',
            # ),
        ]
        return custom_urls + urls

    def token_actions(self, obj):
        # TODO: Render action buttons
        return format_html(
            '<a class="button" href="{}">Uniswap</a> ',
            # '<a class="button" href="{}">Withdraw</a>',
            # reverse('admin:account-deposit', args=[obj.pk]),
            reverse('admin:token-uniswap', args=[obj.pk]),
        )

    token_actions.short_description = 'Token Actions'
    token_actions.allow_tags = True

    def process_uniswap(self, request, token_id, *args, **kwargs):
        obj = TrustedPairs.objects.get(id=token_id)
        try:
            uniObj = ModuleUniswap.objects.get(tokenid__icontains=obj.contract)
            uniObj.tsymbol = obj.tsymbol
            uniObj.is_active = True
            uniObj.save()
        except:
            obj = ModuleUniswap(tokenid=obj.contract, highest_bid=0, lowest_ask=0, volume=0, tsymbol=obj.tsymbol,
                                exch_direction=obj.token, is_active=True)
            obj.save()
        return HttpResponseRedirect("/admin/exchange_pairs/trustedpairs/")
        # TODO

    def process_withdraw(self):
        pass
        # TODO


@admin.register(WebsocketLog)
class WebsocketLogAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'log')
    list_filter = ('datetime',)
    search_fields = ('datetime',)


@admin.register(HitbtcMarkets)
class HitbtcMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(HotbitMarkets)
class HotbitMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(IdexMarkets)
class IdexMarketsAdmin(admin.ModelAdmin):
    list_display = ('market', 'token', 'tsymbol', 'is_active')
    search_fields = ('market', 'tsymbol',)
    actions = [activate, deactivate]


@admin.register(ModuleKyber)
class KyberAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'tsymbol', 'is_active')
    search_fields = ('exch_direction', 'tsymbol',)


@admin.register(ModuleUniswap)
class UniswapAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'tsymbol', 'is_active')
    search_fields = ('exch_direction', 'tsymbol',)


@admin.register(ModuleUniswapOne)
class UniswapOneAdmin(admin.ModelAdmin):
    list_display = ('exch_direction', 'tsymbol', 'is_active')
    search_fields = ('exch_direction', 'tsymbol',)


@admin.register(V3PoolsContracts)
class V3PollsContractsAdmin(admin.ModelAdmin):
    list_display = ('contract', 'checked')
    search_fields = ('contract',)
