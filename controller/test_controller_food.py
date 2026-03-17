from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random
import uuid  # to generate a dummy token

app = FastAPI()

@app.get("/food")
async def random_response():
    """
    Selects an HTTP status and response body at random and returns them as a JSONResponse.
    
    Returns:
        JSONResponse: A response whose body is one of the predefined success or error payloads and whose status code matches the chosen payload.
    """
    responses = [
        (200, {"status": "success", "message": "Operation succeeded!", "data":[
            {"id":1, "name":"apple", "price":100, "stock":10},
            {"id":2, "name":"manggo", "price":200, "stock":20},
            {"id":3, "name":"jackfruit", "price":300, "stock":30},
            {"id":4, "name":"watermelon", "price":400, "stock":40},
            {"id":5, "name":"banana", "price":500, "stock":50},
            {"id":6, "name":"dragon fruit", "price":600, "stock":60},
            {"id":7, "name":"orange", "price":700, "stock":70},
            {"id":8, "name":"strawberry", "price":800, "stock":80},
            {"id":9, "name":"blueberry", "price":900, "stock":90},
            {"id":10, "name":"raspberry", "price":1000, "stock":100}
            ]}),
        (400, {"status": "error", "message": "Bad request."}),
        (403, {"status": "error", "message": "Forbidden."}),
        (404, {"status": "error", "message": "Not found."}),
        (500, {"status": "error", "message": "Internal server error."}),
    ]
    status_code, body = random.choice(responses)
    return JSONResponse(content=body, status_code=status_code)

@app.get("/food/{id}")
async def get_response(id: int):
    """
    Return a JSONResponse containing the food item for the given id or an error if the id is invalid.
    
    Parameters:
        id (int): Path identifier for the requested food item. Valid values are 1 or 2.
    
    Returns:
        JSONResponse: If id is 1 or 2, a 200 response with {"status":"success","message":<string>,"data":{id,name,price,stock}}.
                      If id is any other value, a 404 response with {"status":"error","message":"Invalid ID. Only 1 or 2 allowed."}.
    """
    if id == 1:
        return JSONResponse(content={"status": "success", "message": "You requested ID 1!", "data": {"id":1, "name":"apple", "price":100, "stock":10}}, status_code=200)
    elif id == 2:
        return JSONResponse(content={"status": "success", "message": "You requested ID 2!", "data":{"id":2, "name":"manggo", "price":200, "stock":20}}, status_code=200)
    else:
        return JSONResponse(content={"status": "error", "message": "Invalid ID. Only 1 or 2 allowed."}, status_code=404)


@app.post("/login")
async def login():
    # Generate a dummy Bearer token
    """
    Generate a dummy Bearer access token and return it in a JSON response.
    
    Returns:
        JSONResponse: A response with `content` containing `access_token` (a UUID4 string) and `token_type` set to `"bearer"`, with HTTP status 200.
    """
    dummy_token = str(uuid.uuid4())
    return JSONResponse(content={"access_token": dummy_token, "token_type": "bearer"}, status_code=200)