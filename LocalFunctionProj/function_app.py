import azure.functions as func
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name(name="HttpExample")
@app.route(route="hello")
def main(req: func.HttpRequest) -> func.HttpResponse:
    fname = req.params.get('fname', 'Default')
    lname = req.params.get('lname', 'User')
    response_data = {'message': f'Hello {fname}{lname}!'}
    
    return func.HttpResponse(
        json.dumps(response_data),
        status_code=200
    )