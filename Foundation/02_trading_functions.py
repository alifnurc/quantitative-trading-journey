#!/usr/bin/env python3

# Simple Price Action Decision
current_price = 1.0850
support_level = 1.0840
resistance_level = 1.0860

print("=== Trading Decision Maker ===")

if current_price > resistance_level:
    print("Breakout: Harga terlalu mahal")
    print("Harga menembus keatas resistance/premium zone\n")
elif current_price < support_level:
    print("Breakdown: Harga terlalu murah")
    print("Harga menembus kebawah support/discount zone\n")
else:
    print("Consolidation: Tunggu untuk mendapatkan sinyal yang jelas")
    print("Harga berada diarea equibrilium\n")

# Advanced Trading Conditions
is_trending_up = True
has_volume = True
is_key_level = False
market_volatility = "low"

print("Advanced Trading Logic")

# AND conditions (kondisi harus checklist semuanya)
if is_trending_up and has_volume and not is_key_level:
    print("STRONG SIGNAL: Trend + Volume + No key level")

# OR conditions (salah satu terchecklist)
if market_volatility == "high" or is_key_level:
    print("CAUTION: High volatility or key level")

# Complex combinations
if (is_trending_up and has_volume) and (market_volatility == "low" or not is_key_level):
    print("OPTIMAL CONDITION: A+ Setup\n")
else:
    print("SUBOPTIMAL: Wait for better setup\n")


# ICT Concept
def ict_trading_signal(price_actions, liquidity, market_structure):
    """Simulate ICT trading signal based on price actions, liquidity, and market structure."""
    print("=== ICT Trading Signal ===")
    print(f"Price Action: {price_actions}")
    print(f"Liquidity: {liquidity}")
    print(f"Market Structure: {market_structure}\n")

    # ICT Decision Logic
    if (
        price_actions == "breakout"
        and liquidity == "present"
        and market_structure == "bullish"
    ):
        return "ICT SIGNAL: Consider long position"
    elif (
        price_actions == "breakdown"
        and liquidity == "present"
        and market_structure == "bearish"
    ):
        return "ICT SIGNAL: Consider short position"
    else:
        return "ICT SIGNAL: No clear signal, stay out"


def analyze_price_series(prices):
    """Analyze:
    - Trend direction
    - Key support/resistance
    - Trading signal"""
    if not prices:
        return
    previous_price = None
    trend_strength = 0
    support_level = []
    resistance_level = []
    price_changes = []
    sl_distance = 0.0005  # 5 pips
    tp_distance = 0.001  # 10 pips

    """enumerate, the function that return index + value from the list"""
    for i, current_price in enumerate(prices):
        if previous_price is None:
            previous_price = current_price
            continue
        change = current_price - previous_price
        price_changes.append(change)

        if change > 0: # bullish move
            trend_strength += 1
            support_level.append(previous_price)
        elif change < 0: # bearish move
            trend_strength -= 1
            resistance_level.append(previous_price)
        previous_price = current_price

    # Trend and signal detection
    if trend_strength > 0:
        trend = "bullish"
        entry = support_level[-1] + 0.0001  # slight buffer above support
        sl = support_level[-1] - sl_distance
        tp = entry + tp_distance
    elif trend_strength < 0:
        trend = "bearish"
        entry = resistance_level[-1] - 0.0001  # slight buffer below resistance
        sl = resistance_level[-1] + sl_distance
        tp = entry - tp_distance
    else:
        trend = "sideways"
        entry = None
        sl = None
        tp = None

    return {
        "trend": trend,
        "support": support_level,
        "resistance": resistance_level,
        "entry": entry if trend != "sideways" else None,
        "stop_loss": sl if trend != "sideways" else None,
        "take_profit": tp if trend != "sideways" else None,
    }


# Test different scenarios
signal1 = ict_trading_signal("breakout", "present", "bullish")
signal2 = ict_trading_signal("breakdown", "present", "bearish")
signal3 = ict_trading_signal("consolidation", "absent", "neutral")

print(signal1)
print(signal2)
print(signal3)
print()

eurusd_price = [1.0850, 1.0852, 1.0851, 1.0853]
signal4 = analyze_price_series(eurusd_price)
print(f"EURUSD price series: {eurusd_price} => {signal4}")
print()
