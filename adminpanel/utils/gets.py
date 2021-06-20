import json
import random
import time

import aiohttp
from aiohttp_socks import SocksConnector, ProxyConnector
from asgiref.sync import async_to_sync, sync_to_async

from exchange_comparison.utils import _query
from exchange_pairs.utils import proxys
import exchange_comparison.global_vars as gv

# 'cddba27a-916f-48e7-bad3-884c0869b627',


p_count = 0
sockets = []


# @sync_to_async
# def init_socks():
#     for i in range(len(proxys)):
#         socks_url = 'socks5://' + proxys[i][2] + ':' + proxys[i][3] + '@' + proxys[i][0] + ':' + proxys[i][1]
#         connector = SocksConnector.from_url(socks_url)
#         sockets.append(connector)


async def raw_idex_depth(symbol, cnt):
    global p_count
    proxy = proxys[cnt]
    if cnt > 39:
        cnt -= 20
    if cnt > 19:
        cnt -= 20
    header = {
        'IDEX-API-KEY': gv.idex_apis[cnt],
    }
    url = f"https://api.idex.io/v1/orderbook?market={symbol}&level=2&limit=20"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    try:
        async with aiohttp.ClientSession(connector=connector, headers=header) as session:
            async with session.get(url) as response:
                html = await response.text()
                jhtml = json.loads(html)
                p_count += 1
                if 'sequence' in html:
                    return jhtml
                elif 'code' in html:
                    if jhtml['code'] != 'MARKET_NOT_FOUND':
                        print('IDEX', symbol, jhtml['code'])
                    return None
    except Exception as exc:
        print(exc, proxy)
        return None


async def get_idex_depth(symbol, cnt):
    global p_count
    proxy = proxys[cnt]
    if cnt > 39:
        cnt -= 20
    if cnt > 19:
        cnt -= 20
    header = {
        'IDEX-API-KEY': gv.idex_apis[cnt],
    }
    url = f"https://api.idex.io/v1/orderbook?market={symbol}&level=2&limit=20"
    socks_url = 'socks5://' + proxy[2] + ':' + proxy[3] + '@' + proxy[0] + ':' + proxy[1]
    connector = SocksConnector.from_url(socks_url)
    try:
        async with aiohttp.ClientSession(connector=connector, headers=header) as session:
            async with session.get(url) as response:
                html = await response.text()
                jhtml = json.loads(html)
                p_count += 1
                if 'sequence' in html:
                    return jhtml
                elif 'code' in html:
                    if jhtml['code'] != 'MARKET_NOT_FOUND':
                        print('IDEX', symbol, jhtml['code'])
                    return None
    except Exception as exc:
        print(exc, proxy)
        return None


async def get_hitbtc_depth(symbol, cnt):
    url = f"https://api.hitbtc.com/api/2/public/orderbook/{symbol.replace('/', '')}"
    socks_url = 'socks5://' + proxys[cnt][2] + ':' + proxys[cnt][3] + '@' + proxys[cnt][0] + ':' + proxys[cnt][1]
    connector = SocksConnector.from_url(socks_url)
    try:
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(url) as response:
                html = await response.text()
                jhtml = json.loads(html)
                if 'ask' in html:
                    return jhtml
                elif 'error' in html:
                    print('hitbtc', jhtml['error'])
                    return None
                else:
                    return None
    except Exception as exc:
        print(exc, proxys[cnt])
        return None


async def get_hotbit_depth(symbol, cnt):
    url = f"https://api.hotbit.io/api/v1/order.depth?interval=1e-8&&limit=20&market={symbol}"
    socks_url = 'socks5://' + proxys[cnt][2] + ':' + proxys[cnt][3] + '@' + proxys[cnt][0] + ':' + proxys[cnt][1]
    connector = SocksConnector.from_url(socks_url)
    try:
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(url) as response:
                html = await response.text()
                jhtml = json.loads(html)
                if jhtml['error'] is None:
                    return jhtml['result']
                elif jhtml['error']:
                    print('hotbit', symbol, jhtml['error'])
                    if 'market not exist' in html:
                        _query(f"""UPDATE hotbit_markets SET "is_active" = 'f' WHERE "market" LIKE '%{symbol}%'""")
                    return None
                else:
                    return None
    except Exception as exc:
        print(exc, proxys[cnt])
        return None


async def get_bilaxy_depth(symbol, cnt):
    url = f"https://newapi.bilaxy.com/v1/orderbook?pair={symbol}"
    socks_url = 'socks5://' + proxys[cnt][2] + ':' + proxys[cnt][3] + '@' + proxys[cnt][0] + ':' + proxys[cnt][1]
    connector = SocksConnector.from_url(socks_url)
    try:
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(url) as response:
                html = await response.text()
                jhtml = json.loads(html)
                if 'timestamp' in html:
                    return jhtml
                else:
                    print('bilaxy', symbol, jhtml)
                    if 'Not found pair' in html:
                        _query(f"""UPDATE bilaxy_markets SET "is_active" = 'f' WHERE "market" LIKE '%{symbol}%'""")
                    return None
    except Exception as exc:
        print(exc, proxys[cnt])
        return None


def get_proxy():
    n = random.randint(0, 20)
    print(n)
    # proxy = proxys[n]
    # print(proxy)


@async_to_sync
async def init():
    idex_depth = await get_idex_depth('ETH-DAI', 30)
    print(idex_depth)


if __name__ == "__main__":
    init()
