from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.get("/working")
def working():
    """testing route
    """
    return {"message": "App is working"}