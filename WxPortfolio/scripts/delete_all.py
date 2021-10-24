from WxPortfolio.models import Coins, TransactionCurrency

def run():
    coins = Coins.objects.all()
    tc = TransactionCurrency.objects.all()
    coins.delete()
    tc.delete()