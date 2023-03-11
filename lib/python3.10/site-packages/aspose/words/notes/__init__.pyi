import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class EndnoteOptions:
    '''Represents the endnote numbering options for a document or section.
    To learn more, visit the `Working with Footnote and Endnote <https://docs.aspose.com/words/net/working-with-footnote-and-endnote/>` documentation article.'''
    
    @property
    def position(self) -> aspose.words.notes.EndnotePosition:
        '''Specifies the endnotes position.'''
        ...
    
    @position.setter
    def position(self, value: aspose.words.notes.EndnotePosition):
        ...
    
    @property
    def number_style(self) -> aspose.words.NumberStyle:
        '''Specifies the number format for automatically numbered endnotes.
        
        Not all number styles are applicable for this property. For the list of applicable
        number styles see the Insert Footnote or Endnote dialog box in Microsoft Word. If you select
        a number style that is not applicable, Microsoft Word will revert to a default value.'''
        ...
    
    @number_style.setter
    def number_style(self, value: aspose.words.NumberStyle):
        ...
    
    @property
    def start_number(self) -> int:
        '''Specifies the starting number or character for the first automatically numbered endnotes.
        
        This property has effect only when :attr:`EndnoteOptions.restart_rule` is set to
        :attr:`FootnoteNumberingRule.CONTINUOUS`.'''
        ...
    
    @start_number.setter
    def start_number(self, value: int):
        ...
    
    @property
    def restart_rule(self) -> aspose.words.notes.FootnoteNumberingRule:
        '''Determines when automatic numbering restarts.
        
        Not all values are applicable to endnotes.
        To ascertain which values are applicable see :class:`FootnoteNumberingRule`.'''
        ...
    
    @restart_rule.setter
    def restart_rule(self, value: aspose.words.notes.FootnoteNumberingRule):
        ...
    
    ...

class Footnote(aspose.words.InlineStory):
    '''Represents a container for text of a footnote or endnote.
    To learn more, visit the `Working with Footnote and Endnote <https://docs.aspose.com/words/net/working-with-footnote-and-endnote/>` documentation article.
    
    The :class:`Footnote` class is used to represent both footnotes and endnotes in a Word document.
    
    :class:`Footnote` is an inline-level node and can only be a child of :class:`aspose.words.Paragraph`.
    
    :class:`Footnote` can contain :class:`aspose.words.Paragraph` and :class:`aspose.words.tables.Table` child nodes.'''
    
    def __init__(self, doc: aspose.words.DocumentBase, footnote_type: aspose.words.notes.FootnoteType):
        '''Initializes an instance of the :class:`Footnote` class.
        
        When :class:`Footnote` is created, it belongs to the specified document, but is not
        yet part of the document and :attr:`aspose.words.Node.parent_node` is ``None``.
        
        To append :class:`Footnote` to the document use :meth:`aspose.words.CompositeNode.insert_after` or :meth:`aspose.words.CompositeNode.insert_before`
        on the paragraph where you want the footnote inserted.
        
        :param doc: The owner document.
        :param footnote_type: A :attr:`Footnote.footnote_type` value
                              that specifies whether this is a footnote or endnote.'''
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        '''Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`aspose.words.DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`aspose.words.DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls DocumentVisitor.VisitFootnoteStart, then calls Accept for all child nodes of the footnote
        and calls DocumentVisitor.VisitFootnoteEnd at the end.'''
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        '''Returns :attr:`aspose.words.NodeType.FOOTNOTE`.'''
        ...
    
    @property
    def story_type(self) -> aspose.words.StoryType:
        '''Returns :attr:`aspose.words.StoryType.FOOTNOTES` or :attr:`aspose.words.StoryType.ENDNOTES`.'''
        ...
    
    @property
    def footnote_type(self) -> aspose.words.notes.FootnoteType:
        '''Returns a value that specifies whether this is a footnote or endnote.'''
        ...
    
    @property
    def is_auto(self) -> bool:
        '''Holds a value that specifies whether this is a auto-numbered footnote or
        footnote with user defined custom reference mark.
        
        :attr:`Footnote.reference_mark` initialized with empty string if :attr:`Footnote.is_auto` set to ``False``.'''
        ...
    
    @is_auto.setter
    def is_auto(self, value: bool):
        ...
    
    @property
    def reference_mark(self) -> str:
        '''Gets/sets custom reference mark to be used for this footnote.
        Default value is **empty string** (System.String.Empty), meaning auto-numbered footnotes are used.
        
        If this property is set to **empty string** (System.String.Empty) or ``None``, then :attr:`Footnote.is_auto` property will automatically be set to ``True``,
        if set to anything else then :attr:`Footnote.is_auto` will be set to ``False``.
        
        RTF-format can only store 1 symbol as custom reference mark, so upon export only the first symbol will be written others will be discard.'''
        ...
    
    @reference_mark.setter
    def reference_mark(self, value: str):
        ...
    
    ...

