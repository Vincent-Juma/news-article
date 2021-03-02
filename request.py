# def get_movie(id):
#     get_movie_details_url = base_url.format(id,api_key)

#     with urllib.request.urlopen(get_movie_details_url) as url:
#         movie_details_data = url.read()
#         movie_details_response = json.loads(movie_details_data)

#         news_object = None
#         if news_details_response:
#             id = news_details_response.get('id')
#             title = news_details_response.get('original_title')
#             overview = news_details_response.get('overview')
#             poster = news_details_response.get('poster_path')
#             vote_average = news_details_response.get('vote_average')
#             vote_count = news_details_response.get('vote_count')

#             news_object = Movie(id,title,overview,poster,vote_average,vote_count)

#     return news_object