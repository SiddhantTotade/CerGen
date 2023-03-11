import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class FieldMergingArgs(aspose.words.mailmerging.FieldMergingArgsBase):
    '''Provides data for the **MergeField** event.
    To learn more, visit the `Mail Merge and Reporting <https://docs.aspose.com/words/net/mail-merge-and-reporting/>` documentation article.
    
    The **MergeField** event occurs during mail merge when a simple mail merge
    field is encountered in the document. You can respond to this event to return
    text for the mail merge engine to insert into the document.'''
    
    @property
    def text(self) -> str:
        '''Gets or sets the text that will be inserted into the document for the current merge field.
        
        When your event handler is called, this property is set to ``None``.
        
        If you leave Text as ``None``, the mail merge engine will insert :attr:`FieldMergingArgsBase.field_value` in place of the merge field.
        
        If you set Text to any string (including empty), the string will be inserted into the document in place of the merge field.'''
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    ...

class FieldMergingArgsBase:
    '''Base class for :class:`FieldMergingArgs` and :class:`ImageFieldMergingArgs`.
    To learn more, visit the `Mail Merge and Reporting <https://docs.aspose.com/words/net/mail-merge-and-reporting/>` documentation article.'''
    
    @property
    def document(self) -> aspose.words.Document:
        '''Returns the :attr:`FieldMergingArgsBase.document` object for which the mail merge is performed.'''
        ...
    
    @property
    def table_name(self) -> str:
        '''Gets the name of the data table for the current merge operation or empty string if the name is not available.'''
        ...
    
    @property
    def record_index(self) -> int:
        '''Gets the zero based index of the record that is being merged.'''
        ...
    
    @property
    def field_name(self) -> str:
        '''Gets the name of the merge field in the data source.
        
        If you have a mapping from a document field name to a different data source field name,
        then this is the mapped field name.
        
        If you specified a field name prefix, for example "Image:MyFieldName" in the document,
        then :attr:`FieldMergingArgsBase.field_name` returns field name without the prefix, that is "MyFieldName".'''
        ...
    
    @property
    def document_field_name(self) -> str:
        '''Gets the name of the merge field as specified in the document.
        
        If you have a mapping from a document field name to a different data source field name,
        then this is the original field name as specified in the document.
        
        If you specified a field name prefix, for example "Image:MyFieldName" in the document,
        then :attr:`FieldMergingArgsBase.document_field_name` returns field name without the prefix, that is "MyFieldName".'''
        ...
    
    @property
    def field_value(self) -> object:
        '''Gets or sets the value of the field from the data source.
        
        This property contains a value that has just been selected from your data source
        for this field by the mail merge engine. You can also replace the value by setting the property.'''
        ...
    
    @field_value.setter
    def field_value(self, value: object):
        ...
    
    @property
    def field(self) -> aspose.words.fields.FieldMergeField:
        '''Gets the object that represents the current merge field.'''
        ...
    
    ...

class IFieldMergingCallback:
    '''Implement this interface if you want to control how data is inserted into merge fields during a mail merge operation.'''
    
    def field_merging(self, args: aspose.words.mailmerging.FieldMergingArgs) -> None:
        '''Called when the Aspose.Words mail merge engine is about to insert data into a merge field in the document.'''
        ...
    
    def image_field_merging(self, args: aspose.words.mailmerging.ImageFieldMergingArgs) -> None:
        '''Called when the Aspose.Words mail merge engine is about to insert an image into a merge field.'''
        ...
    
    ...

class IMailMergeCallback:
    '''Implement this interface if you want to receive notifications while mail merge is performed.'''
    
    def tags_replaced(self) -> None:
        '''Called when "mustache" text tags are replaced with MERGEFIELD fields.'''
        ...
    
    ...

