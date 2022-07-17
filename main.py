import http.client
import json

conn = http.client.HTTPSConnection("fiu-uat.setu.co")
headers = {
    'x-client-id': "255d0b6c-492d-44cf-8581-e9494c7b0914",
    'x-client-secret': "9c2fc756-3d17-46d6-b28d-be4d71953e83",
    'content-type': "application/json"
    }



#----------------------------------------------------- Consent flow ------------------------------------------------------------------

def create_consent():
    payload = {
        "Detail": {
            "consentStart": "2022-07-18T18:00:13.273Z",
            "consentExpiry": "2022-07-30T05:44:53.822Z",
            "Customer": {
                "id": "9770643299@onemoney"
            },
            "FIDataRange": {
                "from": "2022-01-17T14:50:00Z",
                "to": "2022-05-01T14:50:00Z"
            },
            "consentMode": "STORE",
            "consentTypes": [
                "TRANSACTIONS",
                "PROFILE",
                "SUMMARY"
            ],
            "fetchType": "PERIODIC",
            "Frequency": {
                "value": 30,
                "unit": "MONTH"
            },
            "DataFilter": [
                {
                    "type": "TRANSACTIONAMOUNT",
                    "value": "5000",
                    "operator": ">="
                }
            ],
            "DataLife": {
                "value": 1,
                "unit": "MONTH"
            },
            "DataConsumer": {
                "id": "setu-fiu-id"
            },
            "Purpose": {
                "Category": {
                    "type": "string"
                },
                "code": "101",
                "text": "Loan underwriting",
                "refUri": "https://api.rebit.org.in/aa/purpose/101.xml"
            },
            "fiTypes": [
                "DEPOSIT"
            ]
        },
        "redirectUrl": "https://setu.co"
    }

    payload = json.dumps(payload)



    conn.request("POST", "/consents", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")
    
def check_status(id):
    
    conn.request("GET", "/consents/{0}".format(str(id)), headers=headers)
     
    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


#--------------------------------- Data Session ----------------------------------------------------

def create_session(id):
    
    payload = {
    "consentId": str(id),
    "DataRange": {
        "from": "2022-01-17T14:50:00.000Z",
        "to": "2022-05-01T14:50:00.000Z"
    },
    "format": "json"
    }
    
    payload = json.dumps(payload)
    
    conn.request("POST", "/sessions", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")
    
    
def get_data(id):
    
    conn.request("GET", "/sessions/{0}".format(str(id)), headers=headers)
     
    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

#-----------------------------------------------------------------------------------------------------

#print(create_consent())
#print(check_status("13a234e4-a848-4f73-a3dc-3640ba2e2aae"))
print(create_session("13a234e4-a848-4f73-a3dc-3640ba2e2aae"))
#print(get_data(id))


