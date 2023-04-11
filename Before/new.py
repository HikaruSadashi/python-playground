import requests
from bs4 import BeautifulSoup

# Define the url of the website
url = 'https://www.linkedin.com/in/will-mcintyre-b05b8b1ab/'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the user profile elements on the page
profiles = soup.find_all('div', class_='user-profile')

# Iterate through the profiles and extract the data
for profile in profiles:
    name = profile.find('h2').text
    job_title = profile.find('p', class_='job-title').text
    company = profile.find('p', class_='company').text
    education = profile.find('p', class_='education').text

    # Print the extracted data
    print('Name:', name)
    print('Job Title:', job_title)
    print('Company:', company)
    print('Education:', education)