from pathlib import Path
import csv
import json


DATA_DIR = Path("data/sample")


def load_instrument():
    with open(DATA_DIR / "instrument.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def main():
    instrument = load_instrument()
    prices = load_prices()

    latest = prices[-1]

    print("=== MarketPulse ===")
    print(f"Instrument: {instrument['ticker']}")
    print(f"Name: {instrument['name']}")
    print(f"Last price: {latest['close']} {instrument['currency']}")
    print(f"Observations: {len(prices)}")


if __name__ == "__main__":
    main()
