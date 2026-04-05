from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="week_3_mls/deployment",
    repo_id="vineeth32/Machine-Failure-Prediction-ETE",
    repo_type="space",
    path_in_repo="",
)
