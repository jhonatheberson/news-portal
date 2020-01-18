from django.core.management.base import BaseCommand
from django.utils import timezone
from bs4 import BeautifulSoup as bs
from portal.models import News, Portal
from requests import get


class Command(BaseCommand):

    help = 'class responsible for web scraping to capture the news and add it to the database'

    def handle(self,  *args, **kwargs):
        """responsible function of web scraping and capturing the headlines of the news.

        Keyword arguments:
        rargs -- django command method default (default)
        kwargs -- django command method default (default)
        """
        base_url = 'https://www.tecmundo.com.br' # url that will be done web scraping
        base_portal = Portal(name=base_url)
        base_portal.save() # saving the url to the database
        title = [] # create a queue to store the titles
        tecmundo = get(base_url) # requests a request to url
        tecmundo_page = bs(tecmundo.text, 'html.parser') # get the text of the request response only html
        boxes = tecmundo_page.find_all("h2") # search all over the site just what is h2 tagged
        size_boxes = len(boxes) 
        for i in range(size_boxes):
            title.append(boxes[i].text) # add titles to the queue
            news = News(title=title[i]) 
            news.save() # saving the title to the database
