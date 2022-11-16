from django.db import models

class Glossary(models.Model):
    term = models.CharField("term", max_length = 100, blank = True, null = True)# "term" predicates an optional first positional argument; see: https://docs.djangoproject.com/en/2.2/topics/db/models/#verbose-field-names
    meaning = models.TextField("meaning of the term", blank = True, null = True)

    def get_meaning(self, query_term):
        return Glossary.objects.filter(term=query_term)[0]
#        return self.meaning[self.term.index(query_term)]

    def __str__(self):
        return self.term + ': ' + self.meaning

class Patient(models.Model):
    dateOfLastAdmission = models.CharField('Date of Last Previous Admission, if any.', max_length=15, null=True, blank=True)
    numberInOrderOfAdmission = models.CharField("Number in Order of Admission", max_length=25, null=True, blank=True)
    dateOfAdmission = models.CharField("Date of Admission", max_length=15, null=True, blank=True)
    fullName = models.CharField("Christian and Surname at Length.", max_length=15, null=True, blank=True)
    age = models.CharField("Present Age.", max_length=25, null=True, blank=True)
    race = models.CharField("Color.", max_length=15, null=True, blank=True)
    sex = models.CharField("Sex", max_length=15, null=True, blank=True)
    nativity = models.CharField("Nativity.", max_length=15, null=True, blank=True)
    civilConditionMarriage = models.CharField("Civil Condition: Married. Single. Widowed.", max_length=15, null=True, blank=True)
    civilConditionChildren = models.CharField("Civil Condition: No. Children Living.", max_length=15, null=True, blank=True)
    civilConditionSiblings = models.CharField("Civil Condition: Bros. & Sisters Living.", max_length=15, null=True, blank=True)
    occupation = models.CharField("Occupation Prior to Insanity.", max_length=25, null=True, blank=True)
    placeOfAbode = models.CharField("Previous Place of Abode.", max_length=25, null=True, blank=True)
    dateOfMedicalCertificates = models.CharField("Date of Medical Certificates, and by whom Signed.", max_length=25, null=True, blank=True)
    bodilyCondition = models.CharField("Bodily Condition: Good. Impaired. Bad.", max_length=25, null=True, blank=True)
    nameOfBodilyDisorder = models.CharField("Name of Disorder, (Bodily), if any.", max_length=25, null=True, blank=True)
    mentalDisorder = models.CharField("Form of Mental Disorder.", max_length=25, null=True, blank=True)
    causeOfInsanity = models.CharField("Supposed Cause of Insanity.", max_length=25, null=True, blank=True)
    complications = models.CharField("Complications: Suicidal. Homicidal. Paralytic. Epileptic.. ", max_length=25, null=True, blank=True)
    congenitalIdiots = models.CharField("Congenital Idiots.", max_length=25, null=True, blank=True)
    durationOfExistingAttack = models.CharField("Duration of Existing Attack: Years. Months. Days.", max_length=25, null=True, blank=True)
    numPreviousAttacks = models.CharField("Number of Previous Attacks.", max_length=25, null=True, blank=True)
    ageAtFirstAttack = models.CharField("Age at First Attack.", max_length=25, null=True, blank=True)
    dateOfDischargeOrDeath = models.CharField("Date of Discharge or Death.", max_length=25, null=True, blank=True)
    outcome = models.CharField("Discharged: Restored. Improved. Much Impr'd. Stationary. Died.", max_length=25, null=True, blank=True)
    relationsInsane = models.CharField("Relations Insane.", max_length=25, null=True, blank=True)
    remarks = models.CharField("Remarks.", max_length = 100, null=True, blank=True)
   
   
    # patientNumber = models.IntegerField('Patient No. as appears on "superspreadsheet.csv"', blank=True, null=True)
    # firstName = models.CharField("first name", max_length=15, null=True, blank=True)
    # lastName = models.CharField("last name", max_length=15, null=True, blank=True)
    # gender = models.CharField("gender", max_length= 10, null=True, blank=True)
    # admitYear = models.CharField('year patient was admitted', max_length=15, blank=True, null=True)
    # admitMonth = models.CharField('month patient was admitted', max_length=15, blank=True, null=True)
    # #admitDate = models.CharField('date patient was admitted', max_length=15, blank=True, null=True)# not useful info and entries are mostly lacking in "superspreadsheet.csv"
    # admitAge = models.IntegerField('age of patient when admitted', blank=True, null=True)
    # admitDateFull = models.CharField("month/day/year patient was admitted", max_length=15, null=True, blank=True)
    # leaveDateFull = models.CharField("date patient was discharged", max_length=15, null=True, blank=True)

    def __str__(self):
        return ('Patient No. %s : %s ' % (str(self.numberInOrderOfAdmission), str(self.fullName)))

    # def __str__(self):
    #     return ('No.%s %s %s: admitted at an age of %s (0 if unavailable), on %s (empty if unavailable), and left on %s (empty if unavailable).' % (str(self.patientNumber), str(self.firstName), str(self.lastName), str(self.admitAge), str(self.admitDateFull), str(self.leaveDateFull)))



    


