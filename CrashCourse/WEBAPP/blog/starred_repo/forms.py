from django import forms

class QueriedLanguageForm(forms.Form):
  CHOICES = [
    ('c', 'c'),
    ('c++','c++'),
    ('go','go'),
    ('java','java'),
    ('javascript','javascript'),
    ('haskell','haskell'),
    ('php','php'),
    ('prolog','prolog'),
    ('python','python'),
    ('rust','rust'),
  ]
  CHOICESORDERED = sorted(CHOICES)
  queriedLanguage = forms.ChoiceField(label="Select a language", choices=CHOICES)