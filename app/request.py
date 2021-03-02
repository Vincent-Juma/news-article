from newsapi import NewsApiClient
from .models import Source
from .models import Article
# new input
from .main import main
import urllib.request,json



#get api key
api_key = None

def configure_request(app):
  '''
  initial configuration for important variables
  args:
    app instance
  '''

  global api_key
  api_key = app.config['NEWS_API_KEY']

def get_sources():
  '''
  function that gets sources from api
  returns:
    array of sources
  '''

  api = NewsApiClient(api_key=api_key)
  news_sources_data = api.get_sources()
  news_sources = []

  for source in news_sources_data['sources']:
    news_sources.append(
      Source(
        source.get('id'),
        source.get('name'),
        source.get('description'),
        source.get('url'),
        source.get('category'),
        source.get('language'),
        source.get('country')
      )
    )

  return news_sources

def get_articles_from_source(source):
  '''
  function to get articles of specifies source from api
  args:
    source: the source from which the articles are to be retrieved
  
  returns:
    array of articles in source
  '''

  api = NewsApiClient(api_key=api_key)
  source_articles = api.get_everything(sources=source)
  articles = []

  for article in source_articles['articles']:
    articles.append(
      Article(
        article.get('author'),
        article.get('title'),
        article.get('description'),
        article.get('url'),
        article.get('urlToImage'),
        article.get('publishedAt'),
        article.get('content')
      )
    )
  
  return articles