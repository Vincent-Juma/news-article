class Article():
  '''
  defines article objects
  '''

  def __init__(self, author, title, description, url, url_to_image, published_at, content):
    '''
    requires for values upon object instantiation
    '''

    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.url_to_image = url_to_image
    self.published_at = published_at
    self.content = content

class Source():
  '''
  defines source objects
  '''

  def __init__(self, id, name, description, url, category, language, country):
    '''
    requires for values upon object instantiation
    '''

    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category
    self.language = language
    self.country = country