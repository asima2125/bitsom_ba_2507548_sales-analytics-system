def read_sales_data(filename):
    encodings = ["utf-8", "latin-1", "cp1252"]
    for enc in encodings:
        try:
            with open(filename, "r", encoding=enc) as f:
                lines = f.readlines()
                break
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print(f"❌ File not found: {filename}")
            return []
    else:
        print("❌ Unable to read file with supported encodings")
        return []

    return [line.strip() for line in lines[1:] if line.strip()]


def parse_transactions(raw_lines):
    transactions = []

    for line in raw_lines:
        parts = line.split("|")
        if len(parts) != 8:
            continue

        tid, date, pid, pname, qty, price, cid, region = parts

        try:
            pname = pname.replace(",", "")
            qty = int(qty.replace(",", ""))
            price = float(price.replace(",", ""))

            transactions.append({
                "TransactionID": tid.strip(),
                "Date": date.strip(),
                "ProductID": pid.strip(),
                "ProductName": pname.strip(),
                "Quantity": qty,
                "UnitPrice": price,
                "CustomerID": cid.strip(),
                "Region": region.strip()
            })
        except ValueError:
            continue

    print(f"Total records parsed: {len(raw_lines)}")
    return transactions


def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    valid = []
    invalid = 0

    regions = sorted({t["Region"] for t in transactions if t["Region"]})
    amounts = [
        t["Quantity"] * t["UnitPrice"]
        for t in transactions
        if t["Quantity"] > 0 and t["UnitPrice"] > 0
    ]

    print(f"Available Regions: {', '.join(regions)}")
    print(f"Transaction Amount Range: ₹{min(amounts):,.2f} - ₹{max(amounts):,.2f}")

    filtered_region = 0
    filtered_amount = 0

    for t in transactions:
        if not (
            t["TransactionID"].startswith("T") and
            t["ProductID"].startswith("P") and
            t["CustomerID"].startswith("C") and
            t["Quantity"] > 0 and
            t["UnitPrice"] > 0 and
            t["Region"]
        ):
            invalid += 1
            continue

        amount = t["Quantity"] * t["UnitPrice"]

        if region and t["Region"].lower() != region.lower():
            filtered_region += 1
            continue
        if min_amount and amount < min_amount:
            filtered_amount += 1
            continue
        if max_amount and amount > max_amount:
            filtered_amount += 1
            continue

        valid.append(t)

    print(f"Invalid records removed: {invalid}")
    print(f"Valid records after cleaning: {len(valid)}")

    summary = {
        "total_input": len(transactions),
        "invalid": invalid,
        "filtered_by_region": filtered_region,
        "filtered_by_amount": filtered_amount,
        "final_count": len(valid)
    }

    return valid, invalid, summary

