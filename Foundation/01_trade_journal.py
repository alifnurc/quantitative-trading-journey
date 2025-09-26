#!/usr/bin/env python3

# List Price Data
bid_prices = [1.0850, 1.0851, 1.0852, 1.0853, 1.0854]
ask_prices = [1.0852, 1.0853, 1.0854, 1.0855, 1.0856]

# List Operation untuk Trading Analysis
print("=== Price Data Analysis ===")
print(f"First price: {bid_prices[0]}")  # First element
print(f"Last price: {bid_prices[-1]}")  # Last element
print(f"Recent price: {bid_prices[-3:]}")  # Last 3 elements
print(f"Price range: {bid_prices[1:4]}")  # Elements from index 1 to 3
print()

# List Method untuk Data Management
bid_prices.append(1.0855)  # Add new price
recent_high = max(bid_prices)  # Highest price
recent_low = min(bid_prices)  # Lowest Price
total_ticks = len(bid_prices)  # Number of data points

print("=== Market Data ===")
print(f"Recent Hight: {recent_high}, Recent Low: {recent_low}")
print(f"Total Ticks: {total_ticks}")
print()

# Trade journal dengan dictionary
trade_journal = {
    "trade_001": {
        "symbol": "EURUSD",
        "entry_price": 1.0850,
        "exit_price": 1.0870,
        "size": 10000,
        "pnl": 200,
        "date": "2025-09-26",
    },
    "trade_002": {
        "symbol": "USDJPY",
        "entry_price": 147.801,
        "exit_price": 147.791,
        "size": 10000,
        "pnl": -100,
        "date": "2025-09-26",
    },
}

# Accessing Trade Data
eurusd_trade = trade_journal["trade_001"]
print("=== Market Data ===")
print(f"EURUSD Trade PnL: {eurusd_trade["pnl"]}")
print(f"Trade date: {eurusd_trade["date"]}")
print()

# Adding New Trades
trade_journal["trade_003"] = {
    "symbol": "EURUSD",
    "entry_price": 1.0840,
    "exit_price": 1.0830,
    "size": 10000,
    "pnl": -100,
    "date": "2025-09-26",
}

# Hourly Data
hourly_highs = [1.0860, 1.0870, 1.0855, 1.0880, 1.0890]
hourly_lows = [1.0840, 1.0850, 1.0840, 1.0860, 1.0870]

# Calculation of Hourly Data
pip_value = 10000
avg_hourly_range = (
    (
        (hourly_highs[0] - hourly_lows[0])
        + (hourly_highs[1] - hourly_lows[1])
        + (hourly_highs[2] - hourly_lows[2])
        + (hourly_highs[3] - hourly_lows[3])
        + (hourly_highs[4] - hourly_lows[4])
    )
    / len(hourly_highs)
    * pip_value
)
total_higher_high = (
    (hourly_highs[0] < hourly_highs[1])
    + (hourly_highs[1] < hourly_highs[2])
    + (hourly_highs[2] < hourly_highs[3])
    + (hourly_highs[3] < hourly_highs[4])
)

print(f"Hourly Ranges: {avg_hourly_range:.2f} pips")
print(f"Highest high: {max(hourly_highs)}")
print(f"Lowest low: {min(hourly_lows)}")
print(f"Total BOS/Higher High: {total_higher_high}/4")
