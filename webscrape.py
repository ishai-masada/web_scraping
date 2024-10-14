'''
Web scraping
'''
import requests

zillow_url = "https://www.zillow.com/"
beta_url = "https://www.beta.team/careers/"
#args = {'username': 'ishai', 'password': 'butts'}
#args = {'page': 2, 'count': 25}
response = requests.get(zillow_url)
#response = requests.post("https://httpbin.org/post", data=payload)
#response = requests.get("https://httpbin.org/basic-auth/ishai/butts", auth=('ishai', 'butts'))

'''
try:
    response = requests.get("https://httpbin.org/delay/9", timeout=3)
except requests.exceptions.ReadTimeout:
    print("The website took too long to retrieve.")
'''

if response.status_code != 204:
    try:
        website_data = response.json()
    except ValueError:
        print("Error. The website does not support json content\n")
        website_data = response.text

#print(website_data)
