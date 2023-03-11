import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class CustomPart:
    '''Represents a custom (arbitrary content) part, that is not defined by the ISO/IEC 29500 standard.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.
    
    This class represents an OOXML part that is a target of an "unknown relationship".
    All relationships not defined within ISO/IEC 29500 are considered "unknown relationships".
    Unknown relationships are permitted within an Office Open XML document provided that they
    conform to relationship markup guidelines.
    
    Microsoft Word preserves custom parts during open/save cycles. Some additional info can be found
    here http://blogs.msdn.com/dmahugh/archive/2006/11/25/arbitrary-content-in-an-opc-package.aspx
    
    Aspose.Words also roundtrips custom parts and in addition, allows to programmatically access
    such parts via the :class:`CustomPart` and :class:`CustomPartCollection` objects.
    
    Do not confuse custom parts with Custom XML Data. Use :class:`CustomXmlPart` if you need
    to access Custom XML Data.'''
    
    def __init__(self):
        ...
    
    def clone(self) -> aspose.words.markup.CustomPart:
        '''Makes a "deep enough" copy of the object.
        Does not duplicate the bytes of the :attr:`CustomPart.data` value.'''
        ...
    
    @property
    def name(self) -> str:
        '''Gets or sets this part's absolute name within the OOXML package or the target URL.
        
        If the relationship target is internal, then this property is the absolute part name within the package.
        If the relationship target is external, then this property is the target URL.
        
        The default value is an empty string. A valid value must be a non-empty string.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def relationship_type(self) -> str:
        '''Gets or sets the relationship type from the parent part to this custom part.
        
        The relationship type for a custom part must be "unknown" e.g. a custom relationship type,
        not one of the relationship types defined within ISO/IEC 29500.
        
        The default value is an empty string. A valid value must be a non-empty string.'''
        ...
    
    @relationship_type.setter
    def relationship_type(self, value: str):
        ...
    
    @property
    def is_external(self) -> bool:
        '''False if this custom part is stored inside the OOXML package. True if this custom part is an external target.
        
        The default value is ``False``.'''
        ...
    
    @is_external.setter
    def is_external(self, value: bool):
        ...
    
    @property
    def content_type(self) -> str:
        '''Specifies the content type of this custom part.
        
        This property is applicable only when :attr:`CustomPart.is_external` is ``False``.
        
        The default value is an empty string. A valid value must be a non-empty string.'''
        ...
    
    @content_type.setter
    def content_type(self, value: str):
        ...
    
    @property
    def data(self) -> bytes:
        '''Contains the data of this custom part.
        
        This property is applicable only when :attr:`CustomPart.is_external` is ``False``.
        
        The default value is an empty byte array. The value cannot be ``None``.'''
        ...
    
    @data.setter
    def data(self, value: bytes):
        ...
    
    ...

class CustomPartCollection:
    '''Represents a collection of :class:`CustomPart` objects.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.
    
    You do not normally need to create instances of this class. You access custom parts
    related to the OOXML package via the :attr:`aspose.words.Document.package_custom_parts` property.'''
    
    def __init__(self):
        ...
    
    def __getitem__(self, index: int) -> aspose.words.markup.CustomPart:
        '''Gets or sets an item at the specified index.
        
        :param index: Zero-based index of the item.'''
        ...
    
    def __setitem__(self, index: int, value: aspose.words.markup.CustomPart):
        ...
    
    def add(self, part: aspose.words.markup.CustomPart) -> None:
        '''Adds an item to the collection.
        
        :param part: The item to add.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes an item at the specified index.
        
        :param index: The zero based index.'''
        ...
    
    def clear(self) -> None:
        '''Removes all elements from the collection.'''
        ...
    
    def clone(self) -> aspose.words.markup.CustomPartCollection:
        '''Makes a deep copy of this collection and its items.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of elements contained in the collection.'''
        ...
    
    ...

class CustomXmlPart:
    '''Represents a Custom XML Data Storage Part (custom XML data within a package).
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.
    
    A DOCX or DOC document can contain one or more Custom XML Data Storage parts. Aspose.Words preserves and
    allows to create and extract Custom XML Data via the :attr:`aspose.words.Document.custom_xml_parts` collection.'''
    
    def __init__(self):
        ...
    
    def clone(self) -> aspose.words.markup.CustomXmlPart:
        '''Makes a "deep enough" copy of the object.
        Does not duplicate the bytes of the :attr:`CustomXmlPart.data` value.'''
        ...
    
    @property
    def id(self) -> str:
        '''Gets or sets the string that identifies this custom XML part within an OOXML document.
        
        ISO/IEC 29500 specifies that this value is a GUID, but old versions of Microsoft Word allowed any
        string here. Aspose.Words does the same for ECMA-376 format. But note, that Microsoft Word Online fails
        to open a document created with a non-GUID value. So, a GUID is preferred value for this property.
        
        A valid value must be an identifier that is unique among all custom XML data parts in this document.
        
        The default value is an empty string. The value cannot be ``None``.'''
        ...
    
    @id.setter
    def id(self, value: str):
        ...
    
    @property
    def schemas(self) -> aspose.words.markup.CustomXmlSchemaCollection:
        '''Specifies the set of XML schemas that are associated with this custom XML part.'''
        ...
    
    @property
    def data(self) -> bytes:
        '''Gets or sets the XML content of this Custom XML Data Storage Part.
        
        The default value is an empty byte array. The value cannot be ``None``.'''
        ...
    
    @data.setter
    def data(self, value: bytes):
        ...
    
    @property
    def data_checksum(self) -> int:
        '''Specifies a cyclic redundancy check (CRC) checksum of the :attr:`CustomXmlPart.data` content.'''
        ...
    
    ...

class CustomXmlPartCollection:
    '''Represents a collection of Custom XML Parts. The items are :class:`CustomXmlPart` objects.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.
    
    You do not normally need to create instances of this class. You can access custom XML data
    stored in a document via the :attr:`aspose.words.Document.custom_xml_parts` property.'''
    
    def __init__(self):
        ...
    
    def __getitem__(self, index: int) -> aspose.words.markup.CustomXmlPart:
        '''Gets or sets an item at the specified index.
        
        :param index: Zero-based index of the item.'''
        ...
    
    def __setitem__(self, index: int, value: aspose.words.markup.CustomXmlPart):
        ...
    
    @overload
    def add(self, part: aspose.words.markup.CustomXmlPart) -> None:
        '''Adds an item to the collection.
        
        :param part: The custom XML part to add.'''
        ...
    
    @overload
    def add(self, id: str, xml: str) -> aspose.words.markup.CustomXmlPart:
        '''Creates a new XML part with the specified XML and adds it to the collection.
        
        :param id: Identifier of a new custom XML part.
        :param xml: XML data of the part.
        :returns: Created custom XML part.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes an item at the specified index.
        
        :param index: The zero based index.'''
        ...
    
    def clear(self) -> None:
        '''Removes all elements from the collection.'''
        ...
    
    def get_by_id(self, id: str) -> aspose.words.markup.CustomXmlPart:
        '''Finds and returns a custom XML part by its identifier.
        
        :param id: Case-sensitive string that identifies the custom XML part.
        :returns: Returns ``None`` if a custom XML part with the specified identifier is not found.'''
        ...
    
    def clone(self) -> aspose.words.markup.CustomXmlPartCollection:
        '''Makes a deep copy of this collection and its items.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of elements contained in the collection.'''
        ...
    
    ...

class CustomXmlProperty:
    '''Represents a single custom XML attribute or a smart tag property.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.
    
    Used as an item of a :class:`CustomXmlPropertyCollection` collection.'''
    
    def __init__(self, name: str, uri: str, value: str):
        '''Initializes a new instance of this class.
        
        :param name: The name of the property. Cannot be ``None``.
        :param uri: The namespace URI of the property. Cannot be ``None``.
        :param value: The value of the property. Cannot be ``None``.'''
        ...
    
    @property
    def name(self) -> str:
        '''Specifies the name of the custom XML attribute or smart tag property.
        
        Cannot be ``None``.
        
        Default is empty string.'''
        ...
    
    @property
    def uri(self) -> str:
        '''Gets or sets the namespace URI of the custom XML attribute or smart tag property.
        
        Cannot be ``None``.
        
        Default is empty string.'''
        ...
    
    @uri.setter
    def uri(self, value: str):
        ...
    
    @property
    def value(self) -> str:
        '''Gets or sets the value of the custom XML attribute or smart tag property.
        
        Cannot be ``None``.
        
        Default is empty string.'''
        ...
    
    @value.setter
    def value(self, value: str):
        ...
    
    ...

class CustomXmlPropertyCollection:
    '''Represents a collection of custom XML attributes or smart tag properties.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.
    
    Items are :class:`CustomXmlProperty` objects.'''
    
    def __getitem__(self, index: int) -> aspose.words.markup.CustomXmlProperty:
        '''Gets a property at the specified index.
        
        :param index: Zero-based index of the property.'''
        ...
    
    def get_by_name(self, name: str) -> aspose.words.markup.CustomXmlProperty:
        '''Gets a property with the specified name.'''
        ...
    
    def add(self, property: aspose.words.markup.CustomXmlProperty) -> None:
        '''Adds a property to the collection.
        
        :param property: The property to add.'''
        ...
    
    def contains(self, name: str) -> bool:
        '''Determines whether the collection contains a property with the given name.
        
        :param name: Case-sensitive name of the property to locate.
        :returns: ``True`` if the item is found in the collection; otherwise, ``False``.'''
        ...
    
    def index_of_key(self, name: str) -> int:
        '''Returns the zero-based index of the specified property in the collection.
        
        :param name: The case-sensitive name of the property.
        :returns: The zero based index. Negative value if not found.'''
        ...
    
    def remove(self, name: str) -> None:
        '''Removes a property with the specified name from the collection.
        
        :param name: The case-sensitive name of the property.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes a property at the specified index.
        
        :param index: The zero based index.'''
        ...
    
    def clear(self) -> None:
        '''Removes all elements from the collection.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of elements contained in the collection.'''
        ...
    
    ...

class CustomXmlSchemaCollection:
    '''A collection of strings that represent XML schemas that are associated with a custom XML part.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.
    
    You do not create instances of this class. You access the collection of XML schemas of a custom XML part
    via the :attr:`CustomXmlPart.schemas` property.'''
    
    def __getitem__(self, index: int) -> str:
        '''Gets or sets the element at the specified index.'''
        ...
    
    def __setitem__(self, index: int, value: str):
        ...
    
    def add(self, value: str) -> None:
        '''Adds an item to the collection.
        
        :param value: The item to add.'''
        ...
    
    def index_of(self, value: str) -> int:
        '''Returns the zero-based index of the specified value in the collection.
        
        :param value: The case-sensitive value to locate.
        :returns: The zero based index. Negative value if not found.'''
        ...
    
    def remove(self, name: str) -> None:
        '''Removes the specified value from the collection.
        
        :param name: The case-sensitive value to remove.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes a value at the specified index.
        
        :param index: The zero based index.'''
        ...
    
    def clear(self) -> None:
        '''Removes all elements from the collection.'''
        ...
    
    def clone(self) -> aspose.words.markup.CustomXmlSchemaCollection:
        '''Makes a deep clone of this object.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of elements contained in the collection.'''
        ...
    
    ...

class IStructuredDocumentTag:
    '''Interface to define a common data for :class:`StructuredDocumentTag` and :class:`StructuredDocumentTagRangeStart`.'''
    
    def is_ranged(self) -> bool:
        '''Returns true if this instance is a ranged structured document tag.'''
        ...
    
    def structured_document_tag_node(self) -> aspose.words.Node:
        '''Returns Node object that implements this interface.'''
        ...
    
    @property
    def id(self) -> int:
        '''Specifies a unique read-only persistent numerical Id for this **SDT**.'''
        ...
    
    @property
    def tag(self) -> str:
        '''Specifies a tag associated with the current SDT node.
        Can not be null.'''
        ...
    
    @tag.setter
    def tag(self, value: str):
        ...
    
    @property
    def title(self) -> str:
        '''Specifies the friendly name associated with this **SDT**.
        Can not be null.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...
    
    @property
    def placeholder(self) -> aspose.words.buildingblocks.BuildingBlock:
        '''Gets the :class:`aspose.words.buildingblocks.BuildingBlock` containing placeholder text which should be displayed when this SDT run contents are empty,
        the associated mapped XML element is empty as specified via the :attr:`IStructuredDocumentTag.xml_mapping` element
        or the :attr:`IStructuredDocumentTag.is_showing_placeholder_text` element is true.
        
        Can be null, meaning that the placeholder is not applicable for this Sdt.'''
        ...
    
    @property
    def placeholder_name(self) -> str:
        '''Gets or sets Name of the :class:`aspose.words.buildingblocks.BuildingBlock` containing placeholder text.
        
        BuildingBlock with this name :attr:`aspose.words.buildingblocks.BuildingBlock.name` has to be present in the :attr:`aspose.words.Document.glossary_document`
        otherwise System.InvalidOperationException will occur.'''
        ...
    
    @placeholder_name.setter
    def placeholder_name(self, value: str):
        ...
    
    @property
    def is_showing_placeholder_text(self) -> bool:
        '''Specifies whether the content of this **SDT** shall be interpreted to contain placeholder text
        (as opposed to regular text contents within the SDT).
        
        if set to true, this state shall be resumed (showing placeholder text) upon opening this document.'''
        ...
    
    @is_showing_placeholder_text.setter
    def is_showing_placeholder_text(self, value: bool):
        ...
    
    @property
    def level(self) -> aspose.words.markup.MarkupLevel:
        '''Gets the level at which this **SDT** occurs in the document tree.'''
        ...
    
    @property
    def sdt_type(self) -> aspose.words.markup.SdtType:
        '''Gets type of this **Structured document tag**.'''
        ...
    
    @property
    def lock_content_control(self) -> bool:
        '''When set to true, this property will prohibit a user from deleting this **SDT**.'''
        ...
    
    @lock_content_control.setter
    def lock_content_control(self, value: bool):
        ...
    
    @property
    def lock_contents(self) -> bool:
        '''When set to true, this property will prohibit a user from editing the contents of this **SDT**.'''
        ...
    
    @lock_contents.setter
    def lock_contents(self, value: bool):
        ...
    
    @property
    def color(self) -> aspose.pydrawing.Color:
        '''Gets or sets the color of the structured document tag.'''
        ...
    
    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def xml_mapping(self) -> aspose.words.markup.XmlMapping:
        '''Gets an object that represents the mapping of this structured document tag to XML data
        in a custom XML part of the current document.
        
        You can use the :meth:`XmlMapping.set_mapping` method of this object to map
        a structured document tag to XML data.'''
        ...
    
    @property
    def word_open_xml(self) -> str:
        '''Gets a string that represents the XML contained within the node in the :attr:`aspose.words.SaveFormat.FLAT_OPC` format.'''
        ...
    
    ...

