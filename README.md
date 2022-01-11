# Covid-API
Covid-19 API made with FastAPI.

Click [here](https://covid-api.herokuapp.com/) to use the api


## Python Template
```python
import requests


cases = requests.get('https://covid-api.herokuapp.com/').json()['confirmed_cases']
print(cases)
```
