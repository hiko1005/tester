from .models import Site

class SiteService:
    def save(self, site_raw):
        site = Site(**site_raw)
        site.save()
        return site
    
    def getAll(self):
        return Site.objects.all()
    
    def delete(self, id):
        Site.objects.filter(id=id).delete()