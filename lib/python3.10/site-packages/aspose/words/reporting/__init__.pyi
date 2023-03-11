import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class CsvDataLoadOptions:
    '''Represents options for parsing CSV data.
    To learn more, visit the `LINQ Reporting Engine <https://docs.aspose.com/words/net/linq-reporting-engine/>` documentation article.
    
    An instance of this class can be passed into constructors of :class:`CsvDataSource`.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of this class with default options.'''
        ...
    
    @overload
    def __init__(self, has_headers: bool):
        '''Initializes a new instance of this class with specifying whether CSV data contains column names
        at the first line.'''
        ...
    
    @property
    def has_headers(self) -> bool:
        '''Gets or sets a value indicating whether the first record of CSV data contains column names.
        
        The default value is ``False``.'''
        ...
    
    @has_headers.setter
    def has_headers(self, value: bool):
        ...
    
    @property
    def delimiter(self) -> str:
        '''Gets or sets the character to be used as a column delimiter.
        
        The default value is ',' (comma).'''
        ...
    
    @delimiter.setter
    def delimiter(self, value: str):
        ...
    
    @property
    def quote_char(self) -> str:
        '''Gets or sets the character that is used to quote field values.
        
        The default value is '"' (quotation mark).
        
        Double the character to place it into quoted text.'''
        ...
    
    @quote_char.setter
    def quote_char(self, value: str):
        ...
    
    @property
    def comment_char(self) -> str:
        '''Gets or sets the character that is used to comment lines of CSV data.
        
        The default value is '#' (number sign).'''
        ...
    
    @comment_char.setter
    def comment_char(self, value: str):
        ...
    
    ...

class CsvDataSource:
    '''Provides access to data of a CSV file or stream to be used within a report.
    To learn more, visit the `LINQ Reporting Engine <https://docs.aspose.com/words/net/linq-reporting-engine/>` documentation article.
    
    To access data of the corresponding file or stream while generating a report, pass an instance of this class as
    a data source to one of :class:`ReportingEngine`.BuildReport overloads.
    
    In template documents, a :class:`CsvDataSource` instance should be treated in the same way as if it was
    a System.Data.DataTable
    instance. For more information, see template syntax reference
    (https://docs.aspose.com/display/wordsnet/Template+Syntax).
    
    Data types of comma-separated values are determined automatically upon their string representations. So in template
    documents, you can work with typed values rather than just strings. The engine is capable to automatically recognize
    values of the following types:
    
    * System.Nullable`1
    
    * System.Nullable`1
    
    * System.Nullable`1
    
    * System.Nullable`1
    
    * System.String
    
    Note that for automatic recognition of data types to work, string representations of comma-separated values should
    be formed using invariant culture settings.
    
    To override default behavior of CSV data loading, initialize and pass a :class:`CsvDataLoadOptions` instance
    to a constructor of this class.'''
    
    @overload
    def __init__(self, csv_path: str):
        '''Creates a new data source with data from a CSV file using default options for parsing CSV data.
        
        :param csv_path: The path to the CSV file to be used as the data source.'''
        ...
    
    @overload
    def __init__(self, csv_path: str, options: aspose.words.reporting.CsvDataLoadOptions):
        '''Creates a new data source with data from a CSV file using the specified options for parsing CSV data.
        
        :param csv_path: The path to the CSV file to be used as the data source.
        :param options: Options for parsing the CSV data.'''
        ...
    
    @overload
    def __init__(self, csv_stream: io.BytesIO):
        '''Creates a new data source with data from a CSV stream using default options for parsing CSV data.
        
        :param csv_stream: The stream of CSV data to be used as the data source.'''
        ...
    
    @overload
    def __init__(self, csv_stream: io.BytesIO, options: aspose.words.reporting.CsvDataLoadOptions):
        '''Creates a new data source with data from a CSV stream using the specified options for parsing CSV data.
        
        :param csv_stream: The stream of CSV data to be used as the data source.
        :param options: Options for parsing the CSV data.'''
        ...
    
    ...

