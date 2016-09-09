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


def get_photos(hashtag):
    '''
    This method queries Instagram 'media/search' 
    (https://www.instagram.com/developer/endpoints/media/)
    API endpoint for a given lati/longi and returns the reply as a json()
    '''
    r = requests.get("https://api.instagram.com/v1/tags/{}/media/recent?access_token={}".format(hashtag, INSTA_ACCESS_TOKEN))
    
    return r.json()


@app.route('/describe/<hashtag>')
def describe_hashtag(hashtag):
    
    photos_urls = get_photos(hashtag)
    print ""
    print ""
    print ""
    print ""
    print ""
    print photos_urls
    print ""
    print ""
    print ""
    print ""
    print ""    
   
    return render_template('./address.html', photos=photos_urls)

if __name__ == "__main__":
    app.run(port=8080, debug=True)