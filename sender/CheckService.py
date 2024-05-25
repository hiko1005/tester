from croniter import croniter
from datetime import datetime
import requests
import re

class CheckService:

    # def check(self, sites):
    #     return self.check(sites)


    def report(self, sites):
        return sites

    def check(self, sites):
        sites = self.cron_filter(sites)
        sites = self.filter_not_available(sites)
        return sites

    def cron_filter(self, sites):
        time = datetime.now().replace(second=0, microsecond=0)
        result = []
        for site in sites:
            cron = croniter(site.cron_schedule, time)
            if cron.get_current(datetime) == time:
                result.append(site)

        return result
    
    def filter_not_available(self, sites):
        result_available = []
        result_notavailable = []
        for site in sites:
            resp = requests.get(site.url)
            source_pattern = site.expected_responce_code_pattern \
                if site.expected_responce_code_pattern is not None \
                    else ""
            flag = str(resp.status_code) in site.expected_responce_code
            pattern = re.compile(source_pattern)
            flag = flag and (pattern.search(resp.content.decode('utf-8')) is not None)

            if not site.inversive_condition:
                if flag:
                    result_available.append(site)
                else:
                    result_notavailable.append(site)
            else:
                if not flag:
                    result_available.append(site)
                else:
                    result_notavailable.append(site)
        return result_available, result_notavailable
            
            

