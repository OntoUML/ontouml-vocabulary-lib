"""Module for handling custom exceptions related to OntoUML.

This module provides a set of custom exceptions designed for handling various error scenarios
that may occur in the manipulation and management of OntoUML graphs and related operations.
Each exception is designed to provide clear, user-friendly error messages to assist in
debugging and issue resolution.
"""


class OUUnavailableTerm(ValueError):
    """Custom exception for handling cases where an OUTerm is unavailable in the OntoUML Vocabulary.

    This exception is raised when a given OUTerm does not exist or is not found in the OntoUML
    Vocabulary, providing clear feedback that the requested term is unavailable or incorrectly
    specified.

    :param ou_term: The OUTerm that does not exist in the OntoUML Vocabulary.
    :type ou_term: str
    """

    def __init__(self, ou_term: str) -> None:
        message = f"The OUTerm '{ou_term}' does not exist in the OntoUML Vocabulary."
        super().__init__(message)
