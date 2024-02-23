from linkedin_api import Linkedin

# # Authenticate using any Linkedin account credentials
# api = Linkedin('reedhoffman@linkedin.com', '*******')

# # GET a profile
# profile = api.get_profile('billy-g')

# # GET a profiles contact info
# contact_info = api.get_profile_contact_info('billy-g')

# # GET 1st degree connections of a given profile
# connections = api.get_profile_connections('1234asc12304')

# nubela
import requests

api_key = 'QjbU0fEoNCQoRi-MW6HEMA'
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'twitter_profile_url': 'https://twitter.com/johnrmarty/',
    'facebook_profile_url': 'https://facebook.com/johnrmarty/',
    'linkedin_profile_url': 'https://linkedin.com/in/johnrmarty/',
    'extra': 'include',
    'github_profile_id': 'include',
    'facebook_profile_id': 'include',
    'twitter_profile_id': 'include',
    'personal_contact_number': 'include',
    'personal_email': 'include',
    'inferred_salary': 'include',
    'skills': 'include',
    'use_cache': 'if-present',
    'fallback_to_cache': 'on-error',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)

# email finder
import requests
 
url = "https://api.prospeo.io/linkedin-email-finder"
api_key = "51b276c6baafc9ced739d0f2e2795e9e"
 
required_headers = {
    'Content-Type': 'application/json',
    'X-KEY': api_key
}
 
data = {
    'url': 'https://www.linkedin.com/in/john-doe/'
}
 
response = requests.post(url, json=data, headers=required_headers)