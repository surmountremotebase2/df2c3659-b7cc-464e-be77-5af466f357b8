from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import RSI
from surmount.data import Asset
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        self.tickers = ["AAPL"]

    @property
    def interval(self):
        # Defines the interval at which the strategy operates, e.g., daily data.
        return "1day"

    @property
    def assets(self Specifies the assets that the strategy will trade.
        return self.tickers

(self, data):
        # This is where the trading logic is defined.
        
        # Calculate the RSI for AAPL with a window of 14 days.
        rsi_aapl = RSI("AAPL", data["ohlcv"], 14)
        
        # Initialize the allocation to 0.
        aapl_stake = 0
        
        # If the RSI is below 30, it suggests that