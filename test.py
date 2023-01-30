import requests;
import json;
import time;
from datetime import date;

TOKEN = '';
# data = {
    # "errorcounter": 1
# }
def auth_request():
    dict={};
    dict['token'] = '';
    dict['expiration_date'] = '';
    return dict;
    


def httprequest():
    # prevrefresh
    endpoint = '';
    headers = {
        "Authorization": "Bearer  "+ str(TOKEN),
        "Content-Type":"application/json"
    }
    i = 0
    while(i < 1):
        time.sleep(10);
        dict = auth_request();
        current_time = date.today();
        expiration = dict['expiration_date'];
        if (current_time>= expiration):
            TOKEN = dict['token'];
            headers = {
            "Authorization": "Bearer  "+ str(TOKEN),
            " Content-Type":"application/json"
            }
        r = requests.get(endpoint, headers = headers)

        # parsing response object results
        data = json.load(r)
        for i in data:
            errorcount = data['errorcounter'];
            if (errorcount > 0) : 
                print("not healthy");
            else:
                print("healthy");
        
        
        if(r.status_code ==200) :
            if (r.elapsed.total_seconds() < 0.5) :
                print('healthy');
            else :
                print('not healthy');
        else:
            print('not healthy');
        
    
    
httprequest();
    