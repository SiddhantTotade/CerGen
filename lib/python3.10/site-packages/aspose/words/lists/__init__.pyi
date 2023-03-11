import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class List:
    '''Represents formatting of a list.
    To learn more, visit the `Working with Lists <https://docs.aspose.com/words/net/working-with-lists/>` documentation article.
    
    A list in a Microsoft Word document is a set of list formatting properties.
    Each list can have up to 9 levels and formatting properties, such as number style, start value,
    indent, tab position etc are defined separately for each level.
    
    A :class:`List` object always belongs to the :class:`ListCollection` collection.
    
    To create a new list, use the Add methods of the :class:`ListCollection` collection.
    
    To modify formatting of a list, use :class:`ListLevel` objects found in
    the :attr:`List.list_levels` collection.
    
    To apply or remove list formatting from a paragraph, use :class:`ListFormat`.'''
    
    @overload
    def compare_to(self, obj: object) -> int:
        '''Compares the specified object to the current object.'''
        ...
    
    @overload
    def compare_to(self, other: aspose.words.lists.List) -> int:
        '''Compares the specified list to the current list.'''
        ...
    
    def equals(self, list: aspose.words.lists.List) -> bool:
        '''Compares with the specified list.'''
        ...
    
    def has_same_template(self, other: aspose.words.lists.List) -> bool:
        '''Returns true if the current list and the given list are created from the same template.'''
        ...
    
    @property
    def list_id(self) -> int:
        '''Gets the unique identifier of the list.
        
        You do not normally need to use this property. But if you use it, you normally do so
        in conjunction with the :meth:`ListCollection.get_list_by_list_id` method to find a
        list by its identifier.'''
        ...
    
    @property
    def document(self) -> aspose.words.DocumentBase:
        '''Gets the owner document.
        
        A list always has a parent document and is valid only in the context of that document.'''
        ...
    
    @property
    def is_multi_level(self) -> bool:
        '''Returns ``True`` when the list contains 9 levels; ``False`` when 1 level.
        
        The lists that you create with Aspose.Words are always multi-level lists and contain 9 levels.
        
        Microsoft Word 2003 and later always create multi-level lists with 9 levels.
        But in some documents, created with earlier versions of Microsoft Word you might encounter
        lists that have 1 level only.'''
        ...
    
    @property
    def list_levels(self) -> aspose.words.lists.ListLevelCollection:
        '''Gets the collection of list levels for this list.
        
        Use this property to access and modify formatting individual to each level of the list.'''
        ...
    
    @property
    def is_restart_at_each_section(self) -> bool:
        '''Specifies whether list should be restarted at each section.
        Default value is ``False``.
        
        This option is supported only in RTF, DOC and DOCX document formats.
        
        This option will be written to DOCX only if :class:`aspose.words.saving.OoxmlCompliance` is higher then :attr:`aspose.words.saving.OoxmlCompliance.ECMA376_2006`.'''
        ...
    
    @is_restart_at_each_section.setter
    def is_restart_at_each_section(self, value: bool):
        ...
    
    @property
    def is_list_style_definition(self) -> bool:
        '''Returns ``True`` if this list is a definition of a list style.
        
        When this property is ``True``, the :attr:`List.style` property returns the list style that
        this list defines.
        
        By modifying properties of a list that defines a list style, you modify the properties
        of the list style.
        
        A list that is a definition of a list style cannot be applied directly to paragraphs
        to make them numbered.'''
        ...
    
    @property
    def is_list_style_reference(self) -> bool:
        '''Returns ``True`` if this list is a reference to a list style.
        
        Note, modifying properties of a list that is a reference to list style has no effect.
        The list formatting specified in the list style itself always takes precedence.'''
        ...
    
    @property
    def style(self) -> aspose.words.Style:
        '''Gets the list style that this list references or defines.
        
        If this list is not associated with a list style, the property will return ``None``.
        
        A list could be a reference to a list style, in this case :attr:`List.is_list_style_reference`
        will be ``True``.
        
        A list could be a definition of a list style, in this case :attr:`List.is_list_style_definition`
        will be ``True``. Such a list cannot be applied to paragraphs in the document directly.'''
        ...
    
    ...

