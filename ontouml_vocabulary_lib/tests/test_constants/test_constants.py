"""Testing Module for OntoUML Tuple Validation

This module carries out tests to validate tuples utilized in the OntoUML model, ensuring that elements contained
within them adhere to the defined criteria (e.g., non-null, type adherence, etc.) and overall tuple integrity
(e.g., non-emptiness, expected size, etc.).
"""
import pytest
from rdflib import URIRef

from ontouml_vocabulary_lib.tests.test_constants.fixtures_test_constants import DICT_TUPLES_SIZE, MUTANTS


@pytest.mark.parametrize("in_tuple", DICT_TUPLES_SIZE.keys())
def test_elements_are_non_null_and_of_type_URIRef(in_tuple: tuple) -> None:
    """Ensure each element within the tuple is non-null and an instance of URIRef.

    :param in_tuple: The tuple whose elements are to be checked for non-nullity and type URIRef.
    :type in_tuple: tuple
    """
    for elem in in_tuple:
        assert elem is not None
        assert isinstance(elem, URIRef)


@pytest.mark.parametrize("in_tuple", DICT_TUPLES_SIZE.keys())
def test_first_element_of_tuple_is_truthy(in_tuple: tuple) -> None:
    """Assert the first element of the tuple evaluates to True.

    :param in_tuple: The tuple whose first element is to be asserted as truthy.
    :type in_tuple: tuple
    """
    assert in_tuple[0]


@pytest.mark.parametrize("in_tuple", DICT_TUPLES_SIZE.keys())
def test_tuple_is_not_empty(in_tuple: tuple) -> None:
    """Ensure the provided tuple is not empty.

    :param in_tuple: The tuple to be checked for non-emptiness.
    :type in_tuple: tuple
    """
    assert len(in_tuple) > 0


@pytest.mark.parametrize("in_tuple, size", DICT_TUPLES_SIZE.items())
def test_tuple_size_matches_expected(in_tuple: tuple, size: int) -> None:
    """Confirm the provided tuple's size matches the expected size.

    :param in_tuple: The tuple whose size is to be checked.
    :type in_tuple: tuple
    :param size: The expected size of the tuple.
    :type size: int
    """
    assert len(in_tuple) == size





@pytest.mark.parametrize("in_tuple", DICT_TUPLES_SIZE.keys())
def test_elements_are_unique(in_tuple: tuple) -> None:
    """Test to ensure that all elements within a tuple are unique.

    :param in_tuple: The input tuple whose elements are to be verified for uniqueness.
    :type in_tuple: tuple
    """
    assert len(in_tuple) == len(set(in_tuple)), "Duplicate elements found in tuple."



@pytest.mark.parametrize("in_tuple", DICT_TUPLES_SIZE.keys())
def test_elements_are_in_alphabetical_order(in_tuple: tuple) -> None:
    """Test to ensure that all elements within a tuple are in alphabetical order.

    :param in_tuple: The input tuple whose elements are to be verified for order.
    :type in_tuple: tuple
    """
    # Extracting the string representations of the elements in the tuple
    string_representations = [str(elem) for elem in in_tuple]

    # Comparing the tuple with its sorted version
    assert string_representations == sorted(string_representations), f"Tuple {in_tuple} is not in alphabetical order."


@pytest.mark.parametrize("original,mutation_func,mutant", MUTANTS)
def test_tuple_mutation(original: tuple, mutation_func, mutant: tuple) -> None:
    """
    Mutation test to ensure that tests can detect alterations in the original tuple.

    :param original: The original tuple.
    :type original: tuple
    :param mutation_func: Function that applies mutation.
    :param mutant: A mutated version of the original tuple.
    :type mutant: tuple
    """
    if len(original) > 1:
        assert (
            original != mutant
        ), f"Mutant {mutant} (created by {mutation_func.__name__}) is not detected as different from the original {original}."
