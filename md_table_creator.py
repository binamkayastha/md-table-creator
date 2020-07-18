# Add utf file or something
import re


def create_md_table(sql_create_table: str) -> str:
    """Converts sql create table syntax into md table."""
    table_name = extract_table_name(sql_create_table)
    expected = (
        f"*{table_name}*\n"
        "Column | Type | Comments\n"
        "-|-|-\n"
        "id|BIGINT AUTO_INCREMENT PRIMARY KEY|"
    )
    return expected


def extract_table_name(sql_create_table: str) -> str:
    """Uses regex to extract the table name from the sql syntax.

    https://dev.mysql.com/doc/refman/5.7/en/create-table.html
    CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name (
    """
    if raw_table := re.search(
        "create (?:temporary )?table (?:if not exists)?(.*)\(",
        sql_create_table,
        re.IGNORECASE,
    ):
        if groups := raw_table.groups():
            return groups[0].strip()
    raise ValueError(
        "Could not parse table name from SQL create table syntax. Make sure it's valid SQL syntax"
    )
