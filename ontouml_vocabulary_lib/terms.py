"""Module for the ONTOUML namespace mapping to the OntoUML vocabulary.

This module defines the ONTOUML class, which serves as a convenient way to access OntoUML terms and concepts in Python
code. It complies with the OntoUML vocabulary version 1.1.0 available at https://w3id.org/ontouml/vocabulary/v1.1.0.

Usage:
    - Import the ONTOUML class from this module to access OntoUML terms with their associated URIs.
    - Use ONTOUML.term_name to access specific OntoUML terms.
    - Use ONTOUML.all() to access all OntoUML terms defined in the OntoUML Vocabulary as a list of URIRefs.

Example:
    ```
    from ontouml_namespace import ONTOUML

    my_ontouml_class = OntoUML.Class
    all_terms = OntoUML.get_list_all()

    # Results:
    my_ontouml_class: rdflib.term.URIRef('https://w3id.org/ontouml#Class')
    all_terms: [rdflib.term.URIRef('https://w3id.org/ontouml#AggregationKind'),
                rdflib.term.URIRef('https://w3id.org/ontouml#Cardinality'),
                rdflib.term.URIRef('https://w3id.org/ontouml#Class'), ...]
    ```

For more information about the OntoUML vocabulary,
refer to the official documentation at: https://w3id.org/ontouml/vocabulary
"""

from rdflib import URIRef
from rdflib.namespace import DefinedNamespace, Namespace

from .exceptions import OUUnavailableTerm


