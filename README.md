## > This project was renamed from `BappG-Attack` to `WAFA`

![2023-12-04_19:40:41](https://github.com/mrxhaikh/WAFA/assets/68729523/23f15d6c-1ad8-4409-be28-ad8d5983b80f)
> This project is only for demonstration, you can't modify and use it in any way.

### Features
* A much advance json.
* Initiator request 
* Each thread per api loop

### How to use?
* Download files
* Unzip them 
* install python 
* install `requests` by running `pip3 insatll requests`
* grab yourself `apidata.json`
* run `main.py` file using python
* Tool will guide you.

### How to add my own apis?
* IDK

### API Data formatting options

It's syntax looks something like: 
```python
{
    "WAFA_API" : {
          "<Type eg. CALL or SMS>:<Name>": {
            "url":"<website>",
            "modifier_map":{"params":"someval" # format with target, "data":{"somecomplexdate":"str" # type}}, 
            "params":{"somval": "{datetime.now()}" # using default imports},
            "data":{"somecomplexdate":""}
            "sleep_time":15,
            "identifier":"success\":true"
          }
    }
}
```

Default values:
```python
headers={}, # additional headers then default one
url="", # url of api
cookies={}, # session cookies
sleep_time=1, # after how much time send next
method="GET", # method of requests ["POST", "GET"]
identifier="", # check if this is in result
data={}, # json data to send
params={}, # url params
modifier_map={}, # map to modify which values
initiator={}, # an pre request (same as an api), it will set result of it to "self.init_result"
```

Default imports:
```python
from datetime import datetime
import os
```

### Examples of APIS
A complex example with initiator request:
```python
"CALL:Somewebsite":{
    "method":"POST",
    "url":"https://www.somewebsite.com/api/io/account/v1/sendOtp",
    "initiator":{
        "url":"https://www.somewebsite.com/api/y/auth/v3/getOtp",
        "method":"POST",
        "data":{
            "mobile": "{}",
            "deviceName": "",
            "refCode": "",
            "isPlayOP": false
        },
        "modifier_map":{"data":"mobile"}
    },
    "data":{
        "otpOnCall": true,
        "otpType": 8,
        "date":{"{datetime.now().strftime('%H:%S')}"},
        "transactionId": "{self.init_result['data']['otpTransactionId']}", # uses otpTransactionId from initiator
        "mobile": "{}"
    },
    # To avoid duplicacy, I have used data, data:, data::
    # they all are same, to will auto cut extra ":"
    "modifier_map":{"data":"mobile", "data:" : {"transactionId":"int"},"data::":{"date":"str"}},
    "identifier":"success\": true",
    "sleep_time":30

```
