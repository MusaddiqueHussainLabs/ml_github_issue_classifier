from pathlib import Path
from pydantic_settings import BaseSettings

class AppConstants(BaseSettings):

    CONFIG_FILE_PATH: Path =  Path("src/github_labeler/core/config.yaml")
    PARAMS_FILE_PATH: Path =  Path("src/github_labeler/core/params.yaml")
    SCHEMA_FILE_PATH: Path =  Path("src/github_labeler/schemas/schema.yaml")
    STATUS_FILE_PATH: Path =  Path("data/interim/status.txt")

constants =    AppConstants()