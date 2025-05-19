from fastapi import FastAPI
import uvicorn

from . import routes
from . import utility
from . import mylogger

app = FastAPI(root_path="/api/v1")
app.include_router(routes.router)
utility.config_load()
mylogger.mylog(utility.config_json)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
