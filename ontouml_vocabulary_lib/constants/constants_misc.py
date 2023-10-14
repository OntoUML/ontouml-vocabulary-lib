"""This module defines various tuples of OntoUML Stereotypes related to relations, properties, \
aggregation kinds, ontological natures, and general elements, which are utilized in OntoUML modeling.

Each tuple groups related stereotypes, offering a structured and semantically relevant method
for utilizing OntoUML stereotypes in model construction and verification.

All tuples are provided sorted in alphabetical order.
"""
from ..terms import OntoUML

ONTOUML_RELATION_STEREOTYPES = (
    OntoUML.bringsAbout,
    OntoUML.characterization,
    OntoUML.comparative,
    OntoUML.componentOf,
    OntoUML.creation,
    OntoUML.derivation,
    OntoUML.externalDependence,
    OntoUML.historicalDependence,
    OntoUML.instantiation,
    OntoUML.manifestation,
    OntoUML.material,
    OntoUML.mediation,
    OntoUML.memberOf,
    OntoUML.participation,
    OntoUML.participational,
    OntoUML.subCollectionOf,
    OntoUML.subQuantityOf,
    OntoUML.termination,
    OntoUML.triggers,
)


ONTOUML_PROPERTY_STEREOTYPES = (
    OntoUML.begin,
    OntoUML.end,
)


ONTOUML_AGGREGATION_KINDS = (
    OntoUML.composite,
    OntoUML.none,
    OntoUML.shared,
)


ONTOUML_ONTOLOGICAL_NATURES = (
    OntoUML.abstractNature,
    OntoUML.collectiveNature,
    OntoUML.eventNature,
    OntoUML.extrinsicModeNature,
    OntoUML.functionalComplexNature,
    OntoUML.intrinsicModeNature,
    OntoUML.qualityNature,
    OntoUML.quantityNature,
    OntoUML.relatorNature,
    OntoUML.situationNature,
    OntoUML.typeNature,
)


ONTOUML_ABSTRACT_ELEMENTS = (
    OntoUML.Cardinality,
    OntoUML.Class,
    OntoUML.Diagram,
    OntoUML.Generalization,
    OntoUML.GeneralizationSet,
    OntoUML.Literal,
    OntoUML.Note,
    OntoUML.Package,
    OntoUML.Project,
    OntoUML.Property,
    OntoUML.Relation,
)


ONTOUML_CONCRETE_ELEMENTS = (
    OntoUML.ClassView,
    OntoUML.GeneralizationSetView,
    OntoUML.GeneralizationView,
    OntoUML.NoteView,
    OntoUML.PackageView,
    OntoUML.Path,
    OntoUML.Point,
    OntoUML.Rectangle,
    OntoUML.RelationView,
    OntoUML.Text,
)