class IMailMergeDataSource:
    '''Implement this interface to allow mail merge from a custom data source, such as a list of objects. Master-detail data is also supported.
    
    When a data source is created, it should be initialized to point to BOF (before the first record).
    The Aspose.Words mail merge engine will invoke :meth:`IMailMergeDataSource.move_next` to advance to next record and
    then invoke :meth:`IMailMergeDataSource.get_value` for every merge field it encounters in the document or the current mail merge region.'''
    
    def move_next(self) -> bool:
        '''Advances to the next record in the data source.
        
        :returns: ``True`` if moved to next record successfully; ``False`` if reached end of the data source.'''
        ...
    
    def get_value(self, field_name: str, field_value) -> bool:
        '''Returns a value for the specified field name or ``False`` if the field is not found.
        
        :param field_name: The name of the data field.
        :param field_value: Returns the field value.
        :returns: ``True`` if value was found.'''
        ...
    
    def get_child_data_source(self, table_name: str) -> aspose.words.mailmerging.IMailMergeDataSource:
        '''The Aspose.Words mail merge engine invokes this method when it encounters a beginning of a nested mail merge region.
        
        When the Aspose.Words mail merge engines populates a mail merge region with data and encounters the beginning of a nested
        mail merge region in the form of MERGEFIELD TableStart:TableName, it invokes :meth:`IMailMergeDataSource.get_child_data_source` on the current
        data source object. Your implementation needs to return a new data source object that will provide access to the child
        records of the current parent record. Aspose.Words will use the returned data source to populate the nested mail merge region.
        
        Below are the rules that the implementation of :meth:`IMailMergeDataSource.get_child_data_source` must follow.
        
        If the table that is represented by this data source object has a related child (detail) table with the specified name,
        then your implementation needs to return a new :class:`IMailMergeDataSource` object that will provide access
        to the child records of the current record.
        
        An example of this is Orders / OrderDetails relationship. Let's assume that the current :class:`IMailMergeDataSource` object
        represents the Orders table and it has a current order record. Next, Aspose.Words encounters "MERGEFIELD TableStart:OrderDetails"
        in the document and invokes :meth:`IMailMergeDataSource.get_child_data_source`. You need to create and return a :class:`IMailMergeDataSource`
        object that will allow Aspose.Words to access the OrderDetails record for the current order.
        
        If this data source object does not have a relation to the table with the specified name, then you need to return
        a :class:`IMailMergeDataSource` object that will provide access to all records of the specified table.
        
        If a table with the specified name does not exist, your implementation should return ``None``.
        
        :param table_name: The name of the mail merge region as specified in the template document. Case-insensitive.
        :returns: A data source object that will provide access to the data records of the specified table.'''
        ...
    
    @property
    def table_name(self) -> str:
        '''Returns the name of the data source.
        
        If you are implementing :class:`IMailMergeDataSource`, return the name of the data
        source from this property.
        
        Aspose.Words uses this name to match against the mail merge region name specified
        in the template document. The comparison between the data source name and
        the mail merge region name is not case sensitive.
        
        :returns: The name of the data source. Empty string if the data source has no name.'''
        ...
    
    ...

class IMailMergeDataSourceRoot:
    '''Implement this interface to allow mail merge from a custom data source with master-detail data.'''
    
    def get_data_source(self, table_name: str) -> aspose.words.mailmerging.IMailMergeDataSource:
        '''The Aspose.Words mail merge engine invokes this method when it encounters a beginning of a top-level mail merge region.
        
        When the Aspose.Words mail merge engines populates a document with data and encounters MERGEFIELD TableStart:TableName,
        it invokes :meth:`IMailMergeDataSourceRoot.get_data_source` on this object. Your implementation needs to return a new data source object.
        Aspose.Words will use the returned data source to populate the mail merge region.
        
        If a data source (table) with the specified name does not exist, your implementation should return ``None``.
        
        :param table_name: The name of the mail merge region as specified in the template document. Case-insensitive.
        :returns: A data source object that will provide access to the data records of the specified table.'''
        ...
    
    ...

