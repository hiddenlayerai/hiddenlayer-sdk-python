import os

from hiddenlayer import HiddenlayerServiceClient

hl_client = HiddenlayerServiceClient(
    host="https://api.hiddenlayer.ai",
    api_id=os.environ.get("HL_CLIENT_ID"),
    api_key=os.environ.get("HL_CLIENT_SECRET"),
)


# [docs_scan_local_file_start]
# Scan a model saved locally on disk
scan_results = hl_client.model_scanner.scan_file(
    model_path="./models/example_model.xgb", model_name="sdk_example_model"
)

# View scan results
print(scan_results)
# [docs_scan_local_file_end]


# [docs_scan_hf_model_start]
# Scan a HuggingFace model
huggingface_scan_results = hl_client.model_scanner.scan_huggingface_model(
    repo_id="drhyrum/bert-tiny-torch-vuln",
)

# See if there were any detections
for result in huggingface_scan_results:
    if result.detections:
        print(result)
# [docs_scan_hf_model_end]
