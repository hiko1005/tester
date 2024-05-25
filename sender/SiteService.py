from datetime import datetime
from db_api import engine, session
from sqlalchemy import select
from models import Contact, Site

class SiteService:
    def __init__(self) -> None:
        pass

    def __enter__(self):
        self.session = session()
        return self
    
    def __exit__(self, exit_type, value, traceback):
        self.session.close()

    def get_active(self):
        q = select(Site).where(Site.cheking_active==True)
        sites = self.session.execute(q).scalars()
        return sites
    
    def update_status(self, sites):
        for set_ in range(len(sites)):
            for site in sites[set_]:
                site.last_checked = datetime.now()
                site.is_alive = set_ == 1

        self.session.commit()        