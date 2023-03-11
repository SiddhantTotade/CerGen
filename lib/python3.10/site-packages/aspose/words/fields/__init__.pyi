import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class BarcodeParameters:
    '''Container class for barcode parameters to pass-through to BarcodeGenerator.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    The set of parameters are according to DISPLAYBARCODE field options.
    See the exact list at https://msdn.microsoft.com/en-us/library/hh745901(v=office.12).aspx'''
    
    def __init__(self):
        ...
    
    @property
    def barcode_type(self) -> str:
        '''Bar code type.'''
        ...
    
    @barcode_type.setter
    def barcode_type(self, value: str):
        ...
    
    @property
    def barcode_value(self) -> str:
        '''Data to be encoded.'''
        ...
    
    @barcode_value.setter
    def barcode_value(self, value: str):
        ...
    
    @property
    def symbol_height(self) -> str:
        '''Bar code image height (in twips - 1/1440 inches)'''
        ...
    
    @symbol_height.setter
    def symbol_height(self, value: str):
        ...
    
    @property
    def foreground_color(self) -> str:
        '''Bar code foreground color (0x000000 - 0xFFFFFF)'''
        ...
    
    @foreground_color.setter
    def foreground_color(self, value: str):
        ...
    
    @property
    def background_color(self) -> str:
        '''Bar code background color (0x000000 - 0xFFFFFF)'''
        ...
    
    @background_color.setter
    def background_color(self, value: str):
        ...
    
    @property
    def symbol_rotation(self) -> str:
        '''Rotation of the barcode symbol. Valid values are [0, 3].'''
        ...
    
    @symbol_rotation.setter
    def symbol_rotation(self, value: str):
        ...
    
    @property
    def scaling_factor(self) -> str:
        '''Scaling factor for the symbol. The value is in whole percentage points and the valid values are [10, 1000].'''
        ...
    
    @scaling_factor.setter
    def scaling_factor(self, value: str):
        ...
    
    @property
    def pos_code_style(self) -> str:
        '''Style of a Point of Sale barcode (barcode types UPCA|UPCE|EAN13|EAN8). The valid values (case insensitive) are [STD|SUP2|SUP5|CASE].'''
        ...
    
    @pos_code_style.setter
    def pos_code_style(self, value: str):
        ...
    
    @property
    def case_code_style(self) -> str:
        '''Style of a Case Code for barcode type ITF14. The valid values are [STD|EXT|ADD]'''
        ...
    
    @case_code_style.setter
    def case_code_style(self, value: str):
        ...
    
    @property
    def error_correction_level(self) -> str:
        '''Error correction level of QR Code. Valid values are [0, 3].'''
        ...
    
    @error_correction_level.setter
    def error_correction_level(self, value: str):
        ...
    
    @property
    def display_text(self) -> bool:
        '''Whether to display barcode data (text) along with image.'''
        ...
    
    @display_text.setter
    def display_text(self, value: bool):
        ...
    
    @property
    def add_start_stop_char(self) -> bool:
        '''Whether to add Start/Stop characters for barcode types NW7 and CODE39.'''
        ...
    
    @add_start_stop_char.setter
    def add_start_stop_char(self, value: bool):
        ...
    
    @property
    def fix_check_digit(self) -> bool:
        '''Whether to fix the check digit if it’s invalid.'''
        ...
    
    @fix_check_digit.setter
    def fix_check_digit(self, value: bool):
        ...
    
    @property
    def postal_address(self) -> str:
        '''Barcode postal address.'''
        ...
    
    @postal_address.setter
    def postal_address(self, value: str):
        ...
    
    @property
    def is_bookmark(self) -> bool:
        '''Whether :attr:`BarcodeParameters.postal_address` is the name of a bookmark.'''
        ...
    
    @is_bookmark.setter
    def is_bookmark(self, value: bool):
        ...
    
    @property
    def facing_identification_mark(self) -> str:
        '''Type of a Facing Identification Mark (FIM).'''
        ...
    
    @facing_identification_mark.setter
    def facing_identification_mark(self, value: str):
        ...
    
    @property
    def is_us_postal_address(self) -> bool:
        '''Whether :attr:`BarcodeParameters.postal_address` is a U.S. postal address.'''
        ...
    
    @is_us_postal_address.setter
    def is_us_postal_address(self, value: bool):
        ...
    
    ...

class ComparisonEvaluationResult:
    '''The comparison evaluation result.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    @overload
    def __init__(self, result: bool):
        '''Creates a comparison evaluation result.'''
        ...
    
    @overload
    def __init__(self, error_message: str):
        '''Creates a failed comparison evaluation result with the corresponding error message.'''
        ...
    
    @property
    def result(self) -> bool:
        '''Gets the comparison evaluation result.'''
        ...
    
    @property
    def error_message(self) -> str:
        '''Gets the failed comparison evaluation result's error message.'''
        ...
    
    ...

class ComparisonExpression:
    '''The comparison expression.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    @property
    def left_expression(self) -> str:
        '''Gets the left expression.'''
        ...
    
    @property
    def comparison_operator(self) -> str:
        '''Gets the comparison operator.'''
        ...
    
    @property
    def right_expression(self) -> str:
        '''Gets the right expression.'''
        ...
    
    ...

class DropDownItemCollection:
    '''A collection of strings that represent all the items in a drop-down form field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __getitem__(self, index: int) -> str:
        '''Gets or sets the element at the specified index.'''
        ...
    
    def __setitem__(self, index: int, value: str):
        ...
    
    def add(self, value: str) -> int:
        '''Adds a string to the end of the collection.
        
        :param value: The string to add to the end of the collection.
        :returns: The zero-based index at which the new element is inserted.'''
        ...
    
    def contains(self, value: str) -> bool:
        '''Determines whether the collection contains the specified value.
        
        :param value: Case-sensitive value to locate.
        :returns: ``True`` if the item is found in the collection; otherwise, ``False``.'''
        ...
    
    def index_of(self, value: str) -> int:
        '''Returns the zero-based index of the specified value in the collection.
        
        :param value: The case-sensitive value to locate.
        :returns: The zero based index. Negative value if not found.'''
        ...
    
    def insert(self, index: int, value: str) -> None:
        '''Inserts a string into the collection at the specified index.
        
        :param index: The zero-based index at which value is inserted.
        :param value: The string to insert.'''
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
    
    @property
    def count(self) -> int:
        '''Gets the number of elements contained in the collection.'''
        ...
    
    ...

class Field:
    '''Represents a Microsoft Word document field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    A field in a Word document is a complex structure consisting of multiple nodes that include field start,
    field code, field separator, field result and field end. Fields can be nested, contain rich content and span
    multiple paragraphs or sections in a document. The :class:`Field` class is a "facade" object that provides
    properties and methods that allow to work with a field as a single object.
    
    The :attr:`Field.start`, :attr:`Field.separator` and :attr:`Field.end` properties point to the
    field start, separator and end nodes of the field respectively.
    
    The content between the field start and separator is the field code. The content between the
    field separator and field end is the field result. The field code typically consists of one or more
    :class:`aspose.words.Run` objects that specify instructions. The processing application is expected to execute
    the field code to calculate the field result.
    
    The process of calculating field results is called the field update. Aspose.Words can update field
    results of most of the field types in exactly the same way as Microsoft Word does it. Most notably,
    Aspose.Words can calculate results of even the most complex formula fields. To calculate the field
    result of a single field use the :meth:`Field.update` method. To update fields in the whole document
    use :meth:`aspose.words.Document.update_fields`.
    
    You can get the plain text version of the field code using the :meth:`Field.get_field_code` method.
    You can get and set the plain text version of the field result using the :attr:`Field.result` property.
    Both the field code and field result can contain complex content, such as nested fields, paragraphs, shapes,
    tables and in this case you might want to work with the field nodes directly if you need more control.
    
    You do not create instances of the :class:`Field` class directly.
    To create a new field use the :meth:`aspose.words.DocumentBuilder.insert_field` method.'''
    
    @overload
    def get_field_code(self) -> str:
        '''Returns text between field start and field separator (or field end if there is no separator).
        Both field code and field result of child fields are included.'''
        ...
    
    @overload
    def get_field_code(self, include_child_field_codes: bool) -> str:
        '''Returns text between field start and field separator (or field end if there is no separator).
        
        :param include_child_field_codes: ``True`` if child field codes should be included.'''
        ...
    
    @overload
    def update(self) -> None:
        '''Performs the field update. Throws if the field is being updated already.'''
        ...
    
    @overload
    def update(self, ignore_merge_format: bool) -> None:
        '''Performs a field update. Throws if the field is being updated already.
        
        :param ignore_merge_format: If ``True`` then direct field result formatting is abandoned, regardless of the MERGEFORMAT switch, otherwise normal update is performed.'''
        ...
    
    def remove(self) -> aspose.words.Node:
        '''Removes the field from the document. Returns a node right after the field. If the field's end is the last child
        of its parent node, returns its parent paragraph. If the field is already removed, returns ``None``.'''
        ...
    
    def unlink(self) -> bool:
        '''Performs the field unlink.
        
        Replaces the field with its most recent result.
        
        Some fields, such as XE (Index Entry) fields and SEQ (Sequence) fields, cannot be unlinked.
        
        :returns: ``True`` if the field has been unlinked, otherwise ``False``.'''
        ...
    
    def as_field(self) -> aspose.words.fields.Field:
        ...
    
    def as_field_unknown(self) -> aspose.words.fields.FieldUnknown:
        ...
    
    def as_field_merge_barcode(self) -> aspose.words.fields.FieldMergeBarcode:
        ...
    
    def as_field_display_barcode(self) -> aspose.words.fields.FieldDisplayBarcode:
        ...
    
    def as_field_print(self) -> aspose.words.fields.FieldPrint:
        ...
    
    def as_field_private(self) -> aspose.words.fields.FieldPrivate:
        ...
    
    def as_field_advance(self) -> aspose.words.fields.FieldAdvance:
        ...
    
    def as_field_form_check_box(self) -> aspose.words.fields.FieldFormCheckBox:
        ...
    
    def as_field_form_drop_down(self) -> aspose.words.fields.FieldFormDropDown:
        ...
    
    def as_field_index(self) -> aspose.words.fields.FieldIndex:
        ...
    
    def as_field_rd(self) -> aspose.words.fields.FieldRD:
        ...
    
    def as_field_ta(self) -> aspose.words.fields.FieldTA:
        ...
    
    def as_field_toa(self) -> aspose.words.fields.FieldToa:
        ...
    
    def as_field_ask(self) -> aspose.words.fields.FieldAsk:
        ...
    
    def as_field_auto_text(self) -> aspose.words.fields.FieldAutoText:
        ...
    
    def as_field_auto_text_list(self) -> aspose.words.fields.FieldAutoTextList:
        ...
    
    def as_field_bibliography(self) -> aspose.words.fields.FieldBibliography:
        ...
    
    def as_field_citation(self) -> aspose.words.fields.FieldCitation:
        ...
    
    def as_field_dde(self) -> aspose.words.fields.FieldDde:
        ...
    
    def as_field_dde_auto(self) -> aspose.words.fields.FieldDdeAuto:
        ...
    
    def as_field_fill_in(self) -> aspose.words.fields.FieldFillIn:
        ...
    
    def as_field_glossary(self) -> aspose.words.fields.FieldGlossary:
        ...
    
    def as_field_import(self) -> aspose.words.fields.FieldImport:
        ...
    
    def as_field_include(self) -> aspose.words.fields.FieldInclude:
        ...
    
    def as_field_shape(self) -> aspose.words.fields.FieldShape:
        ...
    
    def as_field_database(self) -> aspose.words.fields.FieldDatabase:
        ...
    
    def as_field_skip_if(self) -> aspose.words.fields.FieldSkipIf:
        ...
    
    def as_field_list_num(self) -> aspose.words.fields.FieldListNum:
        ...
    
    def as_field_rev_num(self) -> aspose.words.fields.FieldRevNum:
        ...
    
    def as_field_section(self) -> aspose.words.fields.FieldSection:
        ...
    
    def as_field_section_pages(self) -> aspose.words.fields.FieldSectionPages:
        ...
    
    def as_field_data(self) -> aspose.words.fields.FieldData:
        ...
    
    def as_field_embed(self) -> aspose.words.fields.FieldEmbed:
        ...
    
    def as_field_ocx(self) -> aspose.words.fields.FieldOcx:
        ...
    
    def as_field_auto_num(self) -> aspose.words.fields.FieldAutoNum:
        ...
    
    def as_field_auto_num_lgl(self) -> aspose.words.fields.FieldAutoNumLgl:
        ...
    
    def as_field_auto_num_out(self) -> aspose.words.fields.FieldAutoNumOut:
        ...
    
    def as_field_add_in(self) -> aspose.words.fields.FieldAddIn:
        ...
    
    def as_field_barcode(self) -> aspose.words.fields.FieldBarcode:
        ...
    
    def as_field_bidi_outline(self) -> aspose.words.fields.FieldBidiOutline:
        ...
    
    def as_field_eq(self) -> aspose.words.fields.FieldEQ:
        ...
    
    def as_field_footnote_ref(self) -> aspose.words.fields.FieldFootnoteRef:
        ...
    
    def as_field_info(self) -> aspose.words.fields.FieldInfo:
        ...
    
    def as_field_user_address(self) -> aspose.words.fields.FieldUserAddress:
        ...
    
    def as_field_user_initials(self) -> aspose.words.fields.FieldUserInitials:
        ...
    
    def as_field_user_name(self) -> aspose.words.fields.FieldUserName:
        ...
    
    def as_field_include_picture(self) -> aspose.words.fields.FieldIncludePicture:
        ...
    
    def as_field_page(self) -> aspose.words.fields.FieldPage:
        ...
    
    def as_field_create_date(self) -> aspose.words.fields.FieldCreateDate:
        ...
    
    def as_field_edit_time(self) -> aspose.words.fields.FieldEditTime:
        ...
    
    def as_field_print_date(self) -> aspose.words.fields.FieldPrintDate:
        ...
    
    def as_field_save_date(self) -> aspose.words.fields.FieldSaveDate:
        ...
    
    def as_field_go_to_button(self) -> aspose.words.fields.FieldGoToButton:
        ...
    
    def as_field_author(self) -> aspose.words.fields.FieldAuthor:
        ...
    
    def as_field_comments(self) -> aspose.words.fields.FieldComments:
        ...
    
    def as_field_file_name(self) -> aspose.words.fields.FieldFileName:
        ...
    
    def as_field_file_size(self) -> aspose.words.fields.FieldFileSize:
        ...
    
    def as_field_keywords(self) -> aspose.words.fields.FieldKeywords:
        ...
    
    def as_field_last_saved_by(self) -> aspose.words.fields.FieldLastSavedBy:
        ...
    
    def as_field_num_chars(self) -> aspose.words.fields.FieldNumChars:
        ...
    
    def as_field_num_pages(self) -> aspose.words.fields.FieldNumPages:
        ...
    
    def as_field_num_words(self) -> aspose.words.fields.FieldNumWords:
        ...
    
    def as_field_subject(self) -> aspose.words.fields.FieldSubject:
        ...
    
    def as_field_template(self) -> aspose.words.fields.FieldTemplate:
        ...
    
    def as_field_title(self) -> aspose.words.fields.FieldTitle:
        ...
    
    def as_field_formula(self) -> aspose.words.fields.FieldFormula:
        ...
    
    def as_field_symbol(self) -> aspose.words.fields.FieldSymbol:
        ...
    
    def as_field_quote(self) -> aspose.words.fields.FieldQuote:
        ...
    
    def as_field_set(self) -> aspose.words.fields.FieldSet:
        ...
    
    def as_field_address_block(self) -> aspose.words.fields.FieldAddressBlock:
        ...
    
    def as_field_compare(self) -> aspose.words.fields.FieldCompare:
        ...
    
    def as_field_date(self) -> aspose.words.fields.FieldDate:
        ...
    
    def as_field_doc_property(self) -> aspose.words.fields.FieldDocProperty:
        ...
    
    def as_field_doc_variable(self) -> aspose.words.fields.FieldDocVariable:
        ...
    
    def as_field_greeting_line(self) -> aspose.words.fields.FieldGreetingLine:
        ...
    
    def as_field_hyperlink(self) -> aspose.words.fields.FieldHyperlink:
        ...
    
    def as_field_if(self) -> aspose.words.fields.FieldIf:
        ...
    
    def as_field_include_text(self) -> aspose.words.fields.FieldIncludeText:
        ...
    
    def as_field_link(self) -> aspose.words.fields.FieldLink:
        ...
    
    def as_field_macro_button(self) -> aspose.words.fields.FieldMacroButton:
        ...
    
    def as_field_merge_field(self) -> aspose.words.fields.FieldMergeField:
        ...
    
    def as_field_merge_rec(self) -> aspose.words.fields.FieldMergeRec:
        ...
    
    def as_field_merge_seq(self) -> aspose.words.fields.FieldMergeSeq:
        ...
    
    def as_field_next(self) -> aspose.words.fields.FieldNext:
        ...
    
    def as_field_next_if(self) -> aspose.words.fields.FieldNextIf:
        ...
    
    def as_field_note_ref(self) -> aspose.words.fields.FieldNoteRef:
        ...
    
    def as_field_page_ref(self) -> aspose.words.fields.FieldPageRef:
        ...
    
    def as_field_ref(self) -> aspose.words.fields.FieldRef:
        ...
    
    def as_field_seq(self) -> aspose.words.fields.FieldSeq:
        ...
    
    def as_field_style_ref(self) -> aspose.words.fields.FieldStyleRef:
        ...
    
    def as_field_tc(self) -> aspose.words.fields.FieldTC:
        ...
    
    def as_field_time(self) -> aspose.words.fields.FieldTime:
        ...
    
    def as_field_toc(self) -> aspose.words.fields.FieldToc:
        ...
    
    def as_field_xe(self) -> aspose.words.fields.FieldXE:
        ...
    
    def as_field_form_text(self) -> aspose.words.fields.FieldFormText:
        ...
    
    @property
    def start(self) -> aspose.words.fields.FieldStart:
        '''Gets the node that represents the start of the field.'''
        ...
    
    @property
    def separator(self) -> aspose.words.fields.FieldSeparator:
        '''Gets the node that represents the field separator. Can be ``None``.'''
        ...
    
    @property
    def end(self) -> aspose.words.fields.FieldEnd:
        '''Gets the node that represents the field end.'''
        ...
    
    @property
    def type(self) -> aspose.words.fields.FieldType:
        '''Gets the Microsoft Word field type.'''
        ...
    
    @property
    def result(self) -> str:
        '''Gets or sets text that is between the field separator and field end.'''
        ...
    
    @result.setter
    def result(self, value: str):
        ...
    
    @property
    def display_result(self) -> str:
        '''Gets the text that represents the displayed field result.
        
        The :meth:`aspose.words.Document.update_list_labels` method must be called to obtain correct value for the
        :class:`FieldListNum`, :class:`FieldAutoNum`, :class:`FieldAutoNumOut` and :class:`FieldAutoNumLgl` fields.'''
        ...
    
    @property
    def is_locked(self) -> bool:
        '''Gets or sets whether the field is locked (should not recalculate its result).'''
        ...
    
    @is_locked.setter
    def is_locked(self, value: bool):
        ...
    
    @property
    def is_dirty(self) -> bool:
        '''Gets or sets whether the current result of the field is no longer correct (stale) due to other modifications made to the document.'''
        ...
    
    @is_dirty.setter
    def is_dirty(self, value: bool):
        ...
    
    @property
    def format(self) -> aspose.words.fields.FieldFormat:
        '''Gets a :class:`FieldFormat` object that provides typed access to field's formatting.'''
        ...
    
    @property
    def locale_id(self) -> int:
        '''Gets or sets the LCID of the field.'''
        ...
    
    @locale_id.setter
    def locale_id(self, value: int):
        ...
    
    ...

