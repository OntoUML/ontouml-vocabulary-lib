"""Module for testing exclusively the attributes of the OntoUML class."""
import pytest
from rdflib import URIRef

from ontouml_vocabulary_lib.ontouml import OntoUML
from ontouml_vocabulary_lib.tests.test_ontouml.fixtures_test_ontouml import (
    ALL_TERMS_STR,
    OK_BASE_URI,
    ALL_TERMS_FRAGMENT,
    NOK_BASE_URI,
)


def test_internal_term_presence_and_type() -> None:
    """Ensure internal terms in OntoUML are present in ALL_TERMS_STR and are instances of URIRef.

    This function loops through every internal term of the OntoUML class, converts it to a Python datatype if possible,
    and then verifies:
    - Its presence in the predefined ALL_TERMS_STR list.
    - Its instantiation from the rdflib.URIRef class.
    """
    for internal_term in dir(OntoUML):
        assert internal_term.toPython() in ALL_TERMS_STR
        assert isinstance(internal_term, URIRef)


@pytest.mark.parametrize("term", ALL_TERMS_STR)
def test_ontouml_terms_as_uri_references(term: str) -> None:
    """Check if OntoUML terms can be recognized as valid URI references.

    :param term: A term from the ALL_TERMS_STR list, representing an OntoUML term.
    :type term: str
    :raises AssertionError: If the URIRef of the term is not found in OntoUML's directory.
    """
    list_valid_terms = dir(OntoUML)
    assert URIRef(term) in list_valid_terms


@pytest.mark.parametrize("term", ALL_TERMS_STR)
def test_ontouml_term_matching_uri(term: str) -> None:
    """Verify that accessing an OntoUML term provides a URI combining OK_BASE_URI and the term itself.

    :param term: A term from the ALL_TERMS_STR list, representing an OntoUML term.
    :type term: str
    :raises AssertionError: If the assembled URI does not match the expected format.
    """
    called_term = str(getattr(OntoUML, term))
    assert called_term == OK_BASE_URI + term


@pytest.mark.parametrize("term", ALL_TERMS_FRAGMENT)
def test_ontouml_has_valid_attributes(term: str) -> None:
    """Verifies that OntoUML possesses the specified attributes.

    :param term: The attribute name to be checked.
    :type term: str
    """

    assert hasattr(OntoUML, term)


@pytest.mark.parametrize("term", ALL_TERMS_STR)
def test_ontouml_term_excludes_invalid_variations(term: str) -> None:
    """Assert that called_term doesn't match any of the undesired/invalid variations.

    :param term: A term from the ALL_TERMS_STR list, representing an OntoUML term.
    :type term: str
    :raises AssertionError: If called_term matches any pattern in the invalid_variations list.
    """
    called_term = str(getattr(OntoUML, term))

    # Creating a list of all the variations to be checked
    invalid_variations = [
        OK_BASE_URI,
        OK_BASE_URI + term.upper(),
        OK_BASE_URI + " " + term,
        " " + OK_BASE_URI + term,
        OK_BASE_URI + term + " ",
        NOK_BASE_URI + term,
        "",
    ]

    # Asserting that called_term is not any of the invalid variations
    assert called_term not in invalid_variations


@pytest.mark.parametrize("term", ALL_TERMS_STR)
def test_ontouml_term_accessibility(term: str) -> None:
    """Verify that each term from ALL_TERMS_STR in OntoUML can be accessed without exceptions and is not None.

    Using getattr, the function dynamically retrieves OntoUML class attributes using terms from ALL_TERMS_STR, ensuring:
    - The accessed attribute is not None.
    - No exceptions are raised during access. If an exception occurs, the function fails and provides an error
    message with the exception’s details.

    :param term: A term from the ALL_TERMS_STR list, representing an OntoUML term to be accessed.
    :type term: str
    :raises pytest.fail: If accessing the term raises any Exception, detailing the exception in the error message.
    """
    try:
        result = getattr(OntoUML, term)
        assert result is not None
    except Exception as e:
        pytest.fail(f"Unexpected error accessing OntoUML.Class: {str(e)}")


@pytest.mark.parametrize(
    "input_string", ["", "abc", "123", "!!!", " ", "!1a", "ab12/#", "class", " Class", "Class ", "cLass", "CLASS"]
)
def test_invalid_ontouml_term_access(input_string: str) -> None:
    """Ensure that attempting to access invalid OntoUML terms raises AttributeError.

    :param input_string: A string input intended to represent an invalid OntoUML term.
    :type input_string: str
    """
    with pytest.raises(AttributeError):
        getattr(OntoUML, input_string)

    assert not (hasattr(OntoUML, input_string))
