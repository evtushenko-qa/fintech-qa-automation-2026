import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()


class BinanceTestnetClient:
    
    def __init__(self):
        self.api_key = os.getenv("BINANCE_TESTNET_API_KEY")
        self.api_secret = os.getenv("BINANCE_TESTNET_SECRET_KEY")

        if not self.api_key or not self.api_secret:
            print("Ошибка: API ключи не найдены!")
            print("Создайте файл .env с ключами")
            print("или получите ключи: https://testnet.binance.vision")
            raise ValueError("API ключи не настроены")

        if len(self.api_key) != 64:
            raise ValueError("Неверный формат API ключа")

        self.client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
            testnet=True
        )
        
        print("Binance Testnet клиент создан")
    
    def ping(self):
        try:
            self.client.ping()
            print("Связь с Binance API установлена")
            return True
        except Exception as e:
            print(f"Ошибка связи: {e}")
            return False

    def get_price(self, symbol="BTCUSDT"):
        try:
            ticker = self.client.get_symbol_ticker(symbol=symbol)
            price = ticker['price']
            print(f"Цена {symbol}: {price}")
            return price
        except Exception as e:
            print(f"Не удалось получить цену: {e}")
            return None

    def get_balance(self, asset="USDT"):
        try:
            account = self.client.get_account()
            for balance in account['balances']:
                if balance['asset'] == asset:
                    free = float(balance['free'])
                    print(f"Баланс {asset}: {free}")
                    return free
            print(f"Валюта {asset} не найдена")
            return 0.0
        except Exception as e:
            print(f"Ошибка получения баланса: {e}")
            return None