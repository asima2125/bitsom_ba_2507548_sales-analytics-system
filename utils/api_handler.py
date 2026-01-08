import requests

def fetch_all_products():
    try:
        r = requests.get("https://dummyjson.com/products?limit=100", timeout=10)
        r.raise_for_status()
        print("✓ API fetch successful")
        return r.json()["products"]
    except Exception as e:
        print(f"❌ API failure: {e}")
        return []


def create_product_mapping(products):
    return {
    p.get("id"): {
        "category": p.get("category"),
        "brand": p.get("brand"),
        "rating": p.get("rating")
    }
    for p in products
    if p.get("id") is not None
  }



def enrich_sales_data(transactions, mapping):
    enriched = []

    for t in transactions:
        try:
            pid = int(t["ProductID"][1:])
            api = mapping.get(pid)
            if api:
                t.update({
                    "API_Category": api["category"],
                    "API_Brand": api["brand"],
                    "API_Rating": api["rating"],
                    "API_Match": True
                })
            else:
                t.update({
                    "API_Category": None,
                    "API_Brand": None,
                    "API_Rating": None,
                    "API_Match": False
                })
        except:
            t["API_Match"] = False

        enriched.append(t)

    save_enriched_data(enriched)
    return enriched


def save_enriched_data(data, filename="data/enriched_sales_data.txt"):
    headers = data[0].keys()

    with open(filename, "w", encoding="utf-8") as f:
        f.write("|".join(headers) + "\n")
        for t in data:
            f.write("|".join("" if t[h] is None else str(t[h]) for h in headers) + "\n")
