"""Module for testing exclusively the method get_namespace of the OntoUML class."""

import pytest
from rdflib import URIRef

from ontouml_vocabulary_lib.terms import OntoUML
from ontouml_vocabulary_lib.exceptions import OUUnavailableTerm
from ontouml_vocabulary_lib.tests.test_ontouml.fixtures_test_ontouml import (
    ALL_TERMS_FRAGMENT,
    ALL_TERMS_STR,
    INVALID_INPUTS,
)


@pytest.mark.parametrize(
    "in_arg",
    ALL_TERMS_FRAGMENT,
)
def test_string_representation_validity(in_arg) -> None:
    """Test if the string representation of a retrieved OntoUML term is valid.

    This test ensures that when provided with a valid term fragment as input, the `get_term` method returns
    a term whose string representation is found within the predefined list of all term strings (ALL_TERMS_STR).

    :param in_arg: A fragment of an OntoUML term used as input to retrieve the term.
    :type in_arg: str
    """
    assert str(OntoUML.get_term(in_arg)) in ALL_TERMS_STR


@pytest.mark.parametrize(
    "in_arg",
    ALL_TERMS_FRAGMENT,
)
def test_term_retrieval_inclusion(in_arg) -> None:
    """Test if a retrieved OntoUML term is included in the list of all OntoUML terms.

    This test ensures that when provided with a valid term fragment as input, the `get_term` method returns
    a term that is found within the predefined list of all OntoUML terms obtained through the `get_list_all` method.

    :param in_arg: A fragment of an OntoUML term used as input to retrieve the term.
    :type in_arg: str
    """
    assert OntoUML.get_term(in_arg) in OntoUML.get_list_all()


@pytest.mark.parametrize(
    "in_arg",
    ALL_TERMS_FRAGMENT,
)
def test_get_term_type(in_arg) -> None:
    """Test if `get_term` returns instances of URIRef for valid term fragments.

    The test ensures that when provided with a valid term fragment as input, the `get_term` method:
    - Does not return None.
    - Returns an instance of `URIRef`.

    :param in_arg: A fragment of an OntoUML term.
    :type in_arg: str
    """
    term = OntoUML.get_term(in_arg)
    assert term is not None
    assert isinstance(term, URIRef)


@pytest.mark.parametrize(
    "in_arg",
    INVALID_INPUTS,
)
def test_get_term_with_invalid_inputs(in_arg) -> None:
    """Test if `get_term` raises OUUnavailableTerm for invalid inputs.

    This test ensures that when provided with an invalid input (that does not correspond to any OntoUML term),
    the `get_term` method raises an exception of type `OUUnavailableTerm`.

    :param in_arg: An invalid OntoUML term fragment.
    :type in_arg: str
    """
    with pytest.raises(OUUnavailableTerm):
        OntoUML.get_term(in_arg)


def test_get_term_with_no_argument() -> None:
    """Test if `get_term` raises a TypeError when called without arguments.

    This test ensures that when the `get_term` method is called without providing any input arguments,
    it raises an exception of type `TypeError`.
    """
    with pytest.raises(TypeError):
        OntoUML.get_term()
