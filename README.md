[![DOI](https://zenodo.org/badge/DOI/XXXXXX/zenodo.XXXXXX.svg)](https://doi.org/10.5281/zenodo.8214977)
[![Project Status - Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
![GitHub - Release Date - PublishedAt](https://img.shields.io/github/release-date/ontouml/ontouml-vocabulary-lib)
![GitHub - Last Commit - Branch](https://img.shields.io/github/last-commit/ontouml/ontouml-vocabulary-lib/main)
![PyPI - Project](https://img.shields.io/pypi/v/ontouml-vocabulary-lib)
![Language - Top](https://img.shields.io/github/languages/top/ontouml/ontouml-vocabulary-lib)
![Language - Version](https://img.shields.io/pypi/pyversions/ontouml-vocabulary-lib)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/ontouml/ontouml-vocabulary-lib)
![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/OntoUML/ontouml-vocabulary-lib/badge)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![License - GitHub](https://img.shields.io/github/license/ontouml/ontouml-vocabulary-lib)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/OntoUML/ontouml-vocabulary-lib/main.svg)](https://results.pre-commit.ci/latest/github/OntoUML/ontouml-vocabulary-lib/main)
![Website](https://img.shields.io/website/http/ontouml.github.io/ontouml-vocabulary-lib.svg)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/ontouml/ontouml-vocabulary-lib/code_testing.yml)

# ontouml-vocabulary-lib

<p align="center"><img src="https://raw.githubusercontent.com/OntoUML/ontouml-vocabulary-lib/main/resources/logo-ontouml-vocabulary-lib-reduced.png" width="740"></p>

**📦 PyPI Package:**
The library is conveniently [available as a PyPI package](https://pypi.org/project/ontouml-vocabulary-lib/), allowing users to easily import it into other RDFLib/Python projects.

**📚 Documentation:**
For inquiries and further information, please refer to the [comprehensive docstring-generated documentation](https://w3id.org/ontouml/vocabulary-lib/docs) available for this project.

## Contents

<!-- TOC -->

* [ontouml-vocabulary-lib](#ontouml-vocabulary-lib)
    * [Contents](#contents)
    * [Installation and Use](#installation-and-use)
        * [Prerequisites](#prerequisites)
        * [Instructions for Users](#instructions-for-users)
        * [Instructions for Contributors](#instructions-for-contributors)
    * [Introduction](#introduction)
        * [The OntoUML Vocabulary](#the-ontouml-vocabulary)
        * [The RDFLib](#the-rdflib)
    * [The ontouml-vocabulary-lib Concepts](#the-ontouml-vocabulary-lib-concepts)
        * [OntoUML Terms](#ontouml-terms)
            * [Descriptions of the Methods:](#descriptions-of-the-methods)
            * [Usage examples](#usage-examples)
        * [OntoUML Constants](#ontouml-constants)
            * [Usage examples](#usage-examples-1)
            * [OUEnumerations Class Method Descriptions](#ouenumerations-class-method-descriptions)
        * [Classes Specializing `_OUElement`](#classes-specializing-ouelement)
        * [Enumeration Classes](#enumeration-classes)
        * [Note](#note)
        * [OntoUML Custom Exceptions](#ontouml-custom-exceptions)
            * [Descriptions of Exceptions](#descriptions-of-exceptions)
    * [How to Contribute](#how-to-contribute)
        * [Report Issues](#report-issues)
        * [Code Contribution](#code-contribution)
        * [Test Contribution](#test-contribution)
        * [General Guidelines](#general-guidelines)
    * [Author](#author)

<!-- TOC -->

## Installation and Use

### Prerequisites

Ensure you have Python installed on your system before utilizing the `ontouml-vocabulary-lib`. It has been tested with Python versions 3.9 to 3.11 on Mac, Windows, and Linux. If not installed, [download and install Python](https://www.python.org/downloads/).

### Instructions for Users

1. Install ontouml-vocabulary-lib: Execute the following command to install the library:

```shell
pip install ontouml-vocabulary-lib
```

All dependencies will be installed automatically.

2. Usage: To use ontouml-vocabulary-lib, you simply have to make the following import in your Python code:

```python
from ontouml_vocabulary_lib import *
```

Now all concepts

### Instructions for Contributors

1. **Fork the Project:**
   Fork the `ontouml-vocabulary-lib` repository to your own GitHub account.

2. **Clone and Setup:**
   Clone your forked repository and navigate to the project directory.

3. **Install Dependencies:**
   Use [Poetry](https://python-poetry.org/) for dependency management. If not installed, refer to Poetry’s [documentation](https://python-poetry.org/docs/#installation) for installation instructions. Then, install all dependencies with:

```shell
poetry install
```

Now, you're ready to make enhancements or fixes and contribute back to ontouml-vocabulary-lib!

## Technological Background

The **ontouml-vocabulary-lib** is a Python library tailored for managing OntoUML concepts on [RDFLib](https://rdflib.readthedocs.io/en/stable/) graphs.

The library complies with the [OntoUML vocabulary]((https://w3id.org/ontouml/vocabulary))—ensuring compatibility with its [version 1.1.0](https://w3id.org/ontouml/vocabulary/v1.1.0).

### The OntoUML Vocabulary

OntoUML is a modeling language that has been developed to support the representation of domain ontologies in the conceptual modeling phase of system development. The [OntoUML Vocabulary](https://w3id.org/ontouml/vocabulary), on the other hand, is an OWL vocabulary designed to allow the serialization and exchanging of OntoUML models in conformance with the [OntoUML Metamodel](https://w3id.org/ontouml/metamodel).

The OntoUML Vocabulary provides the necessary resources for mapping OntoUML models to OWL ontologies, which is a crucial step for utilizing OntoUML in Semantic Web applications.

### The RDFLib

[RDFLib](https://rdflib.readthedocs.io/en/stable/) is a Python library that provides a comprehensive toolkit for working with [Resource Description Framework (RDF)](https://www.w3.org/RDF/) data, which is fundamental to the Semantic Web and linked data technologies. RDFLib enables developers to create, manipulate, and query RDF graphs, making it a powerful tool for managing knowledge graphs within the Python ecosystem.

## Concepts

When working with the ontouml-vocabulary-lib library, users will primarily engage with five fundamental concepts, each contributing to the seamless manipulation of OntoUML models and RDF graphs. These key concepts include OUTerm, which represents OntoUML terms and ensures semantic consistency; OUElement, serving as a container for various OntoUML model elements and maintaining their structured details; OUGraph, a pivotal orchestrator for OntoUML vocabulary elements within RDF graphs, enabling systematic access and manipulation; OUEnumeration, which provides organized enumerations for OntoUML concepts and stereotypes; and Graph, a core concept from RDFLib, offering a structured framework for managing RDF data. Together, these concepts empower users to efficiently handle OntoUML models, navigate their semantic complexities, and interact with RDF graphs, making ontouml-vocabulary-lib a valuable tool for ontology-driven conceptual modeling and semantic web technologies.

### OntoUML Terms

The `OntoUML` class in this library encapsulates the OntoUML vocabulary, enabling easy interaction with ontological terms to enhance the accuracy and consistency of your model. This class is designed to operate similarly to how RDFLib handles vocabularies like OWL, RDF, and RDFS. In RDFLib, you can access concepts from these vocabularies directly, for instance, `RDFS.subClassOf` or `RDF.type` (for more information, [access here](https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.namespace.html#rdflib.namespace.Namespace)). Similarly, with this library, you can access OntoUML terms directly, e.g., `OntoUML.kind`.

Additionally, this library integrates the `URIRef` concept from RDFLib, which allows for the clear and unambiguous definition of relationships and properties through universal resource identifiers (URIs). A [URIRef in RDFLib](https://rdflib.readthedocs.io/en/stable/rdf_terms.html#uriref) is a unique identifier used to identify resources in semantic web technologies.

#### Methods

Here are the methods provided by the `OntoUML` class:

- **`get_list_all`**: Retrieves all OntoUML terms as a list of `URIRef` objects.
- **`get_namespace`**: Returns the OntoUML namespace as a string.
- **`get_term`**: Given a term name as a string, retrieves the corresponding OntoUML term as a `URIRef`.

| Method Name     | Description                  | Arguments        | Return Type       |
|-----------------|------------------------------|------------------|-------------------|
| `get_list_all`  | Lists all OntoUML terms      | None             | List of `URIRef`  |
| `get_namespace` | Gets OntoUML namespace       | None             | `str`             |
| `get_term`      | Gets a specific OntoUML term | `term_name: str` | `URIRef` or Error |

#### Usage Examples

For having access to the OntoUML concept, the following importing is required:
```python
from ontouml_vocabulary_lib import OntoUML
```

1. Accessing a specific OntoUML Term:

```python
# Accessing a specific OntoUML term
my_ontouml_class = OntoUML.Class

# Output
print(my_ontouml_class)  # https://w3id.org/ontouml#Class
```

The result "https://w3id.org/ontouml#Class" from box 1 is of [type URIRef in RDFLib](https://rdflib.readthedocs.io/en/stable/rdf_terms.html#uriref), which represents a Uniform Resource Identifier (URI) within the Resource Description Framework (RDF) data model, serving as a unique identifier for resources in semantic web technologies.

2. Accessing all OntoUML Terms

```python
# Accessing all OntoUML terms
all_terms = OntoUML.get_list_all()

# Output
print(all_terms)  # [rdflib.term.URIRef('https://w3id.org/ontouml#abstract'), rdflib.term.URIRef('https://w3id.org/ontouml#abstractNature'), rdflib.term.URIRef('https://w3id.org/ontouml#aggregationKind'), ...]
```

As can be seen, the result is a list of URIRefs.

3. Accessing the OntoUML Vocabulary base namespace

The `get_namespace` method is used to retrieve the namespace URI for OntoUML Vocabulary. Here is an example demonstrating how to use this method:

```python
# Getting the namespace for OntoUML
namespace_uri = OntoUML.get_namespace()

# Output
print(namespace_uri)  # https://w3id.org/ontouml#
```

These methods ease the process of working with OntoUML terms, making it intuitive to use them within your projects.

### OntoUML Constants

### OntoUML Constants

The `ontouml-vocabulary-lib` library includes a set of predefined constants that group OntoUML stereotypes into semantically relevant categories, allowing for a structured approach to accessing and utilizing OntoUML concepts in your Python programs. These constants are organized into tuples with alphabetically sorted elements. Each tuple represents a different categorization of OntoUML stereotypes.

- **Class Stereotypes**:
  - Base Sortal Class Stereotypes: `ONTOUML_BASE_SORTAL_CLASS_STEREOTYPES`
  - Ultimate Sortal Class Stereotypes: `ONTOUML_ULTIMATE_SORTAL_CLASS_STEREOTYPES`
  - Sortal Class Stereotypes: `ONTOUML_SORTAL_CLASS_STEREOTYPES`
  - Non-Sortal Class Stereotypes: `ONTOUML_NON_SORTAL_CLASS_STEREOTYPES`
  - Abstract Class Stereotypes: `ONTOUML_ABSTRACT_CLASS_STEREOTYPES`
  - Rigid Class Stereotypes: `ONTOUML_RIGID_CLASS_STEREOTYPES`
  - Anti-Rigid Class Stereotypes: `ONTOUML_ANTI_RIGID_CLASS_STEREOTYPES`
  - Semi-Rigid Class Stereotypes: `ONTOUML_SEMI_RIGID_CLASS_STEREOTYPES`
  - All Class Stereotypes: `ONTOUML_CLASS_STEREOTYPES`

- **Miscellaneous Stereotypes**:
  - Relation Stereotypes: `ONTOUML_RELATION_STEREOTYPES`
  - Property Stereotypes: `ONTOUML_PROPERTY_STEREOTYPES`
  - Aggregation Kinds: `ONTOUML_AGGREGATION_KINDS`
  - Ontological Natures: `ONTOUML_ONTOLOGICAL_NATURES`
  - Abstract Elements: `ONTOUML_ABSTRACT_ELEMENTS`
  - Concrete Elements: `ONTOUML_CONCRETE_ELEMENTS`

#### Usage Examples

In these examples, we are utilizing the `*` import statement to import all the constants from the `constants_classes` and `constants_misc` modules within the `ontouml_vocabulary_lib.constants` sub-package. Ensure you have the `ontouml-vocabulary-lib` library installed and accessible in your environment.

1. **Listing All Base Sortal Class Stereotypes**:
```python
from ontouml_vocabulary_lib.constants.constants_classes import *

# Listing all base sortal class stereotypes
print(ONTOUML_BASE_SORTAL_CLASS_STEREOTYPES)
```

Output: 
```txt
(OntoUML.historicalRole, OntoUML.phase, OntoUML.role, OntoUML.subkind)
```

2. Validating an OntoUML Concept against a Set of Stereotypes:

```python
from ontouml_vocabulary_lib.constants.constants_classes import *
from ontouml_vocabulary_lib.terms import OntoUML

# A given OntoUML Concept (Assume OntoUML.kind is of type URIRef)
given_ontouml_concept = OntoUML.kind

# Validate if it's a base sortal
is_base_sortal = given_ontouml_concept in ONTOUML_BASE_SORTAL_CLASS_STEREOTYPES

# Output the validation result
print(f"Is {given_ontouml_concept} a base sortal stereotype?")
print("Yes" if is_base_sortal else "No")
```
Output:
```txt
Is OntoUML.kind a base sortal stereotype?
No
```
3. Comparing Values between Different Sets of Stereotypes:

```python
from ontouml_vocabulary_lib.constants.constants_classes import *

# Retrieve all ultimate and base sortals
all_ultimate_sortals = ONTOUML_ULTIMATE_SORTAL_CLASS_STEREOTYPES
all_base_sortals = ONTOUML_BASE_SORTAL_CLASS_STEREOTYPES

# Find common stereotypes between ultimate and base sortals, if any
common_stereotypes = set(all_ultimate_sortals).intersection(set(all_base_sortals))

# Output common stereotypes
print("Common stereotypes between Ultimate and Base Sortals:")
print(common_stereotypes)
``````

Output:
```txt
Common stereotypes between Ultimate and Base Sortals:
{OntoUML.historicalRole, OntoUML.phase, OntoUML.role, OntoUML.subkind}
```

4. Listing All Relation Stereotypes:
```python
from ontouml_vocabulary_lib.constants.constants_misc import *

# Listing all relation stereotypes
print(ONTOUML_RELATION_STEREOTYPES)
```
Output:
```txt
(OntoUML.bringsAbout, OntoUML.characterization, OntoUML.comparative, OntoUML.componentOf, OntoUML.creation, OntoUML.derivation, OntoUML.externalDependence, OntoUML.historicalDependence, OntoUML.instantiation, OntoUML.manifestation, OntoUML.material, OntoUML.mediation, OntoUML.memberOf, OntoUML.participation, OntoUML.participational, OntoUML.subCollectionOf, OntoUML.subQuantityOf, OntoUML.termination, OntoUML.triggers)
```


### OntoUML Exceptions

This document provides a detailed explanation of the custom exceptions used in the handling and management of OntoUML graphs and related operations. These custom exceptions are designed to provide explicit and user-friendly error messages, assisting developers in debugging and resolving issues.

For the current version, a single custom exception is defined.

- **OUUnavailableTerm**: Raised when an OUTerm is not available or does not exist in the OntoUML Vocabulary.

## Code Testing

The provided code was substantially tested. Tests can be accessed in the 'tests' folder and executed from within the project folder as follows:

```bash
ontouml-vocabulary-lib> pytest .\ontouml_vocabulary_lib\tests
```

## How to Contribute

### Report Issues

- Report bugs or suggest features by [opening an issue](https://github.com/OntoUML/ontouml-vocabulary-lib/issues/new).
- Point out any discrepancies in the AI-generated documentation by [opening an issue](https://github.com/OntoUML/ontouml-vocabulary-lib/issues/new).

### Code Contribution

1. Fork the Repository: Fork the project repository and create your feature branch: `git checkout -b feature/YourFeatureName`.
2. Commit Changes: Make and commit your changes with meaningful commit messages.
3. Push to Branch: Push your work back up to your fork: `git push origin feature/YourFeatureName`.
4. Submit a Pull Request: Open a pull request to merge your feature branch into the main project repository.

### Test Contribution

- Improve reliability by adding or enhancing tests.

### General Guidelines

- Ensure your code adheres to our coding standards.
- Update documentation as needed.
- Ensure that your code does not introduce additional issues.

Thank you for investing your time and expertise into this project!

## Author

This project is maintained by the [Semantics, Cybersecurity & Services (SCS) Group](https://www.utwente.nl/en/eemcs/scs/) of the [University of Twente](https://www.utwente.nl/), The Netherlands. Its developer is:

- [Pedro Paulo Favato Barcelos](https://orcid.org/0000-0003-2736-7817) [[GitHub](https://github.com/pedropaulofb)] [[LinkedIn](https://www.linkedin.com/in/pedro-paulo-favato-barcelos/)]

Feel free to get in touch using the provided links. For questions, contributions, or to report any problem, you can **[open an issue](https://github.com/OntoUML/ontouml-vocabulary-lib/issues/new)** at this repository.
