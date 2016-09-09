import os
import time
import geocoder

import requests

from flask import Flask, render_template

INSTA_ACCESS_TOKEN = '1233376.e029fea.bb5a53f0d27445a1b00851b91f378094'
WEATHER_API_KEY = '4ad8eb1a625428af3b0490405229ad0d'
GOOGLE_MAPS_STATIC_API_KEY = 'AIzaSyBNRDUgu_WkHe8X3qdvyQYLYxz2Ln8oN0I'
GOOGLE_MAPS_STREETVIEW_API_KEY = 'AIzaSyDhgbOzc2OKdiJJj1_LQKpKu4C3-Xf2AlY'

# Better way (yet still kinda bad) to load secrets
# secrets = dict()
# with open("SECRETS.json") as f:
#     secrets = json.loads(f.read())

# 'static_folder' is used for serving static files
proj_dir = os.path.abspath(os.path.dirname(__file__))
static_folder = os.path.join(proj_dir, 'static')


app = Flask(__name__)


def get_photos():
    '''
    This method queries Instagram 'media/search' 
    (https://www.instagram.com/developer/endpoints/media/)
    API endpoint for a given lati/longi and returns the reply as a json()
    '''
    insta_address = "https://api.instagram.com/v1/tags/100tjejerkodar/media/recent?access_token={}".format(INSTA_ACCESS_TOKEN)

    photos = requests.get(insta_address)
    
    return photos.json()

# def _get_hashtag(insta_address):

#     '''
#     I want this to define an instagramhashtag that the get_photos-function can use instead of lati, longi.
#     '''
#     insta_address = "https://api.instagram.com/v1/tags/search?q=tjejerkodar&access_token={}".format(INSTA_ACCESS_TOKEN)

#     hashtag = request.get(insta_address)

#     return hashtag.json()


@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/describe/<address>')
def describe_address(address):

    # This is a list jsons which has a )
    photos_urls = get_photos()
    print "\n\n\n\n\n"
    print photos_urls
    print "\n\n\n\n\n"
    raise
    return render_template('./address.html', address=address.capitalize(),
                           lati=None, longi=None, weather=None,
                           photos=photos_urls, static_map=None,
                           street_view=None), 


if __name__ == "__main__":
    app.run(port=8080, debug=True)