from utils.file_handler import *
from utils.data_processor import *
from utils.api_handler import *
from datetime import datetime

def generate_sales_report(transactions, enriched, filename="output/sales_report.txt"):
    total_revenue = calculate_total_revenue(transactions)
    daily = daily_sales_trend(transactions)
    peak = find_peak_sales_day(transactions)
    regions = region_wise_sales(transactions)
    top_products = top_selling_products(transactions)
    customers = list(customer_analysis(transactions).items())[:5]
    low_products = low_performing_products(transactions)

    enriched_count = sum(1 for t in enriched if t["API_Match"])
    failed = [t["ProductName"] for t in enriched if not t["API_Match"]]

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("SALES ANALYTICS REPORT\n")
        f.write(f"Generated: {datetime.now()}\n")
        f.write(f"Records Processed: {len(transactions)}\n")
        f.write("=" * 50 + "\n\n")

        f.write("OVERALL SUMMARY\n")
        f.write(f"Total Revenue: ₹{total_revenue:,.2f}\n")
        f.write(f"Total Transactions: {len(transactions)}\n")
        f.write(f"Date Range: {min(daily)} to {max(daily)}\n\n")

        f.write("REGION PERFORMANCE\n")
        for r, v in regions.items():
            f.write(f"{r}: ₹{v['total_sales']:,.2f} ({v['percentage']}%)\n")

        f.write("\nTOP PRODUCTS\n")
        for i, p in enumerate(top_products, 1):
            f.write(f"{i}. {p[0]} | Qty: {p[1]} | Rev: ₹{p[2]:,.2f}\n")

        f.write("\nPEAK SALES DAY\n")
        f.write(f"{peak[0]} | ₹{peak[1]:,.2f} | {peak[2]} transactions\n")

        f.write("\nAPI ENRICHMENT\n")
        f.write(f"Enriched: {enriched_count}/{len(enriched)}\n")
        f.write(f"Failed Products: {set(failed)}\n")

def main():
    try:
        print("=" * 40)
        print("SALES ANALYTICS SYSTEM")
        print("=" * 40)

        raw = read_sales_data("data/sales_data.txt")
        parsed = parse_transactions(raw)

        choice = input("Do you want to filter data? (y/n): ").strip().lower()
        region = None
        if choice == "y":
            region = input("Enter region: ").strip()
        elif choice != "n":
            print("❌ Invalid choice. Please enter 'y' or 'n'.")
            return
        valid, invalid, summary = validate_and_filter(parsed, region=region)

        api_products = fetch_all_products()
        mapping = create_product_mapping(api_products)
        enriched = enrich_sales_data(valid, mapping)

        generate_sales_report(valid, enriched)

        print("✓ Enriched data saved")
        print("✓ Report generated")
        print("✓ Process complete")

    except Exception as e:
        print(f"❌ Fatal error: {e}")


if __name__ == "__main__":
    main()
