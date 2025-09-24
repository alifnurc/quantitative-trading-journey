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
risk_per_trade = account_balance * (risk_percentage / 100)  # 100

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
