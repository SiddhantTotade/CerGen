import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class DefaultFontSubstitutionRule(aspose.words.fonts.FontSubstitutionRule):
    '''Default font substitution rule.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.
    
    This rule defines single default font name to be used for substitution if the original font is not available.'''
    
    @property
    def default_font_name(self) -> str:
        '''Gets or sets the default font name.
        
        The default value is 'Times New Roman'.'''
        ...
    
    @default_font_name.setter
    def default_font_name(self, value: str):
        ...
    
    ...

class FileFontSource(aspose.words.fonts.FontSourceBase):
    '''Represents the single TrueType font file stored in the file system.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.'''
    
    @overload
    def __init__(self, file_path: str):
        '''Ctor.
        
        :param file_path: Path to font file.'''
        ...
    
    @overload
    def __init__(self, file_path: str, priority: int):
        '''Ctor.
        
        :param file_path: Path to font file.
        :param priority: Font source priority. See the :attr:`FontSourceBase.priority` property description for more information.'''
        ...
    
    @overload
    def __init__(self, file_path: str, priority: int, cache_key: str):
        '''Ctor.
        
        :param file_path: Path to font file.
        :param priority: Font source priority. See the :attr:`FontSourceBase.priority` property description for more information.
        :param cache_key: The key of this source in the cache. See :attr:`FileFontSource.cache_key` property description for more information.'''
        ...
    
    @property
    def type(self) -> aspose.words.fonts.FontSourceType:
        '''Returns the type of the font source.'''
        ...
    
    @property
    def file_path(self) -> str:
        '''Path to the font file.'''
        ...
    
    @property
    def cache_key(self) -> str:
        '''The key of this source in the cache.
        
        This key is used to identify cache item when saving/loading font search cache with
        :meth:`FontSettings.save_search_cache` and
        :meth:`FontSettings.set_fonts_sources` methods.
        
        If key is not specified then :attr:`FileFontSource.file_path` will be used as a key instead.'''
        ...
    
    ...

class FolderFontSource(aspose.words.fonts.FontSourceBase):
    '''Represents the folder that contains TrueType font files.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.'''
    
    @overload
    def __init__(self, folder_path: str, scan_subfolders: bool):
        '''Ctor.
        
        :param folder_path: Path to folder.
        :param scan_subfolders: Determines whether or not to scan subfolders.'''
        ...
    
    @overload
    def __init__(self, folder_path: str, scan_subfolders: bool, priority: int):
        '''Ctor.
        
        :param folder_path: Path to folder.
        :param scan_subfolders: Determines whether or not to scan subfolders.
        :param priority: Font source priority. See the :attr:`FontSourceBase.priority` property description for more information.'''
        ...
    
    @property
    def type(self) -> aspose.words.fonts.FontSourceType:
        '''Returns the type of the font source.'''
        ...
    
    @property
    def folder_path(self) -> str:
        '''Path to the folder.'''
        ...
    
    @property
    def scan_subfolders(self) -> bool:
        '''Determines whether or not to scan the subfolders.'''
        ...
    
    ...

class FontConfigSubstitutionRule(aspose.words.fonts.FontSubstitutionRule):
    '''Font config substitution rule.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.
    
    This rule uses fontconfig utility on Linux (and other Unix-like) platforms to get the substitution
    if the original font is not available.
    
    If fontconfig utility is not available then this rule will be ignored.'''
    
    def is_font_config_available(self) -> bool:
        '''Check if fontconfig utility is available or not.'''
        ...
    
    def reset_cache(self) -> None:
        '''Resets the cache of fontconfig calling results.'''
        ...
    
    @property
    def enabled(self) -> bool:
        '''Specifies whether the rule is enabled or not.'''
        ...
    
    @enabled.setter
    def enabled(self, value: bool):
        ...
    
    ...