class ImageFieldMergingArgs(aspose.words.mailmerging.FieldMergingArgsBase):
    '''Provides data for the :meth:`IFieldMergingCallback.image_field_merging` event.
    To learn more, visit the `Mail Merge and Reporting <https://docs.aspose.com/words/net/mail-merge-and-reporting/>` documentation article.
    
    This event occurs during mail merge when an image mail merge
    field is encountered in the document. You can respond to this event to return a
    file name, stream, or an SkiaSharp.SKBitmap object to the mail merge
    engine so it is inserted into the document.
    
    There are three properties available :attr:`ImageFieldMergingArgs.image_file_name`,
    :attr:`ImageFieldMergingArgs.image_stream` and Aspose.Words.MailMerging.ImageFieldMergingArgs.Image to specify where the image must be taken from.
    Set only one of these properties.
    
    To insert an image mail merge field into a document in Word, select Insert/Field command,
    then select MergeField and type Image:MyFieldName.'''
    
    @property
    def image_file_name(self) -> str:
        '''Sets the file name of the image that the mail merge engine must insert into the document.'''
        ...
    
    @image_file_name.setter
    def image_file_name(self, value: str):
        ...
    
    @property
    def image_stream(self) -> io.BytesIO:
        '''Specifies the stream for the mail merge engine to read an image from.
        
        Aspose.Words closes this stream after it merges the image into the document.'''
        ...
    
    @image_stream.setter
    def image_stream(self, value: io.BytesIO):
        ...
    
    @property
    def shape(self) -> aspose.words.drawing.Shape:
        '''Specifies the shape that the mail merge engine must insert into the document.
        
        When this property is specified, the mail merge engine ignores all other properties like :attr:`ImageFieldMergingArgs.image_file_name` or :attr:`ImageFieldMergingArgs.image_stream`
        and simply inserts the shape into the document.
        
        Use this property to fully control the process of merging an image merge field.
        For example, you can specify :attr:`aspose.words.drawing.ShapeBase.wrap_type` or any other shape property to fine tune the resulting node. However, please note that
        you are responsible for providing the content of the shape.'''
        ...
    
    @shape.setter
    def shape(self, value: aspose.words.drawing.Shape):
        ...
    
    @property
    def image_width(self) -> aspose.words.fields.MergeFieldImageDimension:
        '''Specifies the image width for the image to insert into the document.
        
        The value of this property initially comes from the corresponding MERGEFIELD's code, contained in the
        template document. To override the initial value, you should assign an instance of
        :class:`aspose.words.fields.MergeFieldImageDimension` class to this property or set the properties for the instance
        of :class:`aspose.words.fields.MergeFieldImageDimension` class, returned by this property.
        
        To indicate that the original value of the image width should be applied, you should assign the ``None``
        value to this property or set the :attr:`aspose.words.fields.MergeFieldImageDimension.value` property for the instance
        of :class:`aspose.words.fields.MergeFieldImageDimension` class, returned by this property, to a negative value.'''
        ...
    
    @image_width.setter
    def image_width(self, value: aspose.words.fields.MergeFieldImageDimension):
        ...
    
    @property
    def image_height(self) -> aspose.words.fields.MergeFieldImageDimension:
        '''Specifies the image height for the image to insert into the document.
        
        The value of this property initially comes from the corresponding MERGEFIELD's code, contained in the
        template document. To override the initial value, you should assign an instance of
        :class:`aspose.words.fields.MergeFieldImageDimension` class to this property or set the properties for the instance
        of :class:`aspose.words.fields.MergeFieldImageDimension` class, returned by this property.
        
        To indicate that the original value of the image height should be applied, you should assign the ``None``
        value to this property or set the :attr:`aspose.words.fields.MergeFieldImageDimension.value` property for the instance
        of :class:`aspose.words.fields.MergeFieldImageDimension` class, returned by this property, to a negative value.'''
        ...
    
    @image_height.setter
    def image_height(self, value: aspose.words.fields.MergeFieldImageDimension):
        ...
    
    ...

