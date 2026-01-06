# DATA FETCHING (Satellite Images)

import pandas as pd
import requests
import os
import time

MAPBOX_TOKEN = "pk.eyJ1IjoiYW51MjQyMSIsImEiOiJjbWplMnhicWYwYWN6M2RzNnNidzE3eHVlIn0.x__VhW_HIFetBZIjiv-nrw"
ZOOM = 18
SIZE = "224x224"

def fetch_images(csv_path, save_dir):
    df = pd.read_csv(csv_path)
    os.makedirs(save_dir, exist_ok=True)

    for _, row in df.iterrows():
        lat, lon, idx = row["lat"], row["long"], row["id"]

        url = (
            f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/"
            f"{lon},{lat},{ZOOM}/{SIZE}"
            f"?access_token={MAPBOX_TOKEN}"
        )

        out_path = f"{save_dir}/{idx}.png"
        if os.path.exists(out_path):
            continue

        r = requests.get(url)
        if r.status_code == 200:
            with open(out_path, "wb") as f:
                f.write(r.content)

        time.sleep(0.3)

if __name__ == "__main__":
    fetch_images("data/train.csv", "images/train")
    fetch_images("data/test.csv", "images/test")
