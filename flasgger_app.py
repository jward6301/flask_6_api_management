from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/hello', methods=['GET'])
def hello_get():
    """
    This endpoint returns a greeting message.
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: World
      - name: lastname
        in: query
        type: string
        required: false
        default: Last name not provided
      - name: age
        in: query
        type: integer
        required: false
        default: 21
      - name: birthyear
        in: query
        type: integer
        required: false
        default: 2000
    responses:
      200:
        description: A greeting message
    """
    
    name = request.args.get('name', 'World')
    lastname = request.args.get('lastname', 'Last name not provided')
    
    age = request.args.get('age', '21')
    age_real = int(age)
    age_analyzed = age_real + 50
    
    birthyear =  request.args.get('birthyear', '2000')   
    birthyear_real = int(birthyear)
    birthyear_analyzed = 2023 - birthyear_real

    return jsonify(
        {'Greeting': f'Hi {name} {lastname}',
        'Age': f'Your analyzed age is {age_analyzed}',
        'Birthyear': f'Your analyzed age based off of your birthyear is {birthyear_analyzed}'}

    )
       

# string for query = hello?name=Frances&lastname=Smith&age=22&birthyear=2001
# string for swagger documentation = /apidocs/

if __name__ == '__main__':
    app.run(debug=True)