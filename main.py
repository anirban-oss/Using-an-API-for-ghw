import requests
import json

# for i in range(100):

# The API endpoint for getting a random quote
api_url = "https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"

# Make the API call
response = requests.get(api_url)

# Parse the JSON response
data = json.loads(response.text)

# Print the quote
print('\n\n\t \033[31mTHE QUOTE OF THE DAY IS: ')
print('\t\t \033[32m','"" ',data["quoteText"],'""',sep='')