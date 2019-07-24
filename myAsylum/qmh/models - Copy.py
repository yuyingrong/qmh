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
    patientNumber = models.IntegerField('Patient No. as appears on "superspreadsheet.csv"', blank=True, null=True)
    firstName = models.CharField("first name", max_length=15, null=True, blank=True)
    lastName = models.CharField("last name", max_length=15, null=True, blank=True)
    gender = models.CharField("gender", max_length= 10, null=True, blank=True)
    admitYear = models.CharField('year patient was admitted', max_length=15, blank=True, null=True)
    admitMonth = models.CharField('month patient was admitted', max_length=15, blank=True, null=True)
    #admitDate = models.CharField('date patient was admitted', max_length=15, blank=True, null=True)# not useful info and entries are mostly lacking in "superspreadsheet.csv"
    admitAge = models.IntegerField('age of patient when admitted', blank=True, null=True)
    admitDateFull = models.CharField("month/day/year patient was admitted", max_length=15, null=True, blank=True)
    leaveDateFull = models.CharField("date patient was discharged", max_length=15, null=True, blank=True)

    def __str__(self):
        return ('No.%s %s %s: admitted at an age of %s (0 if unavailable), on %s (empty if unavailable), and left on %s (empty if unavailable).' % (str(self.patientNumber), str(self.firstName), str(self.lastName), str(self.admitAge), str(self.admitDateFull), str(self.leaveDateFull)))



    


