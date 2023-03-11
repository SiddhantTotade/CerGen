import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class BasicTextShaperCache:
    '''Implements basic cache for :class:`ITextShaper` instances. This class is thread-safe.'''
    
    def __init__(self, factory: aspose.words.shaping.ITextShaperFactory):
        '''Wraps  and caches:meth:`ITextShaperFactory.get_text_shaper` results.'''
        ...
    
    ...

class Cluster:
    '''Encapsulates code points and glyphs composing a grapheme.'''
    
    def __init__(self, codepoints: list[int], glyphs: list[aspose.words.shaping.Glyph]):
        '''Initializes new instance of this class.
        
        :param codepoints: Array of Unicode points composing a grapheme.
        :param glyphs: Array of :class:`Glyph`\> composing a grapheme.'''
        ...
    
    @overload
    @staticmethod
    def get_string(self, clusters: list[aspose.words.shaping.Cluster]) -> str:
        '''Creates System.String using codepoints from the specified clusters.'''
        ...
    
    @overload
    def get_string(self) -> str:
        '''Creates System.String using codepoints from this cluster.'''
        ...
    
    def get_width(self, em: int, font_size: float) -> float:
        '''Returns width of the cluster.'''
        ...
    
    def deep_clone(self) -> aspose.words.shaping.Cluster:
        '''Returns a deep clone of this instance.'''
        ...
    
    @property
    def codepoints(self) -> list[int]:
        '''Gets codepoints of the cluster.'''
        ...
    
    @property
    def codepoints_length(self) -> int:
        '''Gets total number of codepoints in the :class:`Cluster`.'''
        ...
    
    @property
    def glyphs(self) -> list[aspose.words.shaping.Glyph]:
        '''Gets glyphs of the cluster.'''
        ...
    
    ...

class Glyph:
    '''Represents a glyph'''
    
    def __init__(self, glyph_index: int, advance: int, advance_offset: int, ascender_offset: int):
        '''Initializes new instance of this class.
        
        :param glyph_index: Glyph index.
        :param advance: Advance metric of the glyph.
        :param advance_offset: Horizontal (x) offset.
        :param ascender_offset: Vertical (y) offset.'''
        ...
    
    def get_width(self, em: int, font_size: float) -> float:
        '''Returns width (advance) of the glyph in points.'''
        ...
    
    def clone(self) -> aspose.words.shaping.Glyph:
        '''Returns a clone of this instance.'''
        ...
    
    @property
    def glyph_index(self) -> int:
        '''Index of the glyph (GID) in the physical font.'''
        ...
    
    @property
    def advance(self) -> int:
        '''Advance width indicating placement for the subsequent glyph.'''
        ...
    
    @advance.setter
    def advance(self, value: int):
        ...
    
    @property
    def advance_offset(self) -> int:
        '''Horizontal (x) offset relative to glyph position.
        Mostly used to attach marks (like diacritics) to base characters.'''
        ...
    
    @property
    def ascender_offset(self) -> int:
        '''Vertical (y) offset relative to glyph position.
        Mostly used to attach marks (like diacritics) to base characters.'''
        ...
    
    ...

class ITextShaper:
    '''Provides methods for text shaping.'''
    
    def shape_text(self, runs: list[str], direction: aspose.words.shaping.Direction, script: aspose.words.shaping.UnicodeScript, font_features: list[aspose.words.shaping.FontFeature]) -> list[list[aspose.words.shaping.Cluster]]:
        '''Returns :class:`Cluster` objects generated from a sequence of text fragments.
        Length of the returned array is equal to length of .
        If run at an index has corresponding clusters then result at the same index will have them recorded.
        
        :param runs: A sequence of text fragments
        :param direction: A direction of text
        :param script: A script
        :param font_features: A set of features to consider'''
        ...
    
    ...

class ITextShaperFactory:
    '''An interface of a factory for constructing :class:`ITextShaper` implementations.'''
    
    @overload
    def get_text_shaper(self, font_path: str, face_index: int) -> aspose.words.shaping.ITextShaper:
        '''Returns new instance of a text shaper for the font specified by  and.
        
        :param font_path: An absolute path to the font file.
        :param face_index: An index of the font face in the TrueType font collection,
                           or 0 if specified font file is not TrueType font collection.'''
        ...
    
    @overload
    def get_text_shaper(self, font_id: str, font_blob: bytes, face_index: int) -> aspose.words.shaping.ITextShaper:
        '''Returns new instance of a text shaper for the font represented by  and.
        
        :param font_id: A unique identifier that can be uniquely associated with the provided font .
        :param font_blob: Byte array with the font data.
        :param face_index: An index of the font face in the TrueType font collection,
                           or 0 if  is not TrueType font collection.'''
        ...
    
    ...

class Direction:
    '''Text direction.'''
    
    DEFAULT: int
    LTR: int
    RTL: int
    TTB: int
    BTT: int

class FontFeature:
    '''Features provide information about how glyphs are used in a font to render a script.
    https://docs.microsoft.com/en-us/typography/opentype/spec/featuretags'''
    
    GLYPH_COMPOSITION_DECOMPOSITION: int
    STANDARD_LIGATURES: int
    REQUIRED_LIGATURES: int
    CONTEXTUAL_LIGATURES: int
    DISCRETIONARY_LIGATURES: int
    HISTORICAL_LIGATURES: int
    PROPORTIONAL_FIGURES: int
    TABULAR_FIGURES: int
    LINING_FIGURES: int
    OLDSTYLE_FIGURES: int
    VERTICAL_ALTERNATES: int
    VERTICAL_ALTERNATES_AND_ROTATION: int
    STYLISTIC_SET01: int
    STYLISTIC_SET02: int
    STYLISTIC_SET03: int
    STYLISTIC_SET04: int
    STYLISTIC_SET05: int
    STYLISTIC_SET06: int
    STYLISTIC_SET07: int
    STYLISTIC_SET08: int
    STYLISTIC_SET09: int
    STYLISTIC_SET10: int
    STYLISTIC_SET11: int
    STYLISTIC_SET12: int
    STYLISTIC_SET13: int
    STYLISTIC_SET14: int
    STYLISTIC_SET15: int
    STYLISTIC_SET16: int
    STYLISTIC_SET17: int
    STYLISTIC_SET18: int
    STYLISTIC_SET19: int
    STYLISTIC_SET20: int
    KERNING: int

