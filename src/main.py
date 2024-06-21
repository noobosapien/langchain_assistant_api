from fastapi import FastAPI
from web import assistant
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(assistant.router)

@app.get("/")
def top():
    return "Top here"

@app.get("/echo/{thing}")
def echo(thing):
    return f"Echoing {thing}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)