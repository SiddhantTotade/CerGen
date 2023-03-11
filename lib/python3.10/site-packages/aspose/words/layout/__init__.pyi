import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class IPageLayoutCallback:
    '''Implement this interface if you want to have your own custom method called during build and rendering of page layout model.
    
    The primary use for this interface is to allow application code to abort build process.
    
    It is possible to build page layout model for only a few pages at start of the document then abort process and render only what has been built already.
    
    Note, however, that rendering results may not match what would be rendered for each page if process would have finished.
    
    This technique may not work for every document or may fail completely.'''
    
    def notify(self, args: aspose.words.layout.PageLayoutCallbackArgs) -> None:
        '''This is called to notify of layout build and rendering progress.
        
        :param args: An argument of the event.
        
        Exception when thrown by implementation aborts layout build process.'''
        ...
    
    ...

class LayoutCollector:
    '''This class allows to compute page numbers of document nodes.
    
    To learn more, visit the `Converting to Fixed-page Format <https://docs.aspose.com/words/net/converting-to-fixed-page-format/>` documentation article.
    
    When you create a :class:`LayoutCollector` and specify a :class:`aspose.words.Document` document object to attach to,
    the collector will record mapping of document nodes to layout objects when the document is formatted into pages.
    
    You will be able to find out on which page a particular document node (e.g. run, paragraph or table cell) is located
    by using the :meth:`LayoutCollector.get_start_page_index`, :meth:`LayoutCollector.get_end_page_index` and :meth:`LayoutCollector.get_num_pages_spanned` methods.
    These methods automatically build page layout model of the document and update fields if required.
    
    When you no longer need to collect layout information, it is best to set the :attr:`LayoutCollector.document` property to ``None``
    to avoid unnecessary collection of more layout mappings.'''
    
    def __init__(self, doc: aspose.words.Document):
        '''Initializes an instance of this class.
        
        :param doc: The document to which this collector instance will be attached to.'''
        ...
    
    def get_start_page_index(self, node: aspose.words.Node) -> int:
        '''Gets 1-based index of the page where node begins. Returns 0 if node cannot be mapped to a page.'''
        ...
    
    def get_end_page_index(self, node: aspose.words.Node) -> int:
        '''Gets 1-based index of the page where node ends. Returns 0 if node cannot be mapped to a page.'''
        ...
    
    def get_num_pages_spanned(self, node: aspose.words.Node) -> int:
        '''Gets number of pages the specified node spans. 0 if node is within a single page.
        This is the same as :meth:`LayoutCollector.get_end_page_index` - :meth:`LayoutCollector.get_start_page_index`.'''
        ...
    
    def clear(self) -> None:
        '''Clears all collected layout data. Call this method after document was manually updated, or layout was rebuilt.'''
        ...
    
    @property
    def document(self) -> aspose.words.Document:
        '''Gets or sets the document this collector instance is attached to.
        
        If you need to access page indexes of the document nodes you need to set this property to point to a document instance,
        before page layout of the document is built. It is best to set this property to ``None`` afterwards,
        otherwise the collector continues to accumulate information from subsequent rebuilds of the document's page layout.'''
        ...
    
    @document.setter
    def document(self, value: aspose.words.Document):
        ...
    
    ...