class JsonDataLoadOptions:
    '''Represents options for parsing JSON data.
    To learn more, visit the `LINQ Reporting Engine <https://docs.aspose.com/words/net/linq-reporting-engine/>` documentation article.
    
    An instance of this class can be passed into constructors of :class:`JsonDataSource`.'''
    
    def __init__(self):
        '''Initializes a new instance of this class with default options.'''
        ...
    
    @property
    def simple_value_parse_mode(self) -> aspose.words.reporting.JsonSimpleValueParseMode:
        '''Gets or sets a mode for parsing JSON simple values (null, boolean, number, integer, and string)
        while loading JSON. Such a mode does not affect parsing of date-time values. The default is
        :attr:`JsonSimpleValueParseMode.LOOSE`.'''
        ...
    
    @simple_value_parse_mode.setter
    def simple_value_parse_mode(self, value: aspose.words.reporting.JsonSimpleValueParseMode):
        ...
    
    @property
    def exact_date_time_parse_format(self) -> str:
        '''Gets or sets an exact format for parsing JSON date-time values while loading JSON. The default is ``None``.
        
        Strings encoded using Microsoft® JSON date-time format (for example, "/Date(1224043200000)/") are always
        recognized as date-time values regardless of a value of this property. The property defines additional
        formats to be used while parsing date-time values from strings in the following way:
        
        * When :attr:`JsonDataLoadOptions.exact_date_time_parse_format` is ``None``, the ISO-8601 format and all date-time formats
          supported for the current, English USA, and English New Zealand cultures are used additionally in
          the mentioned order.
        
        * When :attr:`JsonDataLoadOptions.exact_date_time_parse_format` is a non-empty string, it is used as a single additional
          date-time format utilizing the current culture.
        
        * When :attr:`JsonDataLoadOptions.exact_date_time_parse_format` is an empty string, no additional date-time formats are used.'''
        ...
    
    @exact_date_time_parse_format.setter
    def exact_date_time_parse_format(self, value: str):
        ...
    
    @property
    def exact_date_time_parse_formats(self) -> Iterable[str]:
        '''Gets or sets exact formats for parsing JSON date-time values while loading JSON. The default is ``None``.
        
        Strings encoded using Microsoft® JSON date-time format (for example, "/Date(1224043200000)/") are always
        recognized as date-time values regardless of a value of this property. The property defines additional
        formats to be used while parsing date-time values from strings in the following way:
        
        * When :attr:`JsonDataLoadOptions.exact_date_time_parse_formats` is ``None``, the ISO-8601 format and all date-time formats
          supported for the current, English USA, and English New Zealand cultures are used additionally in
          the mentioned order.
        
        * When :attr:`JsonDataLoadOptions.exact_date_time_parse_formats` contains strings, they are used as additional date-time
          formats utilizing the current culture.
        
        * When :attr:`JsonDataLoadOptions.exact_date_time_parse_formats` is empty, no additional date-time formats are used.'''
        ...
    
    @exact_date_time_parse_formats.setter
    def exact_date_time_parse_formats(self, value: Iterable[str]):
        ...
    
    @property
    def always_generate_root_object(self) -> bool:
        '''Gets or sets a flag indicating whether a generated data source will always contain an object for a JSON root
        element. If a JSON root element contains a single complex property, such an object is not created by default.
        
        The default value is ``False``.'''
        ...
    
    @always_generate_root_object.setter
    def always_generate_root_object(self, value: bool):
        ...
    
    ...

class JsonDataSource:
    '''Provides access to data of a JSON file or stream to be used within a report.
    To learn more, visit the `LINQ Reporting Engine <https://docs.aspose.com/words/net/linq-reporting-engine/>` documentation article.
    
    To access data of the corresponding file or stream while generating a report, pass an instance of this class as
    a data source to one of :class:`ReportingEngine`.BuildReport overloads.
    
    In template documents, if a top-level JSON element is an array, a :class:`JsonDataSource` instance should be
    treated in the same way as if it was a System.Data.DataTable
    instance. If a top-level JSON element
    is an object, a :class:`JsonDataSource` instance should be treated in the same way as if it was
    a System.Data.DataRow
    instance. For more information, see template syntax reference
    (https://docs.aspose.com/display/wordsnet/Template+Syntax).
    
    In template documents, you can work with typed values of JSON elements. For convenience, the engine replaces the set
    of JSON simple types with the following one:
    
    * System.Nullable`1
    
    * System.Nullable`1
    
    * System.Nullable`1
    
    * System.Nullable`1
    
    * System.String
    
    The engine automatically recognizes values of the extra types upon their JSON representations.
    
    To override default behavior of JSON data loading, initialize and pass a :class:`JsonDataLoadOptions` instance
    to a constructor of this class.'''
    
    @overload
    def __init__(self, json_path: str):
        '''Creates a new data source with data from a JSON file using default options for parsing JSON data.
        
        :param json_path: The path to the JSON file to be used as the data source.'''
        ...
    
    @overload
    def __init__(self, json_stream: io.BytesIO):
        '''Creates a new data source with data from a JSON stream using default options for parsing JSON data.
        
        :param json_stream: The stream of JSON data to be used as the data source.'''
        ...
    
    @overload
    def __init__(self, json_path: str, options: aspose.words.reporting.JsonDataLoadOptions):
        '''Creates a new data source with data from a JSON file using the specified options for parsing JSON data.
        
        :param json_path: The path to the JSON file to be used as the data source.
        :param options: Options for parsing JSON data.'''
        ...
    
    @overload
    def __init__(self, json_stream: io.BytesIO, options: aspose.words.reporting.JsonDataLoadOptions):
        '''Creates a new data source with data from a JSON stream using the specified options for parsing JSON data.
        
        :param json_stream: The stream of JSON data to be used as the data source.
        :param options: Options for parsing JSON data.'''
        ...
    
    ...