class ScriptShapingLevel:
    '''Describes shaping levels required by a script.'''
    
    NONE: int
    UNKNOWN: int
    MINIMUM: int
    FULL: int

class UnicodeScript:
    '''Unicode Character Database property: Script (sc).
    
    http://www.unicode.org/reports/tr24/tr24-29.html
    https://www.unicode.org/iso15924/
    http://goo.gl/x9ilM'''
    
    ADLAM: int
    CAUCASIAN_ALBANIAN: int
    AHOM: int
    ARABIC: int
    IMPERIAL_ARAMAIC: int
    ARMENIAN: int
    AVESTAN: int
    BALINESE: int
    BAMUM: int
    BASSA_VAH: int
    BATAK: int
    BENGALI: int
    BHAIKSUKI: int
    BOPOMOFO: int
    BRAHMI: int
    BRAILLE: int
    BUGINESE: int
    BUHID: int
    CHAKMA: int
    CANADIAN_ABORIGINAL: int
    CARIAN: int
    CHAM: int
    CHEROKEE: int
    CHORASMIAN: int
    COPTIC: int
    CYPRIOT: int
    CYRILLIC: int
    DEVANAGARI: int
    DIVES_AKURU: int
    DOGRA: int
    DESERET: int
    DUPLOYAN: int
    EGYPTIAN_HIEROGLYPHS: int
    ELBASAN: int
    ELYMAIC: int
    ETHIOPIC: int
    GEORGIAN: int
    GLAGOLITIC: int
    GUNJALA_GONDI: int
    MASARAM_GONDI: int
    GOTHIC: int
    GRANTHA: int
    GREEK: int
    GUJARATI: int
    GURMUKHI: int
    HANGUL: int
    HAN: int
    HANUNOO: int
    HATRAN: int
    HEBREW: int
    HIRAGANA: int
    ANATOLIAN_HIEROGLYPHS: int
    PAHAWH_HMONG: int
    NYIAKENG_PUACHUE_HMONG: int
    KATAKANA_OR_HIRAGANA: int
    OLD_HUNGARIAN: int
    OLD_ITALIC: int
    JAVANESE: int
    KAYAH_LI: int
    KATAKANA: int
    KHAROSHTHI: int
    KHMER: int
    KHOJKI: int
    KHITAN_SMALL_SCRIPT: int
    KANNADA: int
    KAITHI: int
    TAI_THAM: int
    LAO: int
    LATIN: int
    LEPCHA: int
    LIMBU: int
    LINEAR_A: int
    LINEAR_B: int
    LISU: int
    LYCIAN: int
    LYDIAN: int
    MAHAJANI: int
    MAKASAR: int
    MANDAIC: int
    MANICHAEAN: int
    MARCHEN: int
    MEDEFAIDRIN: int
    MENDE_KIKAKUI: int
    MEROITIC_CURSIVE: int
    MEROITIC_HIEROGLYPHS: int
    MALAYALAM: int
    MODI: int
    MONGOLIAN: int
    MRO: int
    MEETEI_MAYEK: int
    MULTANI: int
    MYANMAR: int
    NANDINAGARI: int
    OLD_NORTH_ARABIAN: int
    NABATAEAN: int
    NEWA: int
    NKO: int
    NUSHU: int
    OGHAM: int
    OL_CHIKI: int
    OLD_TURKIC: int
    ORIYA: int
    OSAGE: int
    OSMANYA: int
    PALMYRENE: int
    PAU_CIN_HAU: int
    OLD_PERMIC: int
    PHAGS_PA: int
    INSCRIPTIONAL_PAHLAVI: int
    PSALTER_PAHLAVI: int
    PHOENICIAN: int
    MIAO: int
    INSCRIPTIONAL_PARTHIAN: int
    REJANG: int
    HANIFI_ROHINGYA: int
    RUNIC: int
    SAMARITAN: int
    OLD_SOUTH_ARABIAN: int
    SAURASHTRA: int
    SIGN_WRITING: int
    SHAVIAN: int
    SHARADA: int
    SIDDHAM: int
    KHUDAWADI: int
    SINHALA: int
    SOGDIAN: int
    OLD_SOGDIAN: int
    SORA_SOMPENG: int
    SOYOMBO: int
    SUNDANESE: int
    SYLOTI_NAGRI: int
    SYRIAC: int
    TAGBANWA: int
    TAKRI: int
    TAI_LE: int
    NEW_TAI_LUE: int
    TAMIL: int
    TANGUT: int
    TAI_VIET: int
    TELUGU: int
    TIFINAGH: int
    TAGALOG: int
    THAANA: int
    THAI: int
    TIBETAN: int
    TIRHUTA: int
    UGARITIC: int
    VAI: int
    WARANG_CITI: int
    WANCHO: int
    OLD_PERSIAN: int
    CUNEIFORM: int
    YEZIDI: int
    YI: int
    ZANABAZAR_SQUARE: int
    INHERITED: int
    COMMON: int
    UNKNOWN: int

