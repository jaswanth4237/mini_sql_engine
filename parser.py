def parse_query(query):
    query = query.strip()
    lower_query = query.lower()

    if not lower_query.startswith("select"):
        raise ValueError("Only SELECT queries are supported")

    if "from" not in lower_query:
        raise ValueError("Missing FROM clause")

    select_part, rest = lower_query.split("from", 1)
    original_select, original_rest = query.split("FROM", 1) if "FROM" in query else query.split("from", 1)

    select_expr = original_select.replace("SELECT", "").replace("select", "").strip()

    is_count = False
    count_column = None

    if select_expr.lower().startswith("count"):
        is_count = True
        inside = select_expr[6:-1].strip()  # content inside COUNT()
        count_column = inside  # * or column name

    where_clause = None

    if "where" in lower_query:
        table_part, where_part = original_rest.split("WHERE", 1) if "WHERE" in original_rest else original_rest.split("where", 1)
        table = table_part.strip()

        col, op, val = where_part.strip().split()
        val = val.strip("'")
        where_clause = {"col": col, "op": op, "val": val}
    else:
        table = original_rest.strip()

    if table != "data":
        raise ValueError(f"Table '{table}' does not exist")

    return {
        "select": select_expr,
        "is_count": is_count,
        "count_column": count_column,
        "where": where_clause
    }