class SdtListItem:
    '''This element specifies a single list item within a parent :attr:`SdtType.COMBO_BOX` or :attr:`SdtType.DROP_DOWN_LIST` structured document tag.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.'''
    
    @overload
    def __init__(self, display_text: str, value: str):
        '''Initializes a new instance of this class.'''
        ...
    
    @overload
    def __init__(self, value: str):
        '''Initializes a new instance of this class.'''
        ...
    
    @property
    def display_text(self) -> str:
        '''Gets the text to display in the run content in place of the :attr:`SdtListItem.value` attribute contents for this list item.
        
        Cannot be ``None`` and cannot be an empty string.'''
        ...
    
    @property
    def value(self) -> str:
        '''Gets the value of this list item.
        
        Cannot be ``None`` and cannot be an empty string.'''
        ...
    
    ...

class SdtListItemCollection:
    '''Provides access to :class:`SdtListItem` elements of a structured document tag.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.markup.SdtListItem:
        '''Returns a :class:`SdtListItem` object given its zero-based index in the collection.'''
        ...
    
    def add(self, item: aspose.words.markup.SdtListItem) -> None:
        '''Adds an item to this collection.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes a list item at the specified index.
        
        :param index: The zero-based index of the item to remove.'''
        ...
    
    def clear(self) -> None:
        '''Clears all items from this collection.'''
        ...
    
    @property
    def selected_value(self) -> aspose.words.markup.SdtListItem:
        '''Specifies currently selected value in this list.
        Null value allowed, meaning that no currently selected entry is associated with this list item collection.'''
        ...
    
    @selected_value.setter
    def selected_value(self, value: aspose.words.markup.SdtListItem):
        ...
    
    @property
    def count(self) -> int:
        '''Gets number of items in the collection.'''
        ...
    
    ...

class SmartTag(aspose.words.CompositeNode):
    '''This element specifies the presence of a smart tag around one or more inline structures
    (runs, images, fields,etc.) within a paragraph.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.
    
    Smart tags is a kind of custom XML markup. Smart tags provide a facility for embedding
    customer-defined semantics into the document via the ability to provide a basic namespace/name
    for a run or set of runs within a document.
    
    :class:`SmartTag` can be a child of a :class:`aspose.words.Paragraph` or
    another :class:`SmartTag` node.
    
    The complete list of child nodes that can occur inside a smart tag consists of
    :class:`aspose.words.BookmarkStart`, :class:`aspose.words.BookmarkEnd`,
    :class:`aspose.words.fields.FieldStart`, :class:`aspose.words.fields.FieldSeparator`, :class:`aspose.words.fields.FieldEnd`, :class:`aspose.words.fields.FormField`,
    :class:`aspose.words.Comment`, :class:`aspose.words.notes.Footnote`,
    :class:`aspose.words.Run`, :class:`aspose.words.SpecialChar`,
    :class:`aspose.words.drawing.Shape`, :class:`aspose.words.drawing.GroupShape`,
    :class:`aspose.words.CommentRangeStart`,
    :class:`aspose.words.CommentRangeEnd`,
    :class:`SmartTag`.'''
    
    def __init__(self, doc: aspose.words.DocumentBase):
        '''Initializes a new instance of the :class:`SmartTag` class.
        
        When you create a new node, you need to specify a document to which the node belongs.
        A node cannot exist without a document because it depends on the document-wide structures
        such as lists and styles. Although a node always belongs to a document, a node might or might
        not be a part of the document tree.
        
        When a node is created, it belongs to a document, but is not yet part of the document tree
        and :attr:`aspose.words.Node.parent_node` is ``None``. To insert a node into the document, use the
        :meth:`aspose.words.CompositeNode.insert_after` or :meth:`aspose.words.CompositeNode.insert_before` methods
        on the parent node.
        
        :param doc: The owner document.'''
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        '''Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`aspose.words.DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`aspose.words.DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`aspose.words.DocumentVisitor.visit_smart_tag_start`, then calls :meth:`aspose.words.Node.accept` for all
        child nodes of the smart tag and calls :meth:`aspose.words.DocumentVisitor.visit_smart_tag_end` at the end.'''
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        '''Returns :attr:`aspose.words.NodeType.SMART_TAG`.'''
        ...
    
    @property
    def element(self) -> str:
        '''Specifies the name of the smart tag within the document.
        
        Cannot be ``None``.
        
        Default is empty string.'''
        ...
    
    @element.setter
    def element(self, value: str):
        ...
    
    @property
    def uri(self) -> str:
        '''Specifies the namespace URI of the smart tag.
        
        Cannot be ``None``.
        
        Default is empty string.'''
        ...
    
    @uri.setter
    def uri(self, value: str):
        ...
    
    @property
    def properties(self) -> aspose.words.markup.CustomXmlPropertyCollection:
        '''A collection of the smart tag properties.
        
        Cannot be ``None``.'''
        ...
    
    ...

class StructuredDocumentTag(aspose.words.CompositeNode):
    '''Represents a structured document tag (SDT or content control) in a document.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.
    
    Structured document tags (SDTs) allow to embed customer-defined semantics as well as its
    behavior and appearance into a document.
    
    In this version Aspose.Words provides a number of public methods and properties to
    manipulate the behavior and content of :class:`StructuredDocumentTag`.
    Mapping of SDT nodes to custom XML packages within a document can be performed with using
    the :attr:`StructuredDocumentTag.xml_mapping` property.
    
    :class:`StructuredDocumentTag` can occur in a document in the following places:
    
    * Block-level - Among paragraphs and tables, as a child of a :class:`aspose.words.Body`, :class:`aspose.words.HeaderFooter`,
      :class:`aspose.words.Comment`, :class:`aspose.words.notes.Footnote` or a :class:`aspose.words.drawing.Shape` node.
    
    * Row-level - Among rows in a table, as a child of a :class:`aspose.words.tables.Table` node.
    
    * Cell-level - Among cells in a table row, as a child of a :class:`aspose.words.tables.Row` node.
    
    * Inline-level - Among inline content inside, as a child of a :class:`aspose.words.Paragraph`.
    
    * Nested inside another :class:`StructuredDocumentTag`.'''
    
    def __init__(self, doc: aspose.words.DocumentBase, type: aspose.words.markup.SdtType, level: aspose.words.markup.MarkupLevel):
        '''Initializes a new instance of the **Structured document tag** class.
        
        The following types of SDT can be created:
        
        * :attr:`SdtType.CHECKBOX`
        
        * :attr:`SdtType.DROP_DOWN_LIST`
        
        * :attr:`SdtType.COMBO_BOX`
        
        * :attr:`SdtType.DATE`
        
        * :attr:`SdtType.BUILDING_BLOCK_GALLERY`
        
        * :attr:`SdtType.GROUP`
        
        * :attr:`SdtType.PICTURE`
        
        * :attr:`SdtType.RICH_TEXT`
        
        * :attr:`SdtType.PLAIN_TEXT`
        
        :param doc: The owner document.
        :param type: Type of SDT node.
        :param level: Level of SDT node within the document.'''
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        '''Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`aspose.words.DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`aspose.words.DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`aspose.words.DocumentVisitor.visit_structured_document_tag_start`, then calls :meth:`aspose.words.Node.accept` for all
        child nodes of the smart tag and calls :meth:`aspose.words.DocumentVisitor.visit_structured_document_tag_end` at the end.'''
        ...
    
    def set_checked_symbol(self, character_code: int, font_name: str) -> None:
        '''Sets the symbol used to represent the checked state of a check box content control.
        
        :param character_code: The character code for the specified symbol.
        :param font_name: The name of the font that contains the symbol.
        
        Accessing this method will only work for :attr:`SdtType.CHECKBOX` SDT types.
        
        For all other SDT types exception will occur.'''
        ...
    
    def set_unchecked_symbol(self, character_code: int, font_name: str) -> None:
        '''Sets the symbol used to represent the unchecked state of a check box content control.
        
        :param character_code: The character code for the specified symbol.
        :param font_name: The name of the font that contains the symbol.
        
        Accessing this method will only work for :attr:`SdtType.CHECKBOX` SDT types.
        
        For all other SDT types exception will occur.'''
        ...
    
    def remove_self_only(self) -> None:
        '''Removes just this SDT node itself, but keeps the content of it inside the document tree.'''
        ...
    
    def clear(self) -> None:
        '''Clears contents of this structured document tag and displays a placeholder if it is defined.
        
        It is not possible to clear contents of a structured document tag if it has revisions.
        
        If this structured document tag is mapped to custom XML (with using the :attr:`StructuredDocumentTag.xml_mapping`
        property), the referenced XML node is cleared.'''
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        '''Returns :attr:`aspose.words.NodeType.STRUCTURED_DOCUMENT_TAG`.'''
        ...
    
    @property
    def placeholder(self) -> aspose.words.buildingblocks.BuildingBlock:
        '''Gets the :class:`aspose.words.buildingblocks.BuildingBlock` containing placeholder text which should be displayed when this SDT run contents are empty,
        the associated mapped XML element is empty as specified via the :attr:`StructuredDocumentTag.xml_mapping` element
        or the :attr:`StructuredDocumentTag.is_showing_placeholder_text` element is ``True``.
        
        Can be ``None``, meaning that the placeholder is not applicable for this Sdt.'''
        ...
    
    @property
    def placeholder_name(self) -> str:
        '''Gets or sets Name of the :class:`aspose.words.buildingblocks.BuildingBlock` containing placeholder text.
        
        :class:`aspose.words.buildingblocks.BuildingBlock` with this name :attr:`aspose.words.buildingblocks.BuildingBlock.name` has to be present in the :attr:`aspose.words.Document.glossary_document`
        otherwise System.InvalidOperationException will occur.'''
        ...
    
    @placeholder_name.setter
    def placeholder_name(self, value: str):
        ...
    
    @property
    def level(self) -> aspose.words.markup.MarkupLevel:
        '''Gets the level at which this **SDT** occurs in the document tree.'''
        ...
    
    @property
    def sdt_type(self) -> aspose.words.markup.SdtType:
        '''Gets type of this **Structured document tag**.'''
        ...
    
    @property
    def id(self) -> int:
        '''Specifies a unique read-only persistent numerical Id for this **SDT**.
        
        Id attribute shall follow these rules:
        
        * The document shall retain SDT ids only if the whole document is cloned :meth:`aspose.words.Document.clone`.
        
        * During :meth:`aspose.words.DocumentBase.import_node`
          Id shall be retained if import does not cause conflicts with other SDT Ids in
          the target document.
        
        * If multiple SDT nodes specify the same decimal number value for the Id attribute,
          then the first SDT in the document shall maintain this original Id,
          and all subsequent SDT nodes shall have new identifiers assigned to them when the document is loaded.
        
        * During standalone SDT Aspose.Words.Markup.StructuredDocumentTag.Clone(System.Boolean,Aspose.Words.INodeCloningListener) operation new unique ID will be generated for the cloned SDT node.
        
        * If Id is not specified in the source document, then the SDT node shall have a new unique identifier assigned
          to it when the document is loaded.'''
        ...
    
    @property
    def lock_content_control(self) -> bool:
        '''When set to ``True``, this property will prohibit a user from deleting this **SDT**.'''
        ...
    
    @lock_content_control.setter
    def lock_content_control(self, value: bool):
        ...
    
    @property
    def lock_contents(self) -> bool:
        '''When set to ``True``, this property will prohibit a user from editing the contents of this **SDT**.'''
        ...
    
    @lock_contents.setter
    def lock_contents(self, value: bool):
        ...
    
    @property
    def is_showing_placeholder_text(self) -> bool:
        '''Specifies whether the content of this **SDT** shall be interpreted to contain placeholder text
        (as opposed to regular text contents within the SDT).
        
        if set to ``True``, this state shall be resumed (showing placeholder text) upon opening this document.'''
        ...
    
    @is_showing_placeholder_text.setter
    def is_showing_placeholder_text(self, value: bool):
        ...
    
    @property
    def tag(self) -> str:
        '''Specifies a tag associated with the current SDT node.
        Can not be ``None``.
        
        A tag is an arbitrary string which applications can associate with SDT
        in order to identify it without providing a visible friendly name.'''
        ...
    
    @tag.setter
    def tag(self, value: str):
        ...
    
    @property
    def contents_font(self) -> aspose.words.Font:
        '''Font formatting that will be applied to text entered into **SDT**.'''
        ...
    
    @property
    def end_character_font(self) -> aspose.words.Font:
        '''Font formatting that will be applied to the last character of text entered into **SDT**.'''
        ...
    
    @property
    def is_temporary(self) -> bool:
        '''Specifies whether this **SDT** shall be removed from the WordProcessingML document when its contents
        are modified.'''
        ...
    
    @is_temporary.setter
    def is_temporary(self, value: bool):
        ...
    
    @property
    def title(self) -> str:
        '''Specifies the friendly name associated with this **SDT**.
        Can not be ``None``.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...
    
    @property
    def list_items(self) -> aspose.words.markup.SdtListItemCollection:
        '''Gets :class:`SdtListItemCollection` associated with this **SDT**.
        
        Accessing this property will only work for :attr:`SdtType.COMBO_BOX` or :attr:`SdtType.DROP_DOWN_LIST`
        SDT types.
        
        For all other SDT types exception will occur.'''
        ...
    
    @property
    def checked(self) -> bool:
        '''Gets/Sets current state of the Checkbox **SDT**.
        Default value for this property is ``False``.
        
        Accessing this property will only work for :attr:`SdtType.CHECKBOX`
        SDT types.
        
        For all other SDT types exception will occur.'''
        ...
    
    @checked.setter
    def checked(self, value: bool):
        ...
    
    @property
    def appearance(self) -> aspose.words.markup.SdtAppearance:
        '''Gets/sets the appearance of a structured document tag.'''
        ...
    
    @appearance.setter
    def appearance(self, value: aspose.words.markup.SdtAppearance):
        ...
    
    @property
    def date_display_locale(self) -> int:
        '''Allows to set/get the language format for the date displayed in this **SDT**.
        
        Accessing this property will only work for :attr:`SdtType.DATE` SDT type.
        
        For all other SDT types exception will occur.'''
        ...
    
    @date_display_locale.setter
    def date_display_locale(self, value: int):
        ...
    
    @property
    def date_display_format(self) -> str:
        '''String that represents the format in which dates are displayed.
        Can not be ``None``.
        
        Accessing this property will only work for :attr:`SdtType.DATE` SDT type.
        
        For all other SDT types exception will occur.'''
        ...
    
    @date_display_format.setter
    def date_display_format(self, value: str):
        ...
    
    @property
    def full_date(self) -> datetime.datetime:
        '''Specifies the full date and time last entered into this **SDT**.
        
        Accessing this property will only work for :attr:`SdtType.DATE` SDT type.
        
        For all other SDT types exception will occur.'''
        ...
    
    @full_date.setter
    def full_date(self, value: datetime.datetime):
        ...
    
    @property
    def date_storage_format(self) -> aspose.words.markup.SdtDateStorageFormat:
        '''Gets/sets format in which the date for a date SDT is stored when the **SDT** is bound to an XML node in the document's data store.
        Default value is :attr:`SdtDateStorageFormat.DATE_TIME`
        
        Accessing this property will only work for :attr:`SdtType.DATE` SDT type.
        
        For all other SDT types exception will occur.'''
        ...
    
    @date_storage_format.setter
    def date_storage_format(self, value: aspose.words.markup.SdtDateStorageFormat):
        ...
    
    @property
    def calendar_type(self) -> aspose.words.markup.SdtCalendarType:
        '''Specifies the type of calendar for this **SDT**.
        Default is :attr:`SdtCalendarType.DEFAULT`
        
        Accessing this property will only work for :attr:`SdtType.DATE` SDT type.
        
        For all other SDT types exception will occur.'''
        ...
    
    @calendar_type.setter
    def calendar_type(self, value: aspose.words.markup.SdtCalendarType):
        ...
    
    @property
    def building_block_gallery(self) -> str:
        '''Specifies type of building block for this **SDT**.
        Can not be ``None``.
        
        Accessing this property will only work for :attr:`SdtType.BUILDING_BLOCK_GALLERY` and
        :attr:`SdtType.DOC_PART_OBJ` SDT types. It is read-only for **SDT** of the document part type.
        
        For all other SDT types exception will occur.'''
        ...
    
    @building_block_gallery.setter
    def building_block_gallery(self, value: str):
        ...
    
    @property
    def building_block_category(self) -> str:
        '''Specifies category of building block for this **SDT** node.
        Can not be ``None``.
        
        Accessing this property will only work for :attr:`SdtType.BUILDING_BLOCK_GALLERY` and
        :attr:`SdtType.DOC_PART_OBJ` SDT types. It is read-only for **SDT** of the document part type.
        
        For all other SDT types exception will occur.'''
        ...
    
    @building_block_category.setter
    def building_block_category(self, value: str):
        ...
    
    @property
    def multiline(self) -> bool:
        '''Specifies whether this **SDT** allows multiple lines of text.
        
        Accessing this property will only work for :attr:`SdtType.RICH_TEXT` and :attr:`SdtType.PLAIN_TEXT` SDT type.
        
        For all other SDT types exception will occur.'''
        ...
    
    @multiline.setter
    def multiline(self, value: bool):
        ...
    
    @property
    def color(self) -> aspose.pydrawing.Color:
        '''Gets or sets the color of the structured document tag.'''
        ...
    
    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def style(self) -> aspose.words.Style:
        '''Gets or sets the Style of the structured document tag.
        
        Only :attr:`aspose.words.StyleType.CHARACTER` style or :attr:`aspose.words.StyleType.PARAGRAPH` style with linked character style can be set.'''
        ...
    
    @style.setter
    def style(self, value: aspose.words.Style):
        ...
    
    @property
    def style_name(self) -> str:
        '''Gets or sets the name of the style applied to the structured document tag.'''
        ...
    
    @style_name.setter
    def style_name(self, value: str):
        ...
    
    @property
    def xml_mapping(self) -> aspose.words.markup.XmlMapping:
        '''Gets an object that represents the mapping of this structured document tag to XML data
        in a custom XML part of the current document.
        
        You can use the :meth:`XmlMapping.set_mapping` method of this object to map
        a structured document tag to XML data.'''
        ...
    
    @property
    def word_open_xml(self) -> str:
        '''Gets a string that represents the XML contained within the node in the :attr:`aspose.words.SaveFormat.FLAT_OPC` format.'''
        ...
    
    ...