class LayoutEnumerator:
    '''Enumerates page layout entities of a document.
    
    You can use this class to walk over the page layout model. Available properties are type, geometry, text and page index where entity is rendered,
    as well as overall structure and relationships.
    Use combination of Aspose.Words.Layout.LayoutCollector.GetEntity(Aspose.Words.Node) and Aspose.Words.Layout.LayoutEnumerator.Current move to the entity which corresponds to a document node.
    To learn more, visit the `Converting to Fixed-page Format <https://docs.aspose.com/words/net/converting-to-fixed-page-format/>` documentation article.'''
    
    def __init__(self, document: aspose.words.Document):
        '''Initializes new instance of this class.
        
        :param document: A document whose page layout model to enumerate.
        
        If page layout model of the document hasn't been built the enumerator calls :meth:`aspose.words.Document.update_page_layout` to build it.
        
        Whenever document is updated and new page layout model is created, a new enumerator must be used to access it.'''
        ...
    
    @overload
    def move_parent(self) -> bool:
        '''Moves to the parent entity.'''
        ...
    
    @overload
    def move_parent(self, types: aspose.words.layout.LayoutEntityType) -> bool:
        '''Moves to the parent entity of the specified type.
        
        :param types: The parent entity type to move to. Use bitwise-OR to specify multiple parent types.
        
        This method is useful if you need to find the cell, column or header/footer parent of the entity.'''
        ...
    
    def reset(self) -> None:
        '''Moves the enumerator to the first page of the document.'''
        ...
    
    def move_next(self) -> bool:
        '''Moves to the next sibling entity in visual order.
        
        When iterating lines of a paragraph broken across pages this method
        will not move to the next page but rather move to the next entity on the same page.'''
        ...
    
    def move_next_logical(self) -> bool:
        '''Moves to the next sibling entity in a logical order.
        
        When iterating lines of a paragraph broken across pages this method
        will move to the next line even if it resides on another page.
        
        Note that all :attr:`LayoutEntityType.SPAN` entities are linked together thus if Aspose.Words.Layout.LayoutEnumerator.Current
        entity is span repeated calling of this method will iterates complete story of the document.'''
        ...
    
    def move_previous(self) -> bool:
        '''Moves to the previous sibling entity.'''
        ...
    
    def move_previous_logical(self) -> bool:
        '''Moves to the previous sibling entity in a logical order.
        
        When iterating lines of a paragraph broken across pages this method
        will move to the previous line even if it resides on another page.
        
        Note that all :attr:`LayoutEntityType.SPAN` entities are linked together thus if Aspose.Words.Layout.LayoutEnumerator.Current
        entity is span repeated calling of this method will iterates complete story of the document.'''
        ...
    
    def move_first_child(self) -> bool:
        '''Moves to the first child entity.'''
        ...
    
    def move_last_child(self) -> bool:
        '''Moves to the last child entity.'''
        ...
    
    def set_current(self, collector: aspose.words.layout.LayoutCollector, node: aspose.words.Node) -> None:
        '''Extracts an opaque position of the :class:`LayoutEnumerator` which corresponds to the specified node and
        sets this position as current position in the page layout model'''
        ...
    
    @property
    def type(self) -> aspose.words.layout.LayoutEntityType:
        '''Gets the type of the current entity.'''
        ...
    
    @property
    def rectangle(self) -> aspose.pydrawing.RectangleF:
        '''Returns the bounding rectangle of the current entity relative to the page top left corner (in points).'''
        ...
    
    @property
    def kind(self) -> str:
        '''Gets the kind of the current entity. This can be an empty string but never ``None``.
        
        This is a more specific type of the current entity, e.g. bookmark span has :attr:`LayoutEntityType.SPAN` type and
        may have either a BOOKMARKSTART or BOOKMARKEND kind.'''
        ...
    
    @property
    def text(self) -> str:
        '''Gets text of the current span entity. Throws for other entity types.'''
        ...
    
    @property
    def page_index(self) -> int:
        '''Gets the 1-based index of a page which contains the current entity.'''
        ...
    
    @property
    def document(self) -> aspose.words.Document:
        '''Gets document this instance enumerates.'''
        ...
    
    ...

