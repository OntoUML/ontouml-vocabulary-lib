"""This module defines various tuples of OntoUML Class Stereotypes used in OntoUML modeling.

Each tuple represents a specific grouping of stereotypes, providing a structured and
semantically relevant means to access and utilize the stereotypes in OntoUML modeling.

All tuples are provided sorted in alphabetical order.
"""
from ..terms import OntoUML

ONTOUML_BASE_SORTAL_CLASS_STEREOTYPES = (
    OntoUML.historicalRole,
    OntoUML.phase,
    OntoUML.role,
    OntoUML.subkind,
)


ONTOUML_ULTIMATE_SORTAL_CLASS_STEREOTYPES = (
    OntoUML.collective,
    OntoUML.kind,
    OntoUML.mode,
    OntoUML.quality,
    OntoUML.quantity,
    OntoUML.relator,
    OntoUML.type,
)


ONTOUML_SORTAL_CLASS_STEREOTYPES = (
    OntoUML.collective,
    OntoUML.historicalRole,
    OntoUML.kind,
    OntoUML.mode,
    OntoUML.phase,
    OntoUML.quality,
    OntoUML.quantity,
    OntoUML.relator,
    OntoUML.role,
    OntoUML.subkind,
    OntoUML.type,
)


ONTOUML_NON_SORTAL_CLASS_STEREOTYPES = (
    OntoUML.category,
    OntoUML.historicalRoleMixin,
    OntoUML.mixin,
    OntoUML.phaseMixin,
    OntoUML.roleMixin,
)


ONTOUML_ABSTRACT_CLASS_STEREOTYPES = (
    OntoUML.abstract,
    OntoUML.datatype,
    OntoUML.enumeration,
)


ONTOUML_RIGID_CLASS_STEREOTYPES = (
    OntoUML.category,
    OntoUML.collective,
    OntoUML.kind,
    OntoUML.mode,
    OntoUML.quality,
    OntoUML.quantity,
    OntoUML.relator,
    OntoUML.subkind,
)


ONTOUML_ANTI_RIGID_CLASS_STEREOTYPES = (
    OntoUML.historicalRole,
    OntoUML.historicalRoleMixin,
    OntoUML.phase,
    OntoUML.phaseMixin,
    OntoUML.role,
    OntoUML.roleMixin,
)


# The comma ensures that Python will understand the following as a tuple
ONTOUML_SEMI_RIGID_CLASS_STEREOTYPES = (OntoUML.mixin,)


ONTOUML_CLASS_STEREOTYPES = (
    OntoUML.abstract,
    OntoUML.category,
    OntoUML.collective,
    OntoUML.datatype,
    OntoUML.enumeration,
    OntoUML.event,
    OntoUML.historicalRole,
    OntoUML.historicalRoleMixin,
    OntoUML.kind,
    OntoUML.mixin,
    OntoUML.mode,
    OntoUML.phase,
    OntoUML.phaseMixin,
    OntoUML.quality,
    OntoUML.quantity,
    OntoUML.relator,
    OntoUML.role,
    OntoUML.roleMixin,
    OntoUML.situation,
    OntoUML.subkind,
    OntoUML.type,
)
