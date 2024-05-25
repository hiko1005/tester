from .models import MailingList, Contact, Site, MailingService

class MailingListService:
    def save(self, mailinglist_raw):
        contacts = Contact.objects.filter(pk__in=mailinglist_raw['contacts'])
        sites = Site.objects.filter(pk__in=mailinglist_raw['sites'])
        mailing_services = MailingService.objects.filter(pk__in=mailinglist_raw['mailing_services'])
        del mailinglist_raw['contacts']
        del mailinglist_raw['sites']
        del mailinglist_raw['mailing_services']
        service = MailingList(**mailinglist_raw)
        service.save()

        for contact in contacts:
            service.contacts.add(contact)
        for site in sites:
            service.sites.add(site)
        for mailing_service in mailing_services:
            service.mailing_services.add(mailing_service)

        # service.contacts.set(contacts)
        # service.sites.set(sites)
        # service.mailing_services.set(mailing_services)
        return service
    
    def getAll(self):
        return MailingList.objects.all()
    
    def delete(self, id):
        MailingList.objects.filter(id=id).delete()