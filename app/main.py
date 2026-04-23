from fastapi import FastAPI

app = None

@app.get('/')
def root():
    return {'message': 'Hello from Fastapi'}