class ListCollection:
    '''Stores and manages formatting of bulleted and numbered lists used in a document.
    To learn more, visit the `Working with Lists <https://docs.aspose.com/words/net/working-with-lists/>` documentation article.
    
    A list in a Microsoft Word document is a set of list formatting properties.
    The formatting of the lists is stored in the :class:`ListCollection` collection separately
    from the paragraphs of text.
    
    You do not create objects of this class. There is always only one :class:`ListCollection`
    object per document and it is accessible via the :attr:`aspose.words.DocumentBase.lists` property.
    
    To create a new list based on a predefined list template or based on a list style,
    use the :meth:`ListCollection.add` method.
    
    To create a new list with formatting identical to an existing list,
    use the :meth:`ListCollection.add_copy` method.
    
    To make a paragraph bulleted or numbered, you need to apply list formatting
    to a paragraph by assigning a :class:`List` object to the
    :attr:`ListFormat.list` property of :class:`ListFormat`.
    
    To remove list formatting from a paragraph, use the :meth:`ListFormat.remove_numbers`
    method.
    
    If you know a bit about WordprocessingML, then you might know it defines separate concepts
    for "list" and "list definition". This exactly corresponds to how list formatting is stored
    in a Microsoft Word document at the low level. List definition is like a "schema" and
    list is like an instance of a list definition.
    
    To simplify programming model, Aspose.Words hides the distinction between list and list
    definition in much the same way like Microsoft Word hides this in its user interface.
    This allows you to concentrate more on how you want your document to look like, rather than
    building low-level objects to satisfy requirements of the Microsoft Word file format.
    
    It is not possible to delete lists once they are created in the current version of Aspose.Words.
    This is similar to Microsoft Word where user does not have explicit control over list definitions.'''
    
    def __getitem__(self, index: int) -> aspose.words.lists.List:
        '''Gets a list by index.'''
        ...
    
    @overload
    def add(self, list_template: aspose.words.lists.ListTemplate) -> aspose.words.lists.List:
        '''Creates a new list based on a predefined template and adds it to the collection of lists in the document.
        
        :param list_template: The template of the list.
        :returns: The newly created list.
        
        Aspose.Words list templates correspond to the 21 list templates available
        in the Bullets and Numbering dialog box in Microsoft Word 2003.
        
        All lists created using this method have 9 list levels.'''
        ...
    
    @overload
    def add(self, list_style: aspose.words.Style) -> aspose.words.lists.List:
        '''Creates a new list that references a list style and adds it to the collection of lists in the document.
        
        :param list_style: The list style.
        :returns: The newly created list.
        
        The newly created list references the list style. If you change the properties of the list
        style, it is reflected in the properties of the list. Vice versa, if you change the properties
        of the list, it is reflected in the properties of the list style.'''
        ...
    
    def add_copy(self, src_list: aspose.words.lists.List) -> aspose.words.lists.List:
        '''Creates a new list by copying the specified list and adding it to the collection of lists in the document.
        
        :param src_list: The source list to copy from.
        :returns: The newly created list.
        
        The source list can be from any document. If the source list belongs to a different document,
        a copy of the list is created and added to the current document.
        
        If the source list is a reference to or a definition of a list style,
        the newly created list is not related to the original list style.'''
        ...
    
    def get_list_by_list_id(self, list_id: int) -> aspose.words.lists.List:
        '''Gets a list by a list identifier.
        
        :param list_id: The list identifier.
        :returns: Returns the list object. Returns ``None`` if a list with the specified identifier was not found.
        
        You don't normally need to use this method. Most of the time you apply list formatting
        to paragraphs just by settings the :attr:`ListFormat.list` property
        of the :class:`ListFormat` object.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the count of numbered and bulleted lists in the document.'''
        ...
    
    @property
    def document(self) -> aspose.words.DocumentBase:
        '''Gets the owner document.'''
        ...
    
    ...

