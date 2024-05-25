import requests
from models import MailingList, Service, Contact
from sqlalchemy import select
from db_api import session
from MailingServiceImpL import MailingServiceImpl

class Reporter:
    def report(self, sites):
        ml = self.get_mailing_lists(sites)
        for site in ml:
            for raw_ms in ml[site].mailing_services:
                ms = MailingServiceImpl(raw_ms)
                for contact in ml[site].contacts:
                    ms.send(site, contact)


    def get_mailing_lists(self, sites):
        q = select(MailingList)
        with session() as s:
            lists = s.execute(q).unique().scalars().all()
            # lists = [i for i in lists.sites if i in sites]
            d = dict()
            for site in sites:
                for list_ in lists:
                    for c in list_.contacts:
                        pass
                    filtered = list(filter(lambda s: s.id==site.id, list_.sites))
                    if len(filtered) >= 1:
                        d[site]=list_
            
            return d
