"""
HiddenLayer SDK Demo - Model Scanning Examples

This demo shows how to use the HiddenLayer SDK to scan ML models for security vulnerabilities.

Prerequisites:
    1. Install the SDK: pip install hiddenlayer-sdk
    2. Set your credentials via environment variables or pass them directly:
       - HIDDENLAYER_TOKEN (Bearer token) OR
       - HIDDENLAYER_CLIENT_ID and HIDDENLAYER_CLIENT_SECRET (OAuth2)
"""


from hiddenlayer import HiddenLayer

# =============================================================================
# Basic Setup - Creating a Client
# =============================================================================

def create_client() -> HiddenLayer:
    """
    Create a HiddenLayer client.
    
    Authentication can be done via:
    1. Bearer token (set HIDDENLAYER_TOKEN env var or pass bearer_token param)
    2. OAuth2 client credentials (set HIDDENLAYER_CLIENT_ID and HIDDENLAYER_CLIENT_SECRET)
    """
    # Option 1: Using environment variables (recommended)
    # The client automatically reads from HIDDENLAYER_TOKEN or 
    # HIDDENLAYER_CLIENT_ID/HIDDENLAYER_CLIENT_SECRET
    client = HiddenLayer()
    
    # Option 2: Passing credentials directly
    # client = HiddenLayer(bearer_token="your-bearer-token")
    
    # Option 3: Using OAuth2 client credentials
    # client = HiddenLayer(
    #     client_id="your-client-id",
    #     client_secret="your-client-secret",
    # )
    
    # Option 4: Specify a different environment (default is "prod-us")
    # client = HiddenLayer(environment="prod-eu")
    
    return client


# =============================================================================
# Example 1: Scan a Local Model File
# =============================================================================

def scan_file_example(client: HiddenLayer, model_path: str) -> None:
    """
    Scan a single model file using the HiddenLayer Model Scanner.
    
    Args:
        client: HiddenLayer client instance
        model_path: Path to the model file to scan
    """
    print(f"\n{'='*60}")
    print("Example 1: Scanning a local model file")
    print(f"{'='*60}")
    
    # Scan the file
    results = client.model_scanner.scan_file(
        model_name="my-model",
        model_path=model_path,
        request_source="Integration",
        origin="github-action",
    )
    
    # Print the results
    print(f"\nScan ID: {results.scan_id}")
    print(f"Status: {results.status}")
    print(f"Files scanned: {results.file_count}")
    print(f"Detections found: {results.detection_count}")
    
    if results.summary.highest_severity:
        print(f"Highest severity: {results.summary.highest_severity}")
    
    # Check for detections
    if results.file_results:
        for file_result in results.file_results:
            print(f"\nFile: {file_result.file_location}")
            print(f"  Status: {file_result.status}")
            print(f"  File type: {file_result.details.file_type}")
            print(f"  SHA256: {file_result.details.sha256}")
            
            if file_result.detections:
                print(f"  Detections ({len(file_result.detections)}):")
                for detection in file_result.detections:
                    print(f"    - [{detection.severity.upper()}] {detection.description}")
                    print(f"      Category: {detection.category}")
                    print(f"      Risk: {detection.risk}")


# =============================================================================
# Example 2: Scan a Folder of Model Files
# =============================================================================

def scan_folder_example(client: HiddenLayer, folder_path: str) -> None:
    """
    Scan all model files in a folder.
    
    Args:
        client: HiddenLayer client instance
        folder_path: Path to the folder containing model files
    """
    print(f"\n{'='*60}")
    print("Example 2: Scanning a folder of model files")
    print(f"{'='*60}")
    
    results = client.model_scanner.scan_folder(
        model_name="my-model-folder",
        path=folder_path,
        request_source="Integration",
        origin="github-action"
    )
    
    print(f"\nScan ID: {results.scan_id}")
    print(f"Status: {results.status}")
    print(f"Files scanned: {results.file_count}")
    print(f"Detections found: {results.detection_count}")
    
    if results.summary.highest_severity:
        print(f"Highest severity: {results.summary.highest_severity}")


# =============================================================================
# Example 3: Scan a HuggingFace Model
# =============================================================================

def scan_huggingface_example(client: HiddenLayer, repo_id: str) -> None:
    """
    Scan a model from HuggingFace Hub.
    
    Requires: pip install huggingface_hub
    
    Args:
        client: HiddenLayer client instance
        repo_id: HuggingFace repository ID (e.g., "bert-base-uncased")
    """
    print(f"\n{'='*60}")
    print("Example 3: Scanning a HuggingFace model")
    print(f"{'='*60}")
    
    results = client.model_scanner.scan_huggingface_model(
        repo_id=repo_id,
        model_name=repo_id,
        hf_token=True,
        request_source="Integration",
    )
    
    print(f"\nScan ID: {results.scan_id}")
    print(f"Status: {results.status}")
    print(f"Files scanned: {results.file_count}")
    print(f"Detections found: {results.detection_count}")
    
    if results.summary.highest_severity:
        print(f"Highest severity: {results.summary.highest_severity}")


# =============================================================================
# Example 4: Scan a Model from S3
# =============================================================================

