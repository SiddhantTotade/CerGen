import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class BuiltInDocumentProperties(aspose.words.properties.DocumentPropertyCollection):
    '''A collection of built-in document properties.
    To learn more, visit the `Work with Document Properties <https://docs.aspose.com/words/net/work-with-document-properties/>` documentation article.
    
    Provides access to :class:`DocumentProperty` objects by their names (using an indexer) and
    via a set of typed properties that return values of appropriate types.
    
    The names of the properties are case-insensitive.
    
    The properties in the collection are sorted alphabetically by name.'''
    
    def __getitem__(self, index: int) -> aspose.words.properties.DocumentProperty:
        ...
    
    @property
    def author(self) -> str:
        '''Gets or sets the name of the document's author.'''
        ...
    
    @author.setter
    def author(self, value: str):
        ...
    
    @property
    def bytes(self) -> int:
        '''Represents an estimate of the number of bytes in the document.
        
        Microsoft Word does not always set this property.
        
        Aspose.Words does not update this property.'''
        ...
    
    @bytes.setter
    def bytes(self, value: int):
        ...
    
    @property
    def characters(self) -> int:
        '''Represents an estimate of the number of characters in the document.
        
        Aspose.Words updates this property when you call :meth:`aspose.words.Document.update_word_count`.'''
        ...
    
    @characters.setter
    def characters(self, value: int):
        ...
    
    @property
    def characters_with_spaces(self) -> int:
        '''Represents an estimate of the number of characters (including spaces) in the document.
        
        Aspose.Words updates this property when you call :meth:`aspose.words.Document.update_word_count`.'''
        ...
    
    @characters_with_spaces.setter
    def characters_with_spaces(self, value: int):
        ...
    
    @property
    def comments(self) -> str:
        '''Gets or sets the document comments.'''
        ...
    
    @comments.setter
    def comments(self, value: str):
        ...
    
    @property
    def category(self) -> str:
        '''Gets or sets the category of the document.'''
        ...
    
    @category.setter
    def category(self, value: str):
        ...
    
    @property
    def company(self) -> str:
        '''Gets or sets the company property.'''
        ...
    
    @company.setter
    def company(self, value: str):
        ...
    
    @property
    def created_time(self) -> datetime.datetime:
        '''Gets or sets date of the document creation in UTC.
        
        For documents originated from RTF format  this property returns local time of the author's machine at the moment of document creation.
        
        Aspose.Words does not update this property.'''
        ...
    
    @created_time.setter
    def created_time(self, value: datetime.datetime):
        ...
    
    @property
    def hyperlink_base(self) -> str:
        '''Specifies the base string used for evaluating relative hyperlinks in this document.
        
        Aspose.Words does not use this property.'''
        ...
    
    @hyperlink_base.setter
    def hyperlink_base(self, value: str):
        ...
    
    @property
    def keywords(self) -> str:
        '''Gets or sets the document keywords.'''
        ...
    
    @keywords.setter
    def keywords(self, value: str):
        ...
    
    @property
    def last_printed(self) -> datetime.datetime:
        '''Gets or sets the date when the document was last printed in UTC.
        
        For documents originated from RTF format this property returns the local time of last print operation.
        
        If the document was never printed, this property will return DateTime.MinValue.
        
        Aspose.Words does not update this property.'''
        ...
    
    @last_printed.setter
    def last_printed(self, value: datetime.datetime):
        ...
    
    @property
    def last_saved_by(self) -> str:
        '''Gets or sets the name of the last author.
        
        Aspose.Words does not update this property.'''
        ...
    
    @last_saved_by.setter
    def last_saved_by(self, value: str):
        ...
    
    @property
    def last_saved_time(self) -> datetime.datetime:
        '''Gets or sets the time of the last save in UTC.
        
        For documents originated from RTF format this property returns the local time of last save operation.
        
        Aspose.Words does not update this property.'''
        ...
    
    @last_saved_time.setter
    def last_saved_time(self, value: datetime.datetime):
        ...
    
    @property
    def lines(self) -> int:
        '''Represents an estimate of the number of lines in the document.
        
        Aspose.Words updates this property when you call :meth:`aspose.words.Document.update_word_count`.'''
        ...
    
    @lines.setter
    def lines(self, value: int):
        ...
    
    @property
    def links_up_to_date(self) -> bool:
        '''Indicates whether hyperlinks in a document are up-to-date.
        
        Aspose.Words does not update this property.'''
        ...
    
    @links_up_to_date.setter
    def links_up_to_date(self, value: bool):
        ...
    
    @property
    def manager(self) -> str:
        '''Gets or sets the manager property.'''
        ...
    
    @manager.setter
    def manager(self, value: str):
        ...
    
    @property
    def name_of_application(self) -> str:
        '''Gets or sets the name of the application.'''
        ...
    
    @name_of_application.setter
    def name_of_application(self, value: str):
        ...
    
    @property
    def pages(self) -> int:
        '''Represents an estimate of the number of pages in the document.
        
        Aspose.Words updates this property when you call :meth:`aspose.words.Document.update_page_layout`.'''
        ...
    
    @pages.setter
    def pages(self, value: int):
        ...
    
    @property
    def paragraphs(self) -> int:
        '''Represents an estimate of the number of paragraphs in the document.
        
        Aspose.Words updates this property when you call :meth:`aspose.words.Document.update_word_count`.'''
        ...
    
    @paragraphs.setter
    def paragraphs(self, value: int):
        ...
    
    @property
    def revision_number(self) -> int:
        '''Gets or sets the document revision number.
        
        Aspose.Words does not update this property.'''
        ...
    
    @revision_number.setter
    def revision_number(self, value: int):
        ...
    
    @property
    def security(self) -> aspose.words.properties.DocumentSecurity:
        '''Specifies the security level of a document as a numeric value.
        
        Use this property for informational purposes only because Microsoft Word does not always
        set this property. This property is available in DOC and OOXML documents only.
        
        To protect or unprotect a document use the
        :meth:`aspose.words.Document.protect` and :meth:`aspose.words.Document.unprotect` methods.
        
        Aspose.Words updates this property to a correct value before saving a document.'''
        ...
    
    @security.setter
    def security(self, value: aspose.words.properties.DocumentSecurity):
        ...
    
    @property
    def subject(self) -> str:
        '''Gets or sets the subject of the document.'''
        ...
    
    @subject.setter
    def subject(self, value: str):
        ...
    
    @property
    def template(self) -> str:
        '''Gets or sets the informational name of the document template.
        
        In Microsoft Word, this property is for informational purposes only and
        usually contains only the file name of the template without the path.
        
        Empty string means the document is attached to the Normal template.
        
        To get or set the actual name of the attached template, use the
        :attr:`aspose.words.Document.attached_template` property.'''
        ...
    
    @template.setter
    def template(self, value: str):
        ...
    
    @property
    def thumbnail(self) -> bytes:
        '''Gets or sets the thumbnail of the document.
        
        For now this property is used only when a document is being exported to ePub,
        it's not read from and written to other document formats.
        
        Image of arbitrary format can be set to this property, but the format is checked during export.
        System.InvalidOperationException is thrown if the image is invalid or its format is unsupported for
        specific format of document.
        
        Only gif, jpeg and png images can be used for ePub publication.'''
        ...
    
    @thumbnail.setter
    def thumbnail(self, value: bytes):
        ...
    
    @property
    def title(self) -> str:
        '''Gets or sets the title of the document.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...
    
    @property
    def total_editing_time(self) -> int:
        '''Gets or sets the total editing time in minutes.'''
        ...
    
    @total_editing_time.setter
    def total_editing_time(self, value: int):
        ...
    
    @property
    def content_type(self) -> str:
        '''Gets or sets the Aspose.Words.Properties.PropertyName.ContentType of the document.'''
        ...
    
    @content_type.setter
    def content_type(self, value: str):
        ...
    
    @property
    def content_status(self) -> str:
        '''Gets or sets the Aspose.Words.Properties.PropertyName.ContentStatus of the document.'''
        ...
    
    @content_status.setter
    def content_status(self, value: str):
        ...
    
    @property
    def version(self) -> int:
        '''Represents the version number of the application that created the document.
        
        When a document was created by Microsoft Word, then high 16 bit represent
        the major version and low 16 bit represent the build number.'''
        ...
    
    @version.setter
    def version(self, value: int):
        ...
    
    @property
    def words(self) -> int:
        '''Represents an estimate of the number of words in the document.
        
        Aspose.Words updates this property when you call :meth:`aspose.words.Document.update_word_count`.'''
        ...
    
    @words.setter
    def words(self, value: int):
        ...
    
    @property
    def heading_pairs(self) -> list[object]:
        '''Specifies document headings and their names.
        
        Every heading pair occupies two elements in this array.
        
        The first element of the pair is a System.String and specifies the heading name.
        The second element of the pair is an System.Int32 and specifies the count of document
        parts for this heading in the :attr:`BuiltInDocumentProperties.titles_of_parts` property.
        
        The total sum of counts for all heading pairs in this property must be equal to the
        number of elements in the :attr:`BuiltInDocumentProperties.titles_of_parts` property.
        
        Aspose.Words does not update this property.'''
        ...
    
    @heading_pairs.setter
    def heading_pairs(self, value: list[object]):
        ...
    
    @property
    def titles_of_parts(self) -> list[str]:
        '''Each string in the array specifies the name of a part in the document.
        
        Aspose.Words does not update this property.'''
        ...
    
    @titles_of_parts.setter
    def titles_of_parts(self, value: list[str]):
        ...
    
    ...

class CustomDocumentProperties(aspose.words.properties.DocumentPropertyCollection):
    '''A collection of custom document properties.
    To learn more, visit the `Work with Document Properties <https://docs.aspose.com/words/net/work-with-document-properties/>` documentation article.
    
    Each :class:`DocumentProperty` object represents a custom property of a container document.
    
    The names of the properties are case-insensitive.
    
    The properties in the collection are sorted alphabetically by name.'''
    
    def __getitem__(self, index: int) -> aspose.words.properties.DocumentProperty:
        ...
    
    @overload
    def add(self, name: str, value: str) -> aspose.words.properties.DocumentProperty:
        '''Creates a new custom document property of the :attr:`PropertyType.STRING` data type.
        
        :param name: The name of the property.
        :param value: The value of the property.
        :returns: The newly created property object.'''
        ...
    
    @overload
    def add(self, name: str, value: int) -> aspose.words.properties.DocumentProperty:
        '''Creates a new custom document property of the :attr:`PropertyType.NUMBER` data type.
        
        :param name: The name of the property.
        :param value: The value of the property.
        :returns: The newly created property object.'''
        ...
    
    @overload
    def add(self, name: str, value: datetime.datetime) -> aspose.words.properties.DocumentProperty:
        '''Creates a new custom document property of the :attr:`PropertyType.DATE_TIME` data type.
        
        :param name: The name of the property.
        :param value: The value of the property.
        :returns: The newly created property object.'''
        ...
    
    @overload
    def add(self, name: str, value: bool) -> aspose.words.properties.DocumentProperty:
        '''Creates a new custom document property of the :attr:`PropertyType.BOOLEAN` data type.
        
        :param name: The name of the property.
        :param value: The value of the property.
        :returns: The newly created property object.'''
        ...
    
    @overload
    def add(self, name: str, value: float) -> aspose.words.properties.DocumentProperty:
        '''Creates a new custom document property of the :attr:`PropertyType.DOUBLE` data type.
        
        :param name: The name of the property.
        :param value: The value of the property.
        :returns: The newly created property object.'''
        ...
    
    def add_link_to_content(self, name: str, link_source: str) -> aspose.words.properties.DocumentProperty:
        '''Creates a new linked to content custom document property.
        
        :param name: The name of the property.
        :param link_source: The source of the property.
        :returns: The newly created property object or ``None`` when the  is invalid.'''
        ...
    
    ...

class DocumentProperty:
    '''Represents a custom or built-in document property.
    To learn more, visit the `Work with Document Properties <https://docs.aspose.com/words/net/work-with-document-properties/>` documentation article.'''
    
    def to_int(self) -> int:
        '''Returns the property value as integer.
        
        Throws an exception if the property type is not :attr:`PropertyType.NUMBER`.'''
        ...
    
    def to_double(self) -> float:
        '''Returns the property value as double.
        
        Throws an exception if the property type is not :attr:`PropertyType.NUMBER`.'''
        ...
    
    def to_date_time(self) -> datetime.datetime:
        '''Returns the property value as **DateTime** in UTC.
        
        Throws an exception if the property type is not :attr:`PropertyType.DATE_TIME`.
        
        Microsoft Word stores only the date part (no time) for custom date properties.'''
        ...
    
    def to_bool(self) -> bool:
        '''Returns the property value as bool.
        
        Throws an exception if the property type is not :attr:`PropertyType.BOOLEAN`.'''
        ...
    
    def to_byte_array(self) -> bytes:
        '''Returns the property value as byte array.
        
        Throws an exception if the property type is not :attr:`PropertyType.BYTE_ARRAY`.'''
        ...
    
    @property
    def name(self) -> str:
        '''Returns the name of the property.
        
        Cannot be ``None`` and cannot be an empty string.'''
        ...
    
    @property
    def value(self) -> object:
        '''Gets or sets the value of the property.
        
        Cannot be ``None``.'''
        ...
    
    @value.setter
    def value(self, value: object):
        ...
    
    @property
    def type(self) -> aspose.words.properties.PropertyType:
        '''Gets the data type of the property.'''
        ...
    
    @property
    def link_source(self) -> str:
        '''Gets the source of a linked custom document property.'''
        ...
    
    @property
    def is_link_to_content(self) -> bool:
        '''Shows whether this property is linked to content or not.'''
        ...
    
    ...

class DocumentPropertyCollection:
    '''Base class for :class:`BuiltInDocumentProperties` and :class:`CustomDocumentProperties` collections.
    To learn more, visit the `Work with Document Properties <https://docs.aspose.com/words/net/work-with-document-properties/>` documentation article.
    
    The names of the properties are case-insensitive.
    
    The properties in the collection are sorted alphabetically by name.'''
    
    def __getitem__(self, index: int) -> aspose.words.properties.DocumentProperty:
        '''Returns a :class:`DocumentProperty` object by index.
        
        :param index: Zero-based index of the :class:`DocumentProperty` to retrieve.'''
        ...
    
    def get_by_name(self, name: str) -> aspose.words.properties.DocumentProperty:
        '''Returns a :class:`DocumentProperty` object by the name of the property.'''
        ...
    
    def contains(self, name: str) -> bool:
        '''Returns ``True`` if a property with the specified name exists in the collection.
        
        :param name: The case-insensitive name of the property.
        :returns: ``True`` if the property exists in the collection; ``False`` otherwise.'''
        ...
    
    def index_of(self, name: str) -> int:
        '''Gets the index of a property by name.
        
        :param name: The case-insensitive name of the property.
        :returns: The zero based index. Negative value if not found.'''
        ...
    
    def remove(self, name: str) -> None:
        '''Removes a property with the specified name from the collection.
        
        :param name: The case-insensitive name of the property.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes a property at the specified index.
        
        :param index: The zero based index.'''
        ...
    
    def clear(self) -> None:
        '''Removes all properties from the collection.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets number of items in the collection.'''
        ...
    
    ...

class DocumentSecurity:
    '''Used as a value for the :attr:`BuiltInDocumentProperties.security` property.
    Specifies the security level of a document as a numeric value.'''
    
    NONE: int
    PASSWORD_PROTECTED: int
    READ_ONLY_RECOMMENDED: int
    READ_ONLY_ENFORCED: int
    READ_ONLY_EXCEPT_ANNOTATIONS: int

class PropertyType:
    '''Specifies data type of a document property.'''
    
    BOOLEAN: int
    DATE_TIME: int
    DOUBLE: int
    NUMBER: int
    STRING: int
    STRING_ARRAY: int
    OBJECT_ARRAY: int
    BYTE_ARRAY: int
    OTHER: int