class FieldAddIn(aspose.words.fields.Field):
    '''Implements the ADDIN field.
    
    Contains data created by an add-in.'''
    
    def __init__(self):
        ...
    
    ...

class FieldAddressBlock(aspose.words.fields.Field):
    '''Implements the ADDRESSBLOCK field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Represents an address block. An *address block* is a block of text specifying information
    appropriate for a postal mailing address, in the order required by the destination country.'''
    
    def __init__(self):
        ...
    
    def get_field_names(self) -> list[str]:
        '''Returns a collection of mail merge field names used by the field.'''
        ...
    
    @property
    def format_address_on_country_or_region(self) -> bool:
        '''Gets or sets whether to format the address according to the country/region of the recipient
        as defined by POST\*CODE (Universal Postal Union 2006).'''
        ...
    
    @format_address_on_country_or_region.setter
    def format_address_on_country_or_region(self, value: bool):
        ...
    
    @property
    def include_country_or_region_name(self) -> str:
        '''Gets or sets whether to include the name of the country/region.'''
        ...
    
    @include_country_or_region_name.setter
    def include_country_or_region_name(self, value: str):
        ...
    
    @property
    def excluded_country_or_region_name(self) -> str:
        '''Gets or sets the excluded country/region name.'''
        ...
    
    @excluded_country_or_region_name.setter
    def excluded_country_or_region_name(self, value: str):
        ...
    
    @property
    def name_and_address_format(self) -> str:
        '''Gets or sets the name and address format.'''
        ...
    
    @name_and_address_format.setter
    def name_and_address_format(self, value: str):
        ...
    
    @property
    def language_id(self) -> str:
        '''Gets or sets the language ID used to format the address.'''
        ...
    
    @language_id.setter
    def language_id(self, value: str):
        ...
    
    ...

class FieldAdvance(aspose.words.fields.Field):
    '''Implements the ADVANCE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Moves the starting point at which the text that lexically follows the field is displayed to the right or left,
    up or down, or to a specific horizontal or vertical position.'''
    
    def __init__(self):
        ...
    
    @property
    def down_offset(self) -> str:
        '''Gets or sets the number of points by which the text that follows the field should be moved down.'''
        ...
    
    @down_offset.setter
    def down_offset(self, value: str):
        ...
    
    @property
    def left_offset(self) -> str:
        '''Gets or sets the number of points by which the text that follows the field should be moved left.'''
        ...
    
    @left_offset.setter
    def left_offset(self, value: str):
        ...
    
    @property
    def right_offset(self) -> str:
        '''Gets or sets the number of points by which the text that follows the field should be moved right.'''
        ...
    
    @right_offset.setter
    def right_offset(self, value: str):
        ...
    
    @property
    def up_offset(self) -> str:
        '''Gets or sets the number of points by which the text that follows the field should be moved up.'''
        ...
    
    @up_offset.setter
    def up_offset(self, value: str):
        ...
    
    @property
    def horizontal_position(self) -> str:
        '''Gets or sets the number of points by which the text that follows the field should be moved horizontally
        from the left edge of the column, frame, or text box.'''
        ...
    
    @horizontal_position.setter
    def horizontal_position(self, value: str):
        ...
    
    @property
    def vertical_position(self) -> str:
        '''Gets or sets the number of points by which the text that follows the field should be moved vertically
        from the top edge of the page.'''
        ...
    
    @vertical_position.setter
    def vertical_position(self, value: str):
        ...
    
    ...

class FieldArgumentBuilder:
    '''Builds a complex field argument consisting of fields, nodes, and plain text.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self):
        '''Initializes an instance of the :class:`FieldArgumentBuilder` class.'''
        ...
    
    def add_text(self, text: str) -> aspose.words.fields.FieldArgumentBuilder:
        '''Adds a plain text to the argument.'''
        ...
    
    def add_node(self, node: aspose.words.Inline) -> aspose.words.fields.FieldArgumentBuilder:
        '''Adds a node to the argument.
        
        Only text level nodes are supported at the moment.'''
        ...
    
    def add_field(self, field_builder: aspose.words.fields.FieldBuilder) -> aspose.words.fields.FieldArgumentBuilder:
        '''Adds a field represented by a :class:`FieldBuilder` to the argument.'''
        ...
    
    ...

class FieldAsk(aspose.words.fields.Field):
    '''Implements the ASK field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Prompts the user to enter information and assigns a bookmark to represent the user's response.'''
    
    def __init__(self):
        ...
    
    @property
    def bookmark_name(self) -> str:
        '''Gets or sets the name of the bookmark.'''
        ...
    
    @bookmark_name.setter
    def bookmark_name(self, value: str):
        ...
    
    @property
    def prompt_text(self) -> str:
        '''Gets or sets the prompt text (the title of the prompt window).'''
        ...
    
    @prompt_text.setter
    def prompt_text(self, value: str):
        ...
    
    @property
    def default_response(self) -> str:
        '''Gets or sets default user response (initial value contained in the prompt window).'''
        ...
    
    @default_response.setter
    def default_response(self, value: str):
        ...
    
    @property
    def prompt_once_on_mail_merge(self) -> bool:
        '''Gets or sets whether the user response should be recieved once per a mail merge operation.'''
        ...
    
    @prompt_once_on_mail_merge.setter
    def prompt_once_on_mail_merge(self, value: bool):
        ...
    
    ...

class FieldAuthor(aspose.words.fields.Field):
    '''Implements the AUTHOR field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves, and optionally sets, the document author's name, as recorded in the **Author** property of the
    built-in document properties.'''
    
    def __init__(self):
        ...
    
    @property
    def author_name(self) -> str:
        '''Gets or sets the document author's name.'''
        ...
    
    @author_name.setter
    def author_name(self, value: str):
        ...
    
    ...

class FieldAutoNum(aspose.words.fields.Field):
    '''Implements the AUTONUM field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts an automatic number.'''
    
    def __init__(self):
        ...
    
    @property
    def separator_character(self) -> str:
        '''Gets or sets the separator character to be used.'''
        ...
    
    @separator_character.setter
    def separator_character(self, value: str):
        ...
    
    ...

class FieldAutoNumLgl(aspose.words.fields.Field):
    '''Implements the AUTONUMLGL field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts an automatic number in legal format.'''
    
    def __init__(self):
        ...
    
    @property
    def remove_trailing_period(self) -> bool:
        '''Gets or sets whether to display the number without a trailing period.'''
        ...
    
    @remove_trailing_period.setter
    def remove_trailing_period(self, value: bool):
        ...
    
    @property
    def separator_character(self) -> str:
        '''Gets or sets the separator character to be used.'''
        ...
    
    @separator_character.setter
    def separator_character(self, value: str):
        ...
    
    ...

class FieldAutoNumOut(aspose.words.fields.Field):
    '''Implements the AUTONUMOUT field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts an automatic number in outline format.'''
    
    def __init__(self):
        ...
    
    ...

class FieldAutoText(aspose.words.fields.Field):
    '''Implements the AUTOTEXT field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts an AutoText entry.'''
    
    def __init__(self):
        ...
    
    @property
    def entry_name(self) -> str:
        '''Gets or sets the name of the AutoText entry.'''
        ...
    
    @entry_name.setter
    def entry_name(self, value: str):
        ...
    
    ...

class FieldAutoTextList(aspose.words.fields.Field):
    '''Implements the AUTOTEXTLIST field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Creates a shortcut menu based on AutoText entries in the active template.'''
    
    def __init__(self):
        ...
    
    @property
    def entry_name(self) -> str:
        '''Gets or sets the name of the AutoText entry.'''
        ...
    
    @entry_name.setter
    def entry_name(self, value: str):
        ...
    
    @property
    def list_style(self) -> str:
        '''Gets or sets the name of the style on which the list to contain entries is based.'''
        ...
    
    @list_style.setter
    def list_style(self, value: str):
        ...
    
    @property
    def screen_tip(self) -> str:
        '''Gets or sets the text of the ScreenTip to show.'''
        ...
    
    @screen_tip.setter
    def screen_tip(self, value: str):
        ...
    
    ...

class FieldBarcode(aspose.words.fields.Field):
    '''Implements the BARCODE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts a postal barcode in a machine-readable form of address used by the U.S. Postal Service.'''
    
    def __init__(self):
        ...
    
    @property
    def postal_address(self) -> str:
        '''Gets or sets the postal address used for generating a barcode or the name of the bookmark that refers to it.'''
        ...
    
    @postal_address.setter
    def postal_address(self, value: str):
        ...
    
    @property
    def is_bookmark(self) -> bool:
        '''Gets or sets whether :attr:`FieldBarcode.postal_address` is the name of a bookmark.'''
        ...
    
    @is_bookmark.setter
    def is_bookmark(self, value: bool):
        ...
    
    @property
    def facing_identification_mark(self) -> str:
        '''Gets or sets the type of a Facing Identification Mark (FIM) to insert.'''
        ...
    
    @facing_identification_mark.setter
    def facing_identification_mark(self, value: str):
        ...
    
    @property
    def is_us_postal_address(self) -> bool:
        '''Gets or sets whether :attr:`FieldBarcode.postal_address` is a U.S. postal address.'''
        ...
    
    @is_us_postal_address.setter
    def is_us_postal_address(self, value: bool):
        ...
    
    ...

class FieldBibliography(aspose.words.fields.Field):
    '''Implements the BIBLIOGRAPHY field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts the contents of the document's Bibliography part in a bibliographic style.'''
    
    def __init__(self):
        ...
    
    @property
    def format_language_id(self) -> str:
        '''Gets or sets the language ID that is used to format the bibliographic sources in the document.'''
        ...
    
    @format_language_id.setter
    def format_language_id(self, value: str):
        ...
    
    ...

class FieldBidiOutline(aspose.words.fields.Field):
    '''Implements the BIDIOUTLINE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    This field is identical to the AUTONUMLGL field, except for the separator that delimits each level
    of the paragraph numbering.'''
    
    def __init__(self):
        ...
    
    ...

class FieldBuilder:
    '''Builds a field from field code tokens (arguments and switches).
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self, field_type: aspose.words.fields.FieldType):
        '''Initializes an instance of the :class:`FieldBuilder` class.
        
        :param field_type: The type of the field to build.'''
        ...
    
    @overload
    def add_argument(self, argument: str) -> aspose.words.fields.FieldBuilder:
        '''Adds a field's argument.
        
        :param argument: The argument value.'''
        ...
    
    @overload
    def add_argument(self, argument: int) -> aspose.words.fields.FieldBuilder:
        '''Adds a field's argument.
        
        :param argument: The argument value.'''
        ...
    
    @overload
    def add_argument(self, argument: float) -> aspose.words.fields.FieldBuilder:
        '''Adds a field's argument.
        
        :param argument: The argument value.'''
        ...
    
    @overload
    def add_argument(self, argument: aspose.words.fields.FieldBuilder) -> aspose.words.fields.FieldBuilder:
        '''Adds a child field represented by another :class:`FieldBuilder` to the field's code.
        
        This overload is used when the argument consists of a single child field.'''
        ...
    
    @overload
    def add_argument(self, argument: aspose.words.fields.FieldArgumentBuilder) -> aspose.words.fields.FieldBuilder:
        '''Adds a field's argument represented by :class:`FieldArgumentBuilder` to the field's code.
        
        This overload is used when the argument consists of a mixture of different parts such as child fields, nodes, and plain text.'''
        ...
    
    @overload
    def add_switch(self, switch_name: str) -> aspose.words.fields.FieldBuilder:
        '''Adds a field's switch.
        
        This overload adds a flag (switch without argument).
        
        :param switch_name: The switch name.'''
        ...
    
    @overload
    def add_switch(self, switch_name: str, switch_argument: str) -> aspose.words.fields.FieldBuilder:
        '''Adds a field's switch.
        
        :param switch_name: The switch name.
        :param switch_argument: The switch value.'''
        ...
    
    @overload
    def add_switch(self, switch_name: str, switch_argument: int) -> aspose.words.fields.FieldBuilder:
        '''Adds a field's switch.
        
        :param switch_name: The switch name.
        :param switch_argument: The switch value.'''
        ...
    
    @overload
    def add_switch(self, switch_name: str, switch_argument: float) -> aspose.words.fields.FieldBuilder:
        '''Adds a field's switch.
        
        :param switch_name: The switch name.
        :param switch_argument: The switch value.'''
        ...
    
    @overload
    def build_and_insert(self, ref_node: aspose.words.Inline) -> aspose.words.fields.Field:
        '''Builds and inserts a field into the document before the specified inline node.
        
        :returns: A :class:`Field` object that represents the inserted field.'''
        ...
    
    @overload
    def build_and_insert(self, ref_node: aspose.words.Paragraph) -> aspose.words.fields.Field:
        '''Builds and inserts a field into the document to the end of the specified paragraph.
        
        :returns: A :class:`Field` object that represents the inserted field.'''
        ...
    
    ...

class FieldChar(aspose.words.SpecialChar):
    '''Base class for nodes that represent field characters in a document.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    A complete field in a Microsoft Word document is a complex structure consisting of
    a field start character, field code, field separator character, field result
    and field end character. Some fields only have field start, field code and field end.
    
    To easily insert a new field into a document, use the :meth:`aspose.words.DocumentBuilder.insert_field`
    method.'''
    
    def get_field(self) -> aspose.words.fields.Field:
        '''Returns a field for the field char.
        
        A new :class:`Field` object is created each time the method is called.
        
        :returns: A field for the field char.'''
        ...
    
    @property
    def field_type(self) -> aspose.words.fields.FieldType:
        '''Returns the type of the field.'''
        ...
    
    @property
    def is_locked(self) -> bool:
        '''Gets or sets whether the parent field is locked (should not recalculate its result).'''
        ...
    
    @is_locked.setter
    def is_locked(self, value: bool):
        ...
    
    @property
    def is_dirty(self) -> bool:
        '''Gets or sets whether the current result of the field is no longer correct (stale) due to other modifications
        made to the document.'''
        ...
    
    @is_dirty.setter
    def is_dirty(self, value: bool):
        ...
    
    ...

class FieldCitation(aspose.words.fields.Field):
    '''Implements the CITATION field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts the contents of the **Source** element with a specified **Tag** element using a bibliographic style.'''
    
    def __init__(self):
        ...
    
    @property
    def source_tag(self) -> str:
        '''Gets or sets a value that mathes the **Tag** element's value of the source to insert.'''
        ...
    
    @source_tag.setter
    def source_tag(self, value: str):
        ...
    
    @property
    def format_language_id(self) -> str:
        '''Gets or sets the language ID that is used in conjunction with the specified bibliographic style to format the citation
        in the document.'''
        ...
    
    @format_language_id.setter
    def format_language_id(self, value: str):
        ...
    
    @property
    def prefix(self) -> str:
        '''Gets or sets a prefix that is prepended to the citation.'''
        ...
    
    @prefix.setter
    def prefix(self, value: str):
        ...
    
    @property
    def suffix(self) -> str:
        '''Gets or sets a suffix that is appended to the citation.'''
        ...
    
    @suffix.setter
    def suffix(self, value: str):
        ...
    
    @property
    def suppress_author(self) -> bool:
        '''Gets or sets whether the author information is suppressed from the citation.'''
        ...
    
    @suppress_author.setter
    def suppress_author(self, value: bool):
        ...
    
    @property
    def suppress_title(self) -> bool:
        '''Gets or sets whether the title information is suppressed from the citation.'''
        ...
    
    @suppress_title.setter
    def suppress_title(self, value: bool):
        ...
    
    @property
    def suppress_year(self) -> bool:
        '''Gets or sets whether the year information is suppressed from the citation.'''
        ...
    
    @suppress_year.setter
    def suppress_year(self, value: bool):
        ...
    
    @property
    def page_number(self) -> str:
        '''Gets or sets a page number associated with the citation.'''
        ...
    
    @page_number.setter
    def page_number(self, value: str):
        ...
    
    @property
    def volume_number(self) -> str:
        '''Gets or sets a volume number associated with the citation.'''
        ...
    
    @volume_number.setter
    def volume_number(self, value: str):
        ...
    
    @property
    def another_source_tag(self) -> str:
        '''Gets or sets a value that mathes the **Tag** element's value of another source to be included in the citation.'''
        ...
    
    @another_source_tag.setter
    def another_source_tag(self, value: str):
        ...
    
    ...

class FieldCollection:
    '''A collection of :class:`Field` objects that represents the fields in the specified range.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    An instance of this collection iterates fields which start fall within the specified range.
    
    The :class:`FieldCollection` collection does not own the fields it contains, rather, is just a selection of fields.
    
    The :class:`FieldCollection` collection is "live", i.e. changes to the children of the node object
    that it was created from are immediately reflected in the fields returned by the :class:`FieldCollection`
    properties and methods.'''
    
    def __getitem__(self, index: int) -> aspose.words.fields.Field:
        '''Returns a field at the specified index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the collection.'''
        ...
    
    def remove(self, field: aspose.words.fields.Field) -> None:
        '''Removes the specified field from this collection and from the document.
        
        :param field: A field to remove.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes a field at the specified index from this collection and from the document.
        
        :param index: An index into the collection.'''
        ...
    
    def clear(self) -> None:
        '''Removes all fields of this collection from the document and from this collection itself.'''
        ...
    
    @property
    def count(self) -> int:
        '''Returns the number of the fields in the collection.'''
        ...
    
    ...