class ListFormat:
    '''Allows to control what list formatting is applied to a paragraph.
    To learn more, visit the `Working with Lists <https://docs.aspose.com/words/net/working-with-lists/>` documentation article.
    
    A paragraph in a Microsoft Word document can be bulleted or numbered.
    When a paragraph is bulleted or numbered, it is said that list formatting
    is applied to the paragraph.
    
    You do not create objects of the :class:`ListFormat` class directly.
    You access :class:`ListFormat` as a property of another object that can
    have list formatting associated with it. At the moment the objects that can
    have list formatting are: :class:`aspose.words.Paragraph`,
    :class:`aspose.words.Style` and :class:`aspose.words.DocumentBuilder`.
    
    :class:`ListFormat` of a :class:`aspose.words.Paragraph` specifies
    what list formatting and list level is applied to that particular paragraph.
    
    :class:`ListFormat` of a :class:`aspose.words.Style` (applicable
    to paragraph styles only) allows to specify what list formatting and list level
    is applied to all paragraphs of that particular style.
    
    :class:`ListFormat` of a :class:`aspose.words.DocumentBuilder`
    provides access to the list formatting at the current cursor position
    inside the :class:`aspose.words.DocumentBuilder`.
    
    The list formatting itself is stored inside a :class:`List`
    object that is stored separately from the paragraphs. The list objects
    are stored inside a :class:`ListCollection` collection. There is a single
    :class:`ListCollection` collection per :class:`aspose.words.Document`.
    
    The paragraphs do not physically belong to a list. The paragraphs just
    reference a particular list object via the :attr:`ListFormat.list` property
    and a particular level in the list via the :attr:`ListFormat.list_level_number` property.
    By setting these two properties you control what bullets and numbering is
    applied to a paragraph.'''
    
    def apply_bullet_default(self) -> None:
        '''Starts a new default bulleted list and applies it to the paragraph.
        
        This is a shortcut method that creates a new list using the default bulleted
        template, applies it to the paragraph and selects the 1st list level.'''
        ...
    
    def apply_number_default(self) -> None:
        '''Starts a new default numbered list and applies it to the paragraph.
        
        This is a shortcut method that creates a new list using the default numbered
        template, applies it to the paragraph and selects the 1st list level.'''
        ...
    
    def remove_numbers(self) -> None:
        '''Removes numbers or bullets from the current paragraph and sets list level to zero.
        
        Calling this method is equivalent to setting the :attr:`ListFormat.list` property to ``None``.'''
        ...
    
    def list_indent(self) -> None:
        '''Increases the list level of the current paragraph by one level.
        
        This method changes the list level and applies formatting properties of the new level.
        
        In Word documents, lists may consist of up to nine levels. List formatting
        for each level specifies what bullet or number is used, left indent, space between
        the bullet and text etc.'''
        ...
    
    def list_outdent(self) -> None:
        '''Decreases the list level of the current paragraph by one level.
        
        This method changes the list level and applies formatting properties of the new level.
        
        In Word documents, lists may consist of up to nine levels. List formatting
        for each level specifies what bullet or number is used, left indent, space between
        the bullet and text etc.'''
        ...
    
    @property
    def list_level_number(self) -> int:
        '''Gets or sets the list level number (0 to 8) for the paragraph.
        
        In Word documents, lists may consist of 1 or 9 levels, numbered 0 to 8.
        
        Has effect only when the :attr:`ListFormat.list` property is set to reference a valid list.'''
        ...
    
    @list_level_number.setter
    def list_level_number(self, value: int):
        ...
    
    @property
    def is_list_item(self) -> bool:
        '''True when the paragraph has bulleted or numbered formatting applied to it.'''
        ...
    
    @property
    def list(self) -> aspose.words.lists.List:
        '''Gets or sets the list this paragraph is a member of.
        
        The list that is being assigned to this property must belong to the current document.
        
        The list that is being assigned to this property must not be a list style definition.
        
        Setting this property to ``None`` removes bullets and numbering from the paragraph
        and sets the list level number to zero. Setting this property to ``None`` is equivalent
        to calling :meth:`ListFormat.remove_numbers`.'''
        ...
    
    @list.setter
    def list(self, value: aspose.words.lists.List):
        ...
    
    @property
    def list_level(self) -> aspose.words.lists.ListLevel:
        '''Returns the list level formatting plus any formatting overrides applied to the current paragraph.'''
        ...
    
    ...

class ListLabel:
    '''Defines properties specific to a list label.
    To learn more, visit the `Working with Lists <https://docs.aspose.com/words/net/working-with-lists/>` documentation article.'''
    
    @property
    def font(self) -> aspose.words.Font:
        '''Gets the list label font.'''
        ...
    
    @property
    def label_string(self) -> str:
        '''Gets a string representation of list label.'''
        ...
    
    @property
    def label_value(self) -> int:
        '''Gets a numeric value for this label.
        
        Use the :meth:`aspose.words.Document.update_list_labels` method to update the value of this property.'''
        ...
    
    ...