class StructuredDocumentTagCollection:
    '''A collection of :class:`IStructuredDocumentTag` instances that represent the structured document tags in the specified range.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.markup.IStructuredDocumentTag:
        '''Returns the structured document tag at the specified index.
        
        :param index: An index into the collection.'''
        ...
    
    def get_by_id(self, id: int) -> aspose.words.markup.IStructuredDocumentTag:
        '''Returns the structured document tag by identifier.
        
        Returns null if the structured document tag with the specified identifier cannot be found.
        
        :param id: The structured document tag identifier.'''
        ...
    
    def get_by_title(self, title: str) -> aspose.words.markup.IStructuredDocumentTag:
        '''Returns the first structured document tag encountered in the collection with the specified title.
        
        Returns null if the structured document tag with the specified title cannot be found.
        
        :param title: The title of structured document tag.'''
        ...
    
    def get_by_tag(self, tag: str) -> aspose.words.markup.IStructuredDocumentTag:
        '''Returns the first structured document tag encountered in the collection with the specified tag.
        
        Returns null if the structured document tag with the specified tag cannot be found.
        
        :param tag: The tag of the structured document tag.'''
        ...
    
    def remove(self, id: int) -> None:
        '''Removes the structured document tag with the specified identifier.
        
        :param id: The structured document tag identifier.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes a structured document tag at the specified index.
        
        :param index: An index into the collection.'''
        ...
    
    @property
    def count(self) -> int:
        '''Returns the number of structured document tags in the collection.'''
        ...
    
    ...

class StructuredDocumentTagRangeEnd(aspose.words.Node):
    '''Represents an end of **ranged** structured document tag which accepts multi-sections content.
    See also :class:`StructuredDocumentTagRangeStart` node.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.
    
    Can be immediate child of :class:`aspose.words.Body` node **only**.'''
    
    def __init__(self, doc: aspose.words.DocumentBase, id: int):
        '''Initializes a new instance of the **Structured document tag range end** class.
        
        :param doc: The owner document.
        :param id: Identifier of the corresponding structured document tag range start.'''
        ...
    
    @property
    def id(self) -> int:
        '''Specifies a unique read-only persistent numerical Id for this **StructuredDocumentTagRange** node.
        Corresponding :class:`StructuredDocumentTagRangeStart` node has the same :attr:`StructuredDocumentTagRangeStart.id`.'''
        ...
    
    ...

class StructuredDocumentTagRangeStart(aspose.words.Node):
    '''Represents a start of **ranged** structured document tag which accepts multi-sections content.
    See also :class:`StructuredDocumentTagRangeEnd`.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.
    
    Can be immediate child of :class:`aspose.words.Body` node **only**.'''
    
    def __init__(self, doc: aspose.words.DocumentBase, type: aspose.words.markup.SdtType):
        '''Initializes a new instance of the **Structured document tag range start** class.
        
        The following types of SDT can be created:
        
        * :attr:`SdtType.CHECKBOX`
        
        * :attr:`SdtType.DROP_DOWN_LIST`
        
        * :attr:`SdtType.COMBO_BOX`
        
        * :attr:`SdtType.DATE`
        
        * :attr:`SdtType.BUILDING_BLOCK_GALLERY`
        
        * :attr:`SdtType.GROUP`
        
        * :attr:`SdtType.PICTURE`
        
        * :attr:`SdtType.RICH_TEXT`
        
        * :attr:`SdtType.PLAIN_TEXT`
        
        :param doc: The owner document.
        :param type: Type of SDT node.'''
        ...
    
    def get_child_nodes(self, node_type: aspose.words.NodeType, is_deep: bool) -> aspose.words.NodeCollection:
        '''Returns a live collection of child nodes that match the specified types.'''
        ...
    
    def append_child(self, new_child: aspose.words.Node) -> aspose.words.Node:
        '''Adds the specified node to the end of the stdContent range.
        
        :param new_child: The node to add.
        :returns: The node added.'''
        ...
    
    def remove_all_children(self) -> None:
        '''Removes all the nodes between this range start node and the range end node.'''
        ...
    
    def remove_self_only(self) -> None:
        '''Removes this range start and appropriate range end nodes of the structured document tag,
        but keeps its content inside the document tree.'''
        ...
    
    @property
    def child_nodes(self) -> aspose.words.NodeCollection:
        '''Gets all nodes between this range start node and the range end node.'''
        ...
    
    @property
    def last_child(self) -> aspose.words.Node:
        '''Gets the last child in the stdContent range.
        
        If there is no last child node, a ``None`` is returned.'''
        ...
    
    @property
    def level(self) -> aspose.words.markup.MarkupLevel:
        '''Gets the level at which this structured document tag range start occurs in the document tree.'''
        ...
    
    @property
    def sdt_type(self) -> aspose.words.markup.SdtType:
        '''Gets type of this structured document tag.'''
        ...
    
    @property
    def color(self) -> aspose.pydrawing.Color:
        '''Gets or sets the color of the structured document tag.'''
        ...
    
    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def id(self) -> int:
        '''Specifies a unique read-only persistent numerical Id for this structured document tag.
        
        Id attribute shall follow these rules:
        
        * The document shall retain structured document tag ids only if the whole document
          is cloned :meth:`aspose.words.Document.clone`.
        
        * During :meth:`aspose.words.DocumentBase.import_node`
          Id shall be retained if import does not cause conflicts with other structured document tag Ids in
          the target document.
        
        * If multiple structured document tag nodes specify the same decimal number value for the Id attribute,
          then the first structured document tag in the document shall maintain this original Id,
          and all subsequent structured document tag nodes shall have new identifiers assigned to them when the document is loaded.
        
        * During standalone structured document tag Aspose.Words.Markup.StructuredDocumentTag.Clone(System.Boolean,Aspose.Words.INodeCloningListener) operation new unique ID will be
          generated for the cloned structured document tag node.
        
        * If Id is not specified in the source document, then the structured document tag node shall have a new unique identifier assigned
          to it when the document is loaded.'''
        ...
    
    @property
    def lock_content_control(self) -> bool:
        '''When set to ``True``, this property will prohibit a user from deleting this structured document tag.'''
        ...
    
    @lock_content_control.setter
    def lock_content_control(self, value: bool):
        ...
    
    @property
    def lock_contents(self) -> bool:
        '''When set to ``True``, this property will prohibit a user from editing the contents of this structured document tag.'''
        ...
    
    @lock_contents.setter
    def lock_contents(self, value: bool):
        ...
    
    @property
    def is_showing_placeholder_text(self) -> bool:
        '''Specifies whether the content of this structured document tag shall be interpreted to contain
        placeholder text (as opposed to regular text contents within the structured document tag).
        
        if set to ``True``, this state shall be resumed (showing placeholder text) upon opening this document.'''
        ...
    
    @is_showing_placeholder_text.setter
    def is_showing_placeholder_text(self, value: bool):
        ...
    
    @property
    def placeholder(self) -> aspose.words.buildingblocks.BuildingBlock:
        '''Gets the :class:`aspose.words.buildingblocks.BuildingBlock` containing placeholder text which should be displayed when
        this structured document tag run contents are empty, the associated mapped XML element is empty as specified
        via the :attr:`StructuredDocumentTagRangeStart.xml_mapping` element or the :attr:`StructuredDocumentTagRangeStart.is_showing_placeholder_text` element is ``True``.
        
        Can be ``None``, meaning that the placeholder is not applicable for this structured document tag.'''
        ...
    
    @property
    def placeholder_name(self) -> str:
        '''Gets or sets Name of the :class:`aspose.words.buildingblocks.BuildingBlock` containing placeholder text.
        
        :class:`aspose.words.buildingblocks.BuildingBlock` with this name :attr:`aspose.words.buildingblocks.BuildingBlock.name` has to be present in the :attr:`aspose.words.Document.glossary_document`
        otherwise System.InvalidOperationException will occur.'''
        ...
    
    @placeholder_name.setter
    def placeholder_name(self, value: str):
        ...
    
    @property
    def tag(self) -> str:
        '''Specifies a tag associated with the current structured document tag node.
        Can not be ``None``.
        
        A tag is an arbitrary string which applications can associate with structured document
        tag in order to identify it without providing a visible friendly name.'''
        ...
    
    @tag.setter
    def tag(self, value: str):
        ...
    
    @property
    def title(self) -> str:
        '''Specifies the friendly name associated with this structured document tag.
        Can not be ``None``.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...
    
    @property
    def word_open_xml(self) -> str:
        '''Gets a string that represents the XML contained within the node in the :attr:`aspose.words.SaveFormat.FLAT_OPC` format.'''
        ...
    
    @property
    def xml_mapping(self) -> aspose.words.markup.XmlMapping:
        '''Gets an object that represents the mapping of this structured document tag range to XML data
        in a custom XML part of the current document.
        
        You can use the :meth:`XmlMapping.set_mapping` method of this
        object to map a structured document tag range to XML data.'''
        ...
    
    @property
    def range_end(self) -> aspose.words.markup.StructuredDocumentTagRangeEnd:
        '''Specifies end of range if the :class:`StructuredDocumentTag` is a ranged structured document tag.
        Otherwise returns ``None``.'''
        ...
    
    ...

