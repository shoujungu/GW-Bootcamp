from flask import Flask,render_template
import pandas as pd
from bs4 import BeautifulSoup
import requests
import mission_to_mars as mtm

app = Flask(__name__)

@app.route('/scrape')
def scrape():
    mng_latest=mtm.mng_latest()
    featured_image_url=mtm.featured_image_url()
    mars_weather=mtm.mars_weather()
    mars_facts=mtm.mars_facts()
    hemisphere_image_urls=mtm.hemisphere_image_urls()
    return render_template('index.html',mng_latest=mng_latest,featured_image_url=featured_image_url,
                          mars_weather=mars_weather,mars_facts=mars_facts,hemisphere_image_urls=hemisphere_image_urls)
                          
@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__=='__main__':
    app.run()