class FieldComments(aspose.words.fields.Field):
    '''Implements the COMMENTS field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves, and optionally sets, the comments relating to the current document, as recorded in the :attr:`aspose.words.properties.BuiltInDocumentProperties.comments` property
    of the built-in document properties.'''
    
    def __init__(self):
        ...
    
    @property
    def text(self) -> str:
        '''Gets or sets the text of the comments.'''
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    ...

class FieldCompare(aspose.words.fields.Field):
    '''Implements the COMPARE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Compares the values designated by the expressions :attr:`FieldCompare.left_expression` and :attr:`FieldCompare.right_expression`
    in comparison using the operator designated by :attr:`FieldCompare.comparison_operator`.'''
    
    def __init__(self):
        ...
    
    @property
    def left_expression(self) -> str:
        '''Gets or sets the left part of the comparison expression.'''
        ...
    
    @left_expression.setter
    def left_expression(self, value: str):
        ...
    
    @property
    def comparison_operator(self) -> str:
        '''Gets or sets the comparison operator.'''
        ...
    
    @comparison_operator.setter
    def comparison_operator(self, value: str):
        ...
    
    @property
    def right_expression(self) -> str:
        '''Gets or sets the right part of the comparison expression.'''
        ...
    
    @right_expression.setter
    def right_expression(self, value: str):
        ...
    
    ...

class FieldCreateDate(aspose.words.fields.Field):
    '''Implements the CREATEDATE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the date and time at which the document was created. By default, the Gregorian calendar is used.'''
    
    def __init__(self):
        ...
    
    @property
    def use_lunar_calendar(self) -> bool:
        '''Gets or sets whether to use the Hijri Lunar or Hebrew Lunar calendar.'''
        ...
    
    @use_lunar_calendar.setter
    def use_lunar_calendar(self, value: bool):
        ...
    
    @property
    def use_saka_era_calendar(self) -> bool:
        '''Gets or sets whether to use the Saka Era calendar.'''
        ...
    
    @use_saka_era_calendar.setter
    def use_saka_era_calendar(self, value: bool):
        ...
    
    @property
    def use_um_al_qura_calendar(self) -> bool:
        '''Gets or sets whether to use the Um-al-Qura calendar.'''
        ...
    
    @use_um_al_qura_calendar.setter
    def use_um_al_qura_calendar(self, value: bool):
        ...
    
    ...

class FieldData(aspose.words.fields.Field):
    '''Implements the DATA field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self):
        ...
    
    ...

class FieldDatabase(aspose.words.fields.Field):
    '''Implements the DATABASE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts the results of a database query into a WordprocessingML table.'''
    
    def __init__(self):
        ...
    
    @property
    def format_attributes(self) -> str:
        '''Gets or sets which attributes of the format are to be applied to the table.'''
        ...
    
    @format_attributes.setter
    def format_attributes(self, value: str):
        ...
    
    @property
    def connection(self) -> str:
        '''Gets or sets a connection to the data.'''
        ...
    
    @connection.setter
    def connection(self, value: str):
        ...
    
    @property
    def file_name(self) -> str:
        '''Gets or sets the complete path and file name of the database'''
        ...
    
    @file_name.setter
    def file_name(self, value: str):
        ...
    
    @property
    def first_record(self) -> str:
        '''Gets or sets the integral record number of the first data record to insert.'''
        ...
    
    @first_record.setter
    def first_record(self, value: str):
        ...
    
    @property
    def insert_headings(self) -> bool:
        '''Gets or sets whether to insert the field names from the database as column headings in
        the resulting table.'''
        ...
    
    @insert_headings.setter
    def insert_headings(self, value: bool):
        ...
    
    @property
    def table_format(self) -> str:
        '''Gets or sets the format that is to be applied to the result of the database query.'''
        ...
    
    @table_format.setter
    def table_format(self, value: str):
        ...
    
    @property
    def insert_once_on_mail_merge(self) -> bool:
        '''Gets or sets whether to insert data at the beginning of a merge.'''
        ...
    
    @insert_once_on_mail_merge.setter
    def insert_once_on_mail_merge(self, value: bool):
        ...
    
    @property
    def query(self) -> str:
        '''Gets or sets a set of SQL instructions that query the database.'''
        ...
    
    @query.setter
    def query(self, value: str):
        ...
    
    @property
    def last_record(self) -> str:
        '''Gets or sets the integral record number of the last data record to insert.'''
        ...
    
    @last_record.setter
    def last_record(self, value: str):
        ...
    
    ...

class FieldDatabaseDataRow:
    '''Provides data for the :class:`FieldDatabase` field result.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self, values: list[str]):
        '''Initializes a new instance of the :class:`FieldDatabaseDataRow` class.'''
        ...
    
    @property
    def values(self) -> list[str]:
        '''Gets values that belong to this row.'''
        ...
    
    ...

class FieldDatabaseDataTable:
    '''Provides data for the :class:`FieldDatabase` field result.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self, column_names: list[str]):
        '''Initializes a new instance of the :class:`FieldDatabaseDataTable` class.'''
        ...
    
    @property
    def column_names(self) -> list[str]:
        '''Gets columns that belong to this table.'''
        ...
    
    @property
    def rows(self) -> list[aspose.words.fields.FieldDatabaseDataRow]:
        '''Gets rows that belong to this table.'''
        ...
    
    ...

class FieldDate(aspose.words.fields.Field):
    '''Implements the DATE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts the current date and time. By default, the Gregorian calendar is used.'''
    
    def __init__(self):
        ...
    
    @property
    def use_lunar_calendar(self) -> bool:
        '''Gets or sets whether to use the Hijri Lunar or Hebrew Lunar calendar.'''
        ...
    
    @use_lunar_calendar.setter
    def use_lunar_calendar(self, value: bool):
        ...
    
    @property
    def use_last_format(self) -> bool:
        '''Gets or sets whether to use a format last used by the hosting application when inserting a new DATE field.'''
        ...
    
    @use_last_format.setter
    def use_last_format(self, value: bool):
        ...
    
    @property
    def use_saka_era_calendar(self) -> bool:
        '''Gets or sets whether to use the Saka Era calendar.'''
        ...
    
    @use_saka_era_calendar.setter
    def use_saka_era_calendar(self, value: bool):
        ...
    
    @property
    def use_um_al_qura_calendar(self) -> bool:
        '''Gets or sets whether to use the Um-al-Qura calendar.'''
        ...
    
    @use_um_al_qura_calendar.setter
    def use_um_al_qura_calendar(self, value: bool):
        ...
    
    ...

class FieldDde(aspose.words.fields.Field):
    '''Implements the DDE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    For information copied from another application, this field links that information to its original source file using DDE.'''
    
    def __init__(self):
        ...
    
    @property
    def prog_id(self) -> str:
        '''Gets or sets the application type of the link information.'''
        ...
    
    @prog_id.setter
    def prog_id(self, value: str):
        ...
    
    @property
    def source_full_name(self) -> str:
        '''Gets or sets the name and location of the source file.'''
        ...
    
    @source_full_name.setter
    def source_full_name(self, value: str):
        ...
    
    @property
    def source_item(self) -> str:
        '''Gets or sets the portion of the source file that's being linked.'''
        ...
    
    @source_item.setter
    def source_item(self, value: str):
        ...
    
    @property
    def auto_update(self) -> bool:
        '''Gets or sets whether to update this field automatically.'''
        ...
    
    @auto_update.setter
    def auto_update(self, value: bool):
        ...
    
    @property
    def insert_as_bitmap(self) -> bool:
        '''Gets or sets whether to insert the linked object as a bitmap.'''
        ...
    
    @insert_as_bitmap.setter
    def insert_as_bitmap(self, value: bool):
        ...
    
    @property
    def is_linked(self) -> bool:
        '''Gets or sets whether to reduce the file size by not storing graphics data with the document.'''
        ...
    
    @is_linked.setter
    def is_linked(self, value: bool):
        ...
    
    @property
    def insert_as_html(self) -> bool:
        '''Gets or sets whether to insert the linked object as HTML format text.'''
        ...
    
    @insert_as_html.setter
    def insert_as_html(self, value: bool):
        ...
    
    @property
    def insert_as_picture(self) -> bool:
        '''Gets or sets whether to insert the linked object as a picture.'''
        ...
    
    @insert_as_picture.setter
    def insert_as_picture(self, value: bool):
        ...
    
    @property
    def insert_as_rtf(self) -> bool:
        '''Gets or sets whether to insert the linked object in rich-text format (RTF).'''
        ...
    
    @insert_as_rtf.setter
    def insert_as_rtf(self, value: bool):
        ...
    
    @property
    def insert_as_text(self) -> bool:
        '''Gets or sets whether to insert the linked object in text-only format.'''
        ...
    
    @insert_as_text.setter
    def insert_as_text(self, value: bool):
        ...
    
    @property
    def insert_as_unicode(self) -> bool:
        '''Gets or sets whether to insert the linked object as Unicode text.'''
        ...
    
    @insert_as_unicode.setter
    def insert_as_unicode(self, value: bool):
        ...
    
    ...

class FieldDdeAuto(aspose.words.fields.Field):
    '''Implements the DDEAUTO field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    For information copied from another application, this field links that information to its original source file using DDE
    and is updated automatically.'''
    
    def __init__(self):
        ...
    
    @property
    def prog_id(self) -> str:
        '''Gets or sets the application type of the link information.'''
        ...
    
    @prog_id.setter
    def prog_id(self, value: str):
        ...
    
    @property
    def source_full_name(self) -> str:
        '''Gets or sets the name and location of the source file.'''
        ...
    
    @source_full_name.setter
    def source_full_name(self, value: str):
        ...
    
    @property
    def source_item(self) -> str:
        '''Gets or sets the portion of the source file that's being linked.'''
        ...
    
    @source_item.setter
    def source_item(self, value: str):
        ...
    
    @property
    def insert_as_bitmap(self) -> bool:
        '''Gets or sets whether to insert the linked object as a bitmap.'''
        ...
    
    @insert_as_bitmap.setter
    def insert_as_bitmap(self, value: bool):
        ...
    
    @property
    def is_linked(self) -> bool:
        '''Gets or sets whether to reduce the file size by not storing graphics data with the document.'''
        ...
    
    @is_linked.setter
    def is_linked(self, value: bool):
        ...
    
    @property
    def insert_as_html(self) -> bool:
        '''Gets or sets whether to insert the linked object as HTML format text.'''
        ...
    
    @insert_as_html.setter
    def insert_as_html(self, value: bool):
        ...
    
    @property
    def insert_as_picture(self) -> bool:
        '''Gets or sets whether to insert the linked object as a picture.'''
        ...
    
    @insert_as_picture.setter
    def insert_as_picture(self, value: bool):
        ...
    
    @property
    def insert_as_rtf(self) -> bool:
        '''Gets or sets whether to insert the linked object in rich-text format (RTF).'''
        ...
    
    @insert_as_rtf.setter
    def insert_as_rtf(self, value: bool):
        ...
    
    @property
    def insert_as_text(self) -> bool:
        '''Gets or sets whether to insert the linked object in text-only format.'''
        ...
    
    @insert_as_text.setter
    def insert_as_text(self, value: bool):
        ...
    
    @property
    def insert_as_unicode(self) -> bool:
        '''Gets or sets whether to insert the linked object as Unicode text.'''
        ...
    
    @insert_as_unicode.setter
    def insert_as_unicode(self, value: bool):
        ...
    
    ...

class FieldDisplayBarcode(aspose.words.fields.Field):
    '''Implements the DISPLAYBARCODE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts a barcode.'''
    
    def __init__(self):
        ...
    
    @property
    def barcode_value(self) -> str:
        '''Gets or sets the barcode value.'''
        ...
    
    @barcode_value.setter
    def barcode_value(self, value: str):
        ...
    
    @property
    def barcode_type(self) -> str:
        '''Gets or sets the barcode type (QR, etc.)'''
        ...
    
    @barcode_type.setter
    def barcode_type(self, value: str):
        ...
    
    @property
    def symbol_height(self) -> str:
        '''Gets or sets the height of the symbol. The units are in TWIPS (1/1440 inch).'''
        ...
    
    @symbol_height.setter
    def symbol_height(self, value: str):
        ...
    
    @property
    def symbol_rotation(self) -> str:
        '''Gets or sets the rotation of the barcode symbol. Valid values are [0, 3]'''
        ...
    
    @symbol_rotation.setter
    def symbol_rotation(self, value: str):
        ...
    
    @property
    def scaling_factor(self) -> str:
        '''Gets or sets a scaling factor for the symbol. The value is in whole percentage points and the valid values are [10, 1000]'''
        ...
    
    @scaling_factor.setter
    def scaling_factor(self, value: str):
        ...
    
    @property
    def foreground_color(self) -> str:
        '''Gets or sets the foreground color of the barcode symbol. Valid values are in the range [0, 0xFFFFFF]'''
        ...
    
    @foreground_color.setter
    def foreground_color(self, value: str):
        ...
    
    @property
    def background_color(self) -> str:
        '''Gets or sets the background color of the barcode symbol. Valid values are in the range [0, 0xFFFFFF]'''
        ...
    
    @background_color.setter
    def background_color(self, value: str):
        ...
    
    @property
    def pos_code_style(self) -> str:
        '''Gets or sets the style of a Point of Sale barcode (barcode types UPCA|UPCE|EAN13|EAN8). The valid values (case insensitive) are [STD|SUP2|SUP5|CASE].'''
        ...
    
    @pos_code_style.setter
    def pos_code_style(self, value: str):
        ...
    
    @property
    def case_code_style(self) -> str:
        '''Gets or sets the style of a Case Code for barcode type ITF14. The valid values are [STD|EXT|ADD]'''
        ...
    
    @case_code_style.setter
    def case_code_style(self, value: str):
        ...
    
    @property
    def error_correction_level(self) -> str:
        '''Gets or sets an error correction level of QR Code. Valid values are [0, 3].'''
        ...
    
    @error_correction_level.setter
    def error_correction_level(self, value: str):
        ...
    
    @property
    def display_text(self) -> bool:
        '''Gets or sets whether to display barcode data (text) along with image.'''
        ...
    
    @display_text.setter
    def display_text(self, value: bool):
        ...
    
    @property
    def add_start_stop_char(self) -> bool:
        '''Gets or sets whether to add Start/Stop characters for barcode types NW7 and CODE39.'''
        ...
    
    @add_start_stop_char.setter
    def add_start_stop_char(self, value: bool):
        ...
    
    @property
    def fix_check_digit(self) -> bool:
        '''Gets or sets whether to fix the check digit if it’s invalid.'''
        ...
    
    @fix_check_digit.setter
    def fix_check_digit(self, value: bool):
        ...
    
    ...

class FieldDocProperty(aspose.words.fields.Field):
    '''Implements the DOCPROPERTY field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the indicated document information.'''
    
    def __init__(self):
        ...
    
    ...

class FieldDocVariable(aspose.words.fields.Field):
    '''Implements DOCVARIABLE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self):
        ...
    
    @property
    def variable_name(self) -> str:
        '''Gets or sets the name of the document variable to retrieve.'''
        ...
    
    @variable_name.setter
    def variable_name(self, value: str):
        ...
    
    ...

class FieldEQ(aspose.words.fields.Field):
    '''Implements the EQ field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self):
        ...
    
    def as_office_math(self) -> aspose.words.math.OfficeMath:
        '''Returns Office Math object corresponded to the EQ field.
        
        :returns: Returns ``None`` if field code is empty or invalid, otherwise an :class:`aspose.words.math.OfficeMath` instance.'''
        ...
    
    ...

class FieldEditTime(aspose.words.fields.Field):
    '''Implements the EDITTIME field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the total editing time, in minutes, since the document was created.'''
    
    def __init__(self):
        ...
    
    ...

class FieldEmbed(aspose.words.fields.Field):
    '''Implements the EMBED field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self):
        ...
    
    ...

class FieldEnd(aspose.words.fields.FieldChar):
    '''Represents an end of a Word field in a document.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    :class:`FieldEnd` is an inline-level node and represented
    by the :attr:`aspose.words.ControlChar.FIELD_END_CHAR` control character in the document.
    
    :class:`FieldEnd` can only be a child of :class:`aspose.words.Paragraph`.
    
    A complete field in a Microsoft Word document is a complex structure consisting of
    a field start character, field code, field separator character, field result
    and field end character. Some fields only have field start, field code and field end.
    
    To easily insert a new field into a document, use the :meth:`aspose.words.DocumentBuilder.insert_field`
    method.'''
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        '''Accepts a visitor.
        
        Calls :meth:`aspose.words.DocumentVisitor.visit_field_end`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the node.
        :returns: **False** if the visitor requested the enumeration to stop.'''
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        '''Returns :attr:`aspose.words.NodeType.FIELD_END`.'''
        ...
    
    @property
    def has_separator(self) -> bool:
        '''Returns ``True`` if this field has a separator.'''
        ...
    
    ...

class FieldFileName(aspose.words.fields.Field):
    '''Implements the FILENAME field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the name of the current document from its storage location.
    
    In the current implementation, uses the :attr:`aspose.words.Document.original_file_name` property to retrieve
    the file name. If the document was loaded from a stream or created blank, uses the name of the file that is being saved to (if known).'''
    
    def __init__(self):
        ...
    
    @property
    def include_full_path(self) -> bool:
        '''Gets or sets whether to include the full file path name.'''
        ...
    
    @include_full_path.setter
    def include_full_path(self, value: bool):
        ...
    
    ...

class FieldFileSize(aspose.words.fields.Field):
    '''Implements the FILESIZE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the size of the current document's file or 0 if the size cannot be determined.
    
    In the current implementation, uses the :attr:`aspose.words.Document.original_file_name` property to retrieve
    the file name used to determine the file size.'''
    
    def __init__(self):
        ...
    
    @property
    def is_in_kilobytes(self) -> bool:
        '''Gets or sets whether to display the file size in kilobytes.'''
        ...
    
    @is_in_kilobytes.setter
    def is_in_kilobytes(self, value: bool):
        ...
    
    @property
    def is_in_megabytes(self) -> bool:
        '''Gets or sets whether to display the file size in megabytes.'''
        ...
    
    @is_in_megabytes.setter
    def is_in_megabytes(self, value: bool):
        ...
    
    ...

class FieldFillIn(aspose.words.fields.Field):
    '''Implements the FILLIN field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Prompts the user to enter text.'''
    
    def __init__(self):
        ...
    
    @property
    def prompt_text(self) -> str:
        '''Gets or sets the prompt text (the title of the prompt window).'''
        ...
    
    @prompt_text.setter
    def prompt_text(self, value: str):
        ...
    
    @property
    def prompt_once_on_mail_merge(self) -> bool:
        '''Gets or sets whether the user response should be recieved once per a mail merge operation.'''
        ...
    
    @prompt_once_on_mail_merge.setter
    def prompt_once_on_mail_merge(self, value: bool):
        ...
    
    @property
    def default_response(self) -> str:
        '''Gets or sets default user response (initial value contained in the prompt window).'''
        ...
    
    @default_response.setter
    def default_response(self, value: str):
        ...
    
    ...

class FieldFootnoteRef(aspose.words.fields.Field):
    '''Implements the FOOTNOTEREF field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self):
        ...
    
    ...

