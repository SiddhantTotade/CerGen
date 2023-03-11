import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class ChmLoadOptions(aspose.words.loading.LoadOptions):
    '''Allows to specify additional options when loading CHM document into a :class:`aspose.words.Document` object.
    To learn more, visit the `Specify Load Options <https://docs.aspose.com/words/net/specify-load-options/>` documentation article.'''
    
    def __init__(self):
        '''Initializes a new instance of this class with default values.'''
        ...
    
    @property
    def original_file_name(self) -> str:
        '''The name of the CHM file.
        Default value is ``None``.
        
        CHM documents may contain links that reference the same document by file name. Aspose.Words supports such links
        and normally uses :attr:`aspose.words.Document.original_file_name` to check whether the file referenced by a link
        is the file that is being loaded. If a document is loaded from a stream, its original file name should be specified
        explicitly via this property, since it cannot be determined automatically.
        
        If a CHM document is loaded from a file and a non-null value for this property is specified, the value will take
        priority over the actual name of the file stored in :attr:`aspose.words.Document.original_file_name`.'''
        ...
    
    @original_file_name.setter
    def original_file_name(self, value: str):
        ...
    
    ...

class DocumentLoadingArgs:
    '''An argument passed into :meth:`IDocumentLoadingCallback.notify`.
    To learn more, visit the `Specify Load Options <https://docs.aspose.com/words/net/specify-load-options/>` documentation article.'''
    
    @property
    def estimated_progress(self) -> float:
        '''Overall estimated percentage progress.'''
        ...
    
    ...

class HtmlLoadOptions(aspose.words.loading.LoadOptions):
    '''Allows to specify additional options when loading HTML document into a :class:`aspose.words.Document` object.
    To learn more, visit the `Specify Load Options <https://docs.aspose.com/words/net/specify-load-options/>` documentation article.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of this class with default values.'''
        ...
    
    @overload
    def __init__(self, password: str):
        '''A shortcut to initialize a new instance of this class with the specified password to load an encrypted document.
        
        :param password: The password to open an encrypted document. Can be ``None`` or empty string.'''
        ...
    
    @overload
    def __init__(self, load_format: aspose.words.LoadFormat, password: str, base_uri: str):
        '''A shortcut to initialize a new instance of this class with properties set to the specified values.
        
        :param load_format: The format of the document to be loaded.
        :param password: The password to open an encrypted document. Can be ``None`` or empty string.
        :param base_uri: The string that will be used to resolve relative URIs to absolute. Can be ``None`` or empty string.'''
        ...
    
    @property
    def support_vml(self) -> bool:
        '''Gets or sets a value indicating whether to support VML images.'''
        ...
    
    @support_vml.setter
    def support_vml(self, value: bool):
        ...
    
    @property
    def web_request_timeout(self) -> int:
        '''The number of milliseconds to wait before the web request times out. The default value is 100000 milliseconds
        (100 seconds).
        
        The number of milliseconds that Aspose.Words waits for a response, when loading external resources (images, style
        sheets) linked in HTML and MHTML documents.'''
        ...
    
    @web_request_timeout.setter
    def web_request_timeout(self, value: int):
        ...
    
    @property
    def preferred_control_type(self) -> aspose.words.loading.HtmlControlType:
        '''Gets or sets preferred type of document nodes that will represent imported \<input\> and \<select\> elements.
        Default value is Aspose.Words.Loading.HtmlControlType.FormField.
        
        Please note that setting this property does not guarantee that all imported controls will be of the specified type.
        If an HTML control is not representable with document nodes of the preferred type, Aspose.Words will use
        a compatible :class:`HtmlControlType` for that control.'''
        ...
    
    @preferred_control_type.setter
    def preferred_control_type(self, value: aspose.words.loading.HtmlControlType):
        ...
    
    @property
    def ignore_noscript_elements(self) -> bool:
        '''Gets or sets a value indicating whether to ignore \<noscript\> HTML elements.
        Default value is ``False``.
        
        Like MS Word, Aspose.Words does not support scripts and by default loads content of \<noscript\> elements
        into the resulting document. In most browsers, however, scripts are supported and content from \<noscript\>
        is not visible. Setting this property to ``True`` forces Aspose.Words to ignore all \<noscript\> elements
        and helps to produce documents that look closer to what is seen in browsers.'''
        ...
    
    @ignore_noscript_elements.setter
    def ignore_noscript_elements(self, value: bool):
        ...
    
    @property
    def convert_svg_to_emf(self) -> bool:
        '''Gets or sets a value indicating whether to convert loaded SVG images to the EMF format.
        Default value is ``False`` and, if possible, loaded SVG images are stored as is without conversion.
        
        Newer versions of MS Word support SVG images natively. If the MS Word version specified in load options supports
        SVG, Aspose.Words will store SVG images as is without conversion. If SVG is not supported, loaded SVG images will be
        converted to the EMF format.
        
        If, however, this option is set to ``True``, Aspose.Words will convert loaded SVG images to EMF even if SVG
        images are supported by the specified version of MS Word.'''
        ...
    
    @convert_svg_to_emf.setter
    def convert_svg_to_emf(self, value: bool):
        ...
    
    @property
    def block_import_mode(self) -> aspose.words.loading.BlockImportMode:
        '''Gets or sets a value that specifies how properties of block-level elements are imported.
        Default value is :attr:`BlockImportMode.MERGE`.'''
        ...
    
    @block_import_mode.setter
    def block_import_mode(self, value: aspose.words.loading.BlockImportMode):
        ...
    
    ...

