from django.db import models

class Glossary(models.Model):
    term = models.CharField("term", max_length = 100, blank = True, null = True)# "term" predicates an optional first positional argument; see: https://docs.djangoproject.com/en/2.2/topics/db/models/#verbose-field-names
    meaning = models.TextField("meaning of the term", blank = True, null = True)

    def get_meaning(self, query_term):
        return Glossary.objects.filter(term=query_term)[0]
#        return self.meaning[self.term.index(query_term)]

    def __str__(self):
        return self.term + ': ' + self.meaning


