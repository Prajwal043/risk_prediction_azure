
from pydantic import BaseModel
from fastapi import FastAPI
from blob_utils import load_models

app = FastAPI()

class DeploymentRequest(BaseModel):

    systems_impacted: int
    num_files_changed: int
    deployment_hour: int
    deployment_day: str
    engineer_experience: int
    historical_failures: int
    dependency_count: int
    rollback_required: int
    test_coverage: int
    change_type: str

model = None
preprocessor = None

@app.on_event("startup")
def startup():

    global model
    global preprocessor

    model, preprocessor = load_models()

@app.post("/predict")
def predict(request: DeploymentRequest):

    X = preprocessor.transform(
        [request.dict()]
    )

    prob = model.predict_proba(X)[0][1]

    prediction = (
        "High Risk"
        if prob > 0.5
        else "Low Risk"
    )

    return {
        "risk_score": float(prob),
        "prediction": prediction
    }    