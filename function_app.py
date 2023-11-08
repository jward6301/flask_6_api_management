import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="hello")

def http_trigger(req: func.HttpRequest) -> func.HttpResponse:

    name = req.params.get('name', 'World')
    lastname = req.params.get('lastname', 'Last name not provided')
    
    age = req.params.get('age', '21')
    age_real = int(age)
    age_analyzed = age_real + 50
    
    birthyear =  req.params.get('birthyear', '2000')   
    birthyear_real = int(birthyear)
    birthyear_analyzed = 2023 - birthyear_real

    response_data = {
        'Greeting': f'Hi {name} {lastname}',
        'Age': f'Your analyzed age is {age_analyzed}',
        'Birthyear': f'Your analyzed age based off of your birthyear is {birthyear_analyzed}'
    }
    
    return func.HttpResponse(
        json.dumps(response_data),
        status_code=200
        )

# string for query = /api/hello?firstname=Frances&lastname=Smith&age=22&birthyear=2001