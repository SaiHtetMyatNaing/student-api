from fastapi import FastAPI
from app.database import engine, Base


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Student API - Go to /docs"}