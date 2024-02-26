"""
randomizing data
"""
import random
from datetime import datetime, timedelta


def create_assets(p):
    """
    to create assets
    """
    today = datetime.now().date()
    assets = []
    for _ in range(p):
        asset_id = len(assets) + 1
        purchase_date = today - timedelta(days=random.randint(500, 2000))
        assets.append(
            {"id": asset_id, "purchase_date": purchase_date.strftime("%Y-%m-%d")}
        )
    return assets


def create_rentals(assets, q):
    """
    to create rent
    """
    rentals = []
    for _ in range(q):
        rental_id = len(rentals) + 1
        asset = random.choice(assets)
        start_date = datetime.strptime(asset["purchase_date"], "%Y-%m-%d").date()
        end_date = today = datetime.now().date()

        while start_date >= end_date:
            start_date = today - timedelta(days=random.randint(1, 365))
            end_date = today - timedelta

        rentals.append(
            {
                "id": rental_id,
                "asset_id": asset["id"],
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
            }
        )

    return rentals


if __name__ == "__main__":
    all_assets = create_assets(50)

    all_rentals = create_rentals(all_assets, 30)
    # print("Assets:",assets)
    # print(assets)

    print(all_rentals)
