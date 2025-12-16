import csv

def load_csv(filename):
    with open(filename, newline='') as file:
        return list(csv.DictReader(file))
def apply_where(data, condition):
    if not condition:
        return data

    result = []
    col, op, val = condition["col"], condition["op"], condition["val"]

    for row in data:
        if col not in row:
            raise ValueError(f"Column '{col}' does not exist")

        cell = row[col]

        try:
            cell_val = int(cell)
            cond_val = int(val)
        except ValueError:
            cell_val = cell.lower()
            cond_val = val.lower()

        if op == ">" and cell_val > cond_val:
            result.append(row)
        elif op == "<" and cell_val < cond_val:
            result.append(row)
        elif op == "=" and cell_val == cond_val:
            result.append(row)
        elif op == ">=" and cell_val >= cond_val:
            result.append(row)
        elif op == "<=" and cell_val <= cond_val:
            result.append(row)
        elif op == "!=" and cell_val != cond_val:
            result.append(row)

    return result


def apply_select(data, columns):
    if columns == "*":
        return data

    cols = [c.strip() for c in columns.split(",")]
    result = []

    for row in data:
        new_row = {}
        for col in cols:
            new_row[col] = row[col]
        result.append(new_row)

    return result
def apply_count(data, column):
    if column == "*":
        return len(data)

    count = 0
    for row in data:
        if row.get(column):
            count += 1
    return count