class IDocumentLoadingCallback:
    '''Implement this interface if you want to have your own custom method called during loading a document.'''
    
    def notify(self, args: aspose.words.loading.DocumentLoadingArgs) -> None:
        '''This is called to notify of document loading progress.
        
        :param args: An argument of the event.
        
        The primary uses for this interface is to allow application code to obtain progress status and abort loading process.
        
        An exception should be threw from the progress callback for abortion and it should be caught in the consumer code.'''
        ...
    
    ...

class IResourceLoadingCallback:
    '''Implement this interface if you want to control how Aspose.Words loads external resource when
    importing a document and inserting images using :class:`aspose.words.DocumentBuilder`.'''
    
    def resource_loading(self, args: aspose.words.loading.ResourceLoadingArgs) -> aspose.words.loading.ResourceLoadingAction:
        '''Called when Aspose.Words loads any external resource.'''
        ...
    
    ...

class LanguagePreferences:
    '''Allows to set up language preferences.
    To learn more, visit the `Specify Load Options <https://docs.aspose.com/words/net/specify-load-options/>` documentation article.
    
    Implements 'Set the Office Language Preferences' dialog in Word.'''
    
    def __init__(self):
        ...
    
    def add_editing_language(self, language: aspose.words.loading.EditingLanguage) -> None:
        '''Adds additional editing language.'''
        ...
    
    def add_editing_languages(self, languages: list[aspose.words.loading.EditingLanguage]) -> None:
        '''Adds additional editing languages.'''
        ...
    
    @property
    def default_editing_language(self) -> aspose.words.loading.EditingLanguage:
        '''Gets or sets default editing language.
        
        The default value is Aspose.Words.Loading.EditingLanguage.EnglishUS.'''
        ...
    
    @default_editing_language.setter
    def default_editing_language(self, value: aspose.words.loading.EditingLanguage):
        ...
    
    ...

