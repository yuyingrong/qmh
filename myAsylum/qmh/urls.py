
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # topnav
    path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),# summer 2019 team decided that a contact form no longer needed; contact button is a link to "mailto:<hc-libraries>"

    # home
    path('visualizations/', views.visualizations, name='visualizations'),
        path('visualizations/scatterplot-patient-admit-age-admit-year/', views.visual_scatterplotPatientAdmitAgeVsAdmitYear, name="visual_scatterplotPatientAdmitAgeVsAdmitYear"),
        path('visualizations/heatmap-patient-monthly-admission-frequency/', views.visual_heatmapPatientMonthlyAdmissionFrequency, name="visual_heatmapPatientMonthlyAdmissionFrequency"),
        path('visualizations/sankey-philanthropists-organizations-association/', views.visual_sankeyPhilanthropistsOrganizationsAssociation, name="visual_sankeyPhilanthropistsOrganizationsAssociation"),

    # sidebar
    # learn # Sarah Horowitz does not like the name "learn", but the summer 2019 team had not settled on an alternative name for the entire body of short articles
    #path('learn/', views.learn, name='learn'),# the summer 2019 team wanted to write a landing page for each topic in "learn", but we aborted the effort
        # "the asylum"
        path('learn/the-york-retreat', views.learn_theYorkRetreat, name='learn_theYorkRetreat'),
        path('learn/foundation', views.learn_foundation, name='learn_foundation'),
        path('learn/changes-in-admin-over-time', views.learn_changesInAdminOverTime, name='learn_changesInAdminOverTime'),
        #path('learn/from-york-retreat-to-friends-asylumf', views.learn_fromYorkRetreatToFriendsAsylum, name='learn_fromYorkRetreatToFriendsAsylum'),# one of the new grouping topic of articles; effort aborted
        #path('learn/reasoning-about-insanity', views.learn_reasoningAboutInsanity, name='learn_reasoningAboutInsanity'),# one of the new grouping topic of articles; effort aborted
        # "medical treatment"
        path('learn/moral-treatment', views.learn_moralTreatment, name='learn_moralTreatment'),
        # "patients"
        path('learn/case-studies', views.learn_caseStudies, name='learn_caseStudies'),
        path('learn/patient-hometowns', views.learn_patientHometowns, name='learn_patientHometowns'),
        # "religion"
        path('learn/mental-health-and-quaker-theology', views.learn_mentalHealthAndQuakerTheology, name='learn_mentalHealthAndQuakerTheology'),
        path('learn/religious-diversity', views.learn_religiousDiversity, name='learn_religiousDiversity'),# adopted from an old html which needed cleaning up

    path('glossary/', views.glossary, name='glossary'),
    path('bibliography/', views.bibliography, name='bibliography'),
]
