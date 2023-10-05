import os
import requests
from dotenv import load_dotenv

load_dotenv()
def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape information from LinkedIn profiles,
     Manually scrape the information from the LinkedIn profile"""
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    headers = {'Authorization': 'Bearer ' + os.environ['PROXYCURL_API_KEY']}