class FontFallbackSettings:
    '''Specifies font fallback mechanism settings.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.
    
    By default fallback settings are initialized with predefined settings which mimics the Microsoft Word fallback.'''
    
    @overload
    def load(self, file_name: str) -> None:
        '''Loads font fallback settings from XML file.
        
        :param file_name: Input file name.'''
        ...
    
    @overload
    def load(self, stream: io.BytesIO) -> None:
        '''Loads fallback settings from XML stream.
        
        :param stream: Input stream.'''
        ...
    
    @overload
    def save(self, output_stream: io.BytesIO) -> None:
        '''Saves the current fallback settings to stream.
        
        :param output_stream: Output stream.'''
        ...
    
    @overload
    def save(self, file_name: str) -> None:
        '''Saves the current fallback settings to file.
        
        :param file_name: Output file name.'''
        ...
    
    def load_ms_office_fallback_settings(self) -> None:
        '''Loads predefined fallback settings which mimics the Microsoft Word fallback and uses Microsoft office fonts.'''
        ...
    
    def load_noto_fallback_settings(self) -> None:
        '''Loads predefined fallback settings which uses Google Noto fonts.'''
        ...
    
    def build_automatic(self) -> None:
        '''Automatically builds the fallback settings by scanning available fonts.
        
        This method may produce non-optimal fallback settings. Fonts are checked by `
                    Unicode Character Range <https://docs.microsoft.com/en-us/typography/opentype/spec/os2#ur>` fields and not by the actual glyphs presence. Also Unicode ranges are checked individually
        and several ranges related to single language/script may use different fallback fonts.'''
        ...
    
    ...

class FontInfo:
    '''Specifies information about a font used in the document.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.
    
    You do not create instances of this class directly.
    Use the :attr:`aspose.words.DocumentBase.font_infos` property to access the collection of fonts
    defined in a document.'''
    
    def get_embedded_font(self, format: aspose.words.fonts.EmbeddedFontFormat, style: aspose.words.fonts.EmbeddedFontStyle) -> bytes:
        '''Gets a specific embedded font file.
        
        :param format: Specifies the font format to retrieve.
        :param style: Specifies the font style to retrieve.
        :returns: Returns ``None`` if the specified font is not embedded.'''
        ...
    
    def get_embedded_font_as_open_type(self, style: aspose.words.fonts.EmbeddedFontStyle) -> bytes:
        '''Gets an embedded font file in OpenType format. Fonts in Embedded OpenType format are converted to OpenType.
        
        :param style: Specifies the font style to retrieve.
        :returns: Returns ``None`` if the specified font is not embedded.'''
        ...
    
    @property
    def pitch(self) -> aspose.words.fonts.FontPitch:
        '''The pitch indicates if the font is fixed pitch, proportionally spaced, or relies on a default setting.'''
        ...
    
    @pitch.setter
    def pitch(self, value: aspose.words.fonts.FontPitch):
        ...
    
    @property
    def is_true_type(self) -> bool:
        '''Indicates that this font is a TrueType or OpenType font as opposed to a raster or vector font.
        Default is ``True``.'''
        ...
    
    @is_true_type.setter
    def is_true_type(self, value: bool):
        ...
    
    @property
    def family(self) -> aspose.words.fonts.FontFamily:
        '''Gets or sets the font family this font belongs to.'''
        ...
    
    @family.setter
    def family(self, value: aspose.words.fonts.FontFamily):
        ...
    
    @property
    def charset(self) -> int:
        '''Gets or sets the character set for the font.'''
        ...
    
    @charset.setter
    def charset(self, value: int):
        ...
    
    @property
    def panose(self) -> bytes:
        '''Gets or sets the PANOSE typeface classification number.
        
        PANOSE is a compact 10-byte description of a fonts critical visual characteristics,
        such as contrast, weight, and serif style. The digits represent Family Kind, Serif Style,
        Weight, Proportion, Contrast, Stroke Variation, Arm Style, Letterform, Midline, and X-Height.
        
        Can be ``None``.'''
        ...
    
    @panose.setter
    def panose(self, value: bytes):
        ...
    
    @property
    def name(self) -> str:
        '''Gets the name of the font.
        
        Cannot be ``None``. Can be an empty string.'''
        ...
    
    @property
    def alt_name(self) -> str:
        '''Gets or sets the alternate name for the font.
        
        Cannot be ``None``. Can be an empty string.'''
        ...
    
    @alt_name.setter
    def alt_name(self, value: str):
        ...
    
    ...

