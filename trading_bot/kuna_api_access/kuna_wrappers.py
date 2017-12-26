import kuna.kuna
import trading_bot.kuna_api_access.kuna_local_config as kuna_config

graph_kuna = kuna.kuna.KunaAPI(access_key=kuna_config.KUNA_API_PUBLIC_KEY,
                          secret_key=kuna_config.KUNA_SECRET_KEY)

