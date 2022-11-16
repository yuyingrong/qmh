
from django.urls import path
from django.urls.conf import re_path
from . import views
from django.contrib.flatpages import views as flat_views
from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [

    #flatpages
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    
    path('bibliography/', flat_views.flatpage, {'url': '/bibliography/'}, name='bibliography'),
    path('health/', flat_views.flatpage, {'url': '/health/'}, name='health'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),

    path('', views.home, name='home'),
    # topnav
    path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),# summer 2019 team decided that a contact form no longer needed; contact button is a link to "mailto:<hc-libraries>"
    path('related-projects/', views.related_projects, name='related-projects'),

    # home
    path('visualizations/', views.visualizations, name='visualizations'),
        path('visualizations/scatterplot-patient-admit-age-admit-year/', views.visual_scatterplotPatientAdmitAgeVsAdmitYear, name="visual_scatterplotPatientAdmitAgeVsAdmitYear"),
        path('visualizations/heatmap-patient-monthly-admission-frequency/', views.visual_heatmapPatientMonthlyAdmissionFrequency, name="visual_heatmapPatientMonthlyAdmissionFrequency"),
        path('visualizations/sankey-philanthropists-organizations-association/', views.visual_sankeyPhilanthropistsOrganizationsAssociation, name="visual_sankeyPhilanthropistsOrganizationsAssociation"),


    # sidebar
    # learn
    #path('learn/', views.learn, name='learn')

        # "the asylum"
        path('the-york-retreat', views.learn_theYorkRetreat, name='learn_theYorkRetreat'),
        path('foundation', views.learn_foundation, name='learn_foundation'),
        path('structure-and-governance', views.learn_structureAndGovernance, name='learn_structureAndGovernance'),
        path('changes-in-admin-over-time', views.learn_changesInAdminOverTime, name='learn_changesInAdminOverTime'),
        path('asylum-architecture', views.learn_asylumArchitecture, name='learn_asylumArchitecture'),
        path('gender-and-staff', views.learn_genderAndStaff, name='learn_genderAndStaff'),
        path('gurney-cottage/', views.learn_gurneyCottage, name='learn_gurneyCottage'),
        path('training-of-doctors', views.learn_trainingOfDoctors, name='learn_trainingOfDoctors'),
        path('training-of-nurses', views.learn_trainingOfNurses, name='learn_trainingOfNurses'),
        path('race-and-staff', views.learn_raceAndStaff, name='learn_raceAndStaff'),
        path('philanthropic-networks', views.learn_philanthropicNetworks, name='learn_philanthropicNetworks'),
        #path('learn/from-york-retreat-to-friends-asylumf', views.learn_fromYorkRetreatToFriendsAsylum, name='learn_fromYorkRetreatToFriendsAsylum'),# one of the new grouping topic of articles; effort aborted
        #path('learn/reasoning-about-insanity', views.learn_reasoningAboutInsanity, name='learn_reasoningAboutInsanity'),# one of the new grouping topic of articles; effort aborted

        # "medical treatment"
        path('types-of-mental-illness', views.learn_typesOfMentalIllness, name='learn_typesOfMentalIllness'),
        path('religiousexcitement', views.learn_religiousexcitement, name='learn_religiousexcitement'),
        path('moral-treatment', views.learn_moralTreatment, name='learn_moralTreatment'),
        path('occupational-therapy', views.learn_occupationalTherapy, name='learn_occupationalTherapy'),
        path('asylum-library', views.learn_asylumLibrary, name='learn_asylumLibrary'),
        path('medical-treatment', views.learn_medicalTreatment, name='learn_medicalTreatment'),
        path('learn-medicalAdvancements', views.learn_medicalAdvancements, name='learn_medicalAdvancements'),
        path('gender-and-length-of-stay', views.learn_genderAndLengthOfStay, name='learn_genderAndLengthOfStay'),
        path('gender-and-treatment', views.learn_genderAndTreatment, name='learn_genderAndTreatment'),
        path('moral-treatment-and-family', views.learn_moralTreatmentAndFamily, name='learn_moralTreatmentAndFamily'),
        path('gender-and-death', views.learn_GenderAndDeath, name='learn_GenderAndDeath'),    

        # "patients"
        path('case-studies', views.learn_caseStudies, name='learn_caseStudies'),
        path('patient-hometowns', views.learn_patientHometowns, name='learn_patientHometowns'),
        path('patient-demographics', views.learn_patientDemographics, name='learn_patientDemographics'),

        # "religion"
        path('mental-health-and-quaker-theology', views.learn_mentalHealthAndQuakerTheology, name='learn_mentalHealthAndQuakerTheology'),
        path('religious-life', views.learn_religiousLife, name='learn_religiousLife'),
        path('religious-diversity', views.learn_religiousDiversity, name='learn_religiousDiversity'),
        path('decision-to-admit-nonquakers', views.learn_decisionToAdmitNonQuakers, name='learn_decisionToAdmitNonQuakers'),
        path('theology-and-family', views.learn_theologyAndFamily, name='learn_theologyAndFamily'),

    path('glossary/', views.glossary, name='glossary'),
    path('bibliography/', views.bibliography, name='bibliography'),

    # essays
    path('essays/', views.essays, name='essays'),
    path('essays/20cbattis/', views.essay_20cbattis, name='essay_20cbattis'),
    path('essays/18bkaplow/', views.essay_18bkaplow, name='essay_18bkaplow'),
    path('essays/18cmichel/', views.essay_18cmichel, name='essay_18cmichel'),
    path('essays/17acorcoran/', views.essay_17acorcoran, name='essay_17acorcoran'),
    path('essays/21zhu/', views.essay_21zhu, name='essay_21zhu'),
    path('essays/21scully/', views.essay_21scully, name='essay_21scully'),
    path('essays/22Bratt/', views.essay_22Bratt, name='essay_22Bratt'),

    path('admission-data/', views.patientTable, name='patientTable'),

    ]
