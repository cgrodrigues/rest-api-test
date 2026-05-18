from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/predict")
async def predict(data: dict):

    feature_1 = data["feature_1"]
    feature_2 = data["feature_2"]
    feature_3 = data["feature_3"]

    result = (
        feature_1 +
        feature_2 +
        feature_3
    ) / 3

    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