class LayoutOptions:
    '''Holds the options that allow controlling the document layout process.
    To learn more, visit the `Converting to Fixed-page Format <https://docs.aspose.com/words/net/converting-to-fixed-page-format/>` documentation article.
    
    You do not create instances of this class directly. Use the :attr:`aspose.words.Document.layout_options` property to access layout options for this document.
    
    Note that after changing any of the options present in this class, :meth:`aspose.words.Document.update_page_layout` method
    should be called in order for the changed options to be applied to the layout.'''
    
    def __init__(self):
        ...
    
    @property
    def revision_options(self) -> aspose.words.layout.RevisionOptions:
        '''Gets revision options.'''
        ...
    
    @property
    def show_hidden_text(self) -> bool:
        '''Gets or sets indication of whether hidden text in the document is rendered.
        Default is ``False``.
        
        This property affects all hidden content, not just text.'''
        ...
    
    @show_hidden_text.setter
    def show_hidden_text(self, value: bool):
        ...
    
    @property
    def show_paragraph_marks(self) -> bool:
        '''Gets or sets indication of whether paragraph marks are rendered.
        Default is ``False``.'''
        ...
    
    @show_paragraph_marks.setter
    def show_paragraph_marks(self, value: bool):
        ...
    
    @property
    def comment_display_mode(self) -> aspose.words.layout.CommentDisplayMode:
        '''Gets or sets the way comments are rendered.
        Default value is :attr:`CommentDisplayMode.SHOW_IN_BALLOONS`.
        
        Note that revisions are not rendered in balloons for :attr:`CommentDisplayMode.SHOW_IN_ANNOTATIONS`.'''
        ...
    
    @comment_display_mode.setter
    def comment_display_mode(self, value: aspose.words.layout.CommentDisplayMode):
        ...
    
    @property
    def text_shaper_factory(self) -> aspose.words.shaping.ITextShaperFactory:
        '''Gets or sets :class:`aspose.words.shaping.ITextShaperFactory` implementation used for Advanced Typography rendering features.'''
        ...
    
    @text_shaper_factory.setter
    def text_shaper_factory(self, value: aspose.words.shaping.ITextShaperFactory):
        ...
    
    @property
    def callback(self) -> aspose.words.layout.IPageLayoutCallback:
        '''Gets or sets :class:`IPageLayoutCallback` implementation used by page layout model.'''
        ...
    
    @callback.setter
    def callback(self, value: aspose.words.layout.IPageLayoutCallback):
        ...
    
    @property
    def ignore_printer_metrics(self) -> bool:
        '''Gets or sets indication of whether the "Use printer metrics to lay out document" compatibility option is ignored.
        Default is ``True``.'''
        ...
    
    @ignore_printer_metrics.setter
    def ignore_printer_metrics(self, value: bool):
        ...
    
    @property
    def continuous_section_page_numbering_restart(self) -> aspose.words.layout.ContinuousSectionRestart:
        '''Gets or sets the mode of behavior for computing page numbers when a continuous section
        restarts the page numbering.
        
        The default value is :attr:`ContinuousSectionRestart.ALWAYS`.
        It matches the behavior of MS Word 2019 which was the latest version at the moment the option was introduced.
        Older page numbering logic demonstrated by MS Word 2016 is available via this option.
        Please :class:`ContinuousSectionRestart` for the behavior description.'''
        ...
    
    @continuous_section_page_numbering_restart.setter
    def continuous_section_page_numbering_restart(self, value: aspose.words.layout.ContinuousSectionRestart):
        ...
    
    ...

class PageLayoutCallbackArgs:
    '''An argument passed into :meth:`IPageLayoutCallback.notify`To learn more, visit the `Converting to Fixed-page Format <https://docs.aspose.com/words/net/converting-to-fixed-page-format/>` documentation article.'''
    
    @property
    def event(self) -> aspose.words.layout.PageLayoutEvent:
        '''Gets event.'''
        ...
    
    @property
    def document(self) -> aspose.words.Document:
        '''Gets document.'''
        ...
    
    @property
    def page_index(self) -> int:
        '''Gets 0-based index of the page in the document this event relates to.
        Returns negative value if there is no associated page, or if page was removed during reflow.'''
        ...
    
    ...

