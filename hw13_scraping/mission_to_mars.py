import pandas as pd
from bs4 import BeautifulSoup
import requests

# Step 1- Scraping

##NASA Mars News
def mng_latest():
    mng_url='https://mars.nasa.gov/'
    mng_res=requests.get(mng_url+'news/')
    mng_soup = BeautifulSoup(mng_res.text, 'html.parser')
    mng_latest_news=mng_soup.find('div',class_='content_title').find('a')
    mng_latest_title=mng_latest_news.string.strip()
    mng_latest_p_url=mng_latest_news.attrs['href']
    mng_latest_p_res=requests.get(mng_url+mng_latest_p_url)
    mng_latest_p_soup=BeautifulSoup(mng_latest_p_res.text, 'html.parser')
    mng_latest_p_iter=mng_latest_p_soup.find('div',class_='wysiwyg_content').find_all('p')
    mng_latest_p=''
    for p in mng_latest_p_iter:
        mng_latest_p+=(p.get_text()+'\n')
    mng_latest_p=mng_latest_p.strip()    
    return mng_latest_title,mng_latest_p


##JPL Mars Space Images - Featured Image
def featured_image_url():
    jpl_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    jpl_soup=BeautifulSoup(requests.get(jpl_url).text, 'html.parser')
    featured_image_url=jpl_soup.find('a', class_='button fancybox').attrs['data-fancybox-href']
    featured_image_url='https://www.jpl.nasa.gov'+featured_image_url
    return featured_image_url


##Mars Weather
def mars_weather():
    mw_url='https://twitter.com/marswxreport?lang=en'
    mw_res=requests.get(mw_url)
    mw_soup=BeautifulSoup(mw_res.text, 'html.parser')
    weather=mw_soup.find_all('div',class_="js-tweet-text-container")
    for w in weather:
        if w.find('p').string:
            weather=w.find('p').string.strip()
            return weather
        else:
            continue
    return 


##Mars Facts
def mars_facts():
    mf_url='https://space-facts.com/mars/'
    df=pd.read_html(mf_url)[0]
    df.columns=['key','value']
    #mars_facts=df.to_html(index=False)
    return df


##Mars Hemisperes
def hemisphere_image_urls():
    mh_start_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    mh_res=requests.get(mh_start_url)
    mh_soup=BeautifulSoup(mh_res.text,'html.parser')
    mh_items=mh_soup.find_all('div',class_='item')
    mh_url='https://astrogeology.usgs.gov'
    hemisphere_image_urls=[]
    for item in mh_items:
        title=item.find('h3').string.strip()
        item_url=item.find('a', class_='itemLink product-item').attrs['href']
        item_url=mh_url+item_url
        item_soup=BeautifulSoup(requests.get(item_url).text,'html.parser')
        item_img_url=item_soup.find('div', class_='downloads').find_all('a', target='_blank')[0].attrs['href']
        dic={'title':title,'img_url':item_img_url}
        hemisphere_image_urls.append(dic)
    return hemisphere_image_urls


if __name__=='__main__':
    #print(mng_latest()[0])
    #print(mng_latest()[1])
    #print(featured_image_url())
    #print(mars_weather())
    #print(mars_facts())
    print(hemisphere_image_urls())







