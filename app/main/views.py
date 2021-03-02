from flask import render_template, redirect, url_for
from . import main
from ..request import get_sources, get_articles_from_source
from ..models import Source, Article

#views
@main.route('/')
def index():
  '''
  view root page functions that returns the index page and its data
  '''
  sources = get_sources()
  news_sources = get_sources()

  return render_template('index.html', news_sources=news_sources)

@main.route('/source/<source_name>')
def source(source_name):
  '''
  features story and returns source.html and its respective articles
  '''

  articles = get_articles_from_source(source_name)

  return render_template('source.html', articles=articles)
