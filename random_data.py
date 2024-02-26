"""
randomizing data
"""
import random
from datetime import datetime, timedelta


def create_assets(p):
    """
    create random assets
    """
    today = datetime.now().date()
    assets = []
    for i in range(p):
        asset_id = i + 1
        purchase_date = today - timedelta(days=random.randint(420, 750))
        assets.append(
            {"id": asset_id, "purchase_date": purchase_date.strftime("%Y-%m-%d")}
        )
    return assets


def create_rentals(assets, q):
    """
    create rent for above assets
    """
    rentals = []
    for asset in assets:
        asset_id = asset["id"]
        purchase_date = datetime.strptime(asset["purchase_date"], "%Y-%m-%d").date()

        if len(assets) / q > 1:
            r = len(assets) / q
        else:
            r = 1
        for _ in range(r):
            rental_id = len(rentals) + 1
            start_date = purchase_date + timedelta(days=random.randint(1, 365))
            end_date = start_date + timedelta(days=random.randint(1, 30))
            rentals.append(
                {
                    "id": rental_id,
                    "asset_id": asset_id,
                    "start_date": start_date.strftime("%Y-%m-%d"),
                    "end_date": end_date.strftime("%Y-%m-%d"),
                }
            )
    result = []
    while len(result) <= q:
        r = random.choice(rentals)
        result.append(r)
    return result


if __name__ == "__main__":
    all_assets = create_assets(5)
    all_rentals = create_rentals(all_assets, 10)

    print("Assets:")
    print(all_assets)
    print("\nRentals:")
    print(all_rentals)
