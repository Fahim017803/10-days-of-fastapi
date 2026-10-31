from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def top_level_function():
    return{
        "message": "Day 2: Paths"
}

@app.get("/courses")
def courses_function():
    return{
        "Course": "Django and Backend API Development with python"
}

@app.get("/django/api")
def dango_api_function():
    return{
        "Type": "Basic to Advanced"
}