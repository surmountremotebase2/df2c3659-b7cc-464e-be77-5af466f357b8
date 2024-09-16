from surmount.base_class import Strategy, TargetAllocation
from surmount.data import SocialSentiment

class TradingStrategy(Strategy):
    def __init__(self):
        # Define the tech stocks to monitor.
        self.tech_stocks = ["AAPL", "GOOGL", "MSFT Prepare the data list for Social        self.data_list = [ stock in self.tech_stocks]

    @property
    def interval(self):
        # Using daily data for social sentiment analysis.
        return "1day"

    @property
    def assets(self):
        # The assets that this strategy will trade.
        return self.tech_stocksproperty
    def data(self):
        # The requested data points for this strategy, focusing        return self    def run(self, data_dict = {}
        total_sent 0
        
 total positive change for normalization
        for.tech_stocks:
            if data[("social_sentiment", stock)][("social_sentiment", stock)]) >= 2:
                current_sentiment =social_sentiment", stock)][1]["twitterSentiment"]
                = data[("social_sent)][-2]["twitterSentiment"]
                sentiment_change = current_sentiment - previous                if sentiment_change > 0 total_sentiment_change += sentiment_change

        # Allocate investments based on normalized sentiment change
        for stock in self.tech_stocks:
            if data[("social_sentiment", stock)] and len(data[("social_sentiment", stock)]) >= 2:
_sentiment = data[("social_sentiment", stock)][-1]["twitterSentiment"]
                previous_sentiment("social_sentiment", stock)][-2iment"]
                sentiment_changeiment - previous_sentiment
                # Allocate only for positive sentiment changes
                > 0 total_sentiment_change > 0:
_allocation = sentiment
                    allocation_dict[stock] = normalized_allocation else:
                   [stock]:
                # In case, assume no allocation
               [stock] = 0

        # Check if allocation bounds (0 to 1 construction.
        return TargetAllocation(allocation_dict)