class ListLevel:
    '''Defines formatting for a list level.
    To learn more, visit the `Working with Lists <https://docs.aspose.com/words/net/working-with-lists/>` documentation article.
    
    You do not create objects of this class. List level objects are created automatically
    when a list is created. You access :class:`ListLevel` objects via the
    :class:`ListLevelCollection` collection.
    
    Use the properties of :class:`ListLevel` to specify list formatting
    for individual list levels.'''
    
    def create_picture_bullet(self) -> None:
        '''Creates picture bullet shape for the current list level.
        
        Please note, :attr:`ListLevel.number_style` will be set to :attr:`aspose.words.NumberStyle.BULLET` and
        :attr:`ListLevel.number_format` to "\\xF0B7" to properly display picture bullet.
        Red cross image will be set as picture bullet image upon creating.
        To change it please use :attr:`ListLevel.image_data`.'''
        ...
    
    def delete_picture_bullet(self) -> None:
        '''Deletes picture bullet for the current list level.
        
        Default bullet will be shown after deleting.'''
        ...
    
    @staticmethod
    def get_effective_value(self, index: int, number_style: aspose.words.NumberStyle, custom_number_style_format: str) -> str:
        '''Reports the string representation of the :class:`ListLevel` object for the specified index
        of the list item. Parameters specify the :class:`aspose.words.NumberStyle` and an optional format string
        used when :attr:`aspose.words.NumberStyle.CUSTOM` is specified.
        
        :param index: The index of the list item (must be in the range from 1 to 32767).
        :param number_style: The :class:`aspose.words.NumberStyle` of the :class:`ListLevel` object.
        :param custom_number_style_format: The optional format string used when :attr:`aspose.words.NumberStyle.CUSTOM` is specified (e.g. "a, ç, ĝ, ...").
                                           In other cases, this parameter must be ``None`` or empty.
        :returns: The string representation of the :class:`ListLevel` object, described by the  parameter and
                  the parameter, in the list item at the position determined by the parameter.
        
        :raises System.ArgumentException: is``None`` or empty when the  is custom.-or- is not``None`` or empty when the  is non-custom.-or- is invalid.
        :raises System.ArgumentOutOfRangeException: index is out of range.'''
        ...
    
    def equals(self, level: aspose.words.lists.ListLevel) -> bool:
        '''Compares with the specified ListLevel.'''
        ...
    
    @property
    def start_at(self) -> int:
        '''Returns or sets the starting number for this list level.
        
        Default value is 1.'''
        ...
    
    @start_at.setter
    def start_at(self, value: int):
        ...
    
    @property
    def number_style(self) -> aspose.words.NumberStyle:
        '''Returns or sets the number style for this list level.'''
        ...
    
    @number_style.setter
    def number_style(self, value: aspose.words.NumberStyle):
        ...
    
    @property
    def custom_number_style_format(self) -> str:
        '''Gets the custom number style format for this list level. For example: "a, ç, ĝ, ...".'''
        ...
    
    @property
    def number_format(self) -> str:
        '''Returns or sets the number format for the list level.
        
        Among normal text characters, the string can contain placeholder characters \\x0000 to \\x0008
        representing the numbers from the corresponding list levels.
        
        For example, the string "\\x0000.\\x0001)" will generate a list label
        that looks something like "1.5)". The number "1" is the current number from
        the 1st list level, the number "5" is the current number from the 2nd list level.
        
        Null is not allowed, but an empty string meaning no number is valid.'''
        ...
    
    @number_format.setter
    def number_format(self, value: str):
        ...
    
    @property
    def alignment(self) -> aspose.words.lists.ListLevelAlignment:
        '''Gets or sets the justification of the actual number of the list item.
        
        The list label is justified relative to the :attr:`ListLevel.number_position` property.'''
        ...
    
    @alignment.setter
    def alignment(self, value: aspose.words.lists.ListLevelAlignment):
        ...
    
    @property
    def is_legal(self) -> bool:
        '''True if the level turns all inherited numbers to Arabic, false if it preserves their number style.'''
        ...
    
    @is_legal.setter
    def is_legal(self, value: bool):
        ...
    
    @property
    def restart_after_level(self) -> int:
        '''Sets or returns the list level that must appear before the specified list level restarts numbering.
        
        The value of -1 means the numbering will continue.'''
        ...
    
    @restart_after_level.setter
    def restart_after_level(self, value: int):
        ...
    
    @property
    def trailing_character(self) -> aspose.words.lists.ListTrailingCharacter:
        '''Returns or sets the character inserted after the number for the list level.'''
        ...
    
    @trailing_character.setter
    def trailing_character(self, value: aspose.words.lists.ListTrailingCharacter):
        ...
    
    @property
    def font(self) -> aspose.words.Font:
        '''Specifies character formatting used for the list label.'''
        ...
    
    @property
    def tab_position(self) -> float:
        '''Returns or sets the tab position (in points) for the list level.
        
        Has effect only when :attr:`ListLevel.trailing_character` is a tab.'''
        ...
    
    @tab_position.setter
    def tab_position(self, value: float):
        ...
    
    @property
    def number_position(self) -> float:
        '''Returns or sets the position (in points) of the number or bullet for the list level.
        
        :attr:`ListLevel.number_position` corresponds to LeftIndent plus FirstLineIndent of the paragraph.'''
        ...
    
    @number_position.setter
    def number_position(self, value: float):
        ...
    
    @property
    def text_position(self) -> float:
        '''Returns or sets the position (in points) for the second line of wrapping text for the list level.
        
        :attr:`ListLevel.text_position` corresponds to LeftIndent of the paragraph.'''
        ...
    
    @text_position.setter
    def text_position(self, value: float):
        ...
    
    @property
    def linked_style(self) -> aspose.words.Style:
        '''Gets or sets the paragraph style that is linked to this list level.
        
        This property is ``None`` when the list level is not linked to a paragraph style.
        This property can be set to ``None``.'''
        ...
    
    @linked_style.setter
    def linked_style(self, value: aspose.words.Style):
        ...
    
    @property
    def image_data(self) -> aspose.words.drawing.ImageData:
        '''Returns image data of the picture bullet shape for the current list level.
        
        If this level doesn't define picture bullet returns ``None``.
        Before setting new image for non picture bullet shape, please use :meth:`ListLevel.create_picture_bullet` method first.'''
        ...
    
    ...

