import requests

def get_convertion(source: str = "BRL") -> dict:
    url: str = f"https://api.exchangerate-api.com/v4/latest/{source}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data["rates"]
    else:
        print("Erro ao obter dados da API")
        return None

rates = get_convertion()
def convert_brl_to_currency(amount: float, currency: str) -> float:
    if rates is not None and currency in rates:
        return amount * rates[currency]
    else:
        print(f"Taxa de conversão para {currency} não disponível")
        return None