class RevisionOptions:
    '''Allows to control how document revisions are handled during layout process.
    To learn more, visit the `Converting to Fixed-page Format <https://docs.aspose.com/words/net/converting-to-fixed-page-format/>` documentation article.'''
    
    @property
    def show_revision_marks(self) -> bool:
        '''Allow to specify whether revision text should be marked with special formatting markup.
        Default value is ``True``.'''
        ...
    
    @show_revision_marks.setter
    def show_revision_marks(self, value: bool):
        ...
    
    @property
    def show_revision_bars(self) -> bool:
        '''Allows to specify whether revision bars should be rendered near lines containing revised content.
        Default value is ``True``.'''
        ...
    
    @show_revision_bars.setter
    def show_revision_bars(self, value: bool):
        ...
    
    @property
    def show_original_revision(self) -> bool:
        '''Allows to specify whether the original text should be shown instead of revised one.
        Default value is ``False``.'''
        ...
    
    @show_original_revision.setter
    def show_original_revision(self, value: bool):
        ...
    
    @property
    def inserted_text_color(self) -> aspose.words.layout.RevisionColor:
        '''Allows to specify the color to be used for inserted content :attr:`aspose.words.RevisionType.INSERTION`.
        Default value is :attr:`RevisionColor.BY_AUTHOR`.'''
        ...
    
    @inserted_text_color.setter
    def inserted_text_color(self, value: aspose.words.layout.RevisionColor):
        ...
    
    @property
    def inserted_text_effect(self) -> aspose.words.layout.RevisionTextEffect:
        '''Allows to specify the effect to be applied to the inserted content :attr:`aspose.words.RevisionType.INSERTION`.
        Default value is :attr:`RevisionTextEffect.UNDERLINE`.
        
        Values of :attr:`RevisionTextEffect.HIDDEN` and :attr:`RevisionTextEffect.DOUBLE_STRIKE_THROUGH`
        are not allowed and will cause System.ArgumentOutOfRangeException.'''
        ...
    
    @inserted_text_effect.setter
    def inserted_text_effect(self, value: aspose.words.layout.RevisionTextEffect):
        ...
    
    @property
    def deleted_text_color(self) -> aspose.words.layout.RevisionColor:
        '''Allows to specify the color to be used for deleted content :attr:`aspose.words.RevisionType.DELETION`.
        Default value is :attr:`RevisionColor.BY_AUTHOR`.'''
        ...
    
    @deleted_text_color.setter
    def deleted_text_color(self, value: aspose.words.layout.RevisionColor):
        ...
    
    @property
    def deleted_text_effect(self) -> aspose.words.layout.RevisionTextEffect:
        '''Allows to specify the effect to be applied to the deleted content :attr:`aspose.words.RevisionType.DELETION`.
        Default value is :attr:`RevisionTextEffect.STRIKE_THROUGH`'''
        ...
    
    @deleted_text_effect.setter
    def deleted_text_effect(self, value: aspose.words.layout.RevisionTextEffect):
        ...
    
    @property
    def moved_from_text_color(self) -> aspose.words.layout.RevisionColor:
        '''Allows to specify the color to be used for areas where content was moved from :attr:`aspose.words.RevisionType.MOVING`.
        Default value is :attr:`RevisionColor.BY_AUTHOR`.'''
        ...
    
    @moved_from_text_color.setter
    def moved_from_text_color(self, value: aspose.words.layout.RevisionColor):
        ...
    
    @property
    def moved_from_text_effect(self) -> aspose.words.layout.RevisionTextEffect:
        '''Allows to specify the effect to be applied to the areas where content was moved from :attr:`aspose.words.RevisionType.MOVING`.
        Default value is :attr:`RevisionTextEffect.DOUBLE_STRIKE_THROUGH`'''
        ...
    
    @moved_from_text_effect.setter
    def moved_from_text_effect(self, value: aspose.words.layout.RevisionTextEffect):
        ...
    
    @property
    def moved_to_text_color(self) -> aspose.words.layout.RevisionColor:
        '''Allows to specify the color to be used for areas where content was moved to :attr:`aspose.words.RevisionType.MOVING`.
        Default value is :attr:`RevisionColor.BY_AUTHOR`.'''
        ...
    
    @moved_to_text_color.setter
    def moved_to_text_color(self, value: aspose.words.layout.RevisionColor):
        ...
    
    @property
    def moved_to_text_effect(self) -> aspose.words.layout.RevisionTextEffect:
        '''Allows to specify the effect to be applied to the areas where content was moved to :attr:`aspose.words.RevisionType.MOVING`.
        Default value is :attr:`RevisionTextEffect.DOUBLE_UNDERLINE`
        
        Values of :attr:`RevisionTextEffect.HIDDEN` and :attr:`RevisionTextEffect.DOUBLE_STRIKE_THROUGH`
        are not allowed and will cause System.ArgumentOutOfRangeException.'''
        ...
    
    @moved_to_text_effect.setter
    def moved_to_text_effect(self, value: aspose.words.layout.RevisionTextEffect):
        ...
    
    @property
    def revised_properties_color(self) -> aspose.words.layout.RevisionColor:
        '''Allows to specify the color to be used for content with changes of formatting properties :attr:`aspose.words.RevisionType.FORMAT_CHANGE`
        Default value is :attr:`RevisionColor.NO_HIGHLIGHT`.'''
        ...
    
    @revised_properties_color.setter
    def revised_properties_color(self, value: aspose.words.layout.RevisionColor):
        ...
    
    @property
    def revised_properties_effect(self) -> aspose.words.layout.RevisionTextEffect:
        '''Allows to specify the effect for content areas with changes of formatting properties :attr:`aspose.words.RevisionType.FORMAT_CHANGE`
        Default value is :attr:`RevisionTextEffect.NONE`
        
        :attr:`RevisionTextEffect.HIDDEN` is not allowed and will cause System.ArgumentOutOfRangeException.'''
        ...
    
    @revised_properties_effect.setter
    def revised_properties_effect(self, value: aspose.words.layout.RevisionTextEffect):
        ...
    
    @property
    def revision_bars_color(self) -> aspose.words.layout.RevisionColor:
        '''Allows to specify the color to be used for side bars that identify document lines containing revised information.
        Default value is :attr:`RevisionColor.RED`.
        
        Setting this property  to :attr:`RevisionColor.BY_AUTHOR` or :attr:`RevisionColor.NO_HIGHLIGHT` values
        will result in hiding revision bars from the layout.'''
        ...
    
    @revision_bars_color.setter
    def revision_bars_color(self, value: aspose.words.layout.RevisionColor):
        ...
    
    @property
    def revision_bars_width(self) -> float:
        '''Gets or sets width of revision bars, points.'''
        ...
    
    @revision_bars_width.setter
    def revision_bars_width(self, value: float):
        ...
    
    @property
    def revision_bars_position(self) -> aspose.words.drawing.HorizontalAlignment:
        '''Gets or sets rendering position of revision bars.
        Default value is :attr:`aspose.words.drawing.HorizontalAlignment.OUTSIDE`.
        
        Values of :attr:`aspose.words.drawing.HorizontalAlignment.CENTER` and :attr:`aspose.words.drawing.HorizontalAlignment.INSIDE`
        are not allowed and will cause System.ArgumentOutOfRangeException.'''
        ...
    
    @revision_bars_position.setter
    def revision_bars_position(self, value: aspose.words.drawing.HorizontalAlignment):
        ...
    
    @property
    def comment_color(self) -> aspose.words.layout.RevisionColor:
        '''Allows to specify the color to be used for comments.
        Default value is :attr:`RevisionColor.RED`.
        
        If set this property  to :attr:`RevisionColor.BY_AUTHOR` or :attr:`RevisionColor.NO_HIGHLIGHT` values,
        as the result this property will be set to default color.'''
        ...
    
    @comment_color.setter
    def comment_color(self, value: aspose.words.layout.RevisionColor):
        ...
    
    @property
    def show_in_balloons(self) -> aspose.words.layout.ShowInBalloons:
        '''Allows to specify whether the revisions are rendered in the balloons.
        Default value is :attr:`ShowInBalloons.NONE`.
        
        Note that revisions are not rendered in balloons for :attr:`CommentDisplayMode.SHOW_IN_ANNOTATIONS`.'''
        ...
    
    @show_in_balloons.setter
    def show_in_balloons(self, value: aspose.words.layout.ShowInBalloons):
        ...
    
    @property
    def measurement_unit(self) -> aspose.words.MeasurementUnits:
        '''Allows to specify the measurement units for revision comments.
        Default value is :attr:`aspose.words.MeasurementUnits.CENTIMETERS`'''
        ...
    
    @measurement_unit.setter
    def measurement_unit(self, value: aspose.words.MeasurementUnits):
        ...
    
    ...

