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
print(f"Recent High: {recent_high}, Recent Low: {recent_low}")
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
print("=== Trade Journal ===")
print(f"EURUSD Trade PnL: {eurusd_trade['pnl']}")
print(f"Trade date: {eurusd_trade['date']}")
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
print()

"""
Price Analysis dengan Data Structures
"""

# Sample Price Data 50 ticks
bid_prices = [1.0850 + i * 0.0001 for i in range(50)]  # Simulated rising market
ask_prices = [bid + 0.0002 for bid in bid_prices]  # Constant spread

# Basic Statistic
first_price = bid_prices[0]
last_price = bid_prices[-1]
highest_price = max(bid_prices)
lowest_price = min(bid_prices)

# Price Change Analysis
price_changes = []
for i in range(1, len(bid_prices)):
    change = bid_prices[i] - bid_prices[i - 1]
    price_changes.append(change)

# Market Condition Analysis
total_upticks = len([ch for ch in price_changes if ch > 0])
total_downticks = len([ch for ch in price_changes if ch < 0])
net_movement = last_price - first_price

print("=== Market Analysis ===")
print(f"Period: {len(bid_prices)} ticks")
print(f"First Price: {first_price:.4f}, Last Price: {last_price:.4f}")
print(f"Highest Price: {highest_price:.4f}, Lowest Price: {lowest_price:.4f}")
print(f"Net Movement: {net_movement:.4f} ({net_movement * 10000:.1f} pips)")
print(f"Total Upticks: {total_upticks}, Total Downticks: {total_downticks}")
print(
    f"Bullish/Bearish Ratio: {total_upticks/total_downticks if total_downticks != 0 else 'N/A'}"
)
print()

"""
Portfolio Management dengan Dictionaries
"""

# Portfolio Structure
portfolio = {
    "account_info": {
        "balance": 10000,
        "equity": 10000,
        "used_margin": 0,
        "free_margin": 10000,
    },
    "open_positions": {
        "EURUSD_001": {
            "symbol": "EURUSD",
            "entry_price": 1.0850,
            "size": 10000,
            "current_price": 1.0865,
            "side": "BUY",
            "stop_loss": 1.0840,
            "take_profit": 1.0870,
        },
    },
    "daily_performance": {
        "2025-09-23": {"pnl": 200, "trades": 1},
        "2025-09-24": {"pnl": -100, "trades": 1},
        "2025-09-25": {"pnl": 100, "trades": 2},
    },
}


# Portfolio Calculations
def update_portfolio(portfolio, symbol, current_price):
    """Update portfolio dengan harga terkini"""
    if symbol in portfolio["open_positions"]:
        position = portfolio["open_positions"][symbol]
        entry = position["entry_price"]
        stop_loss = position["stop_loss"]
        take_profit = position["take_profit"]
        size = position["size"]

        # Calculate unrealized pnl and risk reward ratio
        if position["side"] == "BUY":
            pnl = (current_price - entry) * size
            risk = entry - stop_loss
            reward = take_profit - entry
        else:  # SELL position
            pnl = (entry - current_price) * size
            risk = stop_loss - entry
            reward = entry - take_profit

        # Risk Reward Ratio
        risk_reward_ratio = reward / risk if risk != 0 else 0

        position["unrealized_pnl"] = pnl
        position["risk_reward_ratio"] = risk_reward_ratio
        position["current_price"] = current_price
        portfolio["account_info"]["equity"] = portfolio["account_info"]["balance"] + pnl

    return portfolio


# Portfolio Analysis
def analyze_portfolio(portfolio):
    """Analisis dasar portfolio"""
    total_pnl = 0
    winning_days = 0

    print("=== Trade History ===")
    for date, performance in portfolio["daily_performance"].items():
        total_pnl += performance["pnl"]
        if performance["pnl"] > 0:
            winning_days += 1
            print(f"Day {date} result: Win")
        else:
            print(f"Day {date} result: Loss")
    print()

    win_rate = (winning_days / len(portfolio["daily_performance"])) * 100
    avg_daily_pnl = total_pnl / len(portfolio["daily_performance"])

    print("=== Portfolio Analysis ===")
    print(f"Total PnL: {total_pnl}")
    print(f"Win Rate: {win_rate:.1f}%")
    print(f"Avg Daily PnL: {avg_daily_pnl:.2f}")
    print(f"Current Equity: {portfolio["account_info"]["equity"]:.2f}")
    print()

    if portfolio["open_positions"]:
        print("=== Open Positions ===")
        for symbol, position in portfolio["open_positions"].items():
            print(
                f"{symbol}: Size {position['size']} at {position['entry_price']}, "
                f"Current Price {position['current_price']}, "
                f"Unrealized PnL {position['unrealized_pnl']:.2f}, "
                f"RRR {position['risk_reward_ratio']:.2f}"
            )
        print()


# Update and Analyze
portfolio = update_portfolio(portfolio, "EURUSD_001", 1.0858)
analyze_portfolio(portfolio)