class OntoUML(DefinedNamespace):
    """Class to provide terms from the OntoUML vocabulary in an easy way.

    This class utilizes RDFLib structure for defining and accessing OntoUML terms. It provides access to OntoUML
    vocabulary terms and their associated URIs.

    It complies with the OntoUML vocabulary version 1.1.0 available at https://w3id.org/ontouml/vocabulary/v1.1.0.

    :cvar abstract: URI for OntoUML term 'abstract'
    :cvar abstractNature: URI for OntoUML term 'abstractNature'
    :cvar aggregationKind: URI for OntoUML term 'aggregationKind'
    :cvar AggregationKind: URI for OntoUML term 'AggregationKind'
    :cvar attribute: URI for OntoUML term 'attribute'
    :cvar begin: URI for OntoUML term 'begin'
    :cvar bringsAbout: URI for OntoUML term 'bringsAbout'
    :cvar cardinality: URI for OntoUML term 'cardinality'
    :cvar Cardinality: URI for OntoUML term 'Cardinality'
    :cvar cardinalityValue: URI for OntoUML term 'cardinalityValue'
    :cvar categorizer: URI for OntoUML term 'categorizer'
    :cvar category: URI for OntoUML term 'category'
    :cvar characterization: URI for OntoUML term 'characterization'
    :cvar Class: URI for OntoUML term 'Class'
    :cvar Classifier: URI for OntoUML term 'Classifier'
    :cvar ClassStereotype: URI for OntoUML term 'ClassStereotype'
    :cvar ClassView: URI for OntoUML term 'ClassView'
    :cvar collective: URI for OntoUML term 'collective'
    :cvar collectiveNature: URI for OntoUML term 'collectiveNature'
    :cvar comparative: URI for OntoUML term 'comparative'
    :cvar componentOf: URI for OntoUML term 'componentOf'
    :cvar composite: URI for OntoUML term 'composite'
    :cvar ConnectorView: URI for OntoUML term 'ConnectorView'
    :cvar containsModelElement: URI for OntoUML term 'containsModelElement'
    :cvar containsView: URI for OntoUML term 'containsView'
    :cvar creation: URI for OntoUML term 'creation'
    :cvar datatype: URI for OntoUML term 'datatype'
    :cvar DecoratableElement: URI for OntoUML term 'DecoratableElement'
    :cvar derivation: URI for OntoUML term 'derivation'
    :cvar description: URI for OntoUML term 'description'
    :cvar diagram: URI for OntoUML term 'diagram'
    :cvar Diagram: URI for OntoUML term 'Diagram'
    :cvar DiagramElement: URI for OntoUML term 'DiagramElement'
    :cvar ElementView: URI for OntoUML term 'ElementView'
    :cvar end: URI for OntoUML term 'end'
    :cvar enumeration: URI for OntoUML term 'enumeration'
    :cvar event: URI for OntoUML term 'event'
    :cvar eventNature: URI for OntoUML term 'eventNature'
    :cvar externalDependence: URI for OntoUML term 'externalDependence'
    :cvar extrinsicModeNature: URI for OntoUML term 'extrinsicModeNature'
    :cvar functionalComplexNature: URI for OntoUML term 'functionalComplexNature'
    :cvar general: URI for OntoUML term 'general'
    :cvar generalization: URI for OntoUML term 'generalization'
    :cvar Generalization: URI for OntoUML term 'Generalization'
    :cvar GeneralizationSet: URI for OntoUML term 'GeneralizationSet'
    :cvar GeneralizationSetView: URI for OntoUML term 'GeneralizationSetView'
    :cvar GeneralizationView: URI for OntoUML term 'GeneralizationView'
    :cvar height: URI for OntoUML term 'height'
    :cvar historicalDependence: URI for OntoUML term 'historicalDependence'
    :cvar historicalRole: URI for OntoUML term 'historicalRole'
    :cvar historicalRoleMixin: URI for OntoUML term 'historicalRoleMixin'
    :cvar instantiation: URI for OntoUML term 'instantiation'
    :cvar intrinsicModeNature: URI for OntoUML term 'intrinsicModeNature'
    :cvar isAbstract: URI for OntoUML term 'isAbstract'
    :cvar isComplete: URI for OntoUML term 'isComplete'
    :cvar isDerived: URI for OntoUML term 'isDerived'
    :cvar isDisjoint: URI for OntoUML term 'isDisjoint'
    :cvar isExtensional: URI for OntoUML term 'isExtensional'
    :cvar isOrdered: URI for OntoUML term 'isOrdered'
    :cvar isPowertype: URI for OntoUML term 'isPowertype'
    :cvar isReadOnly: URI for OntoUML term 'isReadOnly'
    :cvar isViewOf: URI for OntoUML term 'isViewOf'
    :cvar kind: URI for OntoUML term 'kind'
    :cvar literal: URI for OntoUML term 'literal'
    :cvar Literal: URI for OntoUML term 'Literal'
    :cvar lowerBound: URI for OntoUML term 'lowerBound'
    :cvar manifestation: URI for OntoUML term 'manifestation'
    :cvar material: URI for OntoUML term 'material'
    :cvar mediation: URI for OntoUML term 'mediation'
    :cvar memberOf: URI for OntoUML term 'memberOf'
    :cvar mixin: URI for OntoUML term 'mixin'
    :cvar mode: URI for OntoUML term 'mode'
    :cvar model: URI for OntoUML term 'model'
    :cvar ModelElement: URI for OntoUML term 'ModelElement'
    :cvar name: URI for OntoUML term 'name'
    :cvar NodeView: URI for OntoUML term 'NodeView'
    :cvar none: URI for OntoUML term 'none'
    :cvar Note: URI for OntoUML term 'Note'
    :cvar NoteView: URI for OntoUML term 'NoteView'
    :cvar OntologicalNature: URI for OntoUML term 'OntologicalNature'
    :cvar OntoumlElement: URI for OntoUML term 'OntoumlElement'
    :cvar order: URI for OntoUML term 'order'
    :cvar owner: URI for OntoUML term 'owner'
    :cvar Package: URI for OntoUML term 'Package'
    :cvar PackageView: URI for OntoUML term 'PackageView'
    :cvar participation: URI for OntoUML term 'participation'
    :cvar participational: URI for OntoUML term 'participational'
    :cvar Path: URI for OntoUML term 'Path'
    :cvar phase: URI for OntoUML term 'phase'
    :cvar phaseMixin: URI for OntoUML term 'phaseMixin'
    :cvar point: URI for OntoUML term 'point'
    :cvar Point: URI for OntoUML term 'Point'
    :cvar project: URI for OntoUML term 'project'
    :cvar Project: URI for OntoUML term 'Project'
    :cvar property: URI for OntoUML term 'property'
    :cvar Property: URI for OntoUML term 'Property'
    :cvar PropertyStereotype: URI for OntoUML term 'PropertyStereotype'
    :cvar propertyType: URI for OntoUML term 'propertyType'
    :cvar quality: URI for OntoUML term 'quality'
    :cvar qualityNature: URI for OntoUML term 'qualityNature'
    :cvar quantity: URI for OntoUML term 'quantity'
    :cvar quantityNature: URI for OntoUML term 'quantityNature'
    :cvar Rectangle: URI for OntoUML term 'Rectangle'
    :cvar RectangularShape: URI for OntoUML term 'RectangularShape'
    :cvar redefinesProperty: URI for OntoUML term 'redefinesProperty'
    :cvar Relation: URI for OntoUML term 'Relation'
    :cvar relationEnd: URI for OntoUML term 'relationEnd'
    :cvar RelationStereotype: URI for OntoUML term 'RelationStereotype'
    :cvar RelationView: URI for OntoUML term 'RelationView'
    :cvar relator: URI for OntoUML term 'relator'
    :cvar relatorNature: URI for OntoUML term 'relatorNature'
    :cvar restrictedTo: URI for OntoUML term 'restrictedTo'
    :cvar role: URI for OntoUML term 'role'
    :cvar roleMixin: URI for OntoUML term 'roleMixin'
    :cvar shape: URI for OntoUML term 'shape'
    :cvar Shape: URI for OntoUML term 'Shape'
    :cvar shared: URI for OntoUML term 'shared'
    :cvar situation: URI for OntoUML term 'situation'
    :cvar situationNature: URI for OntoUML term 'situationNature'
    :cvar sourceEnd: URI for OntoUML term 'sourceEnd'
    :cvar sourceView: URI for OntoUML term 'sourceView'
    :cvar specific: URI for OntoUML term 'specific'
    :cvar stereotype: URI for OntoUML term 'stereotype'
    :cvar Stereotype: URI for OntoUML term 'Stereotype'
    :cvar subCollectionOf: URI for OntoUML term 'subCollectionOf'
    :cvar subkind: URI for OntoUML term 'subkind'
    :cvar subQuantityOf: URI for OntoUML term 'subQuantityOf'
    :cvar subsetsProperty: URI for OntoUML term 'subsetsProperty'
    :cvar targetEnd: URI for OntoUML term 'targetEnd'
    :cvar targetView: URI for OntoUML term 'targetView'
    :cvar termination: URI for OntoUML term 'termination'
    :cvar text: URI for OntoUML term 'text'
    :cvar Text: URI for OntoUML term 'Text'
    :cvar topLeftPosition: URI for OntoUML term 'topLeftPosition'
    :cvar triggers: URI for OntoUML term 'triggers'
    :cvar type: URI for OntoUML term 'type'
    :cvar typeNature: URI for OntoUML term 'typeNature'
    :cvar upperBound: URI for OntoUML term 'upperBound'
    :cvar width: URI for OntoUML term 'width'
    :cvar xCoordinate: URI for OntoUML term 'xCoordinate'
    :cvar yCoordinate: URI for OntoUML term 'yCoordinate'

    :cvar _fail: Flag indicating whether failed lookups should raise an exception.
    :cvar _NS: Namespace for the OntoUML vocabulary.

    """

    abstract: URIRef  # https://w3id.org/ontouml#abstract
    abstractNature: URIRef  # https://w3id.org/ontouml#abstractNature
    aggregationKind: URIRef  # https://w3id.org/ontouml#aggregationKind
    AggregationKind: URIRef  # https://w3id.org/ontouml#AggregationKind
    attribute: URIRef  # https://w3id.org/ontouml#attribute
    begin: URIRef  # https://w3id.org/ontouml#begin
    bringsAbout: URIRef  # https://w3id.org/ontouml#bringsAbout
    cardinality: URIRef  # https://w3id.org/ontouml#cardinality
    Cardinality: URIRef  # https://w3id.org/ontouml#Cardinality
    cardinalityValue: URIRef  # https://w3id.org/ontouml#cardinalityValue
    categorizer: URIRef  # https://w3id.org/ontouml#categorizer
    category: URIRef  # https://w3id.org/ontouml#category
    characterization: URIRef  # https://w3id.org/ontouml#characterization
    Class: URIRef  # https://w3id.org/ontouml#Class
    Classifier: URIRef  # https://w3id.org/ontouml#Classifier
    ClassStereotype: URIRef  # https://w3id.org/ontouml#ClassStereotype
    ClassView: URIRef  # https://w3id.org/ontouml#ClassView
    collective: URIRef  # https://w3id.org/ontouml#collective
    collectiveNature: URIRef  # https://w3id.org/ontouml#collectiveNature
    comparative: URIRef  # https://w3id.org/ontouml#comparative
    componentOf: URIRef  # https://w3id.org/ontouml#componentOf
    composite: URIRef  # https://w3id.org/ontouml#composite
    ConnectorView: URIRef  # https://w3id.org/ontouml#ConnectorView
    containsModelElement: URIRef  # https://w3id.org/ontouml#containsModelElement
    containsView: URIRef  # https://w3id.org/ontouml#containsView
    creation: URIRef  # https://w3id.org/ontouml#creation
    datatype: URIRef  # https://w3id.org/ontouml#datatype
    DecoratableElement: URIRef  # https://w3id.org/ontouml#DecoratableElement
    derivation: URIRef  # https://w3id.org/ontouml#derivation
    description: URIRef  # https://w3id.org/ontouml#description
    diagram: URIRef  # https://w3id.org/ontouml#diagram
    Diagram: URIRef  # https://w3id.org/ontouml#Diagram
    DiagramElement: URIRef  # https://w3id.org/ontouml#DiagramElement
    ElementView: URIRef  # https://w3id.org/ontouml#ElementView
    end: URIRef  # https://w3id.org/ontouml#end
    enumeration: URIRef  # https://w3id.org/ontouml#enumeration
    event: URIRef  # https://w3id.org/ontouml#event
    eventNature: URIRef  # https://w3id.org/ontouml#eventNature
    externalDependence: URIRef  # https://w3id.org/ontouml#externalDependence
    extrinsicModeNature: URIRef  # https://w3id.org/ontouml#extrinsicModeNature
    functionalComplexNature: URIRef  # https://w3id.org/ontouml#functionalComplexNature
    general: URIRef  # https://w3id.org/ontouml#general
    generalization: URIRef  # https://w3id.org/ontouml#generalization
    Generalization: URIRef  # https://w3id.org/ontouml#Generalization
    GeneralizationSet: URIRef  # https://w3id.org/ontouml#GeneralizationSet
    GeneralizationSetView: URIRef  # https://w3id.org/ontouml#GeneralizationSetView
    GeneralizationView: URIRef  # https://w3id.org/ontouml#GeneralizationView
    height: URIRef  # https://w3id.org/ontouml#height
    historicalDependence: URIRef  # https://w3id.org/ontouml#historicalDependence
    historicalRole: URIRef  # https://w3id.org/ontouml#historicalRole
    historicalRoleMixin: URIRef  # https://w3id.org/ontouml#historicalRoleMixin
    instantiation: URIRef  # https://w3id.org/ontouml#instantiation
    intrinsicModeNature: URIRef  # https://w3id.org/ontouml#intrinsicModeNature
    isAbstract: URIRef  # https://w3id.org/ontouml#isAbstract
    isComplete: URIRef  # https://w3id.org/ontouml#isComplete
    isDerived: URIRef  # https://w3id.org/ontouml#isDerived
    isDisjoint: URIRef  # https://w3id.org/ontouml#isDisjoint
    isExtensional: URIRef  # https://w3id.org/ontouml#isExtensional
    isOrdered: URIRef  # https://w3id.org/ontouml#isOrdered
    isPowertype: URIRef  # https://w3id.org/ontouml#isPowertype
    isReadOnly: URIRef  # https://w3id.org/ontouml#isReadOnly
    isViewOf: URIRef  # https://w3id.org/ontouml#isViewOf
    kind: URIRef  # https://w3id.org/ontouml#kind
    literal: URIRef  # https://w3id.org/ontouml#literal
    Literal: URIRef  # https://w3id.org/ontouml#Literal
    lowerBound: URIRef  # https://w3id.org/ontouml#lowerBound
    manifestation: URIRef  # https://w3id.org/ontouml#manifestation
    material: URIRef  # https://w3id.org/ontouml#material
    mediation: URIRef  # https://w3id.org/ontouml#mediation
    memberOf: URIRef  # https://w3id.org/ontouml#memberOf
    mixin: URIRef  # https://w3id.org/ontouml#mixin
    mode: URIRef  # https://w3id.org/ontouml#mode
    model: URIRef  # https://w3id.org/ontouml#model
    ModelElement: URIRef  # https://w3id.org/ontouml#ModelElement
    name: URIRef  # https://w3id.org/ontouml#name
    NodeView: URIRef  # https://w3id.org/ontouml#NodeView
    none: URIRef  # https://w3id.org/ontouml#none
    Note: URIRef  # https://w3id.org/ontouml#Note
    NoteView: URIRef  # https://w3id.org/ontouml#NoteView
    OntologicalNature: URIRef  # https://w3id.org/ontouml#OntologicalNature
    OntoumlElement: URIRef  # https://w3id.org/ontouml#OntoumlElement
    order: URIRef  # https://w3id.org/ontouml#order
    owner: URIRef  # https://w3id.org/ontouml#owner
    Package: URIRef  # https://w3id.org/ontouml#Package
    PackageView: URIRef  # https://w3id.org/ontouml#PackageView
    participation: URIRef  # https://w3id.org/ontouml#participation
    participational: URIRef  # https://w3id.org/ontouml#participational
    Path: URIRef  # https://w3id.org/ontouml#Path
    phase: URIRef  # https://w3id.org/ontouml#phase
    phaseMixin: URIRef  # https://w3id.org/ontouml#phaseMixin
    point: URIRef  # https://w3id.org/ontouml#point
    Point: URIRef  # https://w3id.org/ontouml#Point
    project: URIRef  # https://w3id.org/ontouml#project
    Project: URIRef  # https://w3id.org/ontouml#Project
    property: URIRef  # https://w3id.org/ontouml#property
    Property: URIRef  # https://w3id.org/ontouml#Property
    PropertyStereotype: URIRef  # https://w3id.org/ontouml#PropertyStereotype
    propertyType: URIRef  # https://w3id.org/ontouml#propertyType
    quality: URIRef  # https://w3id.org/ontouml#quality
    qualityNature: URIRef  # https://w3id.org/ontouml#qualityNature
    quantity: URIRef  # https://w3id.org/ontouml#quantity
    quantityNature: URIRef  # https://w3id.org/ontouml#quantityNature
    Rectangle: URIRef  # https://w3id.org/ontouml#Rectangle
    RectangularShape: URIRef  # https://w3id.org/ontouml#RectangularShape
    redefinesProperty: URIRef  # https://w3id.org/ontouml#redefinesProperty
    Relation: URIRef  # https://w3id.org/ontouml#Relation
    relationEnd: URIRef  # https://w3id.org/ontouml#relationEnd
    RelationStereotype: URIRef  # https://w3id.org/ontouml#RelationStereotype
    RelationView: URIRef  # https://w3id.org/ontouml#RelationView
    relator: URIRef  # https://w3id.org/ontouml#relator
    relatorNature: URIRef  # https://w3id.org/ontouml#relatorNature
    restrictedTo: URIRef  # https://w3id.org/ontouml#restrictedTo
    role: URIRef  # https://w3id.org/ontouml#role
    roleMixin: URIRef  # https://w3id.org/ontouml#roleMixin
    shape: URIRef  # https://w3id.org/ontouml#shape
    Shape: URIRef  # https://w3id.org/ontouml#Shape
    shared: URIRef  # https://w3id.org/ontouml#shared
    situation: URIRef  # https://w3id.org/ontouml#situation
    situationNature: URIRef  # https://w3id.org/ontouml#situationNature
    sourceEnd: URIRef  # https://w3id.org/ontouml#sourceEnd
    sourceView: URIRef  # https://w3id.org/ontouml#sourceView
    specific: URIRef  # https://w3id.org/ontouml#specific
    stereotype: URIRef  # https://w3id.org/ontouml#stereotype
    Stereotype: URIRef  # https://w3id.org/ontouml#Stereotype
    subCollectionOf: URIRef  # https://w3id.org/ontouml#subCollectionOf
    subkind: URIRef  # https://w3id.org/ontouml#subkind
    subQuantityOf: URIRef  # https://w3id.org/ontouml#subQuantityOf
    subsetsProperty: URIRef  # https://w3id.org/ontouml#subsetsProperty
    targetEnd: URIRef  # https://w3id.org/ontouml#targetEnd
    targetView: URIRef  # https://w3id.org/ontouml#targetView
    termination: URIRef  # https://w3id.org/ontouml#termination
    text: URIRef  # https://w3id.org/ontouml#text
    Text: URIRef  # https://w3id.org/ontouml#Text
    topLeftPosition: URIRef  # https://w3id.org/ontouml#topLeftPosition
    triggers: URIRef  # https://w3id.org/ontouml#triggers
    type: URIRef  # https://w3id.org/ontouml#type
    typeNature: URIRef  # https://w3id.org/ontouml#typeNature
    upperBound: URIRef  # https://w3id.org/ontouml#upperBound
    width: URIRef  # https://w3id.org/ontouml#width
    xCoordinate: URIRef  # https://w3id.org/ontouml#xCoordinate
    yCoordinate: URIRef  # https://w3id.org/ontouml#yCoordinate

    _fail = True

    _NS = Namespace("https://w3id.org/ontouml#")  # has type RDFLib.Namespace.

    @classmethod
    def get_list_all(cls) -> list[URIRef]:
        """Retrieve a list of all public attributes of the OntoUML class, i.e., all terms contained in the OntoUML \
        Vocabulary.

        This method uses introspection to find all attributes and methods of the OntoUML
        class that do not begin with an underscore (which by convention are considered private),
        and returns a list containing the names of these attributes and methods.

        :return: A list containing the names of all public attributes and methods of the OntoUML class.
        :rtype: list[URIRef]
        """
        all_dict = {k: getattr(OntoUML, k) for k in dir(OntoUML) if not k.startswith("_")}
        return list(all_dict.keys())

    @classmethod
    def get_namespace(cls) -> str:
        """Retrieve the OntoUML namespace URI.

        This method returns the OntoUML namespace URI as a string.
        The namespace URI is a prefix that can be used to construct full URIs for terms in the OntoUML vocabulary.

        Usage example:

            ```
            ns = OntoUML.get_namespace()
            ```

        :return: The OntoUML namespace URI as a string.
        :rtype: str
        """
        # The OntoUML namespace URI. This constant defines the URI for the OntoUML namespace used in RDF triples.
        return str(cls._NS)

    @classmethod
    def get_term(cls, str_term: str) -> URIRef:
        """Retrieve the URIRef of a term from the OntoUML vocabulary.

        Given a term name as a string, this method retrieves its associated URIRef from the OntoUML vocabulary. The
        method ensures compliance with OntoUML vocabulary version 1.1.0. If the term is unavailable or nonexistent,
        an exception is raised.

        :param str_term: The name of the OntoUML term to retrieve.
        :type str_term: str
        :return: URIRef associated with the specified OntoUML term.
        :rtype: URIRef
        :raises OUUnavailableOUTerm: If the term is not available in the OntoUML vocabulary.

        Example:
            ```
            from ontouml_namespace import OntoUML

            try:
                my_term = OntoUML.get_term('Class')
                # Result: rdflib.term.URIRef('https://w3id.org/ontouml#Class')
            except OUUnavailableOUTerm:
                print("Specified term is not available in OntoUML vocabulary.")
            ```
        """
        for term in dir(cls):
            if str_term == term.fragment:
                return term
        else:
            raise OUUnavailableTerm(str_term)
