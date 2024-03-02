<!-- FastAPI Sample Project Setup Guide -->
<!-- Introduction -->
This guide provides step-by-step instructions on how to initialize and create a sample project using FastAPI. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

<!-- Prerequisites -->
Before proceeding, ensure you have the following installed:

Python 3.6+
pip (Python package installer)
Installation


First, let's install FastAPI and uvicorn using pip:
--------------------------------------------------

1, pip install fastapi uvicorn

Optionally, you can install uvicorn with additional standard dependencies:
---------------------------------------------------------------------


1.Additional, pip install uvicorn[standard]

Project Initialization
-------------------------

Create a new directory for your project:
----------------------------------------

2, mkdir my_fastapi_project
3, cd my_fastapi_project
Inside the project directory, create a new Python file, for example, main.py.

4, echo .> filename

Open main.py in your preferred code editor and import FastAPI:
--------------------------------------------------------------


5, import fastapi
   from fastapi import FastAPI

# Create an instance of FastAPI
6, app = FastAPI()
   Running the Application


To run your FastAPI application, use uvicorn:
----------------------------------------------

7, uvicorn main:app --reload
Here, main refers to the name of your Python file (main.py) and app is the instance of FastAPI created in your file.

Accessing the API Documentation
--------------------------------

Once the server is running, you can access the interactive API documentation by navigating to:

<!-- http://127.0.0.1:8000/docs -->

Creating Sample Endpoints
--------------------------

Now, let's create some sample endpoints in your main.py file. We'll demonstrate the usage of path parameters and query parameters.


from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
In the above code:

We define a Pydantic model Item to represent our item data.
We create two sample endpoints: one to read an item and another to update an item.
The read_item endpoint accepts a path parameter item_id and an optional query parameter q.
The update_item endpoint accepts a path parameter item_id and a request body containing an Item object.