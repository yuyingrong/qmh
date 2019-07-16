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

def visual_heatmapPatientMonthlyAdmissionFrequency(request):
    return render(request, 'visual_heatmapPatientMonthlyAdmissionFrequency.html')

def visual_sankeyPhilanthropistsOrganizationsAssociation(request):
    return render(request, 'visual_sankeyPhilanthropistsOrganizationsAssociation.html')


###### end visualizations ######


def contact(request):
    return render(request, 'contact.html')

def bibliography(request):
    return render(request, 'bibliography.html')

###### learn ######

def learn(request):
    return render(request, 'learn.html')

def learn_theYorkRetreat(request):
    return render(request, 'learn_theYorkRetreat.html')

def learn_changesInAdminOverTime(request):
    return render(request, 'learn_changesInAdminOverTime.html')

def learn_fromYorkRetreatToFriendsAsylum(request):
    return render(request, 'learn_fromYorkRetreatToFriendsAsylum.html')

def learn_reasoningAboutInsanity(request):
    return render(request, 'learn_reasoningAboutInsanity.html')

def learn_typesOfMentalIllness(request):
    return render(request, 'learn_typesOfMentalIllness.html')

def learn_moralTreatment(request):
    return render(request, 'learn_moralTreatment.html')

def learn_caseStudies(request):
    return render(request, 'learn_caseStudies.html')

def learn_patientHometowns(request):
    return render(request, 'learn_patientHometowns.html')

def learn_mentalHealthAndQuakerTheology(request):
    glossary_list = Glossary.objects.order_by('term')
    term_list = ['_'.join([w.lower() for w in glossary.term.split(' ')]) for glossary in glossary_list]# due to string joining, now to retrieve value from the dict, all keys need to have no separator
    meaning_list = [glossary.meaning for glossary in glossary_list]
    glossary_dict = {}
    for (term, meaning) in zip(term_list, meaning_list):
        glossary_dict[term] = meaning
    return render(request, 'learn_mentalHealthAndQuakerTheology.html', {'glossary_dict': glossary_dict})


###### end learn ######

def glossary(request):
    glossary_list = Glossary.objects.order_by('term')
    term_list = [glossary.term for glossary in glossary_list]
    meaning_list = [glossary.meaning for glossary in glossary_list]
    glossary_dict = {}
    for (term, meaning) in zip(term_list, meaning_list):
        glossary_dict[term] = meaning 

    return render(request, 'glossary.html', {'glossary_dict': glossary_dict})




