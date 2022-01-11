from fastapi import FastAPI
from covid import Covid

covid=Covid()
app = FastAPI()

confirmed_cases = lambda country: covid.get_status_by_country_name(country)['confirmed']

@app.get('/')
def main():
    return {'confirmed_cases': confirmed_cases('pakistan')}
# Thanks for reading...
