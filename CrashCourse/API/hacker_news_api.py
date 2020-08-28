import json
import requests
from operator import itemgetter

# Make an API call to HackerNews and ranks the top 10 articles in order of the
# number of comments they got.


# First, get the ids of the top articles (top 500).
top_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(top_url)
submission_ids = r.json()

# Second, make a dictionary of dictionaries for the top 10 articles.
submission_dicts = []
for articlenumber in submission_ids[:10]:
  article_url = f'https://hacker-news.firebaseio.com/v0/item/{articlenumber}.json'
  requested_article = requests.get(article_url)
  requested_article_dict = requested_article.json()
  submission_dict = {
    'title': requested_article_dict['title'],
    'url_html': requested_article_dict['url'],
    'comments': requested_article_dict['descendants'],
  }
  submission_dicts.append(submission_dict)
  submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)
  print(f"id: {articlenumber}\t status: {requested_article.status_code}")

# Print the desired information.
for submission_dict in submission_dicts:
  print(f"Title: {submission_dict['title']}")
  print(f"Link: {submission_dict['url_html']}")
  print(f"Number of comments: {submission_dict['comments']}\n")


# Expand this to send an email with the top articles.