class FieldFormCheckBox(aspose.words.fields.Field):
    '''Implements the FORMCHECKBOX field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts a check box style form field.'''
    
    def __init__(self):
        ...
    
    ...

class FieldFormDropDown(aspose.words.fields.Field):
    '''Implements the FORMDROPDOWN field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts a drop-down list style form field.'''
    
    def __init__(self):
        ...
    
    ...

class FieldFormText(aspose.words.fields.Field):
    '''Implements the FORMTEXT field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts a text box style form field.'''
    
    def __init__(self):
        ...
    
    ...

class FieldFormat:
    '''Provides typed access to field's numeric, date and time, and general formatting.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    @property
    def numeric_format(self) -> str:
        '''Gets or sets a formatting that is applied to a numeric field result. Corresponds to the \\# switch.'''
        ...
    
    @numeric_format.setter
    def numeric_format(self, value: str):
        ...
    
    @property
    def date_time_format(self) -> str:
        '''Gets or sets a formatting that is applied to a date and time field result. Corresponds to the \\@ switch.'''
        ...
    
    @date_time_format.setter
    def date_time_format(self, value: str):
        ...
    
    @property
    def general_formats(self) -> aspose.words.fields.GeneralFormatCollection:
        '''Gets a collection of general formats that are applied to a numeric, text or any field result.
        Corresponds to the \\\* switches.'''
        ...
    
    ...

class FieldFormula(aspose.words.fields.Field):
    '''Implements the = (formula) field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Calcualtes the result of an expression.'''
    
    def __init__(self):
        ...
    
    ...

class FieldGlossary(aspose.words.fields.Field):
    '''Implements the GLOSSARY field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts a glossary entry.'''
    
    def __init__(self):
        ...
    
    @property
    def entry_name(self) -> str:
        '''Gets or sets the name of the glossary entry to insert.'''
        ...
    
    @entry_name.setter
    def entry_name(self, value: str):
        ...
    
    ...

class FieldGoToButton(aspose.words.fields.Field):
    '''Implements the GOTOBUTTON field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts a jump command, such that when it is activated, the insertion point of the document is
    moved to the specified location.'''
    
    def __init__(self):
        ...
    
    @property
    def location(self) -> str:
        '''Gets or sets the name of a bookmark, a page number, or some other item to jump to.'''
        ...
    
    @location.setter
    def location(self, value: str):
        ...
    
    @property
    def display_text(self) -> str:
        '''Gets or sets the text of the "button" that appears in the document, such that it can be selected to activate the jump.'''
        ...
    
    @display_text.setter
    def display_text(self, value: str):
        ...
    
    ...

class FieldGreetingLine(aspose.words.fields.Field):
    '''Implements the GREETINGLINE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts a mail merge greeting line.'''
    
    def __init__(self):
        ...
    
    def get_field_names(self) -> list[str]:
        '''Returns a collection of mail merge field names used by the field.'''
        ...
    
    @property
    def alternate_text(self) -> str:
        '''Gets or sets the text to include in the field if the name is blank.'''
        ...
    
    @alternate_text.setter
    def alternate_text(self, value: str):
        ...
    
    @property
    def name_format(self) -> str:
        '''Gets or sets the format of the name included in the field.'''
        ...
    
    @name_format.setter
    def name_format(self, value: str):
        ...
    
    @property
    def language_id(self) -> str:
        '''Gets or sets the language id used to format the name.'''
        ...
    
    @language_id.setter
    def language_id(self, value: str):
        ...
    
    ...

class FieldHyperlink(aspose.words.fields.Field):
    '''Implements the HYPERLINK field
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    When selected, causes control to jump to the location such as a bookmark or a URL.'''
    
    def __init__(self):
        ...
    
    @property
    def target(self) -> str:
        '''Gets or sets the target to which the link should be redirected.'''
        ...
    
    @target.setter
    def target(self, value: str):
        ...
    
    @property
    def address(self) -> str:
        '''Gets or sets a location where this hyperlink jumps.'''
        ...
    
    @address.setter
    def address(self, value: str):
        ...
    
    @property
    def sub_address(self) -> str:
        '''Gets or sets a location in the file, such as a bookmark, where this hyperlink jumps.'''
        ...
    
    @sub_address.setter
    def sub_address(self, value: str):
        ...
    
    @property
    def is_image_map(self) -> bool:
        '''Gets or sets whether to append coordinates to the hyperlink for a server-side image map.'''
        ...
    
    @is_image_map.setter
    def is_image_map(self, value: bool):
        ...
    
    @property
    def open_in_new_window(self) -> bool:
        '''Gets or sets whether to open the destination site in a new web browser window.'''
        ...
    
    @open_in_new_window.setter
    def open_in_new_window(self, value: bool):
        ...
    
    @property
    def screen_tip(self) -> str:
        '''Gets or sets the ScreenTip text for the hyperlink.'''
        ...
    
    @screen_tip.setter
    def screen_tip(self, value: str):
        ...
    
    ...

class FieldIf(aspose.words.fields.Field):
    '''Implements the IF field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Compares the values designated by the expressions :attr:`FieldIf.left_expression` and :attr:`FieldIf.right_expression`
    in comparison using the operator designated by :attr:`FieldIf.comparison_operator`.
    
    A field in the following format will be used as a mail merge source: { IF 0 = 0 "{PatientsNameFML}" "" \\\* MERGEFORMAT }'''
    
    def __init__(self):
        ...
    
    def evaluate_condition(self) -> aspose.words.fields.FieldIfComparisonResult:
        '''Evaluates the condition.
        
        :returns: A :class:`FieldIfComparisonResult` value that represents the result of the condition evaluation.'''
        ...
    
    @property
    def left_expression(self) -> str:
        '''Gets or sets the left part of the comparison expression.'''
        ...
    
    @left_expression.setter
    def left_expression(self, value: str):
        ...
    
    @property
    def comparison_operator(self) -> str:
        '''Gets or sets the comparison operator.'''
        ...
    
    @comparison_operator.setter
    def comparison_operator(self, value: str):
        ...
    
    @property
    def right_expression(self) -> str:
        '''Gets or sets the right part of the comparison expression.'''
        ...
    
    @right_expression.setter
    def right_expression(self, value: str):
        ...
    
    @property
    def true_text(self) -> str:
        '''Gets or sets the text displayed if the comparison expression is true.'''
        ...
    
    @true_text.setter
    def true_text(self, value: str):
        ...
    
    @property
    def false_text(self) -> str:
        '''Gets or sets the text displayed if the comparison expression is ``False``.'''
        ...
    
    @false_text.setter
    def false_text(self, value: str):
        ...
    
    ...

class FieldImport(aspose.words.fields.Field):
    '''Implements the IMPORT field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the picture contained in the document.'''
    
    def __init__(self):
        ...
    
    @property
    def source_full_name(self) -> str:
        '''Gets or sets the location of the picture.'''
        ...
    
    @source_full_name.setter
    def source_full_name(self, value: str):
        ...
    
    @property
    def graphic_filter(self) -> str:
        '''Gets or sets the name of the filter for the format of the graphic that is to be inserted.'''
        ...
    
    @graphic_filter.setter
    def graphic_filter(self, value: str):
        ...
    
    @property
    def is_linked(self) -> bool:
        '''Gets or sets whether to reduce the file size by not storing graphics data with the document.'''
        ...
    
    @is_linked.setter
    def is_linked(self, value: bool):
        ...
    
    ...

class FieldInclude(aspose.words.fields.Field):
    '''Implements the INCLUDE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts all or part of the text and graphics contained in another document.'''
    
    def __init__(self):
        ...
    
    @property
    def source_full_name(self) -> str:
        '''Gets or sets the location of the document.'''
        ...
    
    @source_full_name.setter
    def source_full_name(self, value: str):
        ...
    
    @property
    def bookmark_name(self) -> str:
        '''Gets or sets the name of the bookmark in the document to include.'''
        ...
    
    @bookmark_name.setter
    def bookmark_name(self, value: str):
        ...
    
    @property
    def lock_fields(self) -> bool:
        '''Gets or sets whether to prevent fields in the included document from being updated.'''
        ...
    
    @lock_fields.setter
    def lock_fields(self, value: bool):
        ...
    
    @property
    def text_converter(self) -> str:
        '''Gets or sets the name of the text converter for the format of the included file.'''
        ...
    
    @text_converter.setter
    def text_converter(self, value: str):
        ...
    
    ...

class FieldIncludePicture(aspose.words.fields.Field):
    '''Implements the INCLUDEPICTURE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves a picture and displays it as the field result.'''
    
    def __init__(self):
        ...
    
    @property
    def source_full_name(self) -> str:
        '''Gets or sets the location of the picture using an IRI.'''
        ...
    
    @source_full_name.setter
    def source_full_name(self, value: str):
        ...
    
    @property
    def graphic_filter(self) -> str:
        '''Gets or sets the name of the filter for the format of the graphic that is to be inserted.'''
        ...
    
    @graphic_filter.setter
    def graphic_filter(self, value: str):
        ...
    
    @property
    def is_linked(self) -> bool:
        '''Gets or sets whether to reduce the file size by not storing graphics data with the document.'''
        ...
    
    @is_linked.setter
    def is_linked(self, value: bool):
        ...
    
    @property
    def resize_horizontally(self) -> bool:
        '''Gets or sets whether to resize the picture horizontally from the source.'''
        ...
    
    @resize_horizontally.setter
    def resize_horizontally(self, value: bool):
        ...
    
    @property
    def resize_vertically(self) -> bool:
        '''Gets or sets whether to resize the picture vertically from the source.'''
        ...
    
    @resize_vertically.setter
    def resize_vertically(self, value: bool):
        ...
    
    ...

class FieldIncludeText(aspose.words.fields.Field):
    '''Implements the INCLUDETEXT field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts all or part of the text and graphics contained in another document.'''
    
    def __init__(self):
        ...
    
    @property
    def source_full_name(self) -> str:
        '''Gets or sets the location of the document using an IRI.'''
        ...
    
    @source_full_name.setter
    def source_full_name(self, value: str):
        ...
    
    @property
    def bookmark_name(self) -> str:
        '''Gets or sets the name of the bookmark in the document to include.'''
        ...
    
    @bookmark_name.setter
    def bookmark_name(self, value: str):
        ...
    
    @property
    def lock_fields(self) -> bool:
        '''Gets or sets whether to prevent fields in the included document from being updated.'''
        ...
    
    @lock_fields.setter
    def lock_fields(self, value: bool):
        ...
    
    @property
    def text_converter(self) -> str:
        '''Gets or sets the name of the text converter for the format of the included file.'''
        ...
    
    @text_converter.setter
    def text_converter(self, value: str):
        ...
    
    @property
    def namespace_mappings(self) -> str:
        '''Gets or sets the namespace mappings for XPath queries.'''
        ...
    
    @namespace_mappings.setter
    def namespace_mappings(self, value: str):
        ...
    
    @property
    def xsl_transformation(self) -> str:
        '''Gets or sets the location of XSL Transformation to format XML data.'''
        ...
    
    @xsl_transformation.setter
    def xsl_transformation(self, value: str):
        ...
    
    @property
    def xpath(self) -> str:
        '''Gets or sets XPath for the desired portion of the XML file.'''
        ...
    
    @xpath.setter
    def xpath(self, value: str):
        ...
    
    @property
    def encoding(self) -> str:
        '''Gets or sets the encoding applied to the data within the referenced file.'''
        ...
    
    @encoding.setter
    def encoding(self, value: str):
        ...
    
    @property
    def mime_type(self) -> str:
        '''Gets or sets the MIME type of the referenced file.'''
        ...
    
    @mime_type.setter
    def mime_type(self, value: str):
        ...
    
    ...

class FieldIndex(aspose.words.fields.Field):
    '''Implements the INDEX field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Builds an index using the index entries specified by XE fields, and inserts that index at this place in the document.'''
    
    def __init__(self):
        ...
    
    @property
    def bookmark_name(self) -> str:
        '''Gets or sets the name of the bookmark that marks the portion of the document used to build the index.'''
        ...
    
    @bookmark_name.setter
    def bookmark_name(self, value: str):
        ...
    
    @property
    def number_of_columns(self) -> str:
        '''Gets or sets the number of columns per page used when building the index.'''
        ...
    
    @number_of_columns.setter
    def number_of_columns(self, value: str):
        ...
    
    @property
    def sequence_separator(self) -> str:
        '''Gets or sets the character sequence that is used to separate sequence numbers and page numbers.'''
        ...
    
    @sequence_separator.setter
    def sequence_separator(self, value: str):
        ...
    
    @property
    def page_number_separator(self) -> str:
        '''Gets or sets the character sequence that is used to separate an index entry and its page number.'''
        ...
    
    @page_number_separator.setter
    def page_number_separator(self, value: str):
        ...
    
    @property
    def has_page_number_separator(self) -> bool:
        '''Gets a value indicating whether a page number separator is overridden through the field's code.'''
        ...
    
    @property
    def entry_type(self) -> str:
        '''Gets or sets an index entry type used to build the index.'''
        ...
    
    @entry_type.setter
    def entry_type(self, value: str):
        ...
    
    @property
    def page_range_separator(self) -> str:
        '''Gets or sets the character sequence that is used to separate the start and end of a page range.'''
        ...
    
    @page_range_separator.setter
    def page_range_separator(self, value: str):
        ...
    
    @property
    def heading(self) -> str:
        '''Gets or sets a heading that appears at the start of each set of entries for any given letter.'''
        ...
    
    @heading.setter
    def heading(self, value: str):
        ...
    
    @property
    def cross_reference_separator(self) -> str:
        '''Gets or sets the character sequence that is used to separate cross references and other entries.'''
        ...
    
    @cross_reference_separator.setter
    def cross_reference_separator(self, value: str):
        ...
    
    @property
    def page_number_list_separator(self) -> str:
        '''Gets or sets the character sequence that is used to separate two page numbers in a page number list.'''
        ...
    
    @page_number_list_separator.setter
    def page_number_list_separator(self, value: str):
        ...
    
    @property
    def letter_range(self) -> str:
        '''Gets or sets a range of letters to which limit the index.'''
        ...
    
    @letter_range.setter
    def letter_range(self, value: str):
        ...
    
    @property
    def run_subentries_on_same_line(self) -> bool:
        '''Gets or sets whether run subentries into the same line as the main entry.'''
        ...
    
    @run_subentries_on_same_line.setter
    def run_subentries_on_same_line(self, value: bool):
        ...
    
    @property
    def sequence_name(self) -> str:
        '''Gets or sets the name of a sequence whose number is included with the page number.'''
        ...
    
    @sequence_name.setter
    def sequence_name(self, value: str):
        ...
    
    @property
    def has_sequence_name(self) -> bool:
        '''Gets a value indicating whether a sequence should be used while the field's result building.'''
        ...
    
    @property
    def use_yomi(self) -> bool:
        '''Gets or sets whether to enable the use of yomi text for index entries.'''
        ...
    
    @use_yomi.setter
    def use_yomi(self, value: bool):
        ...
    
    @property
    def language_id(self) -> str:
        '''Gets or sets the language ID used to generate the index.'''
        ...
    
    @language_id.setter
    def language_id(self, value: str):
        ...
    
    ...

class FieldInfo(aspose.words.fields.Field):
    '''Implements the INFO field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts information about a document property.'''
    
    def __init__(self):
        ...
    
    @property
    def info_type(self) -> str:
        '''Gets or sets the type of the document property to insert.'''
        ...
    
    @info_type.setter
    def info_type(self, value: str):
        ...
    
    @property
    def new_value(self) -> str:
        '''Gets or sets an optional value that updates the property.'''
        ...
    
    @new_value.setter
    def new_value(self, value: str):
        ...
    
    ...

class FieldKeywords(aspose.words.fields.Field):
    '''Implements the KEYWORDS field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves, and optionally sets, the document's keywords, as recorded in the **Keywords** property of the
    built-in document properties.'''
    
    def __init__(self):
        ...
    
    @property
    def text(self) -> str:
        '''Gets or sets the text of the keywords.'''
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    ...

class FieldLastSavedBy(aspose.words.fields.Field):
    '''Implements the LASTSAVEDBY field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the name of the user who last modified and saved the current document, as recorded in the **LastModifiedBy**
    property of the built-in document properties.'''
    
    def __init__(self):
        ...
    
    ...

class FieldLink(aspose.words.fields.Field):
    '''Implements the LINK field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    For information copied from another application, this field links that information to its original
    source file.'''
    
    def __init__(self):
        ...
    
    @property
    def prog_id(self) -> str:
        '''Gets or sets the application type of the link information.'''
        ...
    
    @prog_id.setter
    def prog_id(self, value: str):
        ...
    
    @property
    def source_full_name(self) -> str:
        '''Gets or sets the name and location of the source file.'''
        ...
    
    @source_full_name.setter
    def source_full_name(self, value: str):
        ...
    
    @property
    def source_item(self) -> str:
        '''Gets or sets the portion of the source file that's being linked.'''
        ...
    
    @source_item.setter
    def source_item(self, value: str):
        ...
    
    @property
    def auto_update(self) -> bool:
        '''Gets or sets whether to update this field automatically.'''
        ...
    
    @auto_update.setter
    def auto_update(self, value: bool):
        ...
    
    @property
    def insert_as_bitmap(self) -> bool:
        '''Gets or sets whether to insert the linked object as a bitmap.'''
        ...
    
    @insert_as_bitmap.setter
    def insert_as_bitmap(self, value: bool):
        ...
    
    @property
    def is_linked(self) -> bool:
        '''Gets or sets whether to reduce the file size by not storing graphics data with the document.'''
        ...
    
    @is_linked.setter
    def is_linked(self, value: bool):
        ...
    
    @property
    def format_update_type(self) -> str:
        '''Gets or sets a way the linked object updates its formatting.'''
        ...
    
    @format_update_type.setter
    def format_update_type(self, value: str):
        ...
    
    @property
    def insert_as_html(self) -> bool:
        '''Gets or sets whether to insert the linked object as HTML format text.'''
        ...
    
    @insert_as_html.setter
    def insert_as_html(self, value: bool):
        ...
    
    @property
    def insert_as_picture(self) -> bool:
        '''Gets or sets whether to insert the linked object as a picture.'''
        ...
    
    @insert_as_picture.setter
    def insert_as_picture(self, value: bool):
        ...
    
    @property
    def insert_as_rtf(self) -> bool:
        '''Gets or sets whether to insert the linked object in rich-text format (RTF).'''
        ...
    
    @insert_as_rtf.setter
    def insert_as_rtf(self, value: bool):
        ...
    
    @property
    def insert_as_text(self) -> bool:
        '''Gets or sets whether to insert the linked object in text-only format.'''
        ...
    
    @insert_as_text.setter
    def insert_as_text(self, value: bool):
        ...
    
    @property
    def insert_as_unicode(self) -> bool:
        '''Gets or sets whether to insert the linked object as Unicode text.'''
        ...
    
    @insert_as_unicode.setter
    def insert_as_unicode(self, value: bool):
        ...
    
    ...

