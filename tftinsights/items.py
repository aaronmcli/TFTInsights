import pandas as pd
import numpy as np
import requests
from .config import DATA_DRAGON_VERSION
from pathlib import Path
import json

def get_mapping_table_for_items():
    root_dir = Path(__file__).resolve().parents[1]
    config_path = root_dir / "Constants" / "tft-item.json"
    with open(config_path, "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    data_expanded = df["data"].apply(pd.Series)
    data_expanded = data_expanded.drop(columns=["image"], errors="ignore")    
    data_expanded["key"] = df.index
    return data_expanded
    

