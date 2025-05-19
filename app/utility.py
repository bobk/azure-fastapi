from fastapi import HTTPException
import subprocess
import os
import json
import jqpy
import requests
from azure.identity import DefaultAzureCredential

from . import mylogger

config_json = {}

def config_load():
    """
    d
    """
    global config_json

    config_file = open('.\\config\\config.json', encoding='UTF-8')
    config_json = json.load(config_file)
    config_file.close()

    return

def make_call(call_name: str):
    """
    d
    """

    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
    resourcegroup_name = os.environ['AZURE_RESOURCEGROUP_NAME']

    if ('AZURE_CLIENT_SECRET' in os.environ):
        resource_url = str(config_json['calls'][call_name]['api_endpoint']['url'])
        resource_url = resource_url.replace('{subscription_id}', subscription_id)
        resource_url = resource_url.replace('{resourcegroup_name}', resourcegroup_name)
        resource_method = str(config_json['calls'][call_name]['api_endpoint']['method'])

        credential = DefaultAzureCredential()
        token = credential.get_token("https://management.azure.com/.default")
        headers = {"Authorization": f"Bearer {token.token}"}
        response = requests.request(resource_method, resource_url, headers=headers, timeout=15)
        if response.status_code == 200:
            mylogger.mylog("API Request successful!")
            mylogger.mylog(response.json())
            return response.json()
        else:
            mylogger.mylog(f"Request failed with status code {response.status_code}")
            mylogger.mylog(response.text)
            return response.text

    else:
        azcmd = [s.replace('{subscription_id}', subscription_id) for s in config_json['calls']['vm_list']['os_command']]
        azcmd = [s.replace('{resourcegroup_name}', resourcegroup_name) for s in azcmd]
        jqfilter = config_json['calls']['vm_list']['os_jqfilter']

        process = subprocess.Popen(azcmd, stdout=subprocess.PIPE)
        out, err = process.communicate()
        mylogger.mylog(str(out))
        if (not err):
            info = json.loads(out)
            info2 = jqpy.jq(jqfilter, info)
            return info2
    raise HTTPException(status_code=404, detail="not found")