def scan_s3_example(client: HiddenLayer, bucket: str, key: str) -> None:
    """
    Scan a model file stored in AWS S3.
    
    Requires: pip install boto3
    
    Args:
        client: HiddenLayer client instance
        bucket: S3 bucket name
        key: S3 object key (path to the model file)
    """
    print(f"\n{'='*60}")
    print("Example 4: Scanning a model from S3")
    print(f"{'='*60}")
    
    results = client.model_scanner.scan_s3_model(
        model_name="my-s3-model",
        bucket=bucket,
        key=key,
        request_source="Integration",
    )
    
    print(f"\nScan ID: {results.scan_id}")
    print(f"Status: {results.status}")
    print(f"Detections found: {results.detection_count}")


# =============================================================================
# Example 5: Scan a Model from Azure Blob Storage
# =============================================================================

def scan_azure_blob_example(
    client: HiddenLayer,
    account_url: str,
    container: str,
    blob: str,
) -> None:
    """
    Scan a model file stored in Azure Blob Storage.
    
    Requires: pip install azure-identity azure-storage-blob
    
    Args:
        client: HiddenLayer client instance
        account_url: Azure storage account URL
        container: Container name
        blob: Blob path (path to the model file)
    """
    print(f"\n{'='*60}")
    print("Example 5: Scanning a model from Azure Blob Storage")
    print(f"{'='*60}")
    
    results = client.model_scanner.scan_azure_blob_model(
        model_name="my-azure-model",
        account_url=account_url,
        container=container,
        blob=blob,
        request_source="Integration",
        credential="AZURE_BLOB_SAS_KEY",
    )
    
    print(f"\nScan ID: {results.scan_id}")
    print(f"Status: {results.status}")
    print(f"Detections found: {results.detection_count}")


# =============================================================================
# Example 6: Community Scanner - Scan a Model from a Remote Location
# =============================================================================

def scan_community_example(
    client: HiddenLayer,
    model_name: str,
    model_path: str,
    model_source: str,
    model_version: str = "main",
) -> None:
    """
    Scan a model from a remote location using the Community Scanner.
    
    This is useful for scanning models stored in various cloud locations
    without downloading them locally first.
    
    Args:
        client: HiddenLayer client instance
        model_name: Name of the model to display in HiddenLayer UI
        model_path: Path/URL to the model in the remote location
        model_source: Source type, one of:
            - "LOCAL" - Local file path
            - "AWS_PRESIGNED" - AWS S3 presigned URL
            - "AWS_IAM_ROLE" - AWS S3 with IAM role authentication
            - "AZURE_BLOB_SAS" - Azure Blob with SAS token
            - "AZURE_BLOB_AD" - Azure Blob with Active Directory
            - "GOOGLE_SIGNED" - Google Cloud signed URL
            - "GOOGLE_OAUTH" - Google Cloud with OAuth
            - "HUGGING_FACE" - HuggingFace Hub model
        model_version: Version of the model (default: "main")
    """
    print(f"\n{'='*60}")
    print("Example 6: Community Scanner - Scanning from remote location")
    print(f"{'='*60}")
    
    scan_result = client.community_scanner.community_scan(
        model_name=model_name,
        model_path=model_path,
        model_source=model_source,
        model_version=model_version,
        origin="github-action",
        request_source="Integration",
    )
    
    print(f"\nScan ID: {scan_result.scan_id}")
    print(f"Status: {scan_result.status}")
    print(f"Files scanned: {scan_result.file_count}")
    print(f"Detections found: {scan_result.detection_count}")
    
    if scan_result.summary.highest_severity:
        print(f"Highest severity: {scan_result.summary.highest_severity}")


# =============================================================================
# Main Entry Point
# =============================================================================

def main() -> None:
    """Run the demo examples."""
    # Create the client
    # client = create_client()
    
    # Example 1: Scan a local file
    # Uncomment and update the path to run:
    # scan_file_example(client, "/path/to/your/model.pkl")
    
    # Example 2: Scan a folder
    # Uncomment and update the path to run:
    # scan_folder_example(client, "/path/to/your/models/folder")
    
    # Example 3: Scan a HuggingFace model
    # Uncomment to run (requires huggingface_hub package):
    # scan_huggingface_example(client, "bert-base-uncased")
    
    # Example 4: Scan from S3
    # Uncomment to run (requires boto3 package):
    # scan_s3_example(client, "my-bucket", "models/my-model.pkl")
    
    # Example 5: Scan from Azure Blob Storage
    # Uncomment to run (requires azure packages):
    # scan_azure_blob_example(
    #     client,
    #     "https://mystorageaccount.blob.core.windows.net",
    #     "my-container",
    #     "models/my-model.pkl",
    # )
    
    # Example 6: Community Scanner - Scan from remote location
    # Uncomment to run with your model details:
    # scan_community_example(
    #     client,
    #     model_name="my-remote-model",
    #     model_path="https://my-presigned-s3-url.com/model.pkl",
    #     model_source="AWS_PRESIGNED",  # or HUGGING_FACE, AZURE_BLOB_SAS, etc.
    #     model_version="v1.0",
    # )
    
    print("\nDemo complete! Uncomment the examples you want to run.")
    print("Make sure to update file paths and credentials as needed.")


if __name__ == "__main__":
    main()