class LoadOptions:
    '''Allows to specify additional options (such as password or base URI) when
    loading a document into a :class:`aspose.words.Document` object.
    To learn more, visit the `Specify Load Options <https://docs.aspose.com/words/net/specify-load-options/>` documentation article.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of this class with default values.'''
        ...
    
    @overload
    def __init__(self, password: str):
        '''A shortcut to initialize a new instance of this class with the specified password to load an encrypted document.
        
        :param password: The password to open an encrypted document. Can be ``None`` or empty string.'''
        ...
    
    @overload
    def __init__(self, load_format: aspose.words.LoadFormat, password: str, base_uri: str):
        '''A shortcut to initialize a new instance of this class with properties set to the specified values.
        
        :param load_format: The format of the document to be loaded.
        :param password: The password to open an encrypted document. Can be ``None`` or empty string.
        :param base_uri: The string that will be used to resolve relative URIs to absolute. Can be ``None`` or empty string.'''
        ...
    
    @property
    def load_format(self) -> aspose.words.LoadFormat:
        '''Specifies the format of the document to be loaded.
        Default is :attr:`aspose.words.LoadFormat.AUTO`.
        
        It is recommended that you specify the :attr:`aspose.words.LoadFormat.AUTO` value and let Aspose.Words detect
        the file format automatically. If you know the format of the document you are about to load, you can specify the format
        explicitly and this will slightly reduce the loading time by the overhead associated with auto detecting the format.
        If you specify an explicit load format and it will turn out to be wrong, the auto detection will be invoked and a second
        attempt to load the file will be made.'''
        ...
    
    @load_format.setter
    def load_format(self, value: aspose.words.LoadFormat):
        ...
    
    @property
    def password(self) -> str:
        '''Gets or sets the password for opening an encrypted document.
        Can be ``None`` or empty string. Default is ``None``.
        
        You need to know the password to open an encrypted document. If the document is not encrypted, set this to ``None`` or empty string.'''
        ...
    
    @password.setter
    def password(self, value: str):
        ...
    
    @property
    def base_uri(self) -> str:
        '''Gets or sets the string that will be used to resolve relative URIs found in the document into absolute URIs when required.
        Can be ``None`` or empty string. Default is ``None``.
        
        This property is used to resolve relative URIs into absolute in the following cases:
        
        1. When loading an HTML document from a stream and the document contains images with
           relative URIs and does not have a base URI specified in the BASE HTML element.
        
        1. When saving a document to PDF and other formats, to retrieve images linked using relative URIs
           so the images can be saved into the output document.'''
        ...
    
    @base_uri.setter
    def base_uri(self, value: str):
        ...
    
    @property
    def encoding(self) -> str:
        '''Gets or sets the encoding that will be used to load an HTML, TXT, or CHM document if the encoding is not specified
        inside the document.
        Can be ``None``. Default is ``None``.
        
        This property is used only when loading HTML, TXT, or CHM documents.
        
        If encoding is not specified inside the document and this property is ``None``, then the system will try to
        automatically detect the encoding.'''
        ...
    
    @encoding.setter
    def encoding(self, value: str):
        ...
    
    @property
    def resource_loading_callback(self) -> aspose.words.loading.IResourceLoadingCallback:
        '''Allows to control how external resources (images, style sheets) are loaded when a document is imported from HTML, MHTML.'''
        ...
    
    @resource_loading_callback.setter
    def resource_loading_callback(self, value: aspose.words.loading.IResourceLoadingCallback):
        ...
    
    @property
    def warning_callback(self) -> aspose.words.IWarningCallback:
        '''Called during a load operation, when an issue is detected that might result in data or formatting fidelity loss.'''
        ...
    
    @warning_callback.setter
    def warning_callback(self, value: aspose.words.IWarningCallback):
        ...
    
    @property
    def progress_callback(self) -> aspose.words.loading.IDocumentLoadingCallback:
        '''Called during loading a document and accepts data about loading progress.
        
        :attr:`aspose.words.LoadFormat.DOCX`, :attr:`aspose.words.LoadFormat.FLAT_OPC`, :attr:`aspose.words.LoadFormat.DOCM`, :attr:`aspose.words.LoadFormat.DOTM`, :attr:`aspose.words.LoadFormat.DOTX`, :attr:`aspose.words.LoadFormat.MARKDOWN`, :attr:`aspose.words.LoadFormat.RTF`, :attr:`aspose.words.LoadFormat.WORD_ML`, :attr:`aspose.words.LoadFormat.DOC`, :attr:`aspose.words.LoadFormat.DOT`, :attr:`aspose.words.LoadFormat.ODT`, :attr:`aspose.words.LoadFormat.OTT` formats supported.'''
        ...
    
    @progress_callback.setter
    def progress_callback(self, value: aspose.words.loading.IDocumentLoadingCallback):
        ...
    
    @property
    def preserve_include_picture_field(self) -> bool:
        '''Gets or sets whether to preserve the INCLUDEPICTURE field when reading Microsoft Word formats.
        The default value is ``False``.
        
        By default, the INCLUDEPICTURE field is converted into a shape object. You can override that if you need
        the field to be preserved, for example, if you wish to update it programmatically. Note however that this
        approach is not common for Aspose.Words. Use it on your own risk.
        
        One of the possible use cases may be using a MERGEFIELD as a child field to dynamically change the source path
        of the picture. In this case you need the INCLUDEPICTURE to be preserved in the model.'''
        ...
    
    @preserve_include_picture_field.setter
    def preserve_include_picture_field(self, value: bool):
        ...
    
    @property
    def convert_shape_to_office_math(self) -> bool:
        '''Gets or sets whether to convert shapes with EquationXML to Office Math objects.'''
        ...
    
    @convert_shape_to_office_math.setter
    def convert_shape_to_office_math(self, value: bool):
        ...
    
    @property
    def font_settings(self) -> aspose.words.fonts.FontSettings:
        '''Allows to specify document font settings.
        
        When loading some formats, Aspose.Words may require to resolve the fonts. For example, when loading HTML documents Aspose.Words
        may resolve the fonts to perform font fallback.
        
        If set to ``None``, default static font settings :attr:`aspose.words.fonts.FontSettings.default_instance` will be used.
        
        The default value is ``None``.'''
        ...
    
    @font_settings.setter
    def font_settings(self, value: aspose.words.fonts.FontSettings):
        ...
    
    @property
    def temp_folder(self) -> str:
        '''Allows to use temporary files when reading document.
        By default this property is ``None`` and no temporary files are used.
        
        The folder must exist and be writable, otherwise an exception will be thrown.
        
        Aspose.Words automatically deletes all temporary files when reading is complete.'''
        ...
    
    @temp_folder.setter
    def temp_folder(self, value: str):
        ...
    
    @property
    def convert_metafiles_to_png(self) -> bool:
        '''Gets or sets whether to convert metafile (Aspose.FileFormat.Wmf or Aspose.FileFormat.Emf) images to Aspose.FileFormat.Png image format.
        
        Metafiles (Aspose.FileFormat.Wmf or Aspose.FileFormat.Emf) is an uncompressed image format and sometimes requires to much RAM to hold and process document.
        This option allows to convert all metafile images to Aspose.FileFormat.Png on document loading.
        Please note - conversion vector graphics to raster decreases quality of the images.'''
        ...
    
    @convert_metafiles_to_png.setter
    def convert_metafiles_to_png(self, value: bool):
        ...
    
    @property
    def msw_version(self) -> aspose.words.settings.MsWordVersion:
        '''Allows to specify that the document loading process should match a specific MS Word version.
        Default value is :attr:`aspose.words.settings.MsWordVersion.WORD2019`
        
        Different Word versions may handle certain aspects of document content and formatting slightly differently
        during the loading process, which may result in minor differences in Document Object Model.'''
        ...
    
    @msw_version.setter
    def msw_version(self, value: aspose.words.settings.MsWordVersion):
        ...
    
    @property
    def update_dirty_fields(self) -> bool:
        '''Specifies whether to update the fields with the ``dirty`` attribute.'''
        ...
    
    @update_dirty_fields.setter
    def update_dirty_fields(self, value: bool):
        ...
    
    @property
    def ignore_ole_data(self) -> bool:
        '''Specifies whether to ignore the OLE data.
        
        Ignoring OLE data may reduce memory consumption and increase performance without data lost in a case when destination format does not support OLE objects.
        
        The default value is ``False``.'''
        ...
    
    @ignore_ole_data.setter
    def ignore_ole_data(self, value: bool):
        ...
    
    @property
    def language_preferences(self) -> aspose.words.loading.LanguagePreferences:
        '''Gets language preferences that will be used when document is loading.'''
        ...
    
    ...

