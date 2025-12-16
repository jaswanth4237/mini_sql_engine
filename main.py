from parser import parse_query
from engine import load_csv, apply_where, apply_select, apply_count


def print_table(rows):
    headers = rows[0].keys()
    print(" | ".join(headers))
    print("-" * 40)
    for row in rows:
        print(" | ".join(row.values()))

data = load_csv("data.csv")

print("Mini SQL Engine Started")
print("Type 'exit' to quit")

while True:
    query = input("sql> ")
    if not query.strip():
        continue


    if query.lower() in ["exit", "quit"]:
        break

    try:
        parsed = parse_query(query)
        filtered_data = apply_where(data, parsed["where"])
        if parsed["is_count"]:
            count = apply_count(filtered_data, parsed["count_column"])
            print(f"COUNT = {count}")
            continue
        else:
            result = apply_select(filtered_data, parsed["select"])
        if not result:
            print("No rows found")
        else:
            print_table(result)



    except Exception as e:
        print("Error:", e)
