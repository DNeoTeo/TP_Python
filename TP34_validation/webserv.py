from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get("/multiEgy/")
async def MultiEgypt(I1 :Optional[str], I2 :Optional[str]):
    if(I1=="" or I2==""):
        return {"Error": "input is missing", "I1": I1, "I2": I2}
    try:
        solu = 0
        Ite = 0
        I1 = int(I1)
        I2 = int(I2)
        if(I2 < I1):
            c = I1
            I1 = I2
            I2 = c
        while I1 != 0:
            if I1 % 2 == 1:
                solu = solu+I2
                Ite += 1
            I1 = I1//2
            I2 = I2+I2
            Ite += 1
        return {"ABmulti" : str(solu), "multiIT" : str(Ite)}
    except Exception as e:
        return {"Error": str(e)}