class PdfLoadOptions(aspose.words.loading.LoadOptions):
    '''Allows to specify additional options when loading Pdf document into a :class:`aspose.words.Document` object.
    To learn more, visit the `Specify Load Options <https://docs.aspose.com/words/net/specify-load-options/>` documentation article.'''
    
    def __init__(self):
        ...
    
    @property
    def page_index(self) -> int:
        '''Gets or sets the 0-based index of the first page to read. Default is 0.'''
        ...
    
    @page_index.setter
    def page_index(self, value: int):
        ...
    
    @property
    def page_count(self) -> int:
        '''Gets or sets the number of pages to read. Default is MaxValue which means all pages of the document will be read.'''
        ...
    
    @page_count.setter
    def page_count(self, value: int):
        ...
    
    @property
    def skip_pdf_images(self) -> bool:
        '''Gets or sets the flag indicating whether images must be skipped while loading PDF document. Default is ``False``.'''
        ...
    
    @skip_pdf_images.setter
    def skip_pdf_images(self, value: bool):
        ...
    
    ...

class ResourceLoadingArgs:
    '''Provides data for the :meth:`IResourceLoadingCallback.resource_loading` method.'''
    
    def set_data(self, data: bytes) -> None:
        '''Sets user provided data of the resource which is used
        if :meth:`IResourceLoadingCallback.resource_loading`
        returns :attr:`ResourceLoadingAction.USER_PROVIDED`.'''
        ...
    
    @property
    def resource_type(self) -> aspose.words.loading.ResourceType:
        '''Type of resource.'''
        ...
    
    @property
    def uri(self) -> str:
        '''URI of the resource which is used for downloading
        if :meth:`IResourceLoadingCallback.resource_loading`
        returns :attr:`ResourceLoadingAction.DEFAULT`.
        
        Initially it's set to absolute URI of the resource,
        but user can redefine it to any value.'''
        ...
    
    @uri.setter
    def uri(self, value: str):
        ...
    
    @property
    def original_uri(self) -> str:
        '''Original URI of the resource as specified in imported document.'''
        ...
    
    ...

