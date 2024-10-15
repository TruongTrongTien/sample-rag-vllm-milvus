import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from app.routers.test import router as test_router

app = FastAPI(debug=True)
app.title = "API Service"
app.version = "0.0"

# Create a GET method that responds with HTML code
@app.get('/', tags = ['home'])
def message():
    return HTMLResponse('<h1>API Service</h1>')

app.include_router(test_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=7860)