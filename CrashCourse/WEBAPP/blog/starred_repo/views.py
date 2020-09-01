from django.shortcuts import render
from . import starred_repos
from .forms import QueriedLanguageForm

def gitgraph(request):
  if request.method != 'POST':
    # No data, display a blank form.
    form = QueriedLanguageForm()
  else:
    # POST data; process.
    form = QueriedLanguageForm(request.POST)
    if form.is_valid():
      queriedLanguage = form.cleaned_data.get('queriedLanguage')
      plot_div = starred_repos.makeGraph(queriedLanguage)
      context = {
        'plot_div': plot_div,
        'form': form
      }
      return render(request, 'starred_repo/gitgraph.html', context)

  context = {'form': form}
  return render(request, 'starred_repo/gitgraph.html', context)
