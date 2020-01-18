from django.core.management.base import BaseCommand
from django.utils import timezone
from bs4 import BeautifulSoup as bs
from portal.models import News, Portal
from requests import get
# import sqlite3
# import datetime
# import time

# connection = sqlite3.connect('db.sqlite3')
# c = connection.cursor()

# date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self,  *args, **kwargs):
        
        
        base_url = 'https://www.tecmundo.com.br'
        base_portal = Portal(name = base_url)
        base_portal.save()        
        title = []
        tecmundo = get(base_url)
        tecmundo_page = bs(tecmundo.text, 'html.parser')
        boxes = tecmundo_page.find_all("h2")
        size_boxes = len(boxes)
        for i in range(size_boxes):
            title.append(boxes[i].text)
            news = News(title = title[i])
            news.save()
            # c.execute('INSERT INTO News(title, portal, create_at, update_at) VALUES (?,?,?,?)',(title[i], base_url, date, date))
            
            # connection.commit()
