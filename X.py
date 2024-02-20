import requests
from bs4 import BeautifulSoup

# Replace this with your Scraper API key
scraper_api_key = '7e44b4ad81513e83b8d31eed2b986f19'

# URL of the Twitter profile page
profile_url = 'https://twitter.com/Collective_Col'

# Use Scraper API to bypass any blocks and retrieve HTML content
scraper_url = f'http://api.scraperapi.com/?api_key={scraper_api_key}&url={profile_url}'
response = requests.get(scraper_url)

if response.status_code == 200:
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract relevant information
    followers_count = soup.find('a', attrs={'data-nav': 'followers'}).find('span', class_='css-901oao css-16my406 r-1qd0xha r-vw2c0b r-ad9z0x r-bcqeeo r-qvutc0').text
    following_count = soup.find('a', attrs={'data-nav': 'following'}).find('span', class_='css-901oao css-16my406 r-1qd0xha r-vw2c0b r-ad9z0x r-bcqeeo r-qvutc0').text
    tweets_count = soup.find('a', attrs={'data-nav': 'tweets'}).find('span', class_='css-901oao css-16my406 r-1qd0xha r-vw2c0b r-ad9z0x r-bcqeeo r-qvutc0').text
    
    # Print extracted information
    print("Followers Count:", followers_count)
    print("Following Count:", following_count)
    print("Tweets Count:", tweets_count)
else:
    print("Error accessing Twitter data:", response.text)