class XmlMapping:
    '''Specifies the information that is used to establish a mapping between the parent
    structured document tag and an XML element stored within a custom XML data part in the document.
    To learn more, visit the `Structured Document Tags or Content Control <https://docs.aspose.com/words/net/working-with-content-control-sdt/>` documentation article.'''
    
    def set_mapping(self, custom_xml_part: aspose.words.markup.CustomXmlPart, x_path: str, prefix_mapping: str) -> bool:
        '''Sets a mapping between the parent structured document tag and an XML node of a custom XML data part.
        
        :param custom_xml_part: A custom XML data part to map to.
        :param x_path: An XPath expression to find the XML node.
        :param prefix_mapping: XML namespace prefix mappings to evaluate the XPath.
        :returns: A flag indicating whether the parent structured document tag is successfully mapped to
                  the XML node.'''
        ...
    
    def delete(self) -> None:
        '''Deletes mapping of the parent structured document to XML data.'''
        ...
    
    @property
    def prefix_mappings(self) -> str:
        '''Returns XML namespace prefix mappings to evaluate the :attr:`XmlMapping.xpath`.
        
        Specifies the set of prefix mappings, which shall be used to interpret the XPath expression
        when the XPath expression is evaluated against the custom XML data parts in the document.'''
        ...
    
    @property
    def xpath(self) -> str:
        '''Returns the XPath expression, which is evaluated to find the custom XML node
        that is mapped to the parent structured document tag.'''
        ...
    
    @property
    def custom_xml_part(self) -> aspose.words.markup.CustomXmlPart:
        '''Returns the custom XML data part to which the parent structured document tag is mapped.'''
        ...
    
    @property
    def is_mapped(self) -> bool:
        '''Returns ``True`` if the parent structured document tag is successfully mapped to XML data.'''
        ...
    
    @property
    def store_item_id(self) -> str:
        '''Specifies the custom XML data identifier for the custom XML data part which
        shall be used to evaluate the :attr:`XmlMapping.xpath` expression.'''
        ...
    
    ...

