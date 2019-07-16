from django.shortcuts import render

from qmh.models import Glossary

###### primary navigation bar ######

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

###### end primary navigation bar ######


###### visualizations ######

def visualizations(request):
    return render(request, 'visualizations.html')

def heatmap(request):
    return render(request, 'heatmap.html')


###### end visualizations ######


def contact(request):
    return render(request, 'contact.html')



###### learn ######

def learn(request):
    return render(request, 'learn.html')

def learn_fromYorkRetreatToFriendsAsylum(request):
    return render(request, 'learn_fromYorkRetreatToFriendsAsylum.html')

def learn_reasoningAboutInsanity(request):
    return render(request, 'learn_reasoningAboutInsanity.html')

def learn_typesOfMentalIllness(request):
    return render(request, 'learn_typesOfMentalIllness.html')

def learn_moralTreatment(request):
    return render(request, 'learn_moralTreatment.html')

def learn_mentalHealthAndQuakerTheology(request):
    return render(request, 'learn_mentalHealthAndQuakerTheology.html')


###### end learn ######

def glossary(request):
    glossary_list = Glossary.objects.order_by('term')
    term_list = [glossary.term for glossary in glossary_list]
    meaning_list = [glossary.meaning for glossary in glossary_list]
    glossary_list = zip(term_list, meaning_list)
    return render(request, 'glossary.html', {'glossary_list': glossary_list})