class FieldListNum(aspose.words.fields.Field):
    '''Implements the LISTNUM field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self):
        ...
    
    @property
    def list_name(self) -> str:
        '''Gets or sets the name of the abstract numbering definition used for the numbering.'''
        ...
    
    @list_name.setter
    def list_name(self, value: str):
        ...
    
    @property
    def has_list_name(self) -> bool:
        '''Returns a value indicating whether the name of an abstract numbering definition
        is provided by the field's code.'''
        ...
    
    @property
    def list_level(self) -> str:
        '''Gets or sets the level in the list, overriding the default behavior of the field.'''
        ...
    
    @list_level.setter
    def list_level(self, value: str):
        ...
    
    @property
    def starting_number(self) -> str:
        '''Gets or sets the starting value for this field.'''
        ...
    
    @starting_number.setter
    def starting_number(self, value: str):
        ...
    
    ...

class FieldMacroButton(aspose.words.fields.Field):
    '''Implements the MACROBUTTON field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Allows a macro or command to be run.
    
    In Aspose.Words this field can also act as a merge field.'''
    
    def __init__(self):
        ...
    
    @property
    def macro_name(self) -> str:
        '''Gets or sets the name of the macro or command to run.'''
        ...
    
    @macro_name.setter
    def macro_name(self, value: str):
        ...
    
    @property
    def display_text(self) -> str:
        '''Gets or sets the text to appear as the "button" that is selected to run the macro or command.'''
        ...
    
    @display_text.setter
    def display_text(self, value: str):
        ...
    
    ...

class FieldMergeBarcode(aspose.words.fields.Field):
    '''Implements the MERGEBARCODE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Mail merge a barcode.'''
    
    def __init__(self):
        ...
    
    @property
    def barcode_value(self) -> str:
        '''Gets or sets the barcode value.'''
        ...
    
    @barcode_value.setter
    def barcode_value(self, value: str):
        ...
    
    @property
    def barcode_type(self) -> str:
        '''Gets or sets the barcode type (QR, etc.)'''
        ...
    
    @barcode_type.setter
    def barcode_type(self, value: str):
        ...
    
    @property
    def symbol_height(self) -> str:
        '''Gets or sets the height of the symbol. The units are in TWIPS (1/1440 inch).'''
        ...
    
    @symbol_height.setter
    def symbol_height(self, value: str):
        ...
    
    @property
    def symbol_rotation(self) -> str:
        '''Gets or sets the rotation of the barcode symbol. Valid values are [0, 3]'''
        ...
    
    @symbol_rotation.setter
    def symbol_rotation(self, value: str):
        ...
    
    @property
    def scaling_factor(self) -> str:
        '''Gets or sets a scaling factor for the symbol. The value is in whole percentage points and the valid values are [10, 1000]'''
        ...
    
    @scaling_factor.setter
    def scaling_factor(self, value: str):
        ...
    
    @property
    def foreground_color(self) -> str:
        '''Gets or sets the foreground color of the barcode symbol. Valid values are in the range [0, 0xFFFFFF]'''
        ...
    
    @foreground_color.setter
    def foreground_color(self, value: str):
        ...
    
    @property
    def background_color(self) -> str:
        '''Gets or sets the background color of the barcode symbol. Valid values are in the range [0, 0xFFFFFF]'''
        ...
    
    @background_color.setter
    def background_color(self, value: str):
        ...
    
    @property
    def pos_code_style(self) -> str:
        '''Gets or sets the style of a Point of Sale barcode (barcode types UPCA|UPCE|EAN13|EAN8). The valid values (case insensitive) are [STD|SUP2|SUP5|CASE].'''
        ...
    
    @pos_code_style.setter
    def pos_code_style(self, value: str):
        ...
    
    @property
    def case_code_style(self) -> str:
        '''Gets or sets the style of a Case Code for barcode type ITF14. The valid values are [STD|EXT|ADD]'''
        ...
    
    @case_code_style.setter
    def case_code_style(self, value: str):
        ...
    
    @property
    def error_correction_level(self) -> str:
        '''Gets or sets an error correction level of QR Code. Valid values are [0, 3].'''
        ...
    
    @error_correction_level.setter
    def error_correction_level(self, value: str):
        ...
    
    @property
    def display_text(self) -> bool:
        '''Gets or sets whether to display barcode data (text) along with image.'''
        ...
    
    @display_text.setter
    def display_text(self, value: bool):
        ...
    
    @property
    def add_start_stop_char(self) -> bool:
        '''Gets or sets whether to add Start/Stop characters for barcode types NW7 and CODE39.'''
        ...
    
    @add_start_stop_char.setter
    def add_start_stop_char(self, value: bool):
        ...
    
    @property
    def fix_check_digit(self) -> bool:
        '''Gets or sets whether to fix the check digit if it’s invalid.'''
        ...
    
    @fix_check_digit.setter
    def fix_check_digit(self, value: bool):
        ...
    
    ...

class FieldMergeField(aspose.words.fields.Field):
    '''Implements the MERGEFIELD field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the name of a data field within the merge characters in a mail merge main document.
    When the main document is merged with the selected data source, information from the specified
    data field is inserted in place of the merge field.'''
    
    @property
    def type(self) -> aspose.words.fields.FieldType:
        '''Gets the Microsoft Word field type.'''
        ...
    
    @property
    def field_name_no_prefix(self) -> str:
        '''Returns just the name of the data field. Any prefix is stripped to the prefix property.'''
        ...
    
    @property
    def field_name(self) -> str:
        '''Gets or sets the name of a data field.'''
        ...
    
    @field_name.setter
    def field_name(self, value: str):
        ...
    
    @property
    def text_before(self) -> str:
        '''Gets or sets the text to be inserted before the field if the field is not blank.'''
        ...
    
    @text_before.setter
    def text_before(self, value: str):
        ...
    
    @property
    def text_after(self) -> str:
        '''Gets or sets the text to be inserted after the field if the field is not blank.'''
        ...
    
    @text_after.setter
    def text_after(self, value: str):
        ...
    
    @property
    def is_mapped(self) -> bool:
        '''Gets or sets whether this field is a mapped field.'''
        ...
    
    @is_mapped.setter
    def is_mapped(self, value: bool):
        ...
    
    @property
    def is_vertical_formatting(self) -> bool:
        '''Gets or sets whether to enable character conversion for vertical formatting.'''
        ...
    
    @is_vertical_formatting.setter
    def is_vertical_formatting(self, value: bool):
        ...
    
    ...

class FieldMergeRec(aspose.words.fields.Field):
    '''Implements the MERGEREC field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    At the moment the MERGEREC and MERGESEQ fields implement the same functionality because we don't know for sure
    how to skip records in Aspose.Words mail merge.'''
    
    def __init__(self):
        ...
    
    ...

class FieldMergeSeq(aspose.words.fields.Field):
    '''Implements the MERGESEQ field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    At the moment the MERGEREC and MERGESEQ fields implement the same functionality because we don't know for sure
    how to skip records in Aspose.Words mail merge.'''
    
    def __init__(self):
        ...
    
    ...

class FieldNext(aspose.words.fields.Field):
    '''Implements the NEXT field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Merges the next data record into the current resulting merged document, rather than starting a
    new merged document.'''
    
    def __init__(self):
        ...
    
    ...

class FieldNextIf(aspose.words.fields.Field):
    '''Implements the NEXTIF field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Compares the values designated by the expressions :attr:`FieldNextIf.left_expression` and :attr:`FieldNextIf.right_expression`
    in comparison using the operator designated by :attr:`FieldNextIf.comparison_operator`. If the comparison is true,
    the next data record is merged into the current merge document. (Merge fields that follow the NEXTIF in the main
    document are replaced by values from the next data record rather than the current data record.)
    If the comparison is false, the next data record is merged into a new merge document.'''
    
    def __init__(self):
        ...
    
    @property
    def left_expression(self) -> str:
        '''Gets or sets the left part of the comparison expression.'''
        ...
    
    @left_expression.setter
    def left_expression(self, value: str):
        ...
    
    @property
    def comparison_operator(self) -> str:
        '''Gets or sets the comparison operator.'''
        ...
    
    @comparison_operator.setter
    def comparison_operator(self, value: str):
        ...
    
    @property
    def right_expression(self) -> str:
        '''Gets or sets the right part of the comparison expression.'''
        ...
    
    @right_expression.setter
    def right_expression(self, value: str):
        ...
    
    ...

class FieldNoteRef(aspose.words.fields.Field):
    '''Implements the NOTEREF field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts the mark of the footnote or endnote that is marked by the specified bookmark.'''
    
    def __init__(self):
        ...
    
    @property
    def bookmark_name(self) -> str:
        '''Gets or sets the name of the bookmark.'''
        ...
    
    @bookmark_name.setter
    def bookmark_name(self, value: str):
        ...
    
    @property
    def insert_reference_mark(self) -> bool:
        '''Inserts the reference mark with the same character formatting as the Footnote Reference
        or Endnote Reference style.'''
        ...
    
    @insert_reference_mark.setter
    def insert_reference_mark(self, value: bool):
        ...
    
    @property
    def insert_hyperlink(self) -> bool:
        '''Gets or sets whether to insert a hyperlink to the bookmarked paragraph.'''
        ...
    
    @insert_hyperlink.setter
    def insert_hyperlink(self, value: bool):
        ...
    
    @property
    def insert_relative_position(self) -> bool:
        '''Gets or sets whether to insert a relative position of the bookmarked paragraph.'''
        ...
    
    @insert_relative_position.setter
    def insert_relative_position(self, value: bool):
        ...
    
    ...

class FieldNumChars(aspose.words.fields.Field):
    '''Implements the NUMCHARS field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the number of characters in the current document, as recorded in the **Characters** property of the
    built-in document properties.'''
    
    def __init__(self):
        ...
    
    ...

class FieldNumPages(aspose.words.fields.Field):
    '''Implements the NUMPAGES field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the number of pages in the current document, as recorded in the **Pages** property of the
    built-in document properties.'''
    
    def __init__(self):
        ...
    
    ...

class FieldNumWords(aspose.words.fields.Field):
    '''Implements the NUMWORDS field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the number of words in the current document, as recorded in the **Words** property of the
    built-in document properties.'''
    
    def __init__(self):
        ...
    
    ...

class FieldOcx(aspose.words.fields.Field):
    '''Implements the OCX field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self):
        ...
    
    ...

class FieldOptions:
    '''Represents options to control field handling in a document.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    @property
    def field_update_culture_source(self) -> aspose.words.fields.FieldUpdateCultureSource:
        '''Specifies what culture to use to format the field result.
        
        By default, the culture of the current thread is used.
        
        The setting affects only date/time fields with \\\\@ format switch.'''
        ...
    
    @field_update_culture_source.setter
    def field_update_culture_source(self, value: aspose.words.fields.FieldUpdateCultureSource):
        ...
    
    @property
    def field_update_culture_provider(self) -> aspose.words.fields.IFieldUpdateCultureProvider:
        '''Gets or sets a provider that returns a culture object specific for each particular field.
        
        The provider is requested when the value of :attr:`FieldOptions.field_update_culture_source` is :attr:`FieldUpdateCultureSource.FIELD_CODE`.
        
        If the provider is present, then the culture object it returns is used for the field update. Otherwise, a system culture is used.'''
        ...
    
    @field_update_culture_provider.setter
    def field_update_culture_provider(self, value: aspose.words.fields.IFieldUpdateCultureProvider):
        ...
    
    @property
    def is_bidi_text_supported_on_update(self) -> bool:
        '''Gets or sets the value indicating whether bidirectional text is fully supported during field update or not.
        
        When this property is set to ``True``, additional steps are performed to produce Right-To-Left language
        (i.e. Arabic or Hebrew) compatible field result during its update.
        
        When this property is set to ``False`` and Right-To-Left language is used, correctness of field result
        after its update is not guaranteed.
        
        The default value is ``False``.'''
        ...
    
    @is_bidi_text_supported_on_update.setter
    def is_bidi_text_supported_on_update(self, value: bool):
        ...
    
    @property
    def user_prompt_respondent(self) -> aspose.words.fields.IFieldUserPromptRespondent:
        '''Gets or sets the respondent to user prompts during field update.
        
        If the value of this property is set to ``None``, the fields that require user response on prompting
        (such as :class:`FieldAsk` or :class:`FieldFillIn`) are not updated.
        
        The default value is ``None``.'''
        ...
    
    @user_prompt_respondent.setter
    def user_prompt_respondent(self, value: aspose.words.fields.IFieldUserPromptRespondent):
        ...
    
    @property
    def comparison_expression_evaluator(self) -> aspose.words.fields.IComparisonExpressionEvaluator:
        '''Gets or sets the field comparison expressions evaluator.'''
        ...
    
    @comparison_expression_evaluator.setter
    def comparison_expression_evaluator(self, value: aspose.words.fields.IComparisonExpressionEvaluator):
        ...
    
    @property
    def default_document_author(self) -> str:
        '''Gets or sets default document author's name. If author's name is already specified in built-in document properties,
        this option is not considered.'''
        ...
    
    @default_document_author.setter
    def default_document_author(self, value: str):
        ...
    
    @property
    def custom_toc_style_separator(self) -> str:
        '''Gets or sets custom style separator for the \\t switch in :class:`FieldToc` field.
        
        By default, custom styles defined by the \\t switch in the :class:`FieldToc` field are separated by a delimiter taken from the current culture.
        This property overrides that behaviour by specifying a user defined delimiter.'''
        ...
    
    @custom_toc_style_separator.setter
    def custom_toc_style_separator(self, value: str):
        ...
    
    @property
    def legacy_number_format(self) -> bool:
        '''Gets or sets the value indicating whether legacy (early than AW 13.10) number format for fields is enabled or not.
        
        When this property is set to ``True``, template symbol "#" worked as in .net:
        Replaces the pound sign with the corresponding digit if one is present; otherwise, no symbols appears in the result string.
        
        When this property is set to ``False``, template symbol "#" works as MS Word:
        This format item specifies the requisite numeric places to display in the result.
        If the result does not include a digit in that place, MS Word displays a space. For example, { = 9 + 6 \\# $### } displays $ 15.
        
        The default value is ``False``.'''
        ...
    
    @legacy_number_format.setter
    def legacy_number_format(self, value: bool):
        ...
    
    @property
    def use_invariant_culture_number_format(self) -> bool:
        '''Gets or sets the value indicating that number format is parsed using invariant culture or not
        
        When this property is set to ``True``, number format is taken from an invariant culture.
        
        When this property is set to ``False``, number format is taken from the current thread's culture.
        
        The default value is ``False``.'''
        ...
    
    @use_invariant_culture_number_format.setter
    def use_invariant_culture_number_format(self, value: bool):
        ...
    
    @property
    def barcode_generator(self) -> aspose.words.fields.IBarcodeGenerator:
        '''Gets or set custom barcode generator.
        
        Custom barcode generator should implement public interface :class:`IBarcodeGenerator`.'''
        ...
    
    @barcode_generator.setter
    def barcode_generator(self, value: aspose.words.fields.IBarcodeGenerator):
        ...
    
    @property
    def field_database_provider(self) -> aspose.words.fields.IFieldDatabaseProvider:
        '''Gets or sets a provider that returns a query result for the :class:`FieldDatabase` field.'''
        ...
    
    @field_database_provider.setter
    def field_database_provider(self, value: aspose.words.fields.IFieldDatabaseProvider):
        ...
    
    @property
    def current_user(self) -> aspose.words.fields.UserInformation:
        '''Gets or sets the current user information.'''
        ...
    
    @current_user.setter
    def current_user(self, value: aspose.words.fields.UserInformation):
        ...
    
    @property
    def toa_categories(self) -> aspose.words.fields.ToaCategories:
        '''Gets or sets the table of authorities categories.'''
        ...
    
    @toa_categories.setter
    def toa_categories(self, value: aspose.words.fields.ToaCategories):
        ...
    
    @property
    def field_index_format(self) -> aspose.words.fields.FieldIndexFormat:
        '''Gets or sets a :attr:`FieldOptions.field_index_format` that represents
        the formatting for the :class:`FieldIndex` fields in the document.'''
        ...
    
    @field_index_format.setter
    def field_index_format(self, value: aspose.words.fields.FieldIndexFormat):
        ...
    
    @property
    def file_name(self) -> str:
        '''Gets or sets the file name of the document.
        
        This property is used by the :class:`FieldFileName` field with higher priority than the :attr:`aspose.words.Document.original_file_name` property.'''
        ...
    
    @file_name.setter
    def file_name(self, value: str):
        ...
    
    @property
    def template_name(self) -> str:
        '''Gets or sets the file name of the template used by the document.
        
        This property is used by the :class:`FieldTemplate` field if the :attr:`aspose.words.Document.attached_template` property is empty.
        
        If this property is empty, the default template file name ``Normal.dotm`` is used.'''
        ...
    
    @template_name.setter
    def template_name(self, value: str):
        ...
    
    @property
    def result_formatter(self) -> aspose.words.fields.IFieldResultFormatter:
        '''Allows to control how the field result is formatted.'''
        ...
    
    @result_formatter.setter
    def result_formatter(self, value: aspose.words.fields.IFieldResultFormatter):
        ...
    
    @property
    def built_in_templates_paths(self) -> list[str]:
        '''Gets or sets paths of MS Word built-in templates.
        
        This property is used by the :class:`FieldAutoText` and :class:`FieldGlossary` fields, if referenced auto text entry is not found in the :attr:`aspose.words.Document.attached_template` template.
        
        By default MS Word stores built-in templates in c:\\Users\\\<username\>\\AppData\\Roaming\\Microsoft\\Document Building Blocks\\1033\\16\\Built-In Building Blocks.dotx and
        C:\\Users\\\<username\>\\AppData\\Roaming\\Microsoft\\Templates\\Normal.dotm files.'''
        ...
    
    @built_in_templates_paths.setter
    def built_in_templates_paths(self, value: list[str]):
        ...
    
    @property
    def field_updating_callback(self) -> aspose.words.fields.IFieldUpdatingCallback:
        '''Gets or sets :class:`IFieldUpdatingCallback` implementation'''
        ...
    
    @field_updating_callback.setter
    def field_updating_callback(self, value: aspose.words.fields.IFieldUpdatingCallback):
        ...
    
    @property
    def field_updating_progress_callback(self) -> aspose.words.fields.IFieldUpdatingProgressCallback:
        '''Gets or sets :class:`IFieldUpdatingProgressCallback` implementation.'''
        ...
    
    @field_updating_progress_callback.setter
    def field_updating_progress_callback(self, value: aspose.words.fields.IFieldUpdatingProgressCallback):
        ...
    
    ...

