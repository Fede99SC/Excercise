#
from fastapi import FastAPI, Body, Depends
# import uvicorn
#
#
app = FastAPI()
body = Body(default=None)
import routes
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8003)