class KnownTypeSet:
    '''Represents an unordered set (i.e. a collection of unique items) containing System.Type objects
    which fully or partially qualified names can be used within report templates to invoke the corresponding
    types' static members, perform type casts, etc.
    To learn more, visit the `LINQ Reporting Engine <https://docs.aspose.com/words/net/linq-reporting-engine/>` documentation article.'''
    
    def add(self, type) -> None:
        '''Adds the specified System.Type object to the set. Throws System.ArgumentException in
        the following cases:
        
        -  is``None``.
        
        -  represents a void type.
        
        -  represents an invisible type, i.e. a non-public type or a public nested type
        which has a non-public outer type.
        
        -  represents a generic type.
        
        -  represents an array type.
        
        -  has been added to the set already.
        
        :param type: A System.Type object to add.'''
        ...
    
    def remove(self, type) -> None:
        '''Removes the specified System.Type object from the set. Throws System.ArgumentException if
         is``None``.
        
        :param type: A System.Type object to remove.'''
        ...
    
    def clear(self) -> None:
        '''Removes all items from the set.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the count of items in the set.'''
        ...
    
    ...

class ReportingEngine:
    '''Provides routines to populate template documents with data and a set of settings to control these routines.
    To learn more, visit the `LINQ Reporting Engine <https://docs.aspose.com/words/net/linq-reporting-engine/>` documentation article.'''
    
    def __init__(self):
        '''Initializes a new instance of this class.'''
        ...
    
    @overload
    def build_report(self, document: aspose.words.Document, data_source: object) -> bool:
        '''Populates the specified template document with data from the specified source making it a ready report.
        
        Using this overload you can reference the data source's members in the template document, but you cannot
        reference the data source object itself. You should use the :meth:`ReportingEngine.build_report`
        overload to achieve this.
        
        A data source object can be of one of the following types:
        
        * :class:`XmlDataSource`
        
        * :class:`JsonDataSource`
        
        * :class:`CsvDataSource`
        
        * System.Data.DataSet
        
        * System.Data.DataTable
        
        * System.Data.DataRow
        
        * System.Data.IDataReader
        
        * System.Data.IDataRecord
        
        * System.Data.DataView
        
        * System.Data.DataRowView
        
        * Any other arbitrary non-dynamic and non-anonymous .NET type
        
        For information on how to work with data sources of different types in template documents, see template syntax
        reference (https://docs.aspose.com/display/wordsnet/Template+Syntax).
        
        :param document: A template document to be populated with data.
        :param data_source: A data source object.
        :returns: A flag indicating whether parsing of the template document was successful.
                  The returned flag makes sense only if a value of the :attr:`ReportingEngine.options` property includes
                  the :attr:`ReportBuildOptions.INLINE_ERROR_MESSAGES` option.'''
        ...
    
    @overload
    def build_report(self, document: aspose.words.Document, data_source: object, data_source_name: str) -> bool:
        '''Populates the specified template document with data from the specified source making it a ready report.
        
        Using this overload you can reference the data source's members and the data source object itself in the template.
        If you are not going to reference the data source object itself, you can omit
        passing``None`` or use the :meth:`ReportingEngine.build_report` overload.
        
        A data source object can be of one of the following types:
        
        * :class:`XmlDataSource`
        
        * :class:`JsonDataSource`
        
        * :class:`CsvDataSource`
        
        * System.Data.DataSet
        
        * System.Data.DataTable
        
        * System.Data.DataRow
        
        * System.Data.IDataReader
        
        * System.Data.IDataRecord
        
        * System.Data.DataView
        
        * System.Data.DataRowView
        
        * Any other arbitrary non-dynamic and non-anonymous .NET type
        
        For information on how to work with data sources of different types in template documents, see template syntax
        reference (https://docs.aspose.com/display/wordsnet/Template+Syntax).
        
        :param document: A template document to be populated with data.
        :param data_source: A data source object.
        :param data_source_name: A name to reference the data source object in the template.
        :returns: A flag indicating whether parsing of the template document was successful.
                  The returned flag makes sense only if a value of the :attr:`ReportingEngine.options` property includes
                  the :attr:`ReportBuildOptions.INLINE_ERROR_MESSAGES` option.'''
        ...
    
    @overload
    def build_report(self, document: aspose.words.Document, data_sources: list[object], data_source_names: list[str]) -> bool:
        '''Populates the specified template document with data from the specified sources making it a ready report.
        
        Using this overload you can reference multiple data source objects and their members in the template.
        The name of the first data source can be omitted (i.e. be an empty string or ``None``) if you are going to
        reference the data source's members but not the data source object itself. Names of the other data sources
        must be specified and unique.
        
        If you are going to use a single data source, consider using of :meth:`ReportingEngine.build_report`
        and :meth:`ReportingEngine.build_report` overloads instead.
        
        A data source object can be of one of the following types:
        
        * :class:`XmlDataSource`
        
        * :class:`JsonDataSource`
        
        * :class:`CsvDataSource`
        
        * System.Data.DataSet
        
        * System.Data.DataTable
        
        * System.Data.DataRow
        
        * System.Data.IDataReader
        
        * System.Data.IDataRecord
        
        * System.Data.DataView
        
        * System.Data.DataRowView
        
        * Any other arbitrary non-dynamic and non-anonymous .NET type
        
        For information on how to work with data sources of different types in template documents, see template syntax
        reference (https://docs.aspose.com/display/wordsnet/Template+Syntax).
        
        :param document: A template document to be populated with data.
        :param data_sources: An array of data source objects.
        :param data_source_names: An array of names to reference the data source objects within the template.
        :returns: A flag indicating whether parsing of the template document was successful.
                  The returned flag makes sense only if a value of the :attr:`ReportingEngine.options` property includes
                  the :attr:`ReportBuildOptions.INLINE_ERROR_MESSAGES` option.'''
        ...
    
    @property
    def options(self) -> aspose.words.reporting.ReportBuildOptions:
        '''Gets or sets a set of flags controlling behavior of this :class:`ReportingEngine` instance
        while building a report.'''
        ...
    
    @options.setter
    def options(self, value: aspose.words.reporting.ReportBuildOptions):
        ...
    
    @property
    def known_types(self) -> aspose.words.reporting.KnownTypeSet:
        '''Gets an unordered set (i.e. a collection of unique items) containing System.Type objects
        which fully or partially qualified names can be used within report templates processed by this engine
        instance to invoke the corresponding types' static members, perform type casts, etc.'''
        ...
    
    use_reflection_optimization: bool
    
    ...

