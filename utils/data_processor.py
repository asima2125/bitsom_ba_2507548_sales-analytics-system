from collections import defaultdict

def calculate_total_revenue(transactions):
    return sum(t["Quantity"] * t["UnitPrice"] for t in transactions)


def region_wise_sales(transactions):
    data = defaultdict(lambda: {"total_sales": 0, "transaction_count": 0})
    total = calculate_total_revenue(transactions)

    for t in transactions:
        amt = t["Quantity"] * t["UnitPrice"]
        r = t["Region"]
        data[r]["total_sales"] += amt
        data[r]["transaction_count"] += 1

    for r in data:
        data[r]["percentage"] = round((data[r]["total_sales"] / total) * 100, 2)

    return dict(sorted(data.items(), key=lambda x: x[1]["total_sales"], reverse=True))


def top_selling_products(transactions, n=5):
    prod = defaultdict(lambda: {"qty": 0, "rev": 0})

    for t in transactions:
        p = t["ProductName"]
        prod[p]["qty"] += t["Quantity"]
        prod[p]["rev"] += t["Quantity"] * t["UnitPrice"]

    return sorted(
        [(p, v["qty"], v["rev"]) for p, v in prod.items()],
        key=lambda x: x[1],
        reverse=True
    )[:n]


def customer_analysis(transactions):
    cust = defaultdict(lambda: {"total": 0, "count": 0, "products": set()})

    for t in transactions:
        amt = t["Quantity"] * t["UnitPrice"]
        c = t["CustomerID"]
        cust[c]["total"] += amt
        cust[c]["count"] += 1
        cust[c]["products"].add(t["ProductName"])

    result = {}
    for c, v in cust.items():
        result[c] = {
            "total_spent": v["total"],
            "purchase_count": v["count"],
            "avg_order_value": round(v["total"] / v["count"], 2),
            "products_bought": sorted(v["products"])
        }

    return dict(sorted(result.items(), key=lambda x: x[1]["total_spent"], reverse=True))


def daily_sales_trend(transactions):
    daily = defaultdict(lambda: {"rev": 0, "count": 0, "cust": set()})

    for t in transactions:
        d = t["Date"]
        daily[d]["rev"] += t["Quantity"] * t["UnitPrice"]
        daily[d]["count"] += 1
        daily[d]["cust"].add(t["CustomerID"])

    return {
        d: {
            "revenue": v["rev"],
            "transaction_count": v["count"],
            "unique_customers": len(v["cust"])
        }
        for d, v in sorted(daily.items())
    }


def find_peak_sales_day(transactions):
    daily = daily_sales_trend(transactions)
    date, info = max(daily.items(), key=lambda x: x[1]["revenue"])
    return date, info["revenue"], info["transaction_count"]


def low_performing_products(transactions, threshold=10):
    prod = defaultdict(lambda: {"qty": 0, "rev": 0})

    for t in transactions:
        p = t["ProductName"]
        prod[p]["qty"] += t["Quantity"]
        prod[p]["rev"] += t["Quantity"] * t["UnitPrice"]

    return sorted(
        [(p, v["qty"], v["rev"]) for p, v in prod.items() if v["qty"] < threshold],
        key=lambda x: x[1]
    )