class MailMerge:
    '''Represents the mail merge functionality.
    To learn more, visit the `Mail Merge and Reporting <https://docs.aspose.com/words/net/mail-merge-and-reporting/>` documentation article.
    
    For mail merge operation to work, the document should contain Word MERGEFIELD and
    optionally NEXT fields. During mail merge operation, merge fields in the document are
    replaced with values from your data source.
    
    There are two distinct ways to use mail merge: with mail merge regions and without.
    
    The simplest mail merge is without regions and it is very similar to how mail merge
    works in Word. Use ``Execute`` methods to merge information from some
    data source such as **DataTable**, **DataSet**, **DataView**, **IDataReader**
    or an array of objects into your document. The
    :class:`MailMerge` object processes all records of the data source and copies and appends
    content of the whole document for each record.
    
    Note that when :class:`MailMerge` object encounters a NEXT field, it selects next record
    in the data source and continues merging without copying any content.
    
    Use :meth:`MailMerge.execute_with_regions` and other overloads to merge information into a
    document with mail merge regions defined. You can use
    **DataSet**, **DataTable**, **DataView** or **IDataReader**
    as data sources for this operation.
    
    You need to use mail merge regions if you want to dynamically grow portions inside the
    document. Without mail merge regions whole document will be repeated for every record of
    the data source.'''
    
    @overload
    def execute(self, data_source: aspose.words.mailmerging.IMailMergeDataSource) -> None:
        '''Performs a mail merge from a custom data source.
        
        Use this method to fill mail merge fields in the document with values from
        any data source such as a list or hashtable or objects. You need to write your
        own class that implements the :class:`IMailMergeDataSource` interface.
        
        You can use this method only when :attr:`aspose.words.fields.FieldOptions.is_bidi_text_supported_on_update` is ``False``,
        that is you do not need Right-To-Left language (such as Arabic or Hebrew) compatibility.
        
        This method ignores the :attr:`MailMergeCleanupOptions.REMOVE_UNUSED_REGIONS` option.
        
        :param data_source: An object that implements the custom mail merge data source interface.'''
        ...
    
    @overload
    def execute(self, field_names: list[str], values: list[object]) -> None:
        '''Performs a mail merge operation for a single record.
        
        Use this method to fill mail merge fields in the document with values from
        an array of objects.
        
        This method merges data for one record only. The array of field names
        and the array of values represent the data of a single record.
        
        This method does not use mail merge regions.
        
        This method ignores the :attr:`MailMergeCleanupOptions.REMOVE_UNUSED_REGIONS` option.
        
        :param field_names: Array of merge field names. Field names are not case sensitive.
                            If a field name that is not found in the document is encountered, it is ignored.
        :param values: Array of values to be inserted into the merge fields.
                       Number of elements in this array must be the same as the number of elements in .'''
        ...
    
    @overload
    def execute_with_regions(self, data_source: aspose.words.mailmerging.IMailMergeDataSource) -> None:
        '''Performs a mail merge from a custom data source with mail merge regions.
        
        Use this method to fill mail merge fields in the document with values from
        any custom data source such as an XML file or collections of business objects. You need to write your
        own class that implements the :class:`IMailMergeDataSource` interface.
        
        You can use this method only when :attr:`aspose.words.fields.FieldOptions.is_bidi_text_supported_on_update` is ``False``,
        that is you do not need Right-To-Left language (such as Arabic or Hebrew) compatibility.
        
        :param data_source: An object that implements the custom mail merge data source interface.'''
        ...
    
    @overload
    def execute_with_regions(self, data_source_root: aspose.words.mailmerging.IMailMergeDataSourceRoot) -> None:
        '''Performs a mail merge from a custom data source with mail merge regions.
        
        Use this method to fill mail merge fields in the document with values from
        any custom data source such as an XML file or collections of business objects. You need to write your own classes
        that implement the :class:`IMailMergeDataSourceRoot` and :class:`IMailMergeDataSource` interfaces.
        
        You can use this method only when :attr:`aspose.words.fields.FieldOptions.is_bidi_text_supported_on_update` is ``False``,
        that is you do not need Right-To-Left language (such as Arabic or Hebrew) compatibility.
        
        :param data_source_root: An object that implements the custom mail merge data source root interface.'''
        ...
    
    @overload
    def get_field_names_for_region(self, region_name: str) -> list[str]:
        '''Returns a collection of mail merge field names available in the region.
        
        Returns full merge field names including optional prefix. Does not eliminate duplicate field names.
        
        If document contains multiple regions with the same name the very first region is processed.
        
        A new string array is created on every call.
        
        :param region_name: Region name (case-insensitive).'''
        ...
    
    @overload
    def get_field_names_for_region(self, region_name: str, region_index: int) -> list[str]:
        '''Returns a collection of mail merge field names available in the region.
        
        Returns full merge field names including optional prefix. Does not eliminate duplicate field names.
        
        If document contains multiple regions with the same name the Nth region (zero-based) is processed.
        
        A new string array is created on every call.
        
        :param region_name: Region name (case-insensitive).
        :param region_index: Region index (zero-based).'''
        ...
    
    def get_field_names(self) -> list[str]:
        '''Returns a collection of mail merge field names available in the document.
        
        Returns full merge field names including optional prefix. Does not eliminate duplicate field names.
        
        A new string array is created on every call.
        
        Includes "mustache" field names if :attr:`MailMerge.use_non_merge_fields` is ``True``.'''
        ...
    
    def get_regions_by_name(self, region_name: str) -> list[aspose.words.mailmerging.MailMergeRegionInfo]:
        '''Returns a collection of mail merge regions with the specified name.
        
        :param region_name: Region name (case-insensitive).
        :returns: The list of regions.'''
        ...
    
    def get_regions_hierarchy(self) -> aspose.words.mailmerging.MailMergeRegionInfo:
        '''Returns a full hierarchy of regions (with fields) available in the document.
        
        Hierarchy is returned in the form of the :class:`MailMergeRegionInfo` class.
        
        :returns: Regions' hierarchy.'''
        ...
    
    def delete_fields(self) -> None:
        '''Removes mail merge related fields from the document.
        
        This method removes MERGEFIELD and NEXT fields from the document.
        
        This method could be useful if your mail merge operation does not always need
        to populate all fields in the document. Use this method to remove all remaining
        mail merge fields.'''
        ...
    
    @property
    def region_start_tag(self) -> str:
        '''Gets or sets a mail merge region start tag.'''
        ...
    
    @region_start_tag.setter
    def region_start_tag(self, value: str):
        ...
    
    @property
    def region_end_tag(self) -> str:
        '''Gets or sets a mail merge region end tag.'''
        ...
    
    @region_end_tag.setter
    def region_end_tag(self, value: str):
        ...
    
    @property
    def cleanup_options(self) -> aspose.words.mailmerging.MailMergeCleanupOptions:
        '''Gets or sets a set of flags that specify what items should be removed during mail merge.'''
        ...
    
    @cleanup_options.setter
    def cleanup_options(self, value: aspose.words.mailmerging.MailMergeCleanupOptions):
        ...
    
    @property
    def cleanup_paragraphs_with_punctuation_marks(self) -> bool:
        '''Gets or sets a value indicating whether paragraphs with punctuation marks are considered as empty
        and should be removed if the :attr:`MailMergeCleanupOptions.REMOVE_EMPTY_PARAGRAPHS` option is specified.
        
        The default value is ``True``.
        
        Here is the complete list of cleanable punctuation marks:
        
        * !
        
        * ,
        
        * .
        
        * :
        
        * ;
        
        * ?
        
        * ¡
        
        * ¿'''
        ...
    
    @cleanup_paragraphs_with_punctuation_marks.setter
    def cleanup_paragraphs_with_punctuation_marks(self, value: bool):
        ...
    
    @property
    def use_non_merge_fields(self) -> bool:
        '''When ``True``, specifies that in addition to MERGEFIELD fields, mail merge is performed into some other types of fields and
        also into "{{fieldName}}" tags.
        
        Normally, mail merge is only performed into MERGEFIELD fields, but several customers had their reporting
        built using other fields and had many documents created this way. To simplify migration (and because this
        approach was independently used by several customers) the ability to mail merge into other fields was introduced.
        
        When :attr:`MailMerge.use_non_merge_fields` is set to ``True``, Aspose.Words will perform mail merge into the following fields:
        
        MERGEFIELD FieldName
        
        MACROBUTTON NOMACRO FieldName
        
        IF 0 = 0 "{FieldName}" ""
        
        Also, when :attr:`MailMerge.use_non_merge_fields` is set to ``True``, Aspose.Words will perform mail merge into text tags
        "{{fieldName}}". These are not fields, but just text tags.'''
        ...
    
    @use_non_merge_fields.setter
    def use_non_merge_fields(self, value: bool):
        ...
    
    @property
    def preserve_unused_tags(self) -> bool:
        '''Gets or sets a value indicating whether the unused "mustache" tags should be preserved.
        
        The default value is ``False``.'''
        ...
    
    @preserve_unused_tags.setter
    def preserve_unused_tags(self, value: bool):
        ...
    
    @property
    def merge_duplicate_regions(self) -> bool:
        '''Gets or sets a value indicating whether all of the document mail merge regions with the name of a data source
        should be merged while executing of a mail merge with regions against the data source or just the first one.
        
        The default value is ``False``.'''
        ...
    
    @merge_duplicate_regions.setter
    def merge_duplicate_regions(self, value: bool):
        ...
    
    @property
    def merge_whole_document(self) -> bool:
        '''Gets or sets a value indicating whether fields in whole document are updated while executing of a mail merge with regions.
        
        The default value is ``False``.'''
        ...
    
    @merge_whole_document.setter
    def merge_whole_document(self, value: bool):
        ...
    
    @property
    def use_whole_paragraph_as_region(self) -> bool:
        '''Gets or sets a value indicating whether whole paragraph with **TableStart** or **TableEnd** field
        or particular range between **TableStart** and **TableEnd** fields should be included into mail merge region.
        
        The default value is ``True``.'''
        ...
    
    @use_whole_paragraph_as_region.setter
    def use_whole_paragraph_as_region(self, value: bool):
        ...
    
    @property
    def restart_lists_at_each_section(self) -> bool:
        '''Gets or sets a value indicating whether lists are restarted at each section after executing of a mail merge.
        
        The default value is ``True``.'''
        ...
    
    @restart_lists_at_each_section.setter
    def restart_lists_at_each_section(self, value: bool):
        ...
    
    @property
    def mapped_data_fields(self) -> aspose.words.mailmerging.MappedDataFieldCollection:
        '''Returns a collection that represents mapped data fields for the mail merge operation.
        
        Mapped data fields allow to automatically map between names of fields in your data source
        and names of mail merge fields in the document.'''
        ...
    
    @property
    def field_merging_callback(self) -> aspose.words.mailmerging.IFieldMergingCallback:
        '''Occurs during mail merge when a mail merge field is encountered in the document.'''
        ...
    
    @field_merging_callback.setter
    def field_merging_callback(self, value: aspose.words.mailmerging.IFieldMergingCallback):
        ...
    
    @property
    def mail_merge_callback(self) -> aspose.words.mailmerging.IMailMergeCallback:
        '''Allows to handle particular events during mail merge.'''
        ...
    
    @mail_merge_callback.setter
    def mail_merge_callback(self, value: aspose.words.mailmerging.IMailMergeCallback):
        ...
    
    @property
    def trim_whitespaces(self) -> bool:
        '''Gets or sets a value indicating whether trailing and leading whitespaces are trimmed from mail merge values.
        
        The default value is ``True``.'''
        ...
    
    @trim_whitespaces.setter
    def trim_whitespaces(self, value: bool):
        ...
    
    @property
    def unconditional_merge_fields_and_regions(self) -> bool:
        '''Gets or sets a value indicating whether merge fields and merge regions are merged regardless of the parent IF field's condition.
        
        The default value is ``False``.'''
        ...
    
    @unconditional_merge_fields_and_regions.setter
    def unconditional_merge_fields_and_regions(self, value: bool):
        ...
    
    @property
    def retain_first_section_start(self) -> bool:
        '''Gets or sets a value indicating whether the :attr:`aspose.words.PageSetup.section_start` of the first document section and its copies for subsequent data source rows
        are retained during mail merge or updated according to MS Word behaviour.
        
        The default value is ``True``.'''
        ...
    
    @retain_first_section_start.setter
    def retain_first_section_start(self, value: bool):
        ...
    
    ...