class RtfLoadOptions(aspose.words.loading.LoadOptions):
    '''Allows to specify additional options when loading :attr:`aspose.words.LoadFormat.RTF` document into a :class:`aspose.words.Document` object.
    To learn more, visit the `Specify Load Options <https://docs.aspose.com/words/net/specify-load-options/>` documentation article.'''
    
    def __init__(self):
        '''Initializes a new instance of this class with default values.'''
        ...
    
    @property
    def recognize_utf8_text(self) -> bool:
        '''When set to ``True``, Aspose.Charset.CharsetDetector will try to detect UTF8 characters,
        they will be preserved during import.
        
        Default value is``False``.'''
        ...
    
    @recognize_utf8_text.setter
    def recognize_utf8_text(self, value: bool):
        ...
    
    ...

class TxtLoadOptions(aspose.words.loading.LoadOptions):
    '''Allows to specify additional options when loading :attr:`aspose.words.LoadFormat.TEXT` document into a :class:`aspose.words.Document` object.
    To learn more, visit the `Specify Load Options <https://docs.aspose.com/words/net/specify-load-options/>` documentation article.'''
    
    def __init__(self):
        '''Initializes a new instance of this class with default values.'''
        ...
    
    @property
    def auto_numbering_detection(self) -> bool:
        '''Gets or sets a boolean value indicating either automatic numbering detection
        will be performed while loading a document.
        The default value is ``True``.'''
        ...
    
    @auto_numbering_detection.setter
    def auto_numbering_detection(self, value: bool):
        ...
    
    @property
    def detect_numbering_with_whitespaces(self) -> bool:
        '''Allows to specify how numbered list items are recognized when document is imported from plain text format.
        The default value is ``True``.
        
        If this option is set to ``False``, lists recognition algorithm detects list paragraphs, when list numbers ends with
        either dot, right bracket or bullet symbols (such as "•", "\*", "-" or "o").
        
        If this option is set to ``True``, whitespaces are also used as list number delimiters:
        list recognition algorithm for Arabic style numbering (1., 1.1.2.) uses both whitespaces and dot (".") symbols.'''
        ...
    
    @detect_numbering_with_whitespaces.setter
    def detect_numbering_with_whitespaces(self, value: bool):
        ...
    
    @property
    def trailing_spaces_options(self) -> aspose.words.loading.TxtTrailingSpacesOptions:
        '''Gets or sets preferred option of a trailing space handling.
        Default value is Aspose.Words.Loading.TxtTrailingSpacesOptions.Trim.'''
        ...
    
    @trailing_spaces_options.setter
    def trailing_spaces_options(self, value: aspose.words.loading.TxtTrailingSpacesOptions):
        ...
    
    @property
    def leading_spaces_options(self) -> aspose.words.loading.TxtLeadingSpacesOptions:
        '''Gets or sets preferred option of a leading space handling.
        Default value is Aspose.Words.Loading.TxtLeadingSpacesOptions.ConvertToIndent.'''
        ...
    
    @leading_spaces_options.setter
    def leading_spaces_options(self, value: aspose.words.loading.TxtLeadingSpacesOptions):
        ...
    
    @property
    def document_direction(self) -> aspose.words.loading.DocumentDirection:
        '''Gets or sets a document direction.
        The default value is :attr:`DocumentDirection.LEFT_TO_RIGHT`.'''
        ...
    
    @document_direction.setter
    def document_direction(self, value: aspose.words.loading.DocumentDirection):
        ...
    
    ...

