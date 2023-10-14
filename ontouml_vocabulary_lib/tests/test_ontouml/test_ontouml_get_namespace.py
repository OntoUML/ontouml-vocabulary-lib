"""Module for testing exclusively the method get_namespace()of the OntoUML class."""
import pytest

from ontouml_vocabulary_lib.terms import OntoUML
from ontouml_vocabulary_lib.tests.test_ontouml.fixtures_test_ontouml import OK_BASE_URI, NOK_BASE_URI, INVALID_INPUTS


def test_get_namespace_equals_ns_attribute_and_ok_base_uri() -> None:
    """Ensure get_namespace returns the expected namespace URI.

    Validates that the OntoUML.get_namespace method returns a namespace URI equivalent to the '_NS' class attribute
    and matches the predefined OK_BASE_URI.
    """
    assert OntoUML.get_namespace() == (str(OntoUML._NS))
    assert OntoUML.get_namespace() == OK_BASE_URI


def test_get_namespace_is_not_none_and_differs_from_nok_base_uri() -> None:
    """Verify get_namespace returns a valid namespace.

    Ensures the namespace returned by OntoUML.get_namespace is not None and does not equate to the
    undesired NOK_BASE_URI.
    """
    assert OntoUML.get_namespace() is not None
    assert OntoUML.get_namespace() != NOK_BASE_URI


def test_get_namespace_returns_string_type() -> None:
    """Check the return type of get_namespace.

    Ensures the namespace URI returned by OntoUML.get_namespace is a string, validating its format
    for URI representation.
    """
    assert isinstance(OntoUML.get_namespace(), str)


@pytest.mark.parametrize(
    "in_arg",
    INVALID_INPUTS,
)
def test_get_namespace_raises_typeerror_with_argument(in_arg) -> None:
    """Confirm get_namespace raises TypeError when provided an argument.

    Tests various input types to ensure that the OntoUML.get_namespace method raises a TypeError when it is provided
    with an argument, affirming its designed usage without parameters.
    """
    with pytest.raises(TypeError):
        OntoUML.get_namespace(in_arg)
