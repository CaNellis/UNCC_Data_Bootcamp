# Step 2: use MongoDB anf flask - Create function to execute scraping code and return one dictionary

# import dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import os

def scrape():
    mars_dict = {}
    
    # a) scrape recent news title and paragraph text from NASA's news site
    # use local NASA file
    filepath = os.path.join("News_NASA_Mars_Exploration_Program.html")
    with open(filepath) as file:
        html = file.read()
    # use bs to write into html
    news_soup = bs(html, "html.parser")
    # find latest title
    news_title = news_soup.find("div", class_="content_title").text
    # find latest paragraph
    news_paragraph = news_soup.find("div", class_="rollover_description").text
    # add title and paragraph text to dictionary
    mars_dict['news_title'] = news_title
    mars_dict['news_paragraph'] = news_paragraph
    
    # b) scrape featured image from JPL Mars Space Images
    # define page to be scraped
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # retrieve page with requests module
    response = requests.get(image_url)
    # create bs object; parse with "lxm"
    image_soup = bs(response.text, "lxml") 
    # examine result to determine element that contains sought info
    #result = image_soup.find("div", class_="carousel_items") 
    # use element to find partial url to add to root of image_url
    partial_url = image_soup.find_all("a", class_="fancybox")[0].get("data-fancybox-href")
    # combine partial url with root url
    combined_image_url = "https://www.jpl.nasa.gov" + partial_url
    # add image url to dictionary
    mars_dict['combined_image_url'] = combined_image_url

    # c) scrape latest weather report from mars weather twitter account
    # define page to be scraped
    weather_url = "https://twitter.com/marswxreport?lang=en"
    # retrieve page with requests module
    response = requests.get(weather_url)
    # create bs object; parse with "lxml"
    weather_soup = bs(response.text, "lxml") 
    # examine result to determine element that contains sought info
    #result = weather_soup.find("div", attrs={"class": "tweet", "data-name": "Mars Weather"})
    mars_weather = weather_soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    # add weather to dictionary
    mars_dict['mars_weather'] = mars_weather

    # d) scrape table of facts about mars from space-facts website
    # define page to be scraped
    facts_url = "https://space-facts.com/mars/"
    # use pandas to read url table
    facts_table = pd.read_html(facts_url)
    # convert table into pandas df
    facts_df = facts_table[0]
    # change column names
    facts_df.columns=["Measure","Value"]
    # set index to Measure column
    facts_df.set_index("Measure", inplace=True)
    # convert and save df as html file
    mars_table = facts_df.to_html(justify='center')
    #mars_table = mars_table.replace("\n", "")
    # add table to dictionary
    mars_dict["mars_table"] = mars_table


    # e) scrape images of Mar's hemispheres from USGS Astrogeology site
    # define page to be scraped
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    # retrieve page with requests module
    response = requests.get(hemispheres_url)
    # create bs object; parse with "lxml"
    hemispheres_soup = bs(response.text, "lxml") 
    # examine results to determine element that contains sought info
    results = hemispheres_soup.find_all("div", class_="item")
    # create list for all hemisphere titles and image urls
    hem2_list = []
    # loop through each hemisphere and add title and image link to dictionary then to list
    for result in results: 
        hem_dict = {}      
        # find and add title
        hem_title = result.find('h3').text.replace(' Enhanced', '') 
        hem_dict['title'] = hem_title 
        # find initial image url
        hem_link = result.find('a', class_='itemLink').get('href')
        hemispheres_url2 = "https://astrogeology.usgs.gov" + hem_link
        # use initial url to find and add target image url
        response2 = requests.get(hemispheres_url2)
        hemispheres_soup2 = bs(response2.text, "lxml")
        result2 = hemispheres_soup2.find("img", class_="wide-image").get("src")
        hem_link2 =  "https://astrogeology.usgs.gov" + result2
        hem_dict['img_url'] = hem_link2
        # Append dictionaries to list
        hem2_list.append(hem_dict)    
    # add hemispheres data to dictionary
    mars_dict['hem2_list'] = hem2_list

    return mars_dict