import kuna.kuna as kuna
import trading_bot.kuna_api_access.kuna_local_config as kuna_config

kuna_api = kuna.KunaAPI(access_key=kuna_config.KUNA_API_PUBLIC_KEY,
                          secret_key=kuna_config.KUNA_SECRET_KEY)

pairs = kuna.VALID_MARKET_DATA_PAIRS
market_data = kuna_api.get_recent_market_data('btcuah')



print(market_data['ticker'])