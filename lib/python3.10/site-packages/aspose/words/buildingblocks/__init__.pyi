import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class BuildingBlock(aspose.words.CompositeNode):
    '''Represents a glossary document entry such as a Building Block, AutoText or an AutoCorrect entry.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/net/aspose-words-document-object-model/>` documentation article.
    
    :class:`BuildingBlock` can contain only :class:`aspose.words.Section` nodes.
    
    :class:`BuildingBlock` can only be a child of :class:`GlossaryDocument`.
    
    You can create new building blocks and insert them into a glossary document.
    You can modify or delete existing building blocks. You can copy or move building blocks
    between documents. You can insert content of a building block into a document.
    
    Corresponds to the **docPart**, **docPartPr** and **docPartBody** elements in OOXML.'''
    
    def __init__(self, glossary_doc: aspose.words.buildingblocks.GlossaryDocument):
        '''Initializes a new instance of this class.
        
        When :class:`BuildingBlock` is created, it belongs to the specified glossary document,
        but is not yet part of the glossary document and :attr:`aspose.words.Node.parent_node` is ``None``.
        
        To append :class:`BuildingBlock` to a :class:`GlossaryDocument` use
        :meth:`aspose.words.CompositeNode.append_child`.
        
        :param glossary_doc: The owner document.'''
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        '''Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`aspose.words.DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`aspose.words.DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`aspose.words.DocumentVisitor.visit_building_block_start`, then calls
        :meth:`aspose.words.Node.accept` for all child nodes of this building block, then calls
        :meth:`aspose.words.DocumentVisitor.visit_building_block_end`.
        
        Note: A building block node and its children are not visited when you execute a
        Visitor over a :class:`aspose.words.Document`. If you want to execute a Visitor over a
        building block, you need to execute the visitor over :class:`GlossaryDocument` or
        call :meth:`BuildingBlock.accept`.'''
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        '''Returns the :attr:`aspose.words.NodeType.BUILDING_BLOCK` value.'''
        ...
    
    @property
    def sections(self) -> aspose.words.SectionCollection:
        '''Returns a collection that represents all sections in the building block.'''
        ...
    
    @property
    def first_section(self) -> aspose.words.Section:
        '''Gets the first section in the building block.
        
        Returns ``None`` if there are no sections.'''
        ...
    
    @property
    def last_section(self) -> aspose.words.Section:
        '''Gets the last section in the building block.
        
        Returns ``None`` if there are no sections.'''
        ...
    
    @property
    def name(self) -> str:
        '''Gets or sets the name of this building block.
        
        The name may contain any string content, usually a friendly identifier.
        Multiple building blocks can have the same name.
        
        Cannot be ``None`` and cannot be an empty string.
        
        Corresponds to the **docPartPr.name** element in OOXML.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def guid(self) -> uuid.UUID:
        '''Gets or sets an identifier (a 128-bit GUID) that uniquely identifies this building block.
        
        Can be used by an application to uniquely reference a building block regardless of
        different naming due to localization.
        
        Corresponds to the **docPartPr.guid** element in OOXML.'''
        ...
    
    @guid.setter
    def guid(self, value: uuid.UUID):
        ...
    
    @property
    def description(self) -> str:
        '''Gets or sets the description associated with this building block.
        
        The description may contain any string content, usually additional information.
        
        Cannot be ``None``, but can be an empty string.
        
        Corresponds to the **docPartPr.description** element in OOXML.'''
        ...
    
    @description.setter
    def description(self, value: str):
        ...
    
    @property
    def gallery(self) -> aspose.words.buildingblocks.BuildingBlockGallery:
        '''Specifies the first-level categorization for the building block for the purposes of
        classification or user interface sorting.
        
        Building blocks in Microsoft Word user interface are arranged
        into Galleries. Each :attr:`BuildingBlock.gallery` can have multiple Categories. Each block within
        a :attr:`BuildingBlock.category` has a :attr:`BuildingBlock.name`.
        
        Corresponds to the **docPartPr.category.gallery** element in OOXML.'''
        ...
    
    @gallery.setter
    def gallery(self, value: aspose.words.buildingblocks.BuildingBlockGallery):
        ...
    
    @property
    def category(self) -> str:
        '''Specifies the second-level categorization for the building block.
        
        Building blocks in Microsoft Word user interface are arranged
        into Galleries. Each :attr:`BuildingBlock.gallery` can have multiple Categories. Each block within
        a :attr:`BuildingBlock.category` has a :attr:`BuildingBlock.name`.
        
        Cannot be ``None`` and cannot be an empty string.
        
        Corresponds to the **docPartPr.category.name** element in OOXML.'''
        ...
    
    @category.setter
    def category(self, value: str):
        ...
    
    @property
    def behavior(self) -> aspose.words.buildingblocks.BuildingBlockBehavior:
        '''Specifies the behavior that shall be applied when the contents of the building block
        is inserted into the main document.'''
        ...
    
    @behavior.setter
    def behavior(self, value: aspose.words.buildingblocks.BuildingBlockBehavior):
        ...
    
    @property
    def type(self) -> aspose.words.buildingblocks.BuildingBlockType:
        '''Specifies the building block type.
        
        The building block type can influence the visibility and behavior of the
        building block in Microsoft Word.
        
        Corresponds to the **docPartPr.types** element in OOXML.'''
        ...
    
    @type.setter
    def type(self, value: aspose.words.buildingblocks.BuildingBlockType):
        ...
    
    ...

class BuildingBlockCollection(aspose.words.NodeCollection):
    '''A collection of :class:`BuildingBlock` objects in the document.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/net/aspose-words-document-object-model/>` documentation article.
    
    You do not create instances of this class directly. To access a collection
    of building blocks use the :attr:`GlossaryDocument.building_blocks` property.'''
    
    def __getitem__(self, index: int) -> aspose.words.buildingblocks.BuildingBlock:
        '''Retrieves a building block at the given index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the list of building blocks.'''
        ...
    
    def to_array(self) -> list[aspose.words.buildingblocks.BuildingBlock]:
        '''Copies all building blocks from the collection to a new array of building blocks.
        
        :returns: An array of building blocks.'''
        ...
    
    ...

class GlossaryDocument(aspose.words.DocumentBase):
    '''Represents the root element for a glossary document within a Word document.
    A glossary document is a storage for AutoText, AutoCorrect entries and Building Blocks.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/net/aspose-words-document-object-model/>` documentation article.
    
    Some documents, usually templates, can contain AutoText, AutoCorrect entries
    and/or Building Blocks (also known as *glossary document entries*, *document parts*
    or *building blocks*).
    
    To access building blocks, you need to load a document into a :class:`aspose.words.Document`
    object. Building blocks will be available via the :attr:`aspose.words.Document.glossary_document` property.
    
    :class:`GlossaryDocument` can contain any number of :class:`BuildingBlock` objects.
    Each :class:`BuildingBlock` represents one document part.
    
    Corresponds to the **glossaryDocument** and **docParts** elements in OOXML.'''
    
    def __init__(self):
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        '''Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`aspose.words.DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`aspose.words.DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`aspose.words.DocumentVisitor.visit_glossary_document_start`, then calls :meth:`aspose.words.Node.accept`
        for all child nodes of this node and then calls :meth:`aspose.words.DocumentVisitor.visit_glossary_document_end`
        at the end.
        
        Note: A glossary document node and its children are not visited when you execute a
        Visitor over a :class:`aspose.words.Document`. If you want to execute a Visitor over a
        glossary document, you need to call :meth:`GlossaryDocument.accept`.'''
        ...
    
    def get_building_block(self, gallery: aspose.words.buildingblocks.BuildingBlockGallery, category: str, name: str) -> aspose.words.buildingblocks.BuildingBlock:
        '''Finds a building block using the specified gallery, category and name.
        
        This is a convenience method that iterates over all building blocks
        in this collection and returns the first building block that matches
        the specified gallery, category and name.
        
        Microsoft Word organizes building blocks into galleries. The galleries
        are predefined using the :class:`BuildingBlockGallery` enum.
        Within each gallery, building blocks can be organized into one or more categories.
        The category name is a string. Each building block has a name. A building block
        name is not guaranteed to be unique.
        
        :param gallery: The gallery criteria.
        :param category: The category criteria. Can be ``None``, in which case it will not be used for comparison.
        :param name: The building block name criteria.
        :returns: The matching building block or ``None`` if a match was not found.'''
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        '''Returns the :attr:`aspose.words.NodeType.GLOSSARY_DOCUMENT` value.'''
        ...
    
    @property
    def building_blocks(self) -> aspose.words.buildingblocks.BuildingBlockCollection:
        '''Returns a typed collection that represents all building blocks in the glossary document.'''
        ...
    
    @property
    def first_building_block(self) -> aspose.words.buildingblocks.BuildingBlock:
        '''Gets the first building block in the glossary document.
        
        Returns ``None`` if there are no building blocks available.'''
        ...
    
    @property
    def last_building_block(self) -> aspose.words.buildingblocks.BuildingBlock:
        '''Gets the last building block in the glossary document.
        
        Returns ``None`` if there are no building blocks available.'''
        ...
    
    ...

class BuildingBlockBehavior:
    '''Specifies the behavior that shall be applied to the contents of the building block
    when it is inserted into the main document.
    
    Corresponds to the **ST_DocPartBehavior** type in OOXML.'''
    
    CONTENT: int
    PARAGRAPH: int
    PAGE: int
    DEFAULT: int

class BuildingBlockGallery:
    '''Specifies the predefined gallery into which a building block is classified.
    
    Corresponds to the **ST_DocPartGallery** type in OOXML.'''
    
    ALL: int
    AUTO_TEXT: int
    BIBLIOGRAPHY: int
    COVER_PAGE: int
    CUSTOM_AUTO_TEXT: int
    CUSTOM_BIBLIOGRAPHY: int
    CUSTOM_COVER_PAGE: int
    CUSTOM_EQUATIONS: int
    CUSTOM_FOOTERS: int
    CUSTOM_HEADERS: int
    CUSTOM1: int
    CUSTOM2: int
    CUSTOM3: int
    CUSTOM4: int
    CUSTOM5: int
    CUSTOM_PAGE_NUMBER: int
    CUSTOM_PAGE_NUMBER_AT_BOTTOM: int
    CUSTOM_PAGE_NUMBER_AT_MARGIN: int
    CUSTOM_PAGE_NUMBER_AT_TOP: int
    CUSTOM_QUICK_PARTS: int
    CUSTOM_TABLE_OF_CONTENTS: int
    CUSTOM_TABLES: int
    CUSTOM_TEXT_BOX: int
    CUSTOM_WATERMARKS: int
    NO_GALLERY: int
    QUICK_PARTS: int
    EQUATIONS: int
    FOOTERS: int
    HEADERS: int
    PAGE_NUMBER: int
    PAGE_NUMBER_AT_BOTTOM: int
    PAGE_NUMBER_AT_MARGIN: int
    PAGE_NUMBER_AT_TOP: int
    STRUCTURED_DOCUMENT_TAG_PLACEHOLDER_TEXT: int
    TABLE_OF_CONTENTS: int
    TABLES: int
    TEXT_BOX: int
    WATERMARKS: int
    DEFAULT: int

class BuildingBlockType:
    '''Specifies a building block type. The type might affect the visibility and behavior of the building block
    in Microsoft Word.
    
    Corresponds to the **ST_DocPartType** type in OOXML.'''
    
    NONE: int
    AUTOMATICALLY_REPLACE_NAME_WITH_CONTENT: int
    STRUCTURED_DOCUMENT_TAG_PLACEHOLDER_TEXT: int
    FORM_FIELD_HELP_TEXT: int
    NORMAL: int
    AUTO_CORRECT: int
    AUTO_TEXT: int
    ALL: int
    DEFAULT: int

