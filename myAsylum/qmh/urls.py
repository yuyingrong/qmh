
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('visualizations/', views.visualizations, name='visualizations'),
        path('visualizations/heatmap-patient-monthly-admission-frequency/', views.visual_heatmapPatientMonthlyAdmissionFrequency, name="visual_heatmapPatientMonthlyAdmissionFrequency"),
        path('visualizations/sankey-philanthropists-organizations-association/', views.visual_sankeyPhilanthropistsOrganizationsAssociation, name="visual_sankeyPhilanthropistsOrganizationsAssociation"),

    path('contact/', views.contact, name='contact'),
    #path('learn/', views.learn, name='learn'),# this is the catalog involving all short articles
        # all short articles are under /learn/, but not necessarily under history/place/people/reflection catagories
        # if want to change article content or title: change path, views, and name here and elsewhere
        path('learn/the-york-retreat', views.learn_theYorkRetreat, name='learn_theYorkRetreat'),
        path('learn/foundation', views.learn_foundation, name='learn_foundation'),
        path('learn/changes-in-admin-over-time', views.learn_changesInAdminOverTime, name='learn_changesInAdminOverTime'),
        path('learn/from-york-retreat-to-friends-asylumf', views.learn_fromYorkRetreatToFriendsAsylum, name='learn_fromYorkRetreatToFriendsAsylum'),
        path('learn/reasoning-about-insanity', views.learn_reasoningAboutInsanity, name='learn_reasoningAboutInsanity'),
        path('learn/moral-treatment', views.learn_moralTreatment, name='learn_moralTreatment'),
        path('learn/mental-health-and-quaker-theology', views.learn_mentalHealthAndQuakerTheology, name='learn_mentalHealthAndQuakerTheology'),
        path('learn/case-studies', views.learn_caseStudies, name='learn_caseStudies'),
        path('learn/patient-hometowns', views.learn_patientHometowns, name='learn_patientHometowns'),

    path('glossary/', views.glossary, name='glossary'),
    path('bibliography/', views.bibliography, name='bibliography'),
]
