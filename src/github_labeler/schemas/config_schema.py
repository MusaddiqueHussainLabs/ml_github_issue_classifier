from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_train_url: str
    source_test_url: str
    local_train_file: Path
    local_test_file: Path