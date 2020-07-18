import pytest

from md_table_creator import create_md_table


def test_create_id_table():
    # fmt: off
    input = (
        "CREATE TABLE table_name (\n"
        "    id BIGINT AUTO_INCREMENT PRIMARY KEY,\n"
        ");"
    )
    # fmt: on
    expected = (
        "*table_name*\n"
        "Column | Type | Comments\n"
        "-|-|-\n"
        "id|BIGINT AUTO_INCREMENT PRIMARY KEY|"
    )
    actual = create_md_table(input)
    assert expected == actual


def test_different_table_name():
    input = (
        "CREATE TABLE diff_table_name (\n"
        "    id BIGINT AUTO_INCREMENT PRIMARY KEY,\n"
        ");"
    )
    expected = (
        "*diff_table_name*\n"
        "Column | Type | Comments\n"
        "-|-|-\n"
        "id|BIGINT AUTO_INCREMENT PRIMARY KEY|"
    )
    actual = create_md_table(input)
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
    input = f"{create_table}\n" "    id BIGINT AUTO_INCREMENT PRIMARY KEY,\n" ");"
    expected = (
        "*table_name*\n"
        "Column | Type | Comments\n"
        "-|-|-\n"
        "id|BIGINT AUTO_INCREMENT PRIMARY KEY|"
    )
    actual = create_md_table(input)
    assert expected == actual
