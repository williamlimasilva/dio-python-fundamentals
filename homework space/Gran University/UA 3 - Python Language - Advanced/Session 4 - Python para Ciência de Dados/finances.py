import pandas as pd
import matplotlib.pyplot as plt

class Investment:
    def __init__(self, name, value, fee, period):
        self.name = name
        self.value = value
        self.fee = fee
        self.period = period

investments = {
    "Investment 1": Investment("Stocks", 10000, 0.02, "1 year"),
    "Investment 2": Investment("Bonds", 5000, 0.01, "6 months"),
    "Investment 3": Investment("Real Estate", 20000, 0.03, "2 years"),
    "Investment 4": Investment("Mutual Funds", 15000, 0.015, "1 year")
}

l_investments = [i.__dict__ for i in investments.values()]
df_investments = pd.DataFrame.from_records(l_investments, index=investments.keys())
def parse_period(period_str):
    # Extract the numeric part and convert to years
    num, unit = period_str.split()
    num = float(num)
    if "month" in unit:
        return num / 12
    return num

df_investments['Return'] = df_investments.apply(
    lambda column: round(column.value * (1 + column.fee) ** parse_period(column.period), 2), axis=1
)
print(df_investments)

df_investments.plot(kind='bar', x='name', y='Return', color='blue')
plt.title('Investment Returns')
plt.xlabel('Investment Name')
plt.ylabel('Return Value')
plt.show()