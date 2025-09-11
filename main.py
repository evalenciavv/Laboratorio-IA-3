import serviceOpenAI
import serviceTwitter
from typing import Union

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/feelingstw/{idTweet}")
def main(idTweet):
    payloadTweet = serviceTwitter.getTweet(idTweet)
    if payloadTweet == None:
        print("Error")
        return {
            "Error": "Error en la solicitud"
        }
    else:
        result = serviceOpenAI.postOpenAI(payloadTweet)
        print(result)
        return {"Resultado: " : result}