class FontInfoCollection:
    '''Represents a collection of fonts used in a document.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.
    
    Items are :class:`FontInfo` objects.
    
    You do not create instances of this class directly.
    Use the :attr:`aspose.words.DocumentBase.font_infos` property to access the collection of fonts
    defined in the document.'''
    
    def __getitem__(self, index: int) -> aspose.words.fonts.FontInfo:
        '''Gets a font at the specified index.
        
        :param index: Zero-based index of the font.'''
        ...
    
    def get_by_name(self, name: str) -> aspose.words.fonts.FontInfo:
        '''Gets a font with the specified name.'''
        ...
    
    def contains(self, name: str) -> bool:
        '''Determines whether the collection contains a font with the given name.
        
        :param name: Case-insensitive name of the font to locate.
        :returns: ``True`` if the item is found in the collection; otherwise, ``False``.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of elements contained in the collection.'''
        ...
    
    @property
    def embed_true_type_fonts(self) -> bool:
        '''Specifies whether or not to embed TrueType fonts in a document when it is saved.
        Default value for this property is ``False``.
        
        Embedding TrueType fonts allows others to view the document with the same fonts that were used to create it,
        but may substantially increase the document size.
        
        This option works for DOC, DOCX and RTF formats only.'''
        ...
    
    @embed_true_type_fonts.setter
    def embed_true_type_fonts(self, value: bool):
        ...
    
    @property
    def embed_system_fonts(self) -> bool:
        '''Specifies whether or not to embed System fonts into the document.
        Default value for this property is ``False``.
        
        This option works only when :attr:`FontInfoCollection.embed_true_type_fonts` option is set to ``True``.
        
        Setting this property to ``True`` is useful if the user is on an East Asian system
        and wants to create a document that is readable by others who do not have fonts for that
        language on their system. For example, a user on a Japanese system could choose to embed the
        fonts in a document so that the Japanese document would be readable on all systems.
        
        This option works for DOC, DOCX and RTF formats only.'''
        ...
    
    @embed_system_fonts.setter
    def embed_system_fonts(self, value: bool):
        ...
    
    @property
    def save_subset_fonts(self) -> bool:
        '''Specifies whether or not to save a subset of the embedded TrueType fonts with the document.
        Default value for this property is ``False``.
        
        This option works only when :attr:`FontInfoCollection.embed_true_type_fonts` property is set to ``True``.
        
        This option works for DOC, DOCX and RTF formats only.'''
        ...
    
    @save_subset_fonts.setter
    def save_subset_fonts(self, value: bool):
        ...
    
    ...

class FontInfoSubstitutionRule(aspose.words.fonts.FontSubstitutionRule):
    '''Font info substitution rule.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.
    
    According to this rule Aspose.Words evaluates all the related fields in :class:`FontInfo` (Panose, Sig etc) for
    the missing font and finds the closest match among the available font sources. If :class:`FontInfo` is not
    available for the missing font then nothing will be done.'''
    
    ...

class FontNameSubstitutionRule(aspose.words.fonts.FontSubstitutionRule):
    '''Font substitution rule for processing font name.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.
    
    According to this rule Aspose.Words tries to process the font name to get the substitution. Particularly
    Aspose.Words tries to removes suffixes with '-', ',' and '(' separators like it does the MS Word.'''
    
    ...