class FootnoteOptions:
    '''Represents the footnote numbering options for a document or section.
    To learn more, visit the `Working with Footnote and Endnote <https://docs.aspose.com/words/net/working-with-footnote-and-endnote/>` documentation article.'''
    
    @property
    def position(self) -> aspose.words.notes.FootnotePosition:
        '''Specifies the footnotes position.'''
        ...
    
    @position.setter
    def position(self, value: aspose.words.notes.FootnotePosition):
        ...
    
    @property
    def number_style(self) -> aspose.words.NumberStyle:
        '''Specifies the number format for automatically numbered footnotes.
        
        Not all number styles are applicable for this property. For the list of applicable
        number styles see the Insert Footnote or Endnote dialog box in Microsoft Word. If you select
        a number style that is not applicable, Microsoft Word will revert to a default value.'''
        ...
    
    @number_style.setter
    def number_style(self, value: aspose.words.NumberStyle):
        ...
    
    @property
    def start_number(self) -> int:
        '''Specifies the starting number or character for the first automatically numbered footnotes.
        
        This property has effect only when :attr:`FootnoteOptions.restart_rule` is set to
        :attr:`FootnoteNumberingRule.CONTINUOUS`.'''
        ...
    
    @start_number.setter
    def start_number(self, value: int):
        ...
    
    @property
    def restart_rule(self) -> aspose.words.notes.FootnoteNumberingRule:
        '''Determines when automatic numbering restarts.'''
        ...
    
    @restart_rule.setter
    def restart_rule(self, value: aspose.words.notes.FootnoteNumberingRule):
        ...
    
    @property
    def columns(self) -> int:
        '''Specifies the number of columns with which the footnotes area is formatted.
        
        If this property has the value of 0, the footnotes area is formatted with a number of columns based on
        the number of columns on the displayed page. The default value is 0.'''
        ...
    
    @columns.setter
    def columns(self, value: int):
        ...
    
    ...

class EndnotePosition:
    '''Defines the endnote position.'''
    
    END_OF_SECTION: int
    END_OF_DOCUMENT: int

class FootnoteNumberingRule:
    '''Determines when automatic footnote or endnote numbering restarts.'''
    
    CONTINUOUS: int
    RESTART_SECTION: int
    RESTART_PAGE: int
    DEFAULT: int

class FootnotePosition:
    '''Defines the footnote position.'''
    
    BOTTOM_OF_PAGE: int
    BENEATH_TEXT: int

class FootnoteType:
    '''Specifies whether this is a footnote or an endnote.
    
    Both footnotes and endnotes are represented by objects by the :attr:`FootnoteType.FOOTNOTE`
    class. Use :attr:`Footnote.footnote_type` to distinguish between footnotes
    and endnotes.'''
    
    FOOTNOTE: int
    ENDNOTE: int

