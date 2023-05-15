import os
import requests

""" Step-1:
    1. A function to fetch and scrape LinkedIn information from a URL
    2. To fetch the linkedIn profile, we use nubela.co proxycurl external service
    3. SignUp for the account and get the token, store the token on .env

"""

def scrape_linkedin_profile(linkedin_profile_url: str):
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    request_header = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_TOKEN")}'}

    # Make a request
    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=request_header
    )

    # We get a JSON of linked profile.
    cleaned_linkedin_profile = response.json()

    # the JSON mayhave lots of information, so let's clean it up.
    cleaned_linkedin_profile = {
        key: value
        # If the JSON values are empty list, or empty string, or None (null) filter these values
        for key, value in cleaned_linkedin_profile.items()
        if value not in ([], "", "", None)
        and key not in ["people_also_viewed", "certifications"]
    }

    if cleaned_linkedin_profile.get("groups"):
        for group_dict in cleaned_linkedin_profile.get("groups"):
            group_dict.pop("profile_pic_url")

    return cleaned_linkedin_profile