class FontSettings:
    '''Specifies font settings for a document.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.
    
    Aspose.Words uses font settings to resolve the fonts in the document. Fonts are resolved mostly when building document layout
    or rendering to fixed page formats. But when loading some formats, Aspose.Words also may require to resolve the fonts. For example, when
    loading HTML documents Aspose.Words may resolve the fonts to perform font fallback. So it is recommended that you set the font settings in
    :class:`aspose.words.loading.LoadOptions` when loading the document. Or at least before building the layout or rendering the document to the fixed-page format.
    
    By default all documents uses single static font settings instance. It could be accessed by
    :attr:`FontSettings.default_instance` property.
    
    Changing font settings is safe at any time from any thread. But it is recommended that you do not change the font settings while
    processing some documents which uses this settings. This can lead to the fact that the same font will be resolved differently
    in different parts of the document.'''
    
    def __init__(self):
        ...
    
    @overload
    def set_fonts_sources(self, sources: list[aspose.words.fonts.FontSourceBase]) -> None:
        '''Sets the sources where Aspose.Words looks for TrueType fonts when rendering documents or embedding fonts.
        
        By default, Aspose.Words looks for fonts installed to the system.
        
        Setting this property resets the cache of all previously loaded fonts.
        
        :param sources: An array of sources that contain TrueType fonts.'''
        ...
    
    @overload
    def set_fonts_sources(self, sources: list[aspose.words.fonts.FontSourceBase], cache_input_stream: io.BytesIO) -> None:
        '''Sets the sources where Aspose.Words looks for TrueType fonts and additionally loads previously saved
        font search cache.
        
        :param sources: An array of sources that contain TrueType fonts.
        :param cache_input_stream: Input stream with saved font search cache.
        
        Loading previously saved font search cache will speed up the font cache initialization process. It is
        especially useful when access to font sources is complicated (e.g. when fonts are loaded via network).
        
        When saving and loading font search cache, fonts in the provided sources are identified via cache key.
        For the fonts in the :class:`SystemFontSource` and :class:`FolderFontSource` cache key is the path
        to the font file. For :class:`MemoryFontSource` and :class:`StreamFontSource` cache key is defined
        in the :attr:`MemoryFontSource.cache_key` and :attr:`StreamFontSource.cache_key` properties
        respectively. For the :class:`FileFontSource` cache key is either :attr:`FileFontSource.cache_key`
        property or a file path if the :attr:`FileFontSource.cache_key` is ``None``.
        
        It is highly recommended to provide the same font sources when loading cache as at the time the cache was saved.
        Any changes in the font sources (e.g. adding new fonts, moving font files or changing the cache key) may lead to the
        inaccurate font resolving by Aspose.Words.'''
        ...
    
    def set_fonts_folder(self, font_folder: str, recursive: bool) -> None:
        '''Sets the folder where Aspose.Words looks for TrueType fonts when rendering documents or embedding fonts.
        This is a shortcut to :meth:`FontSettings.set_fonts_folders` for setting only one font directory.
        
        :param font_folder: The folder that contains TrueType fonts.
        :param recursive: True to scan the specified folders for fonts recursively.'''
        ...
    
    def set_fonts_folders(self, fonts_folders: list[str], recursive: bool) -> None:
        '''Sets the folders where Aspose.Words looks for TrueType fonts when rendering documents or embedding fonts.
        
        By default, Aspose.Words looks for fonts installed to the system.
        
        Setting this property resets the cache of all previously loaded fonts.
        
        :param fonts_folders: An array of folders that contain TrueType fonts.
        :param recursive: True to scan the specified folders for fonts recursively.'''
        ...
    
    def get_fonts_sources(self) -> list[aspose.words.fonts.FontSourceBase]:
        '''Gets a copy of the array that contains the list of sources where Aspose.Words looks for TrueType fonts.
        
        The returned value is a copy of the data that Aspose.Words uses. If you change the entries
        in the returned array, it will have no effect on document rendering. To specify new font sources
        use the :meth:`FontSettings.set_fonts_sources` method.
        
        :returns: A copy of the current font sources.'''
        ...
    
    def reset_font_sources(self) -> None:
        '''Resets the fonts sources to the system default.'''
        ...
    
    def save_search_cache(self, output_stream: io.BytesIO) -> None:
        '''Saves the font search cache to the stream.
        
        :param output_stream: Output stream.
        
        See :meth:`FontSettings.set_fonts_sources` method description for more info.'''
        ...
    
    default_instance: aspose.words.fonts.FontSettings
    
    @property
    def fallback_settings(self) -> aspose.words.fonts.FontFallbackSettings:
        '''Settings related to font fallback mechanism.'''
        ...
    
    @property
    def substitution_settings(self) -> aspose.words.fonts.FontSubstitutionSettings:
        '''Settings related to font substitution mechanism.'''
        ...
    
    ...

