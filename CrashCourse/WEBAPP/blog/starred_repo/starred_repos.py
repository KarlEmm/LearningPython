import requests
from plotly.graph_objs import Bar
from plotly.offline import plot

# This File Makes a bar chart with Plotly showing the popularity of each repo
# mainly written with Python.

#queriedLanguage = 'python'
# Make an API call to GitHub for all the repo in Python; sorts them by stars.
def fetchRepos(queriedLanguage):
  url = f'https://api.github.com/search/repositories?q=language:{queriedLanguage}&sort=stars'
  headers = {'Accept': 'application/vnd.github.v3+json'}
  r = requests.get(url, headers=headers)
  print(f"Status code: {r.status_code}.")

  # Process results.
  response_dict = r.json()
  return response_dict['items']

def buildData(queriedLanguage):
  repo_dicts = fetchRepos(queriedLanguage)
  repo_links, stars, labels = [], [], []
  for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}<br />{description}'
    labels.append(label)
  return [repo_links, stars, labels]
  
def makeGraph(queriedLanguage):
  dataDict = buildData(queriedLanguage)
  repo_links = dataDict[0]
  stars = dataDict[1]
  labels = dataDict[2]
  # Make visualization
  data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'marker': {
      'color': 'lightblue',
      'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
    'hovertext': labels,
  }]

  my_layout = {
    'title': f'Most-starred {queriedLanguage} Projects on GitHub',
    'xaxis': {
      'title': 'Repository',
      'titlefont': {'size': 24},
      'tickfont': {'size': 14}
    },
    'yaxis': {
      'title': 'Stars',
      'titlefont': {'size': 24},
      'tickfont': {'size': 14}
    },
    'height': 900
  }

  fig = {'data': data, 'layout': my_layout}
  plot_div = plot(fig, output_type='div')
  return plot_div


