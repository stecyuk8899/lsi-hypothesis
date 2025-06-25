from hypothesis import given, strategies as st
from hypothesis import assume as hypothesis_assume
import pytest

from src.random_operations import (
    find_largest_smallest_item,
    sort_array,
    reverse_string,
    complex_string_operation,
)


# Property Based Unit Testing
@given(st.lists(st.integers(), min_size=1, max_size=25))
def test_find_largest_smallest_item_hypothesis(input_list):
    assert find_largest_smallest_item(input_list) == (max(input_list), min(input_list))


@given(
    st.lists(
        st.fixed_dictionaries({"name": st.text(), "age": st.integers()}),
    )
)
def test_sort_array_hypothesis(input_list):
    if len(input_list) == 0:
        with pytest.raises(ValueError):
            sort_array(input_list, "age")

    hypothesis_assume(len(input_list) > 0)
    assert sort_array(input_list, "age") == sorted(
        input_list, key=lambda x: x["age"], reverse=True
    )


@given(st.text())
def test_reverse_string_hypothesis(input_string):
    assert reverse_string(input_string) == input_string[::-1]


@given(st.text())
def test_complex_string_operation_hypothesis(input_string):
    assert complex_string_operation(input_string) == input_string.strip().replace(
        " ", ""
    ).upper().replace("A", "").replace("E", "").replace("I", "").replace(
        "O", ""
    ).replace(
        "U", ""
    )
