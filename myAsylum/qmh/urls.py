
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
        path('learn/structure-and-governance', views.learn_structureAndGovernance, name='learn_structureAndGovernance'),
        path('learn/changes-in-admin-over-time', views.learn_changesInAdminOverTime, name='learn_changesInAdminOverTime'),
        path('learn/asylum-architecture', views.learn_asylumArchitecture, name='learn_asylumArchitecture'),
        path('learn/gender-and-staff', views.learn_genderAndStaff, name='learn_genderAndStaff'),
        path('learn/race-and-staff', views.learn_raceAndStaff, name='learn_raceAndStaff'),
        path('learn/philanthropic-networks', views.learn_philanthropicNetworks, name='learn_philanthropicNetworks'),
        #path('learn/from-york-retreat-to-friends-asylumf', views.learn_fromYorkRetreatToFriendsAsylum, name='learn_fromYorkRetreatToFriendsAsylum'),# one of the new grouping topic of articles; effort aborted
        #path('learn/reasoning-about-insanity', views.learn_reasoningAboutInsanity, name='learn_reasoningAboutInsanity'),# one of the new grouping topic of articles; effort aborted

        # "medical treatment"
        path('learn/types-of-mental-illness', views.learn_typesOfMentalIllness, name='learn_typesOfMentalIllness'),
        path('learn/moral-treatment', views.learn_moralTreatment, name='learn_moralTreatment'),
        path('learn/occupational-therapy', views.learn_occupationalTherapy, name='learn_occupationalTherapy'),
        path('learn/asylum-library', views.learn_asylumLibrary, name='learn_asylumLibrary'),
        path('learn/medical-treatment', views.learn_medicalTreatment, name='learn_medicalTreatment'),
        path('learn/gender-and-length-of-stay', views.learn_genderAndLengthOfStay, name='learn_genderAndLengthOfStay'),
        path('learn/gender-and-treatment', views.learn_genderAndTreatment, name='learn_genderAndTreatment'),
        path('learn/moral-treatment-and-family', views.learn_moralTreatmentAndFamily, name='learn_moralTreatmentAndFamily'),

        # "patients"
        path('learn/case-studies', views.learn_caseStudies, name='learn_caseStudies'),
        path('learn/patient-hometowns', views.learn_patientHometowns, name='learn_patientHometowns'),
        path('learn/patient-demographics', views.learn_patientDemographics, name='learn_patientDemographics'),

        # "religion"
        path('learn/mental-health-and-quaker-theology', views.learn_mentalHealthAndQuakerTheology, name='learn_mentalHealthAndQuakerTheology'),
        path('learn/religious-life', views.learn_religiousLife, name='learn_religiousLife'),
        path('learn/religious-diversity', views.learn_religiousDiversity, name='learn_religiousDiversity'),
        path('learn/decision-to-admit-nonquakers', views.learn_decisionToAdmitNonQuakers, name='learn_decisionToAdmitNonQuakers'),
        path('learn/theology-and-family', views.learn_theologyAndFamily, name='learn_theologyAndFamily'),

    path('glossary/', views.glossary, name='glossary'),
    path('bibliography/', views.bibliography, name='bibliography'),

    # essays
    path('essays/', views.essays, name='essays'),
    path('essays/20cbattis/', views.essay_20cbattis, name='essay_20cbattis'),
    path('essays/18bkaplow/', views.essay_18bkaplow, name='essay_18bkaplow'),
    path('essays/18cmichel/', views.essay_18cmichel, name='essay_18cmichel'),
    path('essays/17acorcoran/', views.essay_17acorcoran, name='essay_17acorcoran'),

]