class FieldPage(aspose.words.fields.Field):
    '''Implements the PAGE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the number of the current page.'''
    
    def __init__(self):
        ...
    
    ...

class FieldPageRef(aspose.words.fields.Field):
    '''Implements the PAGEREF field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts the number of the page containing the specified bookmark for a cross-reference.'''
    
    def __init__(self):
        ...
    
    @property
    def bookmark_name(self) -> str:
        '''Gets or sets the name of the bookmark.'''
        ...
    
    @bookmark_name.setter
    def bookmark_name(self, value: str):
        ...
    
    @property
    def insert_hyperlink(self) -> bool:
        '''Gets or sets whether to insert a hyperlink to the bookmarked paragraph.'''
        ...
    
    @insert_hyperlink.setter
    def insert_hyperlink(self, value: bool):
        ...
    
    @property
    def insert_relative_position(self) -> bool:
        '''Gets or sets whether to insert a relative position of the bookmarked paragraph.'''
        ...
    
    @insert_relative_position.setter
    def insert_relative_position(self, value: bool):
        ...
    
    ...

class FieldPrint(aspose.words.fields.Field):
    '''Implements the PRINT field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    An instruction to send the printer-specific control code characters to the selected printer
    when the document is printed.'''
    
    def __init__(self):
        ...
    
    @property
    def printer_instructions(self) -> str:
        '''Gets or sets the printer-specific control code characters or PostScript instructions.'''
        ...
    
    @printer_instructions.setter
    def printer_instructions(self, value: str):
        ...
    
    @property
    def post_script_group(self) -> str:
        '''Gets or sets the drawing rectangle that the PostScript instructions operate on.'''
        ...
    
    @post_script_group.setter
    def post_script_group(self, value: str):
        ...
    
    ...

class FieldPrintDate(aspose.words.fields.Field):
    '''Implements the PRINTDATE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the date and time on which the document was last printed. By default, the Gregorian calendar is used.'''
    
    def __init__(self):
        ...
    
    @property
    def use_lunar_calendar(self) -> bool:
        '''Gets or sets whether to use the Hijri Lunar or Hebrew Lunar calendar.'''
        ...
    
    @use_lunar_calendar.setter
    def use_lunar_calendar(self, value: bool):
        ...
    
    @property
    def use_saka_era_calendar(self) -> bool:
        '''Gets or sets whether to use the Saka Era calendar.'''
        ...
    
    @use_saka_era_calendar.setter
    def use_saka_era_calendar(self, value: bool):
        ...
    
    @property
    def use_um_al_qura_calendar(self) -> bool:
        '''Gets or sets whether to use the Um-al-Qura calendar.'''
        ...
    
    @use_um_al_qura_calendar.setter
    def use_um_al_qura_calendar(self, value: bool):
        ...
    
    ...

class FieldPrivate(aspose.words.fields.Field):
    '''Implements the PRIVATE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Provides a private storage area. This field is used to store data for documents converted from other
    file formats.'''
    
    def __init__(self):
        ...
    
    ...

class FieldQuote(aspose.words.fields.Field):
    '''Implements the QUOTE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the specified text.'''
    
    def __init__(self):
        ...
    
    @property
    def text(self) -> str:
        '''Gets or sets the text to retrieve.'''
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    ...

class FieldRD(aspose.words.fields.Field):
    '''Implements the RD field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Identifies a file to include when you create a table of contents, a table of authorities, or an index
    with the TOC, TOA, or INDEX field'''
    
    def __init__(self):
        ...
    
    @property
    def file_name(self) -> str:
        '''Gets or sets the name of the file to include when generating a table of contents, table of authorities, or index.'''
        ...
    
    @file_name.setter
    def file_name(self, value: str):
        ...
    
    @property
    def is_path_relative(self) -> bool:
        '''Gets or sets whether the path is relative to the current document.'''
        ...
    
    @is_path_relative.setter
    def is_path_relative(self, value: bool):
        ...
    
    ...

class FieldRef(aspose.words.fields.Field):
    '''Implements the REF field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts the text or graphics represented by the specified bookmark.'''
    
    def __init__(self):
        ...
    
    @property
    def bookmark_name(self) -> str:
        '''Gets or sets the referenced bookmark's name.'''
        ...
    
    @bookmark_name.setter
    def bookmark_name(self, value: str):
        ...
    
    @property
    def number_separator(self) -> str:
        '''Gets or sets the character sequence that is used to separate sequence numbers and page numbers.'''
        ...
    
    @number_separator.setter
    def number_separator(self, value: str):
        ...
    
    @property
    def include_note_or_comment(self) -> bool:
        '''Gets or sets whether to increment footnote, endnote, and annotation numbers that are
        marked by the bookmark, and insert the corresponding footnote, endnote, and comment text.'''
        ...
    
    @include_note_or_comment.setter
    def include_note_or_comment(self, value: bool):
        ...
    
    @property
    def insert_hyperlink(self) -> bool:
        '''Gets or sets whether to create a hyperlink to the bookmarked paragraph.'''
        ...
    
    @insert_hyperlink.setter
    def insert_hyperlink(self, value: bool):
        ...
    
    @property
    def insert_paragraph_number(self) -> bool:
        '''Gets or sets whether to insert the paragraph number of the referenced paragraph exactly as it appears in the document.'''
        ...
    
    @insert_paragraph_number.setter
    def insert_paragraph_number(self, value: bool):
        ...
    
    @property
    def insert_relative_position(self) -> bool:
        '''Gets or sets whether to insert the relative position of the referenced paragraph.'''
        ...
    
    @insert_relative_position.setter
    def insert_relative_position(self, value: bool):
        ...
    
    @property
    def insert_paragraph_number_in_relative_context(self) -> bool:
        '''Gets or sets whether to insert the paragraph number of the referenced paragraph in relative context.'''
        ...
    
    @insert_paragraph_number_in_relative_context.setter
    def insert_paragraph_number_in_relative_context(self, value: bool):
        ...
    
    @property
    def suppress_non_delimiters(self) -> bool:
        '''Gets or sets whether to suppress non-delimiter characters.'''
        ...
    
    @suppress_non_delimiters.setter
    def suppress_non_delimiters(self, value: bool):
        ...
    
    @property
    def insert_paragraph_number_in_full_context(self) -> bool:
        '''Gets or sets whether to insert the paragraph number of the referenced paragraph in full context.'''
        ...
    
    @insert_paragraph_number_in_full_context.setter
    def insert_paragraph_number_in_full_context(self, value: bool):
        ...
    
    ...

class FieldRevNum(aspose.words.fields.Field):
    '''Implements the REVNUM field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the document's revision number, as recorded in the **Revision** property of the
    built-in document properties.'''
    
    def __init__(self):
        ...
    
    ...

class FieldSaveDate(aspose.words.fields.Field):
    '''Implements the SAVEDATE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the date and time on which the document was last saved. By default, the Gregorian calendar is used.'''
    
    def __init__(self):
        ...
    
    @property
    def use_lunar_calendar(self) -> bool:
        '''Gets or sets whether to use the Hijri Lunar or Hebrew Lunar calendar.'''
        ...
    
    @use_lunar_calendar.setter
    def use_lunar_calendar(self, value: bool):
        ...
    
    @property
    def use_saka_era_calendar(self) -> bool:
        '''Gets or sets whether to use the Saka Era calendar.'''
        ...
    
    @use_saka_era_calendar.setter
    def use_saka_era_calendar(self, value: bool):
        ...
    
    @property
    def use_um_al_qura_calendar(self) -> bool:
        '''Gets or sets whether to use the Um-al-Qura calendar.'''
        ...
    
    @use_um_al_qura_calendar.setter
    def use_um_al_qura_calendar(self, value: bool):
        ...
    
    ...

class FieldSection(aspose.words.fields.Field):
    '''Implements the SECTION field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the number of the current section.'''
    
    def __init__(self):
        ...
    
    ...

class FieldSectionPages(aspose.words.fields.Field):
    '''Implements the SECTIONPAGES field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the number of the current page within the current section.'''
    
    def __init__(self):
        ...
    
    ...

class FieldSeparator(aspose.words.fields.FieldChar):
    '''Represents a Word field separator that separates the field code from the field result.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    :class:`FieldSeparator` is an inline-level node and represented
    by the :attr:`aspose.words.ControlChar.FIELD_SEPARATOR_CHAR` control character in the document.
    
    :class:`FieldSeparator` can only be a child of :class:`aspose.words.Paragraph`.
    
    A complete field in a Microsoft Word document is a complex structure consisting of
    a field start character, field code, field separator character, field result
    and field end character. Some fields only have field start, field code and field end.
    
    To easily insert a new field into a document, use the :meth:`aspose.words.DocumentBuilder.insert_field`
    method.'''
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        '''Accepts a visitor.
        
        Calls :meth:`aspose.words.DocumentVisitor.visit_field_separator`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the node.
        :returns: **False** if the visitor requested the enumeration to stop.'''
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        '''Returns :attr:`aspose.words.NodeType.FIELD_SEPARATOR`.'''
        ...
    
    ...

class FieldSeq(aspose.words.fields.Field):
    '''Implements the SEQ field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Sequentially numbers chapters, tables, figures, and other user-defined lists of items in a document.'''
    
    def __init__(self):
        ...
    
    @property
    def sequence_identifier(self) -> str:
        '''Gets or sets the name assigned to the series of items that are to be numbered.'''
        ...
    
    @sequence_identifier.setter
    def sequence_identifier(self, value: str):
        ...
    
    @property
    def bookmark_name(self) -> str:
        '''Gets or sets a bookmark name that refers to an item elsewhere in the document rather than in the current location.'''
        ...
    
    @bookmark_name.setter
    def bookmark_name(self, value: str):
        ...
    
    @property
    def insert_next_number(self) -> bool:
        '''Gets or sets whether to insert the next sequence number for the specified item.'''
        ...
    
    @insert_next_number.setter
    def insert_next_number(self, value: bool):
        ...
    
    @property
    def reset_number(self) -> str:
        '''Gets or sets an integer number to reset the sequence number to. Returns -1 if the number is absent.'''
        ...
    
    @reset_number.setter
    def reset_number(self, value: str):
        ...
    
    @property
    def reset_heading_level(self) -> str:
        '''Gets or sets an integer number representing a heading level to reset the sequence number to.
        Returns -1 if the number is absent.'''
        ...
    
    @reset_heading_level.setter
    def reset_heading_level(self, value: str):
        ...
    
    ...

class FieldSet(aspose.words.fields.Field):
    '''Implements the SET field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Assigns new text to a bookmark.'''
    
    def __init__(self):
        ...
    
    @property
    def bookmark_name(self) -> str:
        '''Gets or sets the name of the bookmark.'''
        ...
    
    @bookmark_name.setter
    def bookmark_name(self, value: str):
        ...
    
    @property
    def bookmark_text(self) -> str:
        '''Gets or sets the new text of the bookmark.'''
        ...
    
    @bookmark_text.setter
    def bookmark_text(self, value: str):
        ...
    
    ...

class FieldShape(aspose.words.fields.Field):
    '''Implements the SHAPE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the specified text.'''
    
    def __init__(self):
        ...
    
    @property
    def text(self) -> str:
        '''Gets or sets the text to retrieve.'''
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    ...

class FieldSkipIf(aspose.words.fields.Field):
    '''Implements the SKIPIF field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Compares the values designated by the expressions :attr:`FieldSkipIf.left_expression` and :attr:`FieldSkipIf.right_expression`
    in comparison using the operator designated by :attr:`FieldSkipIf.comparison_operator`. If the comparison is true, SKIPIF
    cancels the current merge document, moves to the next data record in the data source, and starts a new merge document.
    If the comparison is false, the current merge document is continued.'''
    
    def __init__(self):
        ...
    
    @property
    def left_expression(self) -> str:
        '''Gets or sets the left part of the comparison expression.'''
        ...
    
    @left_expression.setter
    def left_expression(self, value: str):
        ...
    
    @property
    def comparison_operator(self) -> str:
        '''Gets or sets the comparison operator.'''
        ...
    
    @comparison_operator.setter
    def comparison_operator(self, value: str):
        ...
    
    @property
    def right_expression(self) -> str:
        '''Gets or sets the right part of the comparison expression.'''
        ...
    
    @right_expression.setter
    def right_expression(self, value: str):
        ...
    
    ...

class FieldStart(aspose.words.fields.FieldChar):
    '''Represents a start of a Word field in a document.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    :class:`FieldStart` is an inline-level node and represented by the
    :attr:`aspose.words.ControlChar.FIELD_START_CHAR` control character in the document.
    
    :class:`FieldStart` can only be a child of :class:`aspose.words.Paragraph`.
    
    A complete field in a Microsoft Word document is a complex structure consisting of
    a field start character, field code, field separator character, field result
    and field end character. Some fields only have field start, field code and field end.
    
    To easily insert a new field into a document, use the :meth:`aspose.words.DocumentBuilder.insert_field`
    method.'''
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        '''Accepts a visitor.
        
        Calls :meth:`aspose.words.DocumentVisitor.visit_field_start`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the node.
        :returns: **False** if the visitor requested the enumeration to stop.'''
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        '''Returns :attr:`aspose.words.NodeType.FIELD_START`.'''
        ...
    
    @property
    def field_data(self) -> bytes:
        '''Gets custom field data which is associated with the field.'''
        ...
    
    ...

class FieldStyleRef(aspose.words.fields.Field):
    '''Implements the STYLEREF field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    The STYLEREF is used to reference a fragment of text within the document that is formatted with
    the specified style.'''
    
    def __init__(self):
        ...
    
    @property
    def style_name(self) -> str:
        '''Gets or sets the name of the style by which the text to search for is formatted.'''
        ...
    
    @style_name.setter
    def style_name(self, value: str):
        ...
    
    @property
    def search_from_bottom(self) -> bool:
        '''Gets or sets whether to search from the bottom of the current page, rather from the top.'''
        ...
    
    @search_from_bottom.setter
    def search_from_bottom(self, value: bool):
        ...
    
    @property
    def insert_paragraph_number(self) -> bool:
        '''Gets or sets whether to insert the paragraph number of the referenced paragraph exactly as it appears in the document.'''
        ...
    
    @insert_paragraph_number.setter
    def insert_paragraph_number(self, value: bool):
        ...
    
    @property
    def insert_relative_position(self) -> bool:
        '''Gets or sets whether to insert the relative position of the referenced paragraph.'''
        ...
    
    @insert_relative_position.setter
    def insert_relative_position(self, value: bool):
        ...
    
    @property
    def insert_paragraph_number_in_relative_context(self) -> bool:
        '''Gets or sets whether to insert the paragraph number of the referenced paragraph in relative context.'''
        ...
    
    @insert_paragraph_number_in_relative_context.setter
    def insert_paragraph_number_in_relative_context(self, value: bool):
        ...
    
    @property
    def suppress_non_delimiters(self) -> bool:
        '''Gets or sets whether to suppress non-delimiter characters.'''
        ...
    
    @suppress_non_delimiters.setter
    def suppress_non_delimiters(self, value: bool):
        ...
    
    @property
    def insert_paragraph_number_in_full_context(self) -> bool:
        '''Gets or sets whether to insert the paragraph number of the referenced paragraph in full context.'''
        ...
    
    @insert_paragraph_number_in_full_context.setter
    def insert_paragraph_number_in_full_context(self, value: bool):
        ...
    
    ...

class FieldSubject(aspose.words.fields.Field):
    '''Implements the SUBJECT field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves, and optionally sets, the document's subject, as recorded in the **Subject** property of the
    built-in document properties.'''
    
    def __init__(self):
        ...
    
    @property
    def text(self) -> str:
        '''Gets or sets the text of the subject.'''
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    ...

class FieldSymbol(aspose.words.fields.Field):
    '''Implements a SYMBOL field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the character whose code point value is specified in decimal or hexadecimal.'''
    
    def __init__(self):
        ...
    
    @property
    def character_code(self) -> str:
        '''Gets or sets the character's code point value in decimal or hexadecimal.'''
        ...
    
    @character_code.setter
    def character_code(self, value: str):
        ...
    
    @property
    def font_name(self) -> str:
        '''Gets or sets the name of the font of the character retrieved by the field.'''
        ...
    
    @font_name.setter
    def font_name(self, value: str):
        ...
    
    @property
    def font_size(self) -> str:
        '''Gets or sets the size in points of the font of the character retrieved by the field.'''
        ...
    
    @font_size.setter
    def font_size(self, value: str):
        ...
    
    @property
    def is_ansi(self) -> bool:
        '''Gets or sets whether the character code is interpreted as the value of an ANSI character.'''
        ...
    
    @is_ansi.setter
    def is_ansi(self, value: bool):
        ...
    
    @property
    def is_unicode(self) -> bool:
        '''Gets or sets whether the character code is interpreted as the value of a Unicode character.'''
        ...
    
    @is_unicode.setter
    def is_unicode(self, value: bool):
        ...
    
    @property
    def is_shift_jis(self) -> bool:
        '''Gets or sets whether the character code is interpreted as the value of a SHIFT-JIS character.'''
        ...
    
    @is_shift_jis.setter
    def is_shift_jis(self, value: bool):
        ...
    
    @property
    def dont_affects_line_spacing(self) -> bool:
        '''Gets or sets whether the character retrieved by the field affects the line spacing of the paragraph.'''
        ...
    
    @dont_affects_line_spacing.setter
    def dont_affects_line_spacing(self, value: bool):
        ...
    
    ...

