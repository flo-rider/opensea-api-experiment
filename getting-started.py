import requests
import pandas as pd

assets = pd.DataFrame(requests.get("https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=20").json()['assets'])
assets.head().T