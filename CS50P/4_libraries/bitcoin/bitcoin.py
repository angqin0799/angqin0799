import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing Command-Line argument")
else:
    response = requests.get("
                            /bpi/currentprice.json")
    data = response.json()
    # print(json.dumps(data, indent =4))

current_bitcoin_usd = data["bpi"]["USD"]["rate_float"]

try:
    num = float(sys.argv[1])
except ValueError:
    sys.exit("Command-Line argument is not a number")
else:
    amount = num * current_bitcoin_usd
    print(f"${amount:,.4f}")