class MarkupLevel:
    '''Specifies the level in the document tree where a particular :class:`StructuredDocumentTag` can occur.'''
    
    UNKNOWN: int
    INLINE: int
    BLOCK: int
    ROW: int
    CELL: int

class SdtAppearance:
    '''Specifies the appearance of a structured document tag.'''
    
    BOUNDING_BOX: int
    TAGS: int
    HIDDEN: int
    DEFAULT: int

class SdtCalendarType:
    '''Specifies the possible types of calendars which can be used to specify :attr:`StructuredDocumentTag.calendar_type`
    in an Office Open XML document.'''
    
    DEFAULT: int
    GREGORIAN: int
    GREGORIAN_ARABIC: int
    GREGORIAN_ME_FRENCH: int
    GREGORIAN_US: int
    GREGORIAN_XLIT_ENGLISH: int
    GREGORIAN_XLIT_FRENCH: int
    HEBREW: int
    HIJRI: int
    JAPAN: int
    KOREA: int
    NONE: int
    SAKA: int
    TAIWAN: int
    THAI: int

class SdtDateStorageFormat:
    '''Specifies how the date for a date SDT is stored/retrieved when the SDT is bound to an XML node in the document's data store.'''
    
    DATE: int
    DATE_TIME: int
    TEXT: int
    DEFAULT: int

class SdtType:
    '''Specifies the type of a structured document tag (SDT) node.'''
    
    NONE: int
    BIBLIOGRAPHY: int
    CITATION: int
    EQUATION: int
    DROP_DOWN_LIST: int
    COMBO_BOX: int
    DATE: int
    BUILDING_BLOCK_GALLERY: int
    DOC_PART_OBJ: int
    GROUP: int
    PICTURE: int
    RICH_TEXT: int
    PLAIN_TEXT: int
    CHECKBOX: int
    REPEATING_SECTION: int
    REPEATING_SECTION_ITEM: int
    ENTITY_PICKER: int

