"""
randomizing data
"""
import random
from datetime import datetime, timedelta


def create_assets(p, x):
    """
    create random assets
    """
    today = datetime.now().date()
    assets = []
    for _ in range(p):
        asset_id = len(assets) + 1
        purchase_date = today - timedelta(days=random.randint(1, x))
        assets.append(
            {"id": asset_id, "purchase_date": purchase_date.strftime("%Y-%m-%d")}
        )
    return assets


def create_rentals(assets, q):
    """
    create rent for above assets
    """
    rentals = []
    rental_dates = set()

    for asset in assets:
        asset_id = asset["id"]
        purchase_date = datetime.strptime(asset["purchase_date"], "%Y-%m-%d").date()

        if len(assets) // q > 1 or q // len(assets) > 1:
            r = max(len(assets) // q, q // len(assets))
        else:
            r = 0
        for _ in range(r + 1):
            rental_id = len(rentals) + 1

            while True:
                start_date = purchase_date + timedelta(days=random.randint(1, 365))
                end_date = start_date + timedelta(days=random.randint(1, 30))

                if (
                    start_date >= purchase_date and end_date >= start_date and asset_id,
                    start_date,
                    end_date,
                ) not in rental_dates:
                    rental_dates.add((asset_id, start_date, end_date))
                    break

            rentals.append(
                {
                    "id": rental_id,
                    "asset_id": asset_id,
                    "start_date": start_date.strftime("%Y-%m-%d"),
                    "end_date": end_date.strftime("%Y-%m-%d"),
                }
            )

    return rentals[:q]


if __name__ == "__main__":
    all_assets = create_assets(5, 30)
    all_rentals = create_rentals(all_assets, 100)

    print("Assets:")
    print(all_assets)
    print("\nRentals:")
    print(all_rentals)
    