class CommentDisplayMode:
    '''Specifies the rendering mode for document comments.'''
    
    HIDE: int
    SHOW_IN_BALLOONS: int
    SHOW_IN_ANNOTATIONS: int

class ContinuousSectionRestart:
    '''Represents different behaviors when computing page numbers in a continuous section that restarts page numbering.'''
    
    ALWAYS: int
    FROM_NEW_PAGE_ONLY: int

class LayoutEntityType:
    '''Types of the layout entities.'''
    
    NONE: int
    PAGE: int
    COLUMN: int
    ROW: int
    CELL: int
    LINE: int
    SPAN: int
    FOOTNOTE: int
    ENDNOTE: int
    NOTE: int
    HEADER_FOOTER: int
    TEXT_BOX: int
    COMMENT: int
    NOTE_SEPARATOR: int

class PageLayoutEvent:
    '''A code of event raised during page layout model build and rendering.
    
    Page layout model is built in two steps.
    First, "conversion step", this is when page layout pulls document content and creates object graph.
    Second, "reflow step", this is when structures are split, merged and arranged into pages.
    
    Depending of the operation which triggered build, page layout model may or may not be further rendered into fixed page format.
    For example, computing number of pages in the document or updating fields does not require rendering, whereas export to Pdf does.'''
    
    NONE: int
    WATCH_DOG: int
    BUILD_STARTED: int
    BUILD_FINISHED: int
    CONVERSION_STARTED: int
    CONVERSION_FINISHED: int
    REFLOW_STARTED: int
    REFLOW_FINISHED: int
    PART_REFLOW_STARTED: int
    PART_REFLOW_FINISHED: int
    PART_RENDERING_STARTED: int
    PART_RENDERING_FINISHED: int

