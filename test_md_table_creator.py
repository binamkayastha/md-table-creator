import pytest

from md_table_creator import create_md_tables


def test_create_id_table():
    # fmt: off
    input = (
        "CREATE TABLE table_name (\n"
        "    id BIGINT AUTO_INCREMENT PRIMARY KEY\n"
        ");"
    )
    # fmt: on
    expected = (
        "**table_name**\n"
        "Column | Type | Comments\n"
        "-|-|-\n"
        "id|BIGINT AUTO_INCREMENT PRIMARY KEY|"
    )
    actual = create_md_tables(input)
    assert expected == actual


def test_different_table_name():
    input = (
        "CREATE TABLE diff_table_name (\n"
        "    id BIGINT AUTO_INCREMENT PRIMARY KEY\n"
        ");"
    )
    expected = (
        "**diff_table_name**\n"
        "Column | Type | Comments\n"
        "-|-|-\n"
        "id|BIGINT AUTO_INCREMENT PRIMARY KEY|"
    )
    actual = create_md_tables(input)
    assert expected == actual


@pytest.mark.parametrize(
    "create_table",
    [
        ("CREATE TEMPORARY TABLE IF NOT EXISTS table_name ("),
        ("create TABLE IF NOT EXISTS table_name ("),
        ("create TABLE table_name ("),
    ],
)
def test_table_name_extracted(create_table):
    # fmt: off
    input = (
        f"{create_table}\n"
        "    id BIGINT AUTO_INCREMENT PRIMARY KEY\n"
        ");"
    )
    # fmt: on
    expected = (
        "**table_name**\n"
        "Column | Type | Comments\n"
        "-|-|-\n"
        "id|BIGINT AUTO_INCREMENT PRIMARY KEY|"
    )
    actual = create_md_tables(input)
    assert expected == actual


def test_different_column_name():
    # fmt: off
    input = (
        "CREATE TABLE table_name (\n"
        "    diff_id BIGINT AUTO_INCREMENT PRIMARY KEY\n"
        ");"
    )
    # fmt: on
    expected = (
        "**table_name**\n"
        "Column | Type | Comments\n"
        "-|-|-\n"
        "diff_id|BIGINT AUTO_INCREMENT PRIMARY KEY|"
    )
    actual = create_md_tables(input)
    assert expected == actual


def test_multiple_columns():
    # fmt: off
    input = (
        "CREATE TABLE table_name (\n"
        "    id BIGINT AUTO_INCREMENT PRIMARY KEY,\n"
        "    name VARCHAR(255)\n"
        ");"
    )
    # fmt: on
    expected = (
        "**table_name**\n"
        "Column | Type | Comments\n"
        "-|-|-\n"
        "id|BIGINT AUTO_INCREMENT PRIMARY KEY|\n"
        "name|VARCHAR(255)|"
    )
    actual = create_md_tables(input)
    assert expected == actual


def test_table_with_attribute():
    # fmt: off
    input = (
        "CREATE TABLE sales.visits ("
        "    visit_id INT PRIMARY KEY,\n"
        "    first_name VARCHAR (50) NOT NULL,\n"
        "    phone VARCHAR(20),\n"
        "    store_id INT NOT NULL,\n"
        "    FOREIGN KEY (store_id) REFERENCES sales.stores (store_id)"
        ");"
    )
    # fmt: on
    expected = (
        "**sales.visits**\n"
        "Attributes:\n"
        "FOREIGN KEY (store_id) REFERENCES sales.stores (store_id)\n"
        "Column | Type | Comments\n"
        "-|-|-\n"
        "visit_id|INT PRIMARY KEY|\n"
        "first_name|VARCHAR (50) NOT NULL|\n"
        "phone|VARCHAR(20)|\n"
        "store_id|INT NOT NULL|"
    )
    actual = create_md_tables(input)
    assert expected == actual


def test_multiple_tables():
    # fmt: off
    input = (
        "CREATE TABLE table_name (\n"
        "    id BIGINT AUTO_INCREMENT PRIMARY KEY\n"
        ");"
        "CREATE TABLE table_name2 (\n"
        "    id BIGINT AUTO_INCREMENT PRIMARY KEY\n"
        ");"
    )
    # fmt: on
    expected = (
        "**table_name**\n"
        "Column | Type | Comments\n"
        "-|-|-\n"
        "id|BIGINT AUTO_INCREMENT PRIMARY KEY|"
        "\n\n"
        "**table_name2**\n"
        "Column | Type | Comments\n"
        "-|-|-\n"
        "id|BIGINT AUTO_INCREMENT PRIMARY KEY|"
    )
    actual = create_md_tables(input)
    assert expected == actual


def test_invalid_sql():
    with pytest.raises(ValueError):
        # fmt: off
        invalid_input = (
            "CREATER TABLE table_name (\n"
            "    id BIGINT AUTO_INCREMENT PRIMARY KEY\n"
            ");"
        )
        # fmt: on
        create_md_tables(invalid_input)


def test_empty_sql():
    with pytest.raises(ValueError):
        invalid_input = ""
        create_md_tables(invalid_input)
