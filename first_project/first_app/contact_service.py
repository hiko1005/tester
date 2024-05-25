from .models import Contact

class ContactService:
    def save(self, contact:dict):
        model_contact = Contact(**contact)
        model_contact.save()
        return model_contact
    
    def getAll(self):
        return Contact.objects.all()
    
    def delete(self, id):
        Contact.objects.filter(id=id).delete()