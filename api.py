from newsapi import NewsApiClient
from instance import news_api_key
import datetime as dt
import pandas as pd


newsapi = NewsApiClient(api_key=news_api_key)