class FontSourceBase:
    '''This is an abstract base class for the classes that allow the user to specify various font sources.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.'''
    
    def get_available_fonts(self) -> list[aspose.words.fonts.PhysicalFontInfo]:
        '''Returns list of fonts available via this source.'''
        ...
    
    def as_file_font_source(self) -> aspose.words.fonts.FileFontSource:
        '''Cast :class:`FontSourceBase` object to :class:`FileFontSource`.'''
        ...
    
    def as_folder_font_source(self) -> aspose.words.fonts.FolderFontSource:
        '''Cast :class:`FontSourceBase` object to :class:`FolderFontSource`.'''
        ...
    
    def as_memory_font_source(self) -> aspose.words.fonts.MemoryFontSource:
        '''Cast :class:`FontSourceBase` object to :class:`MemoryFontSource`.'''
        ...
    
    def as_stream_font_source(self) -> aspose.words.fonts.StreamFontSource:
        '''Cast :class:`FontSourceBase` object to :class:`StreamFontSource`.'''
        ...
    
    def as_system_font_source(self) -> aspose.words.fonts.SystemFontSource:
        '''Cast :class:`FontSourceBase` object to :class:`SystemFontSource`.'''
        ...
    
    @property
    def type(self) -> aspose.words.fonts.FontSourceType:
        '''Returns the type of the font source.'''
        ...
    
    @property
    def priority(self) -> int:
        '''Returns the font source priority.
        
        This value is used when there are fonts with the same family name and style in different font sources.
        In this case Aspose.Words selects the font from the source with the higher priority value.
        
        The default value is 0.'''
        ...
    
    @property
    def warning_callback(self) -> aspose.words.IWarningCallback:
        '''Called during processing of font source when an issue is detected that might result in formatting fidelity loss.'''
        ...
    
    @warning_callback.setter
    def warning_callback(self, value: aspose.words.IWarningCallback):
        ...
    
    ...

class FontSubstitutionRule:
    '''This is an abstract base class for the font substitution rule.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.'''
    
    @property
    def enabled(self) -> bool:
        '''Specifies whether the rule is enabled or not.'''
        ...
    
    @enabled.setter
    def enabled(self, value: bool):
        ...
    
    ...

class FontSubstitutionSettings:
    '''Specifies font substitution mechanism settings.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.
    
    Font substitution process consists of several rules which are checked one by one in specific order.
    If the first rule can't resolve the font then second rule is checked and so on.
    
    The order of the rules is following:
    1. Font name substitution rule (enabled by default)
    2. Font config substitution rule (disabled by default)
    3. Table substitution rule (enabled by default)
    4. Font info substitution rule (enabled by default)
    5. Default font rule (enabled by default)
    
    Note that font info substitution rule will always resolve the font if :class:`FontInfo` is available
    and will override the default font rule. If you want to use the default font rule then you should disable the
    font info substitution rule.
    
    Note that font config substitution rule will resolve the font in most cases and thus overrides all other rules.'''
    
    @property
    def table_substitution(self) -> aspose.words.fonts.TableSubstitutionRule:
        '''Settings related to table substitution rule.'''
        ...
    
    @property
    def font_info_substitution(self) -> aspose.words.fonts.FontInfoSubstitutionRule:
        '''Settings related to font info substitution rule.'''
        ...
    
    @property
    def default_font_substitution(self) -> aspose.words.fonts.DefaultFontSubstitutionRule:
        '''Settings related to default font substitution rule.'''
        ...
    
    @property
    def font_config_substitution(self) -> aspose.words.fonts.FontConfigSubstitutionRule:
        '''Settings related to font config substitution rule.'''
        ...
    
    @property
    def font_name_substitution(self) -> aspose.words.fonts.FontNameSubstitutionRule:
        '''Settings related to font name substitution rule.'''
        ...
    
    ...

