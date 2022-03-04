from django.shortcuts import render

members = [
  # Alex Palmer.
  {
    'first': 'Alex',
    'middle': '',
    'last': 'Palmer',
    'description': 'Computer Science student',
  },
  # Ameen El-Rasheedy
  {
    'first': 'Ameen',
    'middle': '',
    'last': 'El-Rasheedy',
    'description': 'Computer Science student',
  },
  # Davina Robinson
  {
    'first': 'Davina',
    'middle': '',
    'last': 'Robinson',
    'description': 'Computer Science student',
  },
  # Fernando Cruz
  {
    'first': 'Fernando',
    'middle': '',
    'last': 'Cruz',
    'description': 'Computer Science student',
  },
  # Luis David Licea Torres
  {
    'first': 'Luis',
    'middle': 'David',
    'last': 'Licea Torres',
    'description': 'Computer Science student, GitHub account is <code>github.com/luis-licea/</code>',
  },
]

# Create your views here.
def home(request):
  context = {
    'title': 'Nifti',
  }
  return render(request, 'home/home.html', context)

def about(request):
  context = {
    'title': 'About',
    'members': members
  }
  return render(request, 'home/about.html', context)
