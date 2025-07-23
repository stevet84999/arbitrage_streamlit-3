def find_arbitrage_opportunities(odds_data):
    opportunities = []

    for sport, events in odds_data.items():
        for event in events:
            event_name = event.get("home_team", "") + " vs " + event.get("away_team", "")
            outcomes = event.get("bookmakers", [])
            outcome_prices = {}

            for bookmaker in outcomes:
                for market in bookmaker.get("markets", []):
                    for outcome in market.get("outcomes", []):
                        name = outcome["name"]
                        price = outcome["price"]
                        if name not in outcome_prices or price > outcome_prices[name]:
                            outcome_prices[name] = price

            if len(outcome_prices) >= 2:
                inv_total = sum(1 / price for price in outcome_prices.values())
                if inv_total < 1:
                    profit_percent = (1 - inv_total) * 100
                    opportunities.append({
                        "event": event_name,
                        "best_odds": outcome_prices,
                        "profit_percent": round(profit_percent, 2)
                    })

    return opportunities