class MemoryFontSource(aspose.words.fonts.FontSourceBase):
    '''Represents the single TrueType font file stored in memory.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.'''
    
    @overload
    def __init__(self, font_data: bytes):
        '''Ctor.
        
        :param font_data: Binary font data.'''
        ...
    
    @overload
    def __init__(self, font_data: bytes, priority: int):
        '''Ctor.
        
        :param font_data: Binary font data.
        :param priority: Font source priority. See the :attr:`FontSourceBase.priority` property description for more information.'''
        ...
    
    @overload
    def __init__(self, font_data: bytes, priority: int, cache_key: str):
        '''Ctor.
        
        :param font_data: Binary font data.
        :param priority: Font source priority. See the :attr:`FontSourceBase.priority` property description for more information.
        :param cache_key: The key of this source in the cache. See :attr:`MemoryFontSource.cache_key` property description for more information.'''
        ...
    
    @property
    def type(self) -> aspose.words.fonts.FontSourceType:
        '''Returns the type of the font source.'''
        ...
    
    @property
    def font_data(self) -> bytes:
        '''Binary font data.'''
        ...
    
    @property
    def cache_key(self) -> str:
        '''The key of this source in the cache.
        
        This key is used to identify cache item when saving/loading font search cache with
        :meth:`FontSettings.save_search_cache` and :meth:`FontSettings.set_fonts_sources` methods.'''
        ...
    
    ...

class PhysicalFontInfo:
    '''Specifies information about physical font available to Aspose.Words font engine.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.'''
    
    @property
    def font_family_name(self) -> str:
        '''Family name of the font.'''
        ...
    
    @property
    def full_font_name(self) -> str:
        '''Full name of the font.'''
        ...
    
    @property
    def version(self) -> str:
        '''Version string of the font.'''
        ...
    
    @property
    def file_path(self) -> str:
        '''Path to the font file if any.'''
        ...
    
    ...

class StreamFontSource(aspose.words.fonts.FontSourceBase):
    '''Base class for user-defined stream font source.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.
    
    In order to use the stream font source you should create a derived class from the :class:`StreamFontSource`
    and provide implementation of the :meth:`StreamFontSource.open_font_data_stream` method.
    
    :meth:`StreamFontSource.open_font_data_stream` method could be called several times. For the first time it will be called
    when Aspose.Words scans the provided font sources to get the list of available fonts. Later it may be called if the
    font is used in the document to parse the font data and to embed the font data to some output formats.
    
    :class:`StreamFontSource` may be useful because it allows to load the font data only when it is required
    and not to store it in the memory for the :class:`FontSettings` lifetime.'''
    
    def open_font_data_stream(self) -> io.BytesIO:
        '''This method should open the stream with font data on demand.
        
        :returns: Font data stream.
        
        The stream will be closed after reading. There is no need to close it explicitly.'''
        ...
    
    @property
    def type(self) -> aspose.words.fonts.FontSourceType:
        '''Returns the type of the font source.'''
        ...
    
    @property
    def cache_key(self) -> str:
        '''The key of this source in the cache.
        
        This key is used to identify cache item when saving/loading font search cache with
        :meth:`FontSettings.save_search_cache` and :meth:`FontSettings.set_fonts_sources` methods.'''
        ...
    
    ...