class MailMergeRegionInfo:
    '''Contains information about a mail merge region.
    To learn more, visit the `Mail Merge and Reporting <https://docs.aspose.com/words/net/mail-merge-and-reporting/>` documentation article.'''
    
    @property
    def parent_region(self) -> aspose.words.mailmerging.MailMergeRegionInfo:
        '''Returns parent region info (null for top-level region).'''
        ...
    
    @property
    def regions(self) -> list[aspose.words.mailmerging.MailMergeRegionInfo]:
        '''Returns a list of child regions.'''
        ...
    
    @property
    def fields(self) -> list[aspose.words.fields.Field]:
        '''Returns a list of child fields.'''
        ...
    
    @property
    def name(self) -> str:
        '''Returns the name of region.'''
        ...
    
    @property
    def start_field(self) -> aspose.words.fields.FieldMergeField:
        '''Returns a start field for the region.'''
        ...
    
    @property
    def end_field(self) -> aspose.words.fields.FieldMergeField:
        '''Returns an end field for the region.'''
        ...
    
    @property
    def level(self) -> int:
        '''Returns the nesting level for the region.'''
        ...
    
    ...

class MappedDataFieldCollection:
    '''Allows to automatically map between names of fields in your data source
    and names of mail merge fields in the document.
    To learn more, visit the `Mail Merge and Reporting <https://docs.aspose.com/words/net/mail-merge-and-reporting/>` documentation article.
    
    This is implemented as a collection of string keys into string values.
    The keys are the names of mail merge fields in the document and the values
    are the names of fields in your data source.'''
    
    def add(self, document_field_name: str, data_source_field_name: str) -> None:
        '''Adds a new field mapping.
        
        :param document_field_name: Case-sensitive name of the mail merge field in the document.
        :param data_source_field_name: Case-sensitive name of the field in the data source.'''
        ...
    
    def contains_key(self, document_field_name: str) -> bool:
        '''Determines whether a mapping from the specified field in the document exists in the collection.
        
        :param document_field_name: Case-sensitive name of the mail merge field in the document.
        :returns: ``True`` if item is found in the collection; otherwise, ``False``.'''
        ...
    
    def contains_value(self, data_source_field_name: str) -> bool:
        '''Determines whether a mapping from the specified field in the data source exists in the collection.
        
        :param data_source_field_name: Case-sensitive name of the field in the data source.
        :returns: ``True`` if item is found in the collection; otherwise, ``False``.'''
        ...
    
    def remove(self, document_field_name: str) -> None:
        '''Removes a field mapping.
        
        :param document_field_name: Case-sensitive name of the mail merge field in the document.'''
        ...
    
    def clear(self) -> None:
        '''Removes all elements from the collection.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of elements contained in the collection.'''
        ...
    
    ...

class MailMergeCleanupOptions:
    '''Specifies options that determine what items are removed during mail merge.'''
    
    NONE: int
    REMOVE_EMPTY_PARAGRAPHS: int
    REMOVE_UNUSED_REGIONS: int
    REMOVE_UNUSED_FIELDS: int
    REMOVE_CONTAINING_FIELDS: int
    REMOVE_STATIC_FIELDS: int
    REMOVE_EMPTY_TABLE_ROWS: int