class RevisionColor:
    '''Allows to specify color of document revisions.'''
    
    AUTO: int
    BLACK: int
    BLUE: int
    BRIGHT_GREEN: int
    CLASSIC_BLUE: int
    CLASSIC_RED: int
    DARK_BLUE: int
    DARK_RED: int
    DARK_YELLOW: int
    GRAY25: int
    GRAY50: int
    GREEN: int
    PINK: int
    RED: int
    TEAL: int
    TURQUOISE: int
    VIOLET: int
    WHITE: int
    YELLOW: int
    NO_HIGHLIGHT: int
    BY_AUTHOR: int

class RevisionTextEffect:
    '''Allows to specify decoration effect for revisions of document text.'''
    
    NONE: int
    COLOR: int
    BOLD: int
    ITALIC: int
    UNDERLINE: int
    DOUBLE_UNDERLINE: int
    STRIKE_THROUGH: int
    DOUBLE_STRIKE_THROUGH: int
    HIDDEN: int

class ShowInBalloons:
    '''Specifies which revisions are rendered in balloons.
    
    Note that revisions are not rendered in balloons for :attr:`CommentDisplayMode.SHOW_IN_ANNOTATIONS`.'''
    
    NONE: int
    FORMAT: int
    FORMAT_AND_DELETE: int