class BlockImportMode:
    '''Specifies how properties of block-level elements are imported from HTML-based documents.'''
    
    MERGE: int
    PRESERVE: int

class DocumentDirection:
    '''Allows to specify the direction to flow the text in a document.'''
    
    LEFT_TO_RIGHT: int
    RIGHT_TO_LEFT: int
    AUTO: int

class EditingLanguage:
    '''Specifies the editing language.'''
    
    AFRIKAANS: int
    ALBANIAN: int
    ALSATIAN: int
    AMHARIC: int
    ARABIC_ALGERIA: int
    ARABIC_BAHRAIN: int
    ARABIC_EGYPT: int
    ARABIC_IRAQ: int
    ARABIC_JORDAN: int
    ARABIC_KUWAIT: int
    ARABIC_LEBANON: int
    ARABIC_LIBYA: int
    ARABIC_MOROCCO: int
    ARABIC_OMAN: int
    ARABIC_QATAR: int
    ARABIC_SAUDI_ARABIA: int
    ARABIC_SYRIA: int
    ARABIC_TUNISIA: int
    ARABIC_UAE: int
    ARABIC_YEMEN: int
    ARMENIAN: int
    ASSAMESE: int
    AZERBAIJANI_CYRILLIC: int
    AZERBAIJANI_LATIN: int
    BANGLA_BANGLADESH: int
    BANGLA_INDIA: int
    BASHKIR: int
    BASQUE: int
    BELARUSIAN: int
    BOSNIAN_CYRILLIC: int
    BOSNIAN_LATIN: int
    BRETON: int
    BULGARIAN: int
    BURMESE: int
    CATALAN: int
    CENTRAL_KURDISH_IRAQ: int
    CHEROKEE: int
    CHINESE_HONG_KONG: int
    CHINESE_MACAO: int
    CHINESE_PRC: int
    CHINESE_SINGAPORE: int
    CHINESE_TAIWAN: int
    CORSICAN: int
    CROATIAN_BOZNIA_AND_HERZEGOVINA: int
    CROATIAN: int
    CZECH: int
    DANISH: int
    DIVEHI: int
    DUTCH_BELGIUM: int
    DUTCH_NETHERLANDS: int
    EDO: int
    ENGLISH_AUSTRALIA: int
    ENGLISH_BELIZE: int
    ENGLISH_CANADA: int
    ENGLISH_CARIBBEAN: int
    ENGLISH_HONG_KONG: int
    ENGLISH_INDIA: int
    ENGLISH_INDONESIA: int
    ENGLISH_IRELAND: int
    ENGLISH_JAMAICA: int
    ENGLISH_MALAYSIA: int
    ENGLISH_NEW_ZEALAND: int
    ENGLISH_PHILIPPINES: int
    ENGLISH_SINGAPORE: int
    ENGLISH_SOUTH_AFRICA: int
    ENGLISH_TRINIDAD_AND_TOBAGO: int
    ENGLISH_UK: int
    ENGLISH_US: int
    ENGLISH_ZIMBABWE: int
    ESTONIAN: int
    FAEROESE: int
    FILIPINO: int
    FINNISH: int
    FRENCH_BELGIUM: int
    FRENCH_CANADA: int
    FRENCH_FRANCE: int
    FRENCH_LUXEMBOURG: int
    FRENCH_MONACO: int
    FRENCH_SWITZERLAND: int
    FRISIAN: int
    FULAH_LATIN_SENEGAL: int
    FULAH_NIGERIA: int
    GALICIAN: int
    GEORGIAN: int
    GERMAN_AUSTRIA: int
    GERMAN_GERMANY: int
    GERMAN_LIECHTENSTEIN: int
    GERMAN_LUXEMBOURG: int
    GERMAN_SWITZERLAND: int
    GREEK: int
    GREENLANDIC: int
    GUARANI: int
    GUJARATI: int
    HAUSA: int
    HAWAIIAN: int
    HEBREW: int
    HINDI: int
    HUNGARIAN: int
    ICELANDIC: int
    IGBO: int
    INARI_SAMI_FINLAND: int
    INDONESIAN: int
    INUKTITUT_LATIN: int
    INUKTITUT_SYLLABICS: int
    IRISH: int
    ISI_XHOSA: int
    ISI_ZULU: int
    ITALIAN_ITALY: int
    ITALIAN_SWITZERLAND: int
    JAPANESE: int
    KANNADA: int
    KANURI: int
    KASHMIRI: int
    KASHMIRI_ARABIC: int
    KAZAKH: int
    KHMER: int
    KICHE: int
    KINYARWANDA: int
    KISWAHILI: int
    KONKANI: int
    KOREAN: int
    KYRGYZ: int
    LAO: int
    LATIN: int
    LATVIAN: int
    LITHUANIAN: int
    LOWER_SORBIAN: int
    LULE_SAMI_NORWAY: int
    LULE_SAMI_SWEDEN: int
    LUXEMBOUGISH: int
    MACEDONIAN: int
    MALAY_MALAYSIA: int
    MALAY_BRUNEI_DARUSSALAM: int
    MALAYALAM: int
    MALTESE: int
    MANIPURI: int
    MAORI: int
    MAPUDUNGUN_CHILE: int
    MARATHI: int
    MOHAWK: int
    MONGOLIAN_CYRILLIC: int
    MONGOLIAN_MONGOLIAN: int
    NEPALI: int
    NORTHERN_SAMI_FINLAND: int
    NORTHERN_SAMI_NORWAY: int
    NORTHERN_SAMI_SWEDEN: int
    NORWEGIAN_BOKMAL: int
    NORWEGIAN_NYNORSK: int
    ORIYA: int
    OROMO: int
    PAPIAMENTU: int
    PASHTO: int
    PERSIAN: int
    POLISH: int
    PORTUGUESE_BRAZIL: int
    PORTUGUESE_PORTUGAL: int
    PUNJABI_INDIA: int
    PUNJABI_PAKISTAN: int
    QUECHUA_BOLIVIA: int
    QUECHUA_ECUADOR: int
    QUECHUA_PERU: int
    ROMANIAN: int
    ROMANSH: int
    RUSSIAN: int
    SAKHA: int
    SANSKRIT: int
    SCOTTISH_GAELIC: int
    SERBIAN_CYRILLIC_BOSNIA_AND_HERZEGOVINA: int
    SERBIAN_CYRILLIC_SERBIA_AND_MONTENEGRO: int
    SERBIAN_LATIN_BOSNIA_AND_HERZEGOVINA: int
    SERBIAN_LATIN_SERBIA_AND_MONTENEGRO: int
    SINDHI: int
    SINDHI_DEVANAGARIC: int
    SINHALESE: int
    SLOVAK: int
    SLOVENIAN: int
    SOMALI: int
    SORBIAN: int
    SPANISH_ARGENTINA: int
    SPANISH_BOLIVIA: int
    SPANISH_CHILE: int
    SPANISH_COLOMBIA: int
    SPANISH_COSTA_RICA: int
    SPANISH_DOMINICAN_REPUBLIC: int
    SPANISH_ECUADOR: int
    SPANISH_EL_SALVADOR: int
    SPANISH_GUATEMALA: int
    SPANISH_HONDURAS: int
    SPANISH_MEXICO: int
    SPANISH_NICARAGUA: int
    SPANISH_PANAMA: int
    SPANISH_PARAGUAY: int
    SPANISH_PERU: int
    SPANISH_PUERTO_RICO: int
    SPANISH_SPAIN_MODERN_SORT: int
    SPANISH_SPAIN_TRADITIONAL_SORT: int
    SPANISH_URUGUAY: int
    SPANISH_VENEZUELA: int
    SUTU: int
    SWEDISH_FINLAND: int
    SWEDISH_SWEDEN: int
    SYRIAC: int
    TAJIK: int
    TAMAZIGHT: int
    TAMAZIGHT_LATIN: int
    TAMIL: int
    TATAR: int
    TELUGU: int
    THAI: int
    TIBETAN_BUTAN: int
    TIBETAN_CHINA: int
    TIGRIGNA_ERITREA: int
    TIGRIGNA_ETHIOPIA: int
    TSONGA: int
    TSWANA: int
    TURKISH: int
    TURKMEN: int
    UKRAINIAN: int
    URDU: int
    UZBEK_CYRILLIC: int
    UZBEK_LATIN: int
    VENDA: int
    VIETNAMESE: int
    WELSH: int
    YI: int
    YIDDISH: int
    YORUBA: int

class HtmlControlType:
    '''Type of document nodes that represent \<input\> and \<select\> elements imported from HTML.'''
    
    FORM_FIELD: int
    STRUCTURED_DOCUMENT_TAG: int

class ResourceLoadingAction:
    '''Specifies the mode of resource loading.
    To learn more, visit the `Specify Load Options <https://docs.aspose.com/words/net/specify-load-options/>` documentation article.'''
    
    DEFAULT: int
    SKIP: int
    USER_PROVIDED: int

class ResourceType:
    '''Type of loaded resource.'''
    
    IMAGE: int
    CSS_STYLE_SHEET: int
    DOCUMENT: int

class TxtLeadingSpacesOptions:
    '''Specifies available options for leading space handling during import from :attr:`aspose.words.LoadFormat.TEXT` file.'''
    
    CONVERT_TO_INDENT: int
    TRIM: int
    PRESERVE: int

class TxtTrailingSpacesOptions:
    '''Specifies available options for trailing spaces handling during import from :attr:`aspose.words.LoadFormat.TEXT` file.'''
    
    TRIM: int
    PRESERVE: int

