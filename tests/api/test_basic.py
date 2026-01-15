import os
import pytest
from dotenv import load_dotenv

load_dotenv()

def has_binance_keys():
    """Проверяем есть ли API ключи"""
    return (os.getenv("BINANCE_TESTNET_API_KEY") and 
            os.getenv("BINANCE_TESTNET_SECRET_KEY"))


class TestBinanceBasic:
    """Базовые тесты Binance клиента"""
    
    @pytest.fixture
    def client(self):
        """Создаем клиент для тестов"""
        if not has_binance_keys():
            pytest.skip("API ключи не настроены. Пропускаем тест.")
        
        from src.clients.binance_client import BinanceTestnetClient
        return BinanceTestnetClient()
    
    def test_ping(self, client):
        """Тест проверки связи"""
        assert client.ping() is True
        print("Ping test passed")
    
    def test_get_price(self, client):
        """Тест получения цены"""
        price = client.get_price("BTCUSDT")
        assert price is not None
        assert float(price) > 0
        print(f"Price test passed: BTC = {price}")
    
    def test_get_balance(self, client):
        """Тест получения баланса"""
        balance = client.get_balance("USDT")
        assert balance is not None
        assert float(balance) >= 0
        print(f"Balance test passed: USDT = {balance}")
    
    def test_test_order(self, client):
        """Тест проверки ордера"""
        result = client.test_order("BTCUSDT", "BUY", 0.001)
        assert result == {}
        print("Test order validation passed")


class TestWithoutKeys:
    """Тесты не требующие API ключей"""
    
    def test_import(self):
        """Просто проверяем что можем импортировать модуль"""
        from src.clients import binance_client
        from src.clients.binance_client import BinanceTestnetClient
        print("Import test passed")
        assert True
