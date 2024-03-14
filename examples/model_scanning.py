import os
from hiddenlayer import HiddenlayerServiceClient


hl_client = HiddenlayerServiceClient(
    host="https://api.hiddenlayer.ai",
    api_id=os.environ.get("HL_CLIENT_ID"),
    api_key=os.environ.get("HL_CLIENT_SECRET"),
)

# Scan a model saved locally on disk
scan_results = hl_client.model_scanner.scan_model_file(
    model_path="./models/example_model.xgb", model_id="sdk_example_model"
)

# View scan results
print(scan_results)
