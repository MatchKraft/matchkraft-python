import json

BASE_URL = "https://app.matchkraft.com/api/"

from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode

class MatchKraft():
    def __init__(self, apikey):
        self.apikey = apikey

    def highlight_duplicates(self,name,primary_list):
        params = {'jobName': name, 'primaryList': primary_list}
        response = call_api("jobs/create-highlight-duplicates-job", params, self.apikey)
        return response
  
    def fuzzy_match(self,name,primary_list,secondary_list):
        params = {'jobName': name, 'primaryList': primary_list, 'secondaryList': secondary_list}
        response = call_api("jobs/create-fuzzy-match-job", params, self.apikey)
        return response

    def execute_job(self,job_id):
        resource = 'jobs/' + job_id +  '/execute'
        response = call_api(resource, None ,self.apikey)
        return response

    def get_results_information(self,job_id):
        resource = 'jobs/' + job_id +  '/download-results'
        response = call_api(resource, None ,self.apikey)
        try:
            json_response = json.loads(response)
            results = []
            for r in json_response:
                results.append(ResultInformation(r['masterRecord'], r['matchRecord']))     
            return results
        except ValueError:
            return response

    def get_job_information(self,job_id):
        resource = 'jobs/' + job_id +  '/export-job-information'
        response = call_api(resource, None ,self.apikey)
        json_response = json.loads(response)
        return JobInformation(json_response['jobId'],json_response['jobName'],json_response['status'],json_response['progress'],json_response['type'])


def call_api(resource, values=None, apikey=None):
    base_url = BASE_URL
    try:
        data = None if values is None else str(json.dumps(values)).encode('utf-8')
        url = base_url + resource
        req = Request(url,data=data)
        req.add_header('Content-Type', 'application/json')
        req.add_header('apikey', apikey)
        response = urlopen(req).read()
        return response.decode("utf-8")
            
    except HTTPError as e:
        print (e)


class JobInformation:

    def __init__(self, id, name, status, progress, type):
        self.id = id
        self.name = name
        self.status = status
        self.progress = progress
        self.type = type


class ResultInformation:

    def __init__(self, master_record, match_record):
        self.master_record = master_record
        self.match_record = match_record