class SystemFontSource(aspose.words.fonts.FontSourceBase):
    '''Represents all TrueType fonts installed to the system.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.'''
    
    @overload
    def __init__(self):
        '''Ctor.'''
        ...
    
    @overload
    def __init__(self, priority: int):
        '''Ctor.
        
        :param priority: Font source priority. See the :attr:`FontSourceBase.priority` property description for more information.'''
        ...
    
    @staticmethod
    def get_system_font_folders(self) -> list[str]:
        '''Returns system font folders or empty array if folders are not accessible.
        
        On some platforms Aspose.Words could search system fonts not only through folders but in other sources too. For example, on Windows platform
        Aspose.Words search fonts also in the registry.'''
        ...
    
    @property
    def type(self) -> aspose.words.fonts.FontSourceType:
        '''Returns the type of the font source.'''
        ...
    
    ...

class TableSubstitutionRule(aspose.words.fonts.FontSubstitutionRule):
    '''Table font substitution rule.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/net/working-with-fonts/>` documentation article.
    
    This rule defines the list of substitute font names to be used if the original font is not available.
    Substitutes will be checked for the font name and the :attr:`FontInfo.alt_name` (if any).'''
    
    @overload
    def load(self, file_name: str) -> None:
        '''Loads table substitution settings from XML file.
        
        :param file_name: Input file name.'''
        ...
    
    @overload
    def load(self, stream: io.BytesIO) -> None:
        '''Loads table substitution settings from XML stream.
        
        :param stream: Input stream.'''
        ...
    
    @overload
    def save(self, file_name: str) -> None:
        '''Saves the current table substitution settings to file.
        
        :param file_name: Output file name.'''
        ...
    
    @overload
    def save(self, output_stream: io.BytesIO) -> None:
        '''Saves the current table substitution settings to stream.
        
        :param output_stream: Output stream.'''
        ...
    
    def load_windows_settings(self) -> None:
        '''Loads predefined table substitution settings for Windows platform.'''
        ...
    
    def load_linux_settings(self) -> None:
        '''Loads predefined table substitution settings for Linux platform.'''
        ...
    
    def load_android_settings(self) -> None:
        '''Loads predefined table substitution settings for Linux platform.'''
        ...
    
    def get_substitutes(self, original_font_name: str) -> Iterable[str]:
        '''Returns array containing substitute font names for the specified original font name.
        
        :param original_font_name: Original font name.
        :returns: List of alternative font names.'''
        ...
    
    def set_substitutes(self, original_font_name: str, substitute_font_names: list[str]) -> None:
        '''Override substitute font names for given original font name.
        
        :param original_font_name: Original font name.
        :param substitute_font_names: List of alternative font names.'''
        ...
    
    def add_substitutes(self, original_font_name: str, substitute_font_names: list[str]) -> None:
        '''Adds substitute font names for given original font name.
        
        :param original_font_name: Original font name.
        :param substitute_font_names: List of alternative font names.'''
        ...
    
    ...

class EmbeddedFontFormat:
    '''Specifies format of particular embedded font inside :class:`FontInfo` object.
    
    When saving a document to a file, only embedded fonts of corresponding format are written down.'''
    
    EMBEDDED_OPEN_TYPE: int
    OPEN_TYPE: int

class EmbeddedFontStyle:
    '''Specifies the style of an embedded font inside a :class:`FontInfo` object.'''
    
    REGULAR: int
    BOLD: int
    ITALIC: int
    BOLD_ITALIC: int

class FontFamily:
    '''Represents the font family.
    
    A font family is a set of fonts having common stroke width and serif characteristics.'''
    
    AUTO: int
    ROMAN: int
    SWISS: int
    MODERN: int
    SCRIPT: int
    DECORATIVE: int

class FontPitch:
    '''Represents the font pitch.
    
    The pitch indicates if the font is fixed pitch, proportionally spaced, or relies on a default setting.'''
    
    DEFAULT: int
    FIXED: int
    VARIABLE: int

class FontSourceType:
    '''Specifies the type of a font source.'''
    
    FONT_FILE: int
    FONTS_FOLDER: int
    MEMORY_FONT: int
    SYSTEM_FONTS: int
    FONT_STREAM: int

