import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin")
    response.raise_for_status()
    content = response.json()

except requests.HTTPError:
    print("Couldn't complete request!")

price = float(content["data"]["priceUsd"])
total = price * n

print(f"${total:,.4f}")
