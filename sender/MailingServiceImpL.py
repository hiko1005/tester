from models import Service
import json
import requests

class MailingServiceImpl:
    def __init__(self, ms: Service) -> None:
        self.ms = ms

    def compile_message(self, site, contact={}):
        if self.ms.message_pattern is None:
            return ""
        return self.format(self.ms.message_pattern, {**site, **contact})
    
    def compile_url(self, site, contact={}):
        return self.format_with_all_data(self.ms.api_url, site, contact)
    
    def data_adapter(self, data):
        if self.ms.body_format == "JSON":
            return {"json":json.loads(data)}
        else:
            return {"data": data}

    def compile_body(self, site, contact={}):
        if self.ms.body_pattern is None:
            return ''
        
        result = self.format_with_all_data(self.ms.body_pattern, site, contact)
        return self.data_adapter(result)
    
    def compile_headers(self, site, contact):
        result = {}
        if self.ms.body_format == "JSON":
            result['content_type'] = "application/json"
        elif self.ms.body_format == "XML":
            result['content_type'] = 'application/xml'
        else:
            result["content_type"] = 'text/plain'

        if self.ms.headers is None:
            return result
        for line in self.ms.headers.split('\n'):
            try:
                header = line.split(":")
                result[header[0].strip(), site, contact] = self.format_with_all_data(line[1], site, contact)
            except ValueError:
                continue
        return result
    
    def format(self, text, d):
        for key in d:
            text = text.replace("{" + str(key) + "}", str(d[key]))
        return text
    
    def format_with_all_data(self, string, site, contact):
        return self.format(string, {**{"site." + k: v for k,v in site.items()}, **{"contact." + k: v for k,v in contact.items()},
                                        'login': self.ms.login, 
                                        "password": self.ms.password, 
                                        'token': self.ms.token,
                                        "message": self.compile_message({"site." + k: v for k,v in site.items()}, {"contact." + k: v for k,v in contact.items()})})

    def send(self, site, contact={}):
        if self.ms.request_type.lower() == "post":
            responce = requests.post(self.compile_url(site.__dict__, contact.__dict__), 
                                     **self.compile_body(site.__dict__, contact.__dict__), 
                                     headers=self.compile_headers(site.__dict__, contact.__dict__))
        print(responce)
