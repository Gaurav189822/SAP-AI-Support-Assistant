from app.rag.retriever import retrieve

query = "SAP MM purchase order error"

results = retrieve(query)

print("\nTop Retrieved Results:\n")

for result in results:

    print(result)

    print("\n---------------------\n")