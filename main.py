from fastapi import FastAPI
from routes.products import router

app = FastAPI()

# Register routers
app.include_router(router)
