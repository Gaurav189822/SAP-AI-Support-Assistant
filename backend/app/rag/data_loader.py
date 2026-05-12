import pandas as pd
from pathlib import Path

DATA_FOLDER = Path("data")

def load_all_datasets():

    datasets = []

    dataset_files = [
        "sap_docs_dataset.xlsx",
        "sap_community_dataset.xlsx",
        "enterprise_scale_sap_dataset.xlsx",
        "sap_noisy_tickets_dataset.xlsx"
    ]

    for file_name in dataset_files:

        file_path = DATA_FOLDER / file_name

        print(f"Loading dataset: {file_name}")

        df = pd.read_excel(file_path)

        df["source_file"] = file_name

        datasets.append(df)

    combined_dataframe = pd.concat(
        datasets,
        ignore_index=True
    )

    print("All datasets loaded successfully!")

    return combined_dataframe