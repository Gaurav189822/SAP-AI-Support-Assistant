import pandas as pd


def clean_data(dataframe):

    print("\nStarting data cleaning...")

    # Remove duplicate rows
    dataframe = dataframe.drop_duplicates()

    print("Duplicates removed")

    # Fill missing values
    dataframe = dataframe.fillna("")

    print("Missing values handled")

    # Convert ALL columns to string
    dataframe = dataframe.astype(str)

    print("Converted all columns to string")

    # Combine ALL columns into one text field
    dataframe["combined_text"] = dataframe.apply(
        lambda row: " ".join(row.values),
        axis=1
    )

    print("Combined text field created")

    print(f"\nTotal records: {len(dataframe)}")

    print("\nData cleaning completed successfully!")

    return dataframe