import matplotlib.pyplot as plt
import pandas as pd

class Campaign:
    def __init__(self, channel, budget, clicks, conversions):
        self.channel = channel
        self.budget = budget
        self.clicks = clicks
        self.conversions = conversions

    def cost_per_click(self):
        return self.budget / self.clicks
    
campaigns = [
    Campaign("Meta ADS", 5000, 15000, 150),
    Campaign("TikTok ADS", 800, 12000, 80),
    Campaign("Google ADS", 1200, 10000, 200),
    Campaign("Email ADS", 5000, 5000, 50)
]
df_campaigns = pd.DataFrame([vars(campaign) for campaign in campaigns])
print(df_campaigns)

channels = [campaign.channel for campaign in campaigns]
print(channels)

cost_per_clicks = [campaign.cost_per_click() for campaign in campaigns]
print(cost_per_clicks)

plt.bar(channels, cost_per_clicks)
plt.xlabel("Channels")
plt.ylabel("Cost per Click")
plt.title("Cost per Click by Channel")
plt.show()