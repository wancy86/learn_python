# need to run with django
class Category(models.Model):
    autoid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=150, blank=False)
    comtype = models.CharField(max_length=20, blank=False)
    catname = models.CharField(max_length=150, blank=False)

    def __unicode__(self):
        return '%s' % (self.catname)

    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
