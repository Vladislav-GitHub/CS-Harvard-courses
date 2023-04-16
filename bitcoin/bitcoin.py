import sys
import requests

try:
    if len(sys.argv) != 2:
        raise IndexError
    elif type(float(sys.argv[1])) != float:
        raise ValueError
    else:
        n = float(sys.argv[1])
except requests.RequestException:
    sys.exit(1)
except IndexError:
    print('Missing command-line argument')
    sys.exit(1)
except ValueError:
    print('Command-line argument is not a number')
    sys.exit(1)
else:
    request = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json') # response 200
    response = request.json() # json object
    amount = response["bpi"]["USD"]["rate_float"]
    print(f"${n * amount:,.4f}")