import csv
import os

# ─────────────────────────────────────────
#  Hardcoded stock prices dictionary
#  (as required by the task)
# ─────────────────────────────────────────
STOCK_PRICES = {
    "AAPL":  180,   # Apple
    "TSLA":  250,   # Tesla
    "GOOGL": 140,   # Google
    "AMZN":  185,   # Amazon
    "MSFT":  420,   # Microsoft
    "NFLX":  620,   # Netflix
    "META":  500,   # Meta
    "NVDA":  870,   # NVIDIA
}


# ─────────────────────────────────────────
#  Show all available stocks
# ─────────────────────────────────────────
def show_available_stocks():
    print("\n  Available stocks:")
    print(f"  {'Symbol':<10} {'Price (USD)':>12}")
    print("  " + "-" * 24)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<10} ${price:>11,}")
    print()


# ─────────────────────────────────────────
#  Get portfolio input from user
# ─────────────────────────────────────────
def get_portfolio():
    portfolio = {}

    print("  Enter stock symbol and quantity.")
    print("  Type 'done' when finished.\n")

    while True:
        stock = input("  Stock symbol (or 'done'): ").strip().upper()

        if stock == "DONE":
            if not portfolio:
                print("  ⚠  No stocks added. Please add at least one stock.\n")
                continue
            break

        # Validate stock symbol
        if stock not in STOCK_PRICES:
            print(f"  ⚠  '{stock}' not found. Choose from the list above.\n")
            continue

        # Get quantity
        qty_input = input(f"  Quantity for {stock}: ").strip()
        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("  ⚠  Please enter a positive whole number for quantity.\n")
            continue

        qty = int(qty_input)

        # If stock already added, update quantity
        if stock in portfolio:
            portfolio[stock] += qty
            print(f"  Updated {stock}: total quantity = {portfolio[stock]}\n")
        else:
            portfolio[stock] = qty
            print(f"  Added {stock} x {qty}\n")

    return portfolio


# ─────────────────────────────────────────
#  Calculate investment values
# ─────────────────────────────────────────
def calculate_portfolio(portfolio):
    results = []
    total = 0

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        results.append({
            "symbol": symbol,
            "qty": qty,
            "price": price,
            "value": value,
        })

    return results, total


# ─────────────────────────────────────────
#  Display portfolio summary
# ─────────────────────────────────────────
def display_summary(results, total):
    print("\n" + "=" * 50)
    print("         PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"  {'Stock':<8} {'Qty':>6} {'Price':>10} {'Value':>12}")
    print("  " + "-" * 40)
    for row in results:
        print(
            f"  {row['symbol']:<8}"
            f" {row['qty']:>6}"
            f"  ${row['price']:>8,}"
            f"  ${row['value']:>10,}"
        )
    print("  " + "-" * 40)
    print(f"  {'TOTAL INVESTMENT':>28}  ${total:>10,}")
    print("=" * 50 + "\n")


# ─────────────────────────────────────────
#  Save results to file (optional)
# ─────────────────────────────────────────
def save_to_file(results, total):
    choice = input("  Save results to a file? (yes / no): ").strip().lower()
    if choice not in ("yes", "y"):
        print("  Results not saved.\n")
        return

    fmt = input("  Save as (1) .txt  or  (2) .csv ? Enter 1 or 2: ").strip()

    if fmt == "1":
        filename = "portfolio_summary.txt"
        with open(filename, "w") as f:
            f.write("STOCK PORTFOLIO SUMMARY\n")
            f.write("=" * 40 + "\n")
            f.write(f"{'Stock':<8} {'Qty':>6} {'Price':>10} {'Value':>12}\n")
            f.write("-" * 40 + "\n")
            for row in results:
                f.write(
                    f"{row['symbol']:<8}"
                    f" {row['qty']:>6}"
                    f"  ${row['price']:>8,}"
                    f"  ${row['value']:>10,}\n"
                )
            f.write("-" * 40 + "\n")
            f.write(f"TOTAL INVESTMENT: ${total:,}\n")
        print(f"\n  Saved to '{filename}'\n")

    elif fmt == "2":
        filename = "portfolio_summary.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price (USD)", "Total Value (USD)"])
            for row in results:
                writer.writerow([row["symbol"], row["qty"], row["price"], row["value"]])
            writer.writerow([])
            writer.writerow(["", "", "TOTAL", total])
        print(f"\n  Saved to '{filename}'\n")

    else:
        print("  Invalid choice. Results not saved.\n")


# ─────────────────────────────────────────
#  Main program
# ─────────────────────────────────────────
def main():
    print("\n" + "=" * 50)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    show_available_stocks()

    portfolio = get_portfolio()
    results, total = calculate_portfolio(portfolio)
    display_summary(results, total)
    save_to_file(results, total)

    print("  Thank you for using Stock Portfolio Tracker!\n")


# ─────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────
if __name__ == "__main__":
    main()
