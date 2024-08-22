from fastapi import FastAPI
import uvicorn

app = FastAPI()
from src.router import router





app.include_router(router)




# if __name__ == '__main__':
  
#   uvicorn.run("main:app", host='0.0.0.0', port =8000, reload=True)