class ListLevelCollection:
    '''A collection of list formatting for each level in a list.
    To learn more, visit the `Working with Lists <https://docs.aspose.com/words/net/working-with-lists/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.lists.ListLevel:
        '''Gets a list level by index.'''
        ...
    
    def __setitem__(self, index: int, value: aspose.words.lists.ListLevel):
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of levels in this list.
        
        There could be 1 or 9 levels in a list.'''
        ...
    
    ...

class ListLevelAlignment:
    '''Specifies alignment for the list number or bullet.
    
    Used as a value for the :attr:`ListLevel.alignment` property.'''
    
    LEFT: int
    CENTER: int
    RIGHT: int

class ListTemplate:
    '''Specifies one of the predefined list formats available in Microsoft Word.
    
    A list template value is used as a parameter into the
    :meth:`ListCollection.add` method.
    
    Aspose.Words list templates correspond to the 21 list templates available
    in the Bullets and Numbering dialog box in Microsoft Word 2003.'''
    
    BULLET_DEFAULT: int
    BULLET_DISK: int
    BULLET_CIRCLE: int
    BULLET_SQUARE: int
    BULLET_DIAMONDS: int
    BULLET_ARROW_HEAD: int
    BULLET_TICK: int
    NUMBER_DEFAULT: int
    NUMBER_ARABIC_DOT: int
    NUMBER_ARABIC_PARENTHESIS: int
    NUMBER_UPPERCASE_ROMAN_DOT: int
    NUMBER_UPPERCASE_LETTER_DOT: int
    NUMBER_LOWERCASE_LETTER_PARENTHESIS: int
    NUMBER_LOWERCASE_LETTER_DOT: int
    NUMBER_LOWERCASE_ROMAN_DOT: int
    OUTLINE_NUMBERS: int
    OUTLINE_LEGAL: int
    OUTLINE_BULLETS: int
    OUTLINE_HEADINGS_ARTICLE_SECTION: int
    OUTLINE_HEADINGS_LEGAL: int
    OUTLINE_HEADINGS_NUMBERS: int
    OUTLINE_HEADINGS_CHAPTER: int

class ListTrailingCharacter:
    '''Specifies the character that separates the list label from the text of the paragraph.
    
    Used as a value for the :attr:`ListLevel.trailing_character` property.'''
    
    TAB: int
    SPACE: int
    NOTHING: int