class FieldTA(aspose.words.fields.Field):
    '''Implements the TA field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Defines the text and page number for a table of authorities entry, which is used by a TOA field.'''
    
    def __init__(self):
        ...
    
    @property
    def is_bold(self) -> bool:
        '''Gets or sets whether to apply bold formatting to the page number for the entry.'''
        ...
    
    @is_bold.setter
    def is_bold(self, value: bool):
        ...
    
    @property
    def entry_category(self) -> str:
        '''Gets or sets the integral entry category, which is a number that corresponds to the order of
        categories.'''
        ...
    
    @entry_category.setter
    def entry_category(self, value: str):
        ...
    
    @property
    def is_italic(self) -> bool:
        '''Gets or sets whether to apply italic formatting to the page number for the entry.'''
        ...
    
    @is_italic.setter
    def is_italic(self, value: bool):
        ...
    
    @property
    def long_citation(self) -> str:
        '''Gets or sets the long citation for the entry.'''
        ...
    
    @long_citation.setter
    def long_citation(self, value: str):
        ...
    
    @property
    def page_range_bookmark_name(self) -> str:
        '''Gets or sets the name of the bookmark that marks a range of pages that is inserted as the entry's page number.'''
        ...
    
    @page_range_bookmark_name.setter
    def page_range_bookmark_name(self, value: str):
        ...
    
    @property
    def short_citation(self) -> str:
        '''Gets or sets the short citation for the entry.'''
        ...
    
    @short_citation.setter
    def short_citation(self, value: str):
        ...
    
    ...

class FieldTC(aspose.words.fields.Field):
    '''Implements the TC field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Defines the text and page number for a table of contents (including a table of figures) entry, which
    is used by a TOC field.'''
    
    def __init__(self):
        ...
    
    @property
    def text(self) -> str:
        '''Gets or sets the text of the entry.'''
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    @property
    def type_identifier(self) -> str:
        '''Gets or sets a type identifier for this field (which is typically a letter).'''
        ...
    
    @type_identifier.setter
    def type_identifier(self, value: str):
        ...
    
    @property
    def entry_level(self) -> str:
        '''Gets or sets the level of the entry.'''
        ...
    
    @entry_level.setter
    def entry_level(self, value: str):
        ...
    
    @property
    def omit_page_number(self) -> bool:
        '''Gets or sets whether page number in TOC should be omitted for this field.'''
        ...
    
    @omit_page_number.setter
    def omit_page_number(self, value: bool):
        ...
    
    ...

class FieldTemplate(aspose.words.fields.Field):
    '''Implements the TEMPLATE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the file name of the template used by the current document.'''
    
    def __init__(self):
        ...
    
    @property
    def include_full_path(self) -> bool:
        '''Gets or sets whether to include the full file path name.'''
        ...
    
    @include_full_path.setter
    def include_full_path(self, value: bool):
        ...
    
    ...

class FieldTime(aspose.words.fields.Field):
    '''Implements the TIME field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Inserts the current date and time.'''
    
    def __init__(self):
        ...
    
    ...

class FieldTitle(aspose.words.fields.Field):
    '''Implements the TITLE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves, and optionally sets, the document's title, as recorded in the **Title** property of the
    built-in document properties.'''
    
    def __init__(self):
        ...
    
    @property
    def text(self) -> str:
        '''Gets or sets the text of the title.'''
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    ...

class FieldToa(aspose.words.fields.Field):
    '''Implements the TOA field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Builds a table of authorities (that is, a list of the references in a legal document, such as references
    to cases, statutes, and rules, along with the numbers of the pages on which the references appear) using the
    entries specified by TA fields.'''
    
    def __init__(self):
        ...
    
    @property
    def bookmark_name(self) -> str:
        '''Gets or sets the name of the bookmark that marks the portion of the document used to build the table.'''
        ...
    
    @bookmark_name.setter
    def bookmark_name(self, value: str):
        ...
    
    @property
    def entry_category(self) -> str:
        '''Gets or sets the integral category for entries included in the table.'''
        ...
    
    @entry_category.setter
    def entry_category(self, value: str):
        ...
    
    @property
    def sequence_separator(self) -> str:
        '''Gets or sets the character sequence that is used to separate sequence numbers and page numbers.'''
        ...
    
    @sequence_separator.setter
    def sequence_separator(self, value: str):
        ...
    
    @property
    def entry_separator(self) -> str:
        '''Gets or sets the character sequence that is used to separate a table of authorities entry and its page number.'''
        ...
    
    @entry_separator.setter
    def entry_separator(self, value: str):
        ...
    
    @property
    def remove_entry_formatting(self) -> bool:
        '''Gets or sets whether to remove the formatting of the entry text in the document from the
        entry in the table of authorities.'''
        ...
    
    @remove_entry_formatting.setter
    def remove_entry_formatting(self, value: bool):
        ...
    
    @property
    def page_range_separator(self) -> str:
        '''Gets or sets the character sequence that is used to separate the start and end of a page range.'''
        ...
    
    @page_range_separator.setter
    def page_range_separator(self, value: str):
        ...
    
    @property
    def use_heading(self) -> bool:
        '''Gets or sets whether to include the category heading for the entries in a table of authorities.'''
        ...
    
    @use_heading.setter
    def use_heading(self, value: bool):
        ...
    
    @property
    def page_number_list_separator(self) -> str:
        '''Gets or sets the character sequence that is used to separate two page numbers in a page number list.'''
        ...
    
    @page_number_list_separator.setter
    def page_number_list_separator(self, value: str):
        ...
    
    @property
    def use_passim(self) -> bool:
        '''Gets or sets whether to replace five or more different page references to the same
        authority with "passim", which is used to indicate that a word or passage occurs frequently
        in the work cited.'''
        ...
    
    @use_passim.setter
    def use_passim(self, value: bool):
        ...
    
    @property
    def sequence_name(self) -> str:
        '''Gets or sets the name of a sequence whose number is included with the page number.'''
        ...
    
    @sequence_name.setter
    def sequence_name(self, value: str):
        ...
    
    ...

class FieldToc(aspose.words.fields.Field):
    '''Implements the TOC field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Builds a table of contents (which can also be a table of figures) using the entries specified by TC fields,
    their heading levels, and specified styles, and inserts that table at this place in the document.'''
    
    def __init__(self):
        ...
    
    def update_page_numbers(self) -> bool:
        '''Updates the page numbers for items in this table of contents.
        
        :returns: ``True`` if the operation is successful. If any of the related TOC bookmarks was removed, ``False`` will be returned.'''
        ...
    
    @property
    def bookmark_name(self) -> str:
        '''Gets or sets the name of the bookmark that marks the portion of the document used to build the table.'''
        ...
    
    @bookmark_name.setter
    def bookmark_name(self, value: str):
        ...
    
    @property
    def table_of_figures_label(self) -> str:
        '''Gets or sets the name of the sequence identifier used when building a table of figures.'''
        ...
    
    @table_of_figures_label.setter
    def table_of_figures_label(self, value: str):
        ...
    
    @property
    def captionless_table_of_figures_label(self) -> str:
        '''Gets or sets the name of the sequence identifier used when building a table of figures that does not include caption's
        label and number.'''
        ...
    
    @captionless_table_of_figures_label.setter
    def captionless_table_of_figures_label(self, value: str):
        ...
    
    @property
    def sequence_separator(self) -> str:
        '''Gets or sets the character sequence that is used to separate sequence numbers and page numbers.'''
        ...
    
    @sequence_separator.setter
    def sequence_separator(self, value: str):
        ...
    
    @property
    def entry_identifier(self) -> str:
        '''Gets or sets a string that should match type identifiers of TC fields being included.'''
        ...
    
    @entry_identifier.setter
    def entry_identifier(self, value: str):
        ...
    
    @property
    def insert_hyperlinks(self) -> bool:
        '''Gets or sets whether to make the table of contents entries hyperlinks.'''
        ...
    
    @insert_hyperlinks.setter
    def insert_hyperlinks(self, value: bool):
        ...
    
    @property
    def entry_level_range(self) -> str:
        '''Gets or sets a range of levels of the table of contents entries to be included.'''
        ...
    
    @entry_level_range.setter
    def entry_level_range(self, value: str):
        ...
    
    @property
    def page_number_omitting_level_range(self) -> str:
        '''Gets or sets a range of levels of the table of contents entries from which to omits page numbers.'''
        ...
    
    @page_number_omitting_level_range.setter
    def page_number_omitting_level_range(self, value: str):
        ...
    
    @property
    def heading_level_range(self) -> str:
        '''Gets or sets a range of heading levels to include.'''
        ...
    
    @heading_level_range.setter
    def heading_level_range(self, value: str):
        ...
    
    @property
    def entry_separator(self) -> str:
        '''Gets or sets a sequence of characters that separate an entry and its page number.'''
        ...
    
    @entry_separator.setter
    def entry_separator(self, value: str):
        ...
    
    @property
    def prefixed_sequence_identifier(self) -> str:
        '''Gets or sets the identifier of a sequence for which a prefix should be added to the entry's page number.'''
        ...
    
    @prefixed_sequence_identifier.setter
    def prefixed_sequence_identifier(self, value: str):
        ...
    
    @property
    def custom_styles(self) -> str:
        '''Gets or sets a list of styles other than the built-in heading styles to include in the table of contents.'''
        ...
    
    @custom_styles.setter
    def custom_styles(self, value: str):
        ...
    
    @property
    def use_paragraph_outline_level(self) -> bool:
        '''Gets or sets whether to use the applied paragraph outline level.'''
        ...
    
    @use_paragraph_outline_level.setter
    def use_paragraph_outline_level(self, value: bool):
        ...
    
    @property
    def preserve_tabs(self) -> bool:
        '''Gets or sets whether to preserve tab entries within table entries.'''
        ...
    
    @preserve_tabs.setter
    def preserve_tabs(self, value: bool):
        ...
    
    @property
    def preserve_line_breaks(self) -> bool:
        '''Gets or sets whether to preserve newline characters within table entries.'''
        ...
    
    @preserve_line_breaks.setter
    def preserve_line_breaks(self, value: bool):
        ...
    
    @property
    def hide_in_web_layout(self) -> bool:
        '''Gets or sets whether to hide tab leader and page numbers in Web layout view.'''
        ...
    
    @hide_in_web_layout.setter
    def hide_in_web_layout(self, value: bool):
        ...
    
    ...

class FieldUnknown(aspose.words.fields.Field):
    '''Implements an unknown or unrecognized field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self):
        ...
    
    ...

class FieldUpdatingProgressArgs:
    '''Provides data for the field updating progress event.'''
    
    @property
    def total_fields_count(self) -> int:
        '''Gets the total fields count to be updated.
        
        The value is not constant and may be increased during updating process.'''
        ...
    
    @property
    def updated_fields_count(self) -> int:
        '''Gets the number of updated fields.'''
        ...
    
    @property
    def update_completed(self) -> bool:
        '''Gets a value indicating whether field updating is completed.'''
        ...
    
    ...

class FieldUserAddress(aspose.words.fields.Field):
    '''Implements the USERADDRESS field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the current user's postal address.'''
    
    def __init__(self):
        ...
    
    @property
    def user_address(self) -> str:
        '''Gets or sets the current user's postal address.'''
        ...
    
    @user_address.setter
    def user_address(self, value: str):
        ...
    
    ...

class FieldUserInitials(aspose.words.fields.Field):
    '''Implements the USERINITIALS field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the current user's initials.'''
    
    def __init__(self):
        ...
    
    @property
    def user_initials(self) -> str:
        '''Gets or sets the current user's initials.'''
        ...
    
    @user_initials.setter
    def user_initials(self, value: str):
        ...
    
    ...

class FieldUserName(aspose.words.fields.Field):
    '''Implements the USERNAME field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Retrieves the current user's name.'''
    
    def __init__(self):
        ...
    
    @property
    def user_name(self) -> str:
        '''Gest or sets the current user's name.'''
        ...
    
    @user_name.setter
    def user_name(self, value: str):
        ...
    
    ...

class FieldXE(aspose.words.fields.Field):
    '''Implements the XE field.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    Defines the text and page number for an index entry, which is used by an INDEX field.'''
    
    def __init__(self):
        ...
    
    @property
    def text(self) -> str:
        '''Gets or sets the text of the entry.'''
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    @property
    def is_bold(self) -> bool:
        '''Gets or sets whether to apply bold formatting to the entry's page number.'''
        ...
    
    @is_bold.setter
    def is_bold(self, value: bool):
        ...
    
    @property
    def entry_type(self) -> str:
        '''Gets or sets an index entry type.'''
        ...
    
    @entry_type.setter
    def entry_type(self, value: str):
        ...
    
    @property
    def is_italic(self) -> bool:
        '''Gets or sets whether to apply italic formatting to the entry's page number.'''
        ...
    
    @is_italic.setter
    def is_italic(self, value: bool):
        ...
    
    @property
    def page_range_bookmark_name(self) -> str:
        '''Gets or sets the name of the bookmark that marks a range of pages that is inserted as the entry's page number.'''
        ...
    
    @page_range_bookmark_name.setter
    def page_range_bookmark_name(self, value: str):
        ...
    
    @property
    def page_number_replacement(self) -> str:
        '''Gets or sets text used in place of a page number.'''
        ...
    
    @page_number_replacement.setter
    def page_number_replacement(self, value: str):
        ...
    
    @property
    def yomi(self) -> str:
        '''Gets or sets the yomi (first phonetic character for sorting indexes) for the index entry'''
        ...
    
    @yomi.setter
    def yomi(self, value: str):
        ...
    
    ...