class XmlDataLoadOptions:
    '''Represents options for XML data loading.
    To learn more, visit the `LINQ Reporting Engine <https://docs.aspose.com/words/net/linq-reporting-engine/>` documentation article.
    
    An instance of this class can be passed into constructors of :class:`XmlDataSource`.'''
    
    def __init__(self):
        '''Initializes a new instance of this class with default options.'''
        ...
    
    @property
    def always_generate_root_object(self) -> bool:
        '''Gets or sets a flag indicating whether a generated data source will always contain an object for an XML root
        element. If an XML root element has no attributes and all its child elements have same names, such an object
        is not created by default.
        
        The default value is ``False``.'''
        ...
    
    @always_generate_root_object.setter
    def always_generate_root_object(self, value: bool):
        ...
    
    ...

class XmlDataSource:
    '''Provides access to data of an XML file or stream to be used within a report.
    To learn more, visit the `LINQ Reporting Engine <https://docs.aspose.com/words/net/linq-reporting-engine/>` documentation article.
    
    To access data of the corresponding file or stream while generating a report, pass an instance of this class as
    a data source to one of :class:`ReportingEngine`.BuildReport overloads.
    
    In template documents, if a top-level XML element contains only a list of elements of the same type,
    an :class:`XmlDataSource` instance should be treated in the same way as if it was
    a System.Data.DataTable
    instance. Otherwise, an :class:`XmlDataSource` instance should be treated in the same way as if it was
    a System.Data.DataRow
    instance. For more information, see template syntax reference
    (https://docs.aspose.com/display/wordsnet/Template+Syntax).
    
    When XML Schema Definition is passed to a constructor of this class, data types of values of simple XML elements
    and attributes are determined according to the schema. So in template documents, you can work with typed values
    rather than just strings.
    
    When XML Schema Definition is not passed to a constructor of this class, data types of values of simple XML elements
    and attributes are determined automatically upon their string representations. So in template documents, you can work
    with typed values in this case as well. The engine is capable to automatically recognize values of the following types:
    
    * System.Nullable`1
    
    * System.Nullable`1
    
    * System.Nullable`1
    
    * System.Nullable`1
    
    * System.String
    
    Note that for automatic recognition of data types to work, string representations of values of simple XML elements
    and attributes should be formed using invariant culture settings.
    
    To override default behavior of XML data loading, initialize and pass a :class:`XmlDataLoadOptions`
    instance to a constructor of this class.'''
    
    @overload
    def __init__(self, xml_path: str):
        '''Creates a new data source with data from an XML file using default options for XML data loading.
        
        :param xml_path: The path to the XML file to be used as the data source.'''
        ...
    
    @overload
    def __init__(self, xml_stream: io.BytesIO):
        '''Creates a new data source with data from an XML stream using default options for XML data loading.
        
        :param xml_stream: The stream of XML data to be used as the data source.'''
        ...
    
    @overload
    def __init__(self, xml_path: str, xml_schema_path: str):
        '''Creates a new data source with data from an XML file using an XML Schema Definition file. Default options
        are used for XML data loading.
        
        :param xml_path: The path to the XML file to be used as the data source.
        :param xml_schema_path: The path to the XML Schema Definition file that provides schema for the XML
                                file.'''
        ...
    
    @overload
    def __init__(self, xml_stream: io.BytesIO, xml_schema_stream: io.BytesIO):
        '''Creates a new data source with data from an XML stream using an XML Schema Definition stream. Default options
        are used for XML data loading.
        
        :param xml_stream: The stream of XML data to be used as the data source.
        :param xml_schema_stream: The stream of XML Schema Definition that provides schema for the XML data.'''
        ...
    
    @overload
    def __init__(self, xml_path: str, options: aspose.words.reporting.XmlDataLoadOptions):
        '''Creates a new data source with data from an XML file using the specified options for XML data loading.
        
        :param xml_path: The path to the XML file to be used as the data source.
        :param options: Options for XML data loading.'''
        ...
    
    @overload
    def __init__(self, xml_stream: io.BytesIO, options: aspose.words.reporting.XmlDataLoadOptions):
        '''Creates a new data source with data from an XML stream using the specified options for XML data loading.
        
        :param xml_stream: The stream of XML data to be used as the data source.
        :param options: Options for XML data loading.'''
        ...
    
    @overload
    def __init__(self, xml_path: str, xml_schema_path: str, options: aspose.words.reporting.XmlDataLoadOptions):
        '''Creates a new data source with data from an XML file using an XML Schema Definition file. The specified
        options are used for XML data loading.
        
        :param xml_path: The path to the XML file to be used as the data source.
        :param xml_schema_path: The path to the XML Schema Definition file that provides schema for the XML
                                file.
        :param options: Options for XML data loading.'''
        ...
    
    @overload
    def __init__(self, xml_stream: io.BytesIO, xml_schema_stream: io.BytesIO, options: aspose.words.reporting.XmlDataLoadOptions):
        '''Creates a new data source with data from an XML stream using an XML Schema Definition stream. The specified
        options are used for XML data loading.
        
        :param xml_stream: The stream of XML data to be used as the data source.
        :param xml_schema_stream: The stream of XML Schema Definition that provides schema for the XML data.
        :param options: Options for XML data loading.'''
        ...
    
    ...

class JsonSimpleValueParseMode:
    '''Specifies a mode for parsing JSON simple values (null, boolean, number, integer, and string) while loading JSON.
    Such a mode does not affect parsing of date-time values.'''
    
    LOOSE: int
    STRICT: int

class ReportBuildOptions:
    '''Specifies options controlling behavior of :class:`ReportingEngine` while building a report.'''
    
    NONE: int
    ALLOW_MISSING_MEMBERS: int
    REMOVE_EMPTY_PARAGRAPHS: int
    INLINE_ERROR_MESSAGES: int
    USE_LEGACY_HEADER_FOOTER_VISITING: int
    RESPECT_JPEG_EXIF_ORIENTATION: int

