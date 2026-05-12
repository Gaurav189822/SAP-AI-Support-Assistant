from app.rag.data_loader import load_all_datasets

dataframe = load_all_datasets()

print("\nColumns:\n")

print(dataframe.columns)

print("\nData Types:\n")

print(dataframe.dtypes)