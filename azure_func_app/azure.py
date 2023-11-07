import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name', 'Default User')
    return func.HttpResponse(
        body=f'Hello {name}!',
        status_code=200,
        mimetype='text/plain'
    )