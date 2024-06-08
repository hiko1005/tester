from .models import MailingService

class ServiceService:
    def save(self, service_raw):
        
        service = MailingService(**service_raw)
        service.save()
        return service
    
    def getAll(self):
        return MailingService.objects.all()
    
    def delete(self, id):
        MailingService.objects.filter(id=id).delete()

    def findById(self, id):
        return MailingService.objects.get(pk = id)