class FormField(aspose.words.SpecialChar):
    '''Represents a single form field.
    To learn more, visit the `Working with Form Fields <https://docs.aspose.com/words/net/working-with-form-fields/>` documentation article.
    
    Microsoft Word provides the following form fields: checkbox, text input and dropdown (combobox).
    
    :class:`FormField` is an inline-node and can only be a child of :class:`aspose.words.Paragraph`.
    
    :class:`FormField` is represented in a document by a special character and
    positioned as a character within a line of text.
    
    A complete form field in a Word document is a complex structure represented by several
    nodes: field start, field code such as FORMTEXT, form field data, field separator,
    field result, field end and a bookmark. To programmatically create form fields in a Word document use
    :meth:`aspose.words.DocumentBuilder.insert_check_box`,
    :meth:`aspose.words.DocumentBuilder.insert_text_input` and
    :meth:`aspose.words.DocumentBuilder.insert_combo_box` which
    make sure all of the form field nodes are created in a correct order and in a suitable state.'''
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        '''Accepts a visitor.
        
        Calls :meth:`aspose.words.DocumentVisitor.visit_form_field`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the node.
        :returns: ``False`` if the visitor requested the enumeration to stop.'''
        ...
    
    def remove_field(self) -> None:
        '''Removes the complete form field, not just the form field special character.
        
        If there is a bookmark associated with the form field, the bookmark is not removed.'''
        ...
    
    def set_text_input_value(self, new_value: object) -> None:
        '''Applies the text format specified in :attr:`FormField.text_input_format` and stores the value in :attr:`FormField.result`.
        
        :param new_value: Can be a string, number or a **DateTime** object.
        
        The :attr:`FormField.text_input_default` value is applied if  is``None``.'''
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        '''Returns :attr:`aspose.words.NodeType.FORM_FIELD`.'''
        ...
    
    @property
    def name(self) -> str:
        '''Gets or sets the form field name.
        
        Microsoft Word allows strings with at most 20 characters.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def type(self) -> aspose.words.fields.FieldType:
        '''Returns the form field type.'''
        ...
    
    @property
    def result(self) -> str:
        '''Gets or sets a string that represents the result of this form field.
        
        For a text form field the result is the text that is in the field.
        
        For a checkbox form field the result can be "1" or "0" to indicate checked or unchecked.
        
        For a dropdown form field the result is the string selected in the dropdown.
        
        Setting :attr:`FormField.result` for a text form field does not apply the text format
        specified in :attr:`FormField.text_input_format`. If you want to set a value and apply the
        format, use the :meth:`FormField.set_text_input_value` method.
        
        For a text form field the :attr:`FormField.text_input_default` value is applied
        if  is``None``.'''
        ...
    
    @result.setter
    def result(self, value: str):
        ...
    
    @property
    def status_text(self) -> str:
        '''Returns or sets the text that's displayed in the status bar when a form field has the focus.
        
        If the :attr:`FormField.own_status` property is set to ``True``, the :attr:`FormField.status_text` property specifies the status bar text.
        If the :attr:`FormField.own_status` property is set to ``False``, the :attr:`FormField.status_text` property specifies the name of an AutoText
        entry that contains status bar text for the form field.
        
        Microsoft Word allows strings with at most 138 characters.'''
        ...
    
    @status_text.setter
    def status_text(self, value: str):
        ...
    
    @property
    def own_status(self) -> bool:
        '''Specifies the source of the text that's displayed in the status bar when a form field has the focus.
        
        If ``True``, the text specified by the :attr:`FormField.status_text` property is displayed.
        If ``False``, the text of the AutoText entry specified by the :attr:`FormField.status_text` property is displayed.'''
        ...
    
    @own_status.setter
    def own_status(self, value: bool):
        ...
    
    @property
    def help_text(self) -> str:
        '''Returns or sets the text that's displayed in a message box when the form field has the focus and the user presses F1.
        
        If the :attr:`FormField.own_help` property is set to ``True``, :attr:`FormField.help_text` specifies the text string value.
        If :attr:`FormField.own_help` is set to ``False``, :attr:`FormField.help_text` specifies the name of an AutoText entry that contains help
        text for the form field.
        
        Microsoft Word allows strings with at most 255 characters.'''
        ...
    
    @help_text.setter
    def help_text(self, value: str):
        ...
    
    @property
    def own_help(self) -> bool:
        '''Specifies the source of the text that's displayed in a message box when a form field has the focus and the user presses F1.
        
        If ``True``, the text specified by the :attr:`FormField.help_text` property is displayed.
        If ``False``, the text in the AutoText entry specified by the :attr:`FormField.help_text` property is displayed.'''
        ...
    
    @own_help.setter
    def own_help(self, value: bool):
        ...
    
    @property
    def calculate_on_exit(self) -> bool:
        '''True if references to the specified form field are automatically updated whenever the field is exited.
        
        Setting :attr:`FormField.calculate_on_exit` only affects the behavior of the form field when
        the document is opened in Microsoft Word. Aspose.Words never updates references
        to the form field.'''
        ...
    
    @calculate_on_exit.setter
    def calculate_on_exit(self, value: bool):
        ...
    
    @property
    def entry_macro(self) -> str:
        '''Returns or sets an entry macro name for the form field.
        
        The entry macro runs when the form field gets the focus in Microsoft Word.
        
        Microsoft Word allows strings with at most 32 characters.'''
        ...
    
    @entry_macro.setter
    def entry_macro(self, value: str):
        ...
    
    @property
    def exit_macro(self) -> str:
        '''Returns or sets an exit macro name for the form field.
        
        The exit macro runs when the form field loses the focus in Microsoft Word.
        
        Microsoft Word allows strings with at most 32 characters.'''
        ...
    
    @exit_macro.setter
    def exit_macro(self, value: str):
        ...
    
    @property
    def enabled(self) -> bool:
        '''True if a form field is enabled.
        
        If a form field is enabled, its contents can be changed as the form is filled in.'''
        ...
    
    @enabled.setter
    def enabled(self, value: bool):
        ...
    
    @property
    def text_input_format(self) -> str:
        '''Returns or sets the text formatting for a text form field.
        
        If the text form field contains regular text, then valid format strings are
        "", "UPPERCASE", "LOWERCASE", "FIRST CAPITAL" and "TITLE CASE". The strings
        are case-insensitive.
        
        If the text form field contains a number or a date/time value, then valid
        format strings are number or date and time format strings.
        
        Microsoft Word allows strings with at most 64 characters.'''
        ...
    
    @text_input_format.setter
    def text_input_format(self, value: str):
        ...
    
    @property
    def text_input_type(self) -> aspose.words.fields.TextFormFieldType:
        '''Gets or sets the type of a text form field.'''
        ...
    
    @text_input_type.setter
    def text_input_type(self, value: aspose.words.fields.TextFormFieldType):
        ...
    
    @property
    def text_input_default(self) -> str:
        '''Gets or sets the default string or a calculation expression of a text form field.
        
        The meaning of this property depends on the value of the :attr:`FormField.text_input_type` property.
        
        When :attr:`FormField.text_input_type` is :attr:`TextFormFieldType.REGULAR` or
        :attr:`TextFormFieldType.NUMBER`, this string specifies the default string for the text form field.
        This string is the content that Microsoft Word will display in the document when the form field is empty.
        
        When :attr:`FormField.text_input_type` is :attr:`TextFormFieldType.CALCULATED`, then this string holds
        the expression to be calculated. The expression needs to be a formula valid according to Microsoft Word formula field
        requirements. When you set a new expression using this property, Aspose.Words calculates the formula result
        automatically and inserts it into the form field.
        
        Microsoft Word allows strings with at most 255 characters.'''
        ...
    
    @text_input_default.setter
    def text_input_default(self, value: str):
        ...
    
    @property
    def max_length(self) -> int:
        '''Maximum length for the text field. Zero when the length is not limited.'''
        ...
    
    @max_length.setter
    def max_length(self, value: int):
        ...
    
    @property
    def drop_down_items(self) -> aspose.words.fields.DropDownItemCollection:
        '''Provides access to the items of a dropdown form field.
        
        Microsoft Word allows maximum 25 items in a dropdown form field.'''
        ...
    
    @property
    def drop_down_selected_index(self) -> int:
        '''Gets or sets the index specifying the currently selected item in a dropdown form field.'''
        ...
    
    @drop_down_selected_index.setter
    def drop_down_selected_index(self, value: int):
        ...
    
    @property
    def checked(self) -> bool:
        '''Gets or sets the checked status of the check box form field.
        Default value for this property is ``False``.
        
        Applicable for a check box form field only.'''
        ...
    
    @checked.setter
    def checked(self, value: bool):
        ...
    
    @property
    def default(self) -> bool:
        '''Gets or sets the default value of the check box form field.
        Default value for this property is ``False``.
        
        Applicable for a check box form field only.'''
        ...
    
    @default.setter
    def default(self, value: bool):
        ...
    
    @property
    def is_check_box_exact_size(self) -> bool:
        '''Gets or sets the boolean value that indicates whether the size of the textbox is automatic or specified explicitly.
        
        Applicable for a check box form field only.'''
        ...
    
    @is_check_box_exact_size.setter
    def is_check_box_exact_size(self, value: bool):
        ...
    
    @property
    def check_box_size(self) -> float:
        '''Gets or sets the size of the checkbox in points. Has effect only when :attr:`FormField.is_check_box_exact_size` is ``True``.
        
        Applicable for a check box form field only.'''
        ...
    
    @check_box_size.setter
    def check_box_size(self, value: float):
        ...
    
    ...

class FormFieldCollection:
    '''A collection of :class:`FormField` objects that represent all the form fields in a range.
    To learn more, visit the `Working with Form Fields <https://docs.aspose.com/words/net/working-with-form-fields/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.fields.FormField:
        '''Returns a form field at the specified index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the collection.'''
        ...
    
    def get_by_name(self, bookmark_name: str) -> aspose.words.fields.FormField:
        '''Returns a form field by bookmark name.'''
        ...
    
    def remove(self, form_field: str) -> None:
        '''Removes a form field with the specified name.
        
        If there is a bookmark associated with the form field, the bookmark is not removed.
        
        :param form_field: The case-insensitive name of the form field to remove.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes a form field at the specified index.
        
        If there is a bookmark associated with the form field, the bookmark is not removed.
        
        :param index: The zero-based index of the form field to remove.'''
        ...
    
    def clear(self) -> None:
        '''Removes all form fields from this collection and from the document.'''
        ...
    
    @property
    def count(self) -> int:
        '''Returns the number of form fields in the collection.'''
        ...
    
    ...

class GeneralFormatCollection:
    '''Represents a typed collection of general formats.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.fields.GeneralFormat:
        '''Gets a general format at the specified index.
        
        :param index: The index of a general format.
        :returns: A general format.'''
        ...
    
    def add(self, item: aspose.words.fields.GeneralFormat) -> None:
        '''Adds a general format to the collection.
        
        :param item: A general format.'''
        ...
    
    def remove(self, item: aspose.words.fields.GeneralFormat) -> None:
        '''Removes all occurrences of the specified general format from the collection.
        
        :param item: A general format.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes a general format occurrence at the specified index.
        
        :param index:'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the total number of the items in the collection.'''
        ...
    
    ...

class IBarcodeGenerator:
    '''Public interface for barcode custom generator. Implementation should be provided by user.
    
    Generator instance should be passed through the :attr:`FieldOptions.barcode_generator` property.'''
    
    ...

class IComparisonExpressionEvaluator:
    '''When implemented, allows to override default comparison expressions evaluation for the :class:`FieldIf` and :class:`FieldCompare` fields.'''
    
    def evaluate(self, field: aspose.words.fields.Field, expression: aspose.words.fields.ComparisonExpression) -> aspose.words.fields.ComparisonEvaluationResult:
        '''Evaluates comparison expression.
        
        The implementation should return ``None`` to indicate that the default evaluation should be performed.'''
        ...
    
    ...

class IFieldDatabaseProvider:
    '''Implement this interface to provide data for the :class:`FieldDatabase` field when it's updated.'''
    
    def get_query_result(self, file_name: str, connection: str, query: str, field: aspose.words.fields.FieldDatabase) -> aspose.words.fields.FieldDatabaseDataTable:
        '''Returns query result.
        
        :param file_name: The complete path and file name of the database specified in the \\d field switch.
        :param connection: The connection to the data specified in the \\c field switch.
        :param query: The set of SQL instructions that query the database specified in the \\s field switch.
        :param field: The field being updated.
        :returns: The :class:`FieldDatabaseDataTable` instance that should be used for the field's update.'''
        ...
    
    ...

class IFieldResultFormatter:
    '''Implement this interface if you want to control how the field result is formatted.'''
    
    @overload
    def format(self, value: str, format: aspose.words.fields.GeneralFormat) -> str:
        '''Called when Aspose.Words applies a capitalization format switch, i.e. \\\* Upper.
        
        The implementation should return ``None`` to indicate that the default formatting should be applied.'''
        ...
    
    @overload
    def format(self, value: float, format: aspose.words.fields.GeneralFormat) -> str:
        '''Called when Aspose.Words applies a number format switch, i.e. \\\* Ordinal.
        
        The implementation should return ``None`` to indicate that the default formatting should be applied.'''
        ...
    
    def format_numeric(self, value: float, format: str) -> str:
        '''Called when Aspose.Words applies a numeric format switch, i.e. \\# "#.##".
        
        The implementation should return ``None`` to indicate that the default formatting should be applied.'''
        ...
    
    def format_date_time(self, value: datetime.datetime, format: str, calendar_type: aspose.words.CalendarType) -> str:
        '''Called when Aspose.Words applies a date/time format switch, i.e. \\@ "dd.MM.yyyy".
        
        The implementation should return ``None`` to indicate that the default formatting should be applied.'''
        ...
    
    ...

class IFieldUpdateCultureProvider:
    '''When implemented, provides a System.Globalization.CultureInfo object that should be used during the update of a particular field.'''
    
    ...

class IFieldUpdatingCallback:
    '''Implement this interface if you want to have your own custom methods called during a field update.'''
    
    def field_updating(self, field: aspose.words.fields.Field) -> None:
        '''A user defined method that is called just before a field is updated.'''
        ...
    
    def field_updated(self, field: aspose.words.fields.Field) -> None:
        '''A user defined method that is called just after a field is updated.'''
        ...
    
    ...

class IFieldUpdatingProgressCallback:
    '''Implement this interface if you want to track field updating progress.'''
    
    def notify(self, args: aspose.words.fields.FieldUpdatingProgressArgs) -> None:
        '''A user defined method that is called when updating progress is changed.'''
        ...
    
    ...

class IFieldUserPromptRespondent:
    '''Represents the respondent to user prompts during field update.
    
    The ASK and FILLIN fields are the examples of fields that prompt the user for some response. Implement this interface
    and assign it to the :attr:`FieldOptions.user_prompt_respondent` property to establish interaction between field update
    and the user.'''
    
    def respond(self, prompt_text: str, default_response: str) -> str:
        '''When implemented, returns a response from the user on prompting.
        Your implementation should return ``None`` to indicate that the user has not responded to the prompt
        (i.e. the user has pressed the Cancel button in the prompt window).
        
        :param prompt_text: Prompt text (i.e. title of the prompt window).
        :param default_response: Default user response (i.e. initial value contained in the prompt window).
        :returns: User response (i.e. confirmed value contained in the prompt window).'''
        ...
    
    ...

class MergeFieldImageDimension:
    '''Represents an image dimension (i.e. the width or the height) used across a mail merge process.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.
    
    To indicate that the image should be inserted with its original dimension during a mail merge,
    you should assign a negative value to the :attr:`MergeFieldImageDimension.value` property.'''
    
    @overload
    def __init__(self, value: float):
        '''Creates an image dimension instance with the given value in points.
        
        You should use a negative value to indicate that the original value of the corresponding image dimension
        should be applied.
        
        :param value: The value.'''
        ...
    
    @overload
    def __init__(self, value: float, unit: aspose.words.fields.MergeFieldImageDimensionUnit):
        '''Creates an image dimension instance with the given value and the given unit.
        
        You should use a negative value to indicate that the original value of the corresponding image dimension
        should be applied.
        
        :param value: The value.
        :param unit: The unit.'''
        ...
    
    @property
    def value(self) -> float:
        '''The value.
        
        You should use a negative value to indicate that the original value of the corresponding image dimension
        should be applied.'''
        ...
    
    @value.setter
    def value(self, value: float):
        ...
    
    @property
    def unit(self) -> aspose.words.fields.MergeFieldImageDimensionUnit:
        '''The unit.'''
        ...
    
    @unit.setter
    def unit(self, value: aspose.words.fields.MergeFieldImageDimensionUnit):
        ...
    
    ...

class ToaCategories:
    '''Represents a table of authorities categories.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self):
        ...
    
    def __getitem__(self, index: int) -> str:
        '''Gets or sets the category heading by category number.'''
        ...
    
    def __setitem__(self, index: int, value: str):
        ...
    
    default_categories: aspose.words.fields.ToaCategories
    
    ...

class UserInformation:
    '''Specifies information about the user.
    To learn more, visit the `Working with Fields <https://docs.aspose.com/words/net/working-with-fields/>` documentation article.'''
    
    def __init__(self):
        ...
    
    @property
    def name(self) -> str:
        '''Gets or sets the user's name.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def initials(self) -> str:
        '''Gets or sets the user's initials.'''
        ...
    
    @initials.setter
    def initials(self, value: str):
        ...
    
    @property
    def address(self) -> str:
        '''Gets or sets the user's postal address.'''
        ...
    
    @address.setter
    def address(self, value: str):
        ...
    
    default_user: aspose.words.fields.UserInformation
    
    ...

class FieldIfComparisonResult:
    '''Specifies the result of the IF field condition evaluation.'''
    
    ERROR: int
    TRUE: int
    FALSE: int

class FieldIndexFormat:
    '''Specifies the formatting for the :class:`FieldIndex` fields in a document.'''
    
    TEMPLATE: int
    CLASSIC: int
    FANCY: int
    MODERN: int
    BULLETED: int
    FORMAL: int
    SIMPLE: int

class FieldType:
    '''Specifies Microsoft Word field types.'''
    
    FIELD_NONE: int
    FIELD_CANNOT_PARSE: int
    FIELD_ADDIN: int
    FIELD_ADDRESS_BLOCK: int
    FIELD_ADVANCE: int
    FIELD_ASK: int
    FIELD_AUTHOR: int
    FIELD_AUTO_NUM: int
    FIELD_AUTO_NUM_LEGAL: int
    FIELD_AUTO_NUM_OUTLINE: int
    FIELD_AUTO_TEXT: int
    FIELD_AUTO_TEXT_LIST: int
    FIELD_BARCODE: int
    FIELD_BIBLIOGRAPHY: int
    FIELD_BIDI_OUTLINE: int
    FIELD_CITATION: int
    FIELD_COMMENTS: int
    FIELD_COMPARE: int
    FIELD_CREATE_DATE: int
    FIELD_DATA: int
    FIELD_DATABASE: int
    FIELD_DATE: int
    FIELD_DDE: int
    FIELD_DISPLAY_BARCODE: int
    FIELD_MERGE_BARCODE: int
    FIELD_DDE_AUTO: int
    FIELD_DOC_PROPERTY: int
    FIELD_DOC_VARIABLE: int
    FIELD_EDIT_TIME: int
    FIELD_EMBED: int
    FIELD_EQUATION: int
    FIELD_FILE_NAME: int
    FIELD_FILE_SIZE: int
    FIELD_FILL_IN: int
    FIELD_FOOTNOTE_REF: int
    FIELD_FORM_CHECK_BOX: int
    FIELD_FORM_DROP_DOWN: int
    FIELD_FORM_TEXT_INPUT: int
    FIELD_FORMULA: int
    FIELD_GREETING_LINE: int
    FIELD_GLOSSARY: int
    FIELD_GO_TO_BUTTON: int
    FIELD_HTML_ACTIVE_X: int
    FIELD_HYPERLINK: int
    FIELD_IF: int
    FIELD_INCLUDE: int
    FIELD_INCLUDE_PICTURE: int
    FIELD_INCLUDE_TEXT: int
    FIELD_INDEX: int
    FIELD_INDEX_ENTRY: int
    FIELD_INFO: int
    FIELD_IMPORT: int
    FIELD_KEYWORD: int
    FIELD_LAST_SAVED_BY: int
    FIELD_LINK: int
    FIELD_LIST_NUM: int
    FIELD_MACRO_BUTTON: int
    FIELD_MERGE_FIELD: int
    FIELD_MERGE_REC: int
    FIELD_MERGE_SEQ: int
    FIELD_NEXT: int
    FIELD_NEXT_IF: int
    FIELD_NOTE_REF: int
    FIELD_NUM_CHARS: int
    FIELD_NUM_PAGES: int
    FIELD_NUM_WORDS: int
    FIELD_OCX: int
    FIELD_PAGE: int
    FIELD_PAGE_REF: int
    FIELD_PRINT: int
    FIELD_PRINT_DATE: int
    FIELD_PRIVATE: int
    FIELD_QUOTE: int
    FIELD_REF: int
    FIELD_REF_NO_KEYWORD: int
    FIELD_REF_DOC: int
    FIELD_REVISION_NUM: int
    FIELD_SAVE_DATE: int
    FIELD_SECTION: int
    FIELD_SECTION_PAGES: int
    FIELD_SEQUENCE: int
    FIELD_SET: int
    FIELD_SHAPE: int
    FIELD_SKIP_IF: int
    FIELD_STYLE_REF: int
    FIELD_SUBJECT: int
    FIELD_SYMBOL: int
    FIELD_TEMPLATE: int
    FIELD_TIME: int
    FIELD_TITLE: int
    FIELD_TOA: int
    FIELD_TOA_ENTRY: int
    FIELD_TOC: int
    FIELD_TOC_ENTRY: int
    FIELD_USER_ADDRESS: int
    FIELD_USER_INITIALS: int
    FIELD_USER_NAME: int

class FieldUpdateCultureSource:
    '''Indicates what culture to use during field update.'''
    
    CURRENT_THREAD: int
    FIELD_CODE: int

class GeneralFormat:
    '''Specifies a general format that is applied to a numeric, text, or any field result.
    A field may have a combination of general formats.'''
    
    NONE: int
    AIUEO: int
    UPPERCASE_ALPHABETIC: int
    LOWERCASE_ALPHABETIC: int
    ARABIC: int
    ARABIC_ABJAD: int
    ARABIC_ALPHA: int
    ARABIC_DASH: int
    BAHT_TEXT: int
    CARD_TEXT: int
    CHINESE_NUM1: int
    CHINESE_NUM2: int
    CHINESE_NUM3: int
    CHOSUNG: int
    CIRCLE_NUM: int
    DB_CHAR: int
    DB_NUM1: int
    DB_NUM2: int
    DB_NUM3: int
    DB_NUM4: int
    DOLLAR_TEXT: int
    GANADA: int
    GB1: int
    GB2: int
    GB3: int
    GB4: int
    HEBREW1: int
    HEBREW2: int
    HEX: int
    HINDI_ARABIC: int
    HINDI_CARD_TEXT: int
    HINDI_LETTER1: int
    HINDI_LETTER2: int
    IROHA: int
    KANJI_NUM1: int
    KANJI_NUM2: int
    KANJI_NUM3: int
    ORDINAL: int
    ORD_TEXT: int
    UPPERCASE_ROMAN: int
    LOWERCASE_ROMAN: int
    SB_CHAR: int
    THAI_ARABIC: int
    THAI_CARD_TEXT: int
    THAI_LETTER: int
    VIET_CARD_TEXT: int
    ZODIAC1: int
    ZODIAC2: int
    ZODIAC3: int
    CAPS: int
    FIRST_CAP: int
    LOWER: int
    UPPER: int
    CHAR_FORMAT: int
    MERGE_FORMAT: int
    MERGE_FORMAT_INET: int

class MergeFieldImageDimensionUnit:
    '''Specifies an unit of an image dimension (i.e. the width or the height) used across a mail merge process.'''
    
    POINT: int
    PERCENT: int

class TextFormFieldType:
    '''Specifies the type of a text form field.'''
    
    REGULAR: int
    NUMBER: int
    DATE: int
    CURRENT_DATE: int
    CURRENT_TIME: int
    CALCULATED: int

