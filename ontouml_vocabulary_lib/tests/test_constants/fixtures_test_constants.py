"""Fixtures for testing the OntoUML constants.

This module provides fixtures for testing the constant values defined in the OntoUML vocabulary library. It imports
various sets of predefined constants from the OntoUML vocabulary library and defines a dictionary to store the expected
size of these sets. It also provides a set of utility functions for performing basic manipulations on tuples, which are
used to generate a list of mutated tuples for testing.
"""

from ontouml_vocabulary_lib.constants.constants_classes import (
    ONTOUML_BASE_SORTAL_CLASS_STEREOTYPES,
    ONTOUML_ULTIMATE_SORTAL_CLASS_STEREOTYPES,
    ONTOUML_SORTAL_CLASS_STEREOTYPES,
    ONTOUML_NON_SORTAL_CLASS_STEREOTYPES,
    ONTOUML_ABSTRACT_CLASS_STEREOTYPES,
    ONTOUML_RIGID_CLASS_STEREOTYPES,
    ONTOUML_ANTI_RIGID_CLASS_STEREOTYPES,
    ONTOUML_SEMI_RIGID_CLASS_STEREOTYPES,
    ONTOUML_CLASS_STEREOTYPES,
)
from ontouml_vocabulary_lib.constants.constants_misc import (
    ONTOUML_RELATION_STEREOTYPES,
    ONTOUML_PROPERTY_STEREOTYPES,
    ONTOUML_AGGREGATION_KINDS,
    ONTOUML_ONTOLOGICAL_NATURES,
    ONTOUML_ABSTRACT_ELEMENTS,
    ONTOUML_CONCRETE_ELEMENTS,
)

DICT_TUPLES_SIZE = {
    ONTOUML_BASE_SORTAL_CLASS_STEREOTYPES: 4,
    ONTOUML_ULTIMATE_SORTAL_CLASS_STEREOTYPES: 7,
    ONTOUML_SORTAL_CLASS_STEREOTYPES: 11,
    ONTOUML_NON_SORTAL_CLASS_STEREOTYPES: 5,
    ONTOUML_ABSTRACT_CLASS_STEREOTYPES: 3,
    ONTOUML_RIGID_CLASS_STEREOTYPES: 8,
    ONTOUML_ANTI_RIGID_CLASS_STEREOTYPES: 6,
    ONTOUML_SEMI_RIGID_CLASS_STEREOTYPES: 1,
    ONTOUML_CLASS_STEREOTYPES: 21,
    ONTOUML_RELATION_STEREOTYPES: 19,
    ONTOUML_PROPERTY_STEREOTYPES: 2,
    ONTOUML_AGGREGATION_KINDS: 3,
    ONTOUML_ONTOLOGICAL_NATURES: 11,
    ONTOUML_ABSTRACT_ELEMENTS: 11,
    ONTOUML_CONCRETE_ELEMENTS: 10,
}


def swap_first_two(original: tuple) -> tuple:
    """Swap the first two elements of a given tuple.

    :param original: The original tuple.
    :type original: tuple
    :return: A new tuple with the first two elements swapped. If the tuple has fewer than two elements, returns the
             original tuple unmodified.
    :rtype: tuple
    """
    mutant = list(original)
    if len(mutant) > 1:
        mutant[0], mutant[1] = mutant[1], mutant[0]
    return tuple(mutant)


def remove_first(original: tuple) -> tuple:
    """Remove the first element from a given tuple.

    :param original: The original tuple.
    :type original: tuple
    :return: A new tuple with the first element removed.
    :rtype: tuple
    """
    return original[1:]


def add_element(original: tuple) -> tuple:
    """Add a None element to the end of a given tuple.

    :param original: The original tuple.
    :type original: tuple
    :return: A new tuple with a None element added at the end.
    :rtype: tuple
    """
    return original + (None,)


def replace_last(original: tuple) -> tuple:
    """Replace the last element of a given tuple with the string "REPLACEMENT".

    :param original: The original tuple.
    :type original: tuple
    :return: A new tuple with the last element replaced by "REPLACEMENT".
    :rtype: tuple
    """
    return original[:-1] + ("REPLACEMENT",)


def reverse_order(original: tuple) -> tuple:
    """Reverse the order of elements in a given tuple.

    :param original: The original tuple.
    :type original: tuple
    :return: A new tuple with the order of elements reversed.
    :rtype: tuple
    """
    return tuple(reversed(original))


# List of mutation functions
MUTATIONS = [swap_first_two, remove_first, add_element, replace_last, reverse_order]


# Extract tuples from your dictionary
TUPLES = DICT_TUPLES_SIZE.keys()

# Generate mutants
MUTANTS = [(original, mutation, mutation(original)) for original in TUPLES for mutation in MUTATIONS]
