from azure.storage.blob import BlobServiceClient
import os
import joblib

def load_models():

    conn_str = os.getenv(
"DefaultEndpointsProtocol=https;AccountName=changeriskstorage;AccountKey=hpWQ5HOkIENKV1MEVvP729oM8E8ElWkdaXxDd+IKLDw3AloB2WX+wLuRBXnklXWKU2m7zAnJsWpi+ASttxcnqA==;EndpointSuffix=core.windows.net"
    )

    service = BlobServiceClient.from_connection_string(
        conn_str
    )

    container = service.get_container_client(
        "models"
    )

    files = [
        "best_xgboost.pkl",
        "preprocessor.pkl"
    ]

    for file in files:

        blob = container.get_blob_client(file)

        with open(file, "wb") as f:
            f.write(
                blob.download_blob().readall()
            )

    model = joblib.load(
        "best_xgboost.pkl"
    )

    preprocessor = joblib.load(
        "preprocessor.pkl"
    )

    return model, preprocessor