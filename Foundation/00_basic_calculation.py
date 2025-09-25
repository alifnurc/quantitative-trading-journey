#!/usr/bin/env python3
"""
Basic trading variables
Goal: Pahami variable types dengan konteks trading
"""

# Basic Setup - Trading Account

## Integer variables
account_balance = 10000  # USD
risk_percentage = 1  # 1% risk per trade
max_daily_trade = 2

## Float variables
current_equity = 10000.0
risk_per_trade = account_balance * (risk_percentage / 100)  # 100 USD

print("=== Account Info ===")
print(f"Balance: ${account_balance}")
print(f"Risk per trade: ${risk_per_trade}")
print(f"Max daily trades: {max_daily_trade}")
print()

# Price Data - Current Market

## Float variables
eurusd_bid = 1.08542
eurusd_ask = 1.08550
usdjpy_bid = 147.891
usdjpy_ask = 147.901

eurusd_spread = eurusd_ask - eurusd_bid
usdjpy_spread = usdjpy_ask - usdjpy_bid

print("=== Market Price ===")
print(f"EURUSD: Bid=${eurusd_bid}, Ask=${eurusd_ask}, Spread=${eurusd_spread:.5f}")
print(f"USDJPY: Bid=${usdjpy_bid}, Ask=${usdjpy_ask}, Spread=${usdjpy_spread:.5f}")
print()

# Trade Parameters - Order Setup

## String variables
trade_symbol = "EURUSD"
trade_direction = "BUY"
timeframe = "M15"

## Float variables
planned_entry = 1.08500
stop_loss = 1.08400
take_profit = 1.08700

risk_pips = abs(planned_entry - stop_loss) * 10000  # 10 pips
reward_pips = abs(take_profit - planned_entry) * 10000  # 20 pips
risk_reward_ratio = reward_pips / risk_pips  # 2.0

print("=== Trading Plan ===")
print(f"Symbol: {trade_symbol}")
print(f"Direction: {trade_direction}")
print(f"Entry: {planned_entry}, SL: {stop_loss}, TP: {take_profit}")
print(f"Risk: {risk_pips} pips, Reward: {reward_pips} pips")
print(f"R:R Ratio: 1:{risk_reward_ratio}")
print()

# Trade History - List & Dictionaries

## List of trade
recent_trades = [-100, -100, -100, 200, -100, 200]

## Dictionary of trade details
pip_value = 10
current_position = {
    "symbol": "EURUSD",
    "entry_price": 1.08500,
    "current_price": 1.08542,
    "size": risk_per_trade / (risk_pips * pip_value),  # lot size
    "unrealized_pnl": 0.0,  # akan dihitung
}

current_position["unrealized_pnl"] = (
    current_position["current_price"] - current_position["entry_price"]
) * current_position["size"]

print("=== Trade History ===")
print(f"Recent PnLs: {recent_trades}")
print(f"Curret Position: {current_position}")
print(f"Unrealized PnL: {current_position['unrealized_pnl']:.2f}")
print()

# Trading Conditions - Booleans

# Boolean variables for market conditions
is_eurusd_above_ma = True
is_market_open = True
has_breaking_news = False
is_volume_high = True

should_enter_trade = (
    is_eurusd_above_ma and is_market_open and not has_breaking_news and is_volume_high
)

print("=== Trading Conditions ===")
print(f"EURUSD above MA: {is_eurusd_above_ma}")
print(f"Market Open: {is_market_open}")
print(f"Breaking News: {has_breaking_news}")
print(f"High Volume: {is_volume_high}")
print(f"Should Enter Trade: {should_enter_trade}")
print()

# Trading History Details

trade1 = {"symbol": "EURUSD", "entry": 1.0850, "exit": 1.0870, "pnl": 200}
trade2 = {"symbol": "USDJPY", "entry": 147.801, "exit": 147.791, "pnl": -100}
trade3 = {"symbol": "EURUSD", "entry": 1.0840, "exit": 1.0830, "pnl": -100}

# winrate = win / total_trades

print("=== Total PnL Previous Month ===")
print(f"{trade1['pnl'] + trade2['pnl'] + trade3['pnl']} USD")
print(f"Winrate: {(1/3)*100:.2f}%")
print()

# Market Analyst

bid_prices = [1.0850, 1.0851, 1.0852, 1.0853, 1.0854]
ask_prices = [1.0852, 1.0853, 1.0854, 1.0855, 1.0856]

avg_spread = (
    (
        (ask_prices[0] - bid_prices[0])
        + (ask_prices[1] - bid_prices[1])
        + (ask_prices[2] - bid_prices[2])
        + (ask_prices[3] - bid_prices[3])
        + (ask_prices[4] - bid_prices[4])
    )
    / 5
    * 10000
)
price_change = (bid_prices[4] - bid_prices[0]) * 10000  # 4 pips

print(f"=== Market Conditions ===")
print(f"Average Spread: {avg_spread:.2f}")
print(f"Price change: {price_change:.2f}")
print(f"Highest bid: {bid_prices[4]}, Lowest bid: {bid_prices[0]}")
