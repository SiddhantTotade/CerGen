import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class Cell(aspose.words.CompositeNode):
    '''Represents a table cell.
    To learn more, visit the `Working with Tables <https://docs.aspose.com/words/net/working-with-tables/>` documentation article.
    
    :class:`Cell` can only be a child of a :class:`Row`.
    
    :class:`Cell` can contain block-level nodes :class:`aspose.words.Paragraph` and :class:`Table`.
    
    A minimal valid cell needs to have at least one :class:`aspose.words.Paragraph`.'''
    
    def __init__(self, doc: aspose.words.DocumentBase):
        '''Initializes a new instance of the :class:`Cell` class.
        
        When :class:`Cell` is created, it belongs to the specified document, but is not
        yet part of the document and :attr:`aspose.words.Node.parent_node` is ``None``.
        
        To append :class:`Cell` to the document use :meth:`aspose.words.CompositeNode.insert_after` or :meth:`aspose.words.CompositeNode.insert_before`
        on the row where you want the cell inserted.
        
        :param doc: The owner document.'''
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        '''Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`aspose.words.DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`aspose.words.DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`aspose.words.DocumentVisitor.visit_cell_start`, then calls :meth:`aspose.words.Node.accept` for all child nodes of the section
        and calls :meth:`aspose.words.DocumentVisitor.visit_cell_end` at the end.'''
        ...
    
    def ensure_minimum(self) -> None:
        '''If the last child is not a paragraph, creates and appends one empty paragraph.'''
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        '''Returns :attr:`aspose.words.NodeType.CELL`.'''
        ...
    
    @property
    def parent_row(self) -> aspose.words.tables.Row:
        '''Returns the parent row of the cell.
        
        Equivalent to Aspose.Words.Node.FirstNonMarkupParentNode casted to :class:`Row`.'''
        ...
    
    @property
    def first_paragraph(self) -> aspose.words.Paragraph:
        '''Gets the first paragraph among the immediate children.'''
        ...
    
    @property
    def last_paragraph(self) -> aspose.words.Paragraph:
        '''Gets the last paragraph among the immediate children.'''
        ...
    
    @property
    def is_first_cell(self) -> bool:
        '''True if this is the first cell inside a row; false otherwise.'''
        ...
    
    @property
    def is_last_cell(self) -> bool:
        '''True if this is the last cell inside a row; false otherwise.'''
        ...
    
    @property
    def cell_format(self) -> aspose.words.tables.CellFormat:
        '''Provides access to the formatting properties of the cell.'''
        ...
    
    @property
    def paragraphs(self) -> aspose.words.ParagraphCollection:
        '''Gets a collection of paragraphs that are immediate children of the cell.'''
        ...
    
    @property
    def tables(self) -> aspose.words.tables.TableCollection:
        '''Gets a collection of tables that are immediate children of the cell.'''
        ...
    
    ...

class CellCollection(aspose.words.NodeCollection):
    '''Provides typed access to a collection of :class:`Cell` nodes.
    To learn more, visit the `Working with Tables <https://docs.aspose.com/words/net/working-with-tables/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.tables.Cell:
        '''Retrieves a :class:`Cell` at the given index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the collection.'''
        ...
    
    def to_array(self) -> list[aspose.words.tables.Cell]:
        '''Copies all cells from the collection to a new array of cells.
        
        :returns: An array of cells.'''
        ...
    
    ...

class CellFormat:
    '''Represents all formatting for a table cell.
    To learn more, visit the `Working with Tables <https://docs.aspose.com/words/net/working-with-tables/>` documentation article.'''
    
    def clear_formatting(self) -> None:
        '''Resets to default cell formatting. Does not change the width of the cell.'''
        ...
    
    def set_paddings(self, left_padding: float, top_padding: float, right_padding: float, bottom_padding: float) -> None:
        '''Sets the amount of space (in points) to add to the left/top/right/bottom of the contents of cell.'''
        ...
    
    @property
    def left_padding(self) -> float:
        '''Returns or sets the amount of space (in points) to add to the left of the contents of cell.'''
        ...
    
    @left_padding.setter
    def left_padding(self, value: float):
        ...
    
    @property
    def right_padding(self) -> float:
        '''Returns or sets the amount of space (in points) to add to the right of the contents of cell.'''
        ...
    
    @right_padding.setter
    def right_padding(self, value: float):
        ...
    
    @property
    def top_padding(self) -> float:
        '''Returns or sets the amount of space (in points) to add above the contents of cell.'''
        ...
    
    @top_padding.setter
    def top_padding(self, value: float):
        ...
    
    @property
    def bottom_padding(self) -> float:
        '''Returns or sets the amount of space (in points) to add below the contents of cell.'''
        ...
    
    @bottom_padding.setter
    def bottom_padding(self, value: float):
        ...
    
    @property
    def borders(self) -> aspose.words.BorderCollection:
        '''Gets collection of borders of the cell.'''
        ...
    
    @property
    def shading(self) -> aspose.words.Shading:
        '''Returns a :class:`aspose.words.Shading` object that refers to the shading formatting for the cell.'''
        ...
    
    @property
    def vertical_alignment(self) -> aspose.words.tables.CellVerticalAlignment:
        '''Returns or sets the vertical alignment of text in the cell.'''
        ...
    
    @vertical_alignment.setter
    def vertical_alignment(self, value: aspose.words.tables.CellVerticalAlignment):
        ...
    
    @property
    def width(self) -> float:
        '''Gets the width of the cell in points.
        
        The width is calculated by Aspose.Words on document loading and saving.
        Currently, not every combination of table, cell and document properties is supported.
        The returned value may not be accurate for some documents.
        It may not exactly match the cell width as calculated by MS Word when the document is opened in MS Word.
        
        Setting this property is not recommended.
        There is no guarantee that the cell will actually have the set width.
        The width may be adjusted to accommodate cell contents in an auto-fit table layout.
        Cells in other rows may have conflicting width settings.
        The table may be resized to fit into the container or to meet table width settings.
        Consider using :attr:`CellFormat.preferred_width` for setting the cell width.
        Setting this property sets :attr:`CellFormat.preferred_width` implicitly since version 15.8.'''
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def preferred_width(self) -> aspose.words.tables.PreferredWidth:
        '''Returns or sets the preferred width of the cell.
        
        The preferred width (along with the table's Auto Fit option) determines how the actual
        width of the cell is calculated by the table layout algorithm. Table layout can be performed by
        Aspose.Words when it saves the document or by Microsoft Word when it displays the document.
        
        The preferred width can be specified in points or in percent. The preferred width
        can also be specified as "auto", which means no preferred width is specified.
        
        The default value is :attr:`PreferredWidth.AUTO`.'''
        ...
    
    @preferred_width.setter
    def preferred_width(self, value: aspose.words.tables.PreferredWidth):
        ...
    
    @property
    def vertical_merge(self) -> aspose.words.tables.CellMerge:
        '''Specifies how the cell is merged with other cells vertically.
        
        Cells can only be merged vertically if their left and right boundaries are identical.
        
        When cells are vertically merged, the display areas of the merged cells are consolidated.
        The consolidated area is used to display the contents of the first vertically merged cell
        and all other vertically merged cells must be empty.'''
        ...
    
    @vertical_merge.setter
    def vertical_merge(self, value: aspose.words.tables.CellMerge):
        ...
    
    @property
    def horizontal_merge(self) -> aspose.words.tables.CellMerge:
        '''Specifies how the cell is merged horizontally with other cells in the row.'''
        ...
    
    @horizontal_merge.setter
    def horizontal_merge(self, value: aspose.words.tables.CellMerge):
        ...
    
    @property
    def orientation(self) -> aspose.words.TextOrientation:
        '''Returns or sets the orientation of text in a table cell.'''
        ...
    
    @orientation.setter
    def orientation(self, value: aspose.words.TextOrientation):
        ...
    
    @property
    def fit_text(self) -> bool:
        '''If ``True``, fits text in the cell, compressing each paragraph to the width of the cell.'''
        ...
    
    @fit_text.setter
    def fit_text(self, value: bool):
        ...
    
    @property
    def wrap_text(self) -> bool:
        '''If ``True``, wrap text for the cell.'''
        ...
    
    @wrap_text.setter
    def wrap_text(self, value: bool):
        ...
    
    ...

class PreferredWidth:
    '''Represents a value and its unit of measure that is used to specify the preferred width of a table or a cell.
    To learn more, visit the `Working with Tables <https://docs.aspose.com/words/net/working-with-tables/>` documentation article.
    
    Preferred width can be specified as a percentage, number of points or a special "none/auto" value.
    
    The instances of this class are immutable.'''
    
    @staticmethod
    def from_percent(self, percent: float) -> aspose.words.tables.PreferredWidth:
        '''A creation method that returns a new instance that represents a preferred width specified as a percentage.
        
        :param percent: The value must be from 0 to 100.'''
        ...
    
    @staticmethod
    def from_points(self, points: float) -> aspose.words.tables.PreferredWidth:
        '''A creation method that returns a new instance that represents a preferred width specified using a number of points.
        
        :param points: The value must be from 0 to 22 inches (22 \* 72 points).'''
        ...
    
    def equals(self, other: aspose.words.tables.PreferredWidth) -> bool:
        '''Determines whether the specified :class:`PreferredWidth` is equal in value to the current :class:`PreferredWidth`.'''
        ...
    
    @property
    def type(self) -> aspose.words.tables.PreferredWidthType:
        '''Gets the unit of measure used for this preferred width value.'''
        ...
    
    @property
    def value(self) -> float:
        '''Gets the preferred width value. The unit of measure is specified in the :attr:`PreferredWidth.type` property.'''
        ...
    
    AUTO: aspose.words.tables.PreferredWidth
    
    ...

class Row(aspose.words.CompositeNode):
    '''Represents a table row.
    To learn more, visit the `Working with Tables <https://docs.aspose.com/words/net/working-with-tables/>` documentation article.
    
    :class:`Row` can only be a child of a :class:`Table`.
    
    :class:`Row` can contain one or more :class:`Cell` nodes.
    
    A minimal valid row needs to have at least one :class:`Cell`.'''
    
    def __init__(self, doc: aspose.words.DocumentBase):
        '''Initializes a new instance of the :class:`Row` class.
        
        When :class:`Row` is created, it belongs to the specified document, but is not
        yet part of the document and :attr:`aspose.words.Node.parent_node` is ``None``.
        
        To append :class:`Row` to the document use :meth:`aspose.words.CompositeNode.insert_after` or :meth:`aspose.words.CompositeNode.insert_before`
        on the table where you want the row inserted.
        
        :param doc: The owner document.'''
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        '''Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`aspose.words.DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`aspose.words.DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`aspose.words.DocumentVisitor.visit_row_start`, then calls :meth:`aspose.words.Node.accept` for all child nodes of the section
        and calls :meth:`aspose.words.DocumentVisitor.visit_row_end` at the end.'''
        ...
    
    def get_text(self) -> str:
        '''Gets the text of all cells in this row including the end of row character.
        
        Returns concatenated text of all child nodes with the end of row character
        :attr:`aspose.words.ControlChar.CELL` appended at the end.
        
        The returned string includes all control and special characters as described in :class:`aspose.words.ControlChar`.'''
        ...
    
    def ensure_minimum(self) -> None:
        '''If the :class:`Row` has no cells, creates and appends one :class:`Cell`.'''
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        '''Returns :attr:`aspose.words.NodeType.ROW`.'''
        ...
    
    @property
    def parent_table(self) -> aspose.words.tables.Table:
        '''Returns the immediate parent table of the row.
        
        Equivalent to Aspose.Words.Node.FirstNonMarkupParentNode casted to :class:`Table`.'''
        ...
    
    @property
    def is_first_row(self) -> bool:
        '''True if this is the first row in a table; false otherwise.'''
        ...
    
    @property
    def is_last_row(self) -> bool:
        '''True if this is the last row in a table; false otherwise.'''
        ...
    
    @property
    def first_cell(self) -> aspose.words.tables.Cell:
        '''Returns the first :class:`Cell` in the row.'''
        ...
    
    @property
    def last_cell(self) -> aspose.words.tables.Cell:
        '''Returns the last :class:`Cell` in the row.'''
        ...
    
    @property
    def cells(self) -> aspose.words.tables.CellCollection:
        '''Provides typed access to the :class:`Cell` child nodes of the row.'''
        ...
    
    @property
    def row_format(self) -> aspose.words.tables.RowFormat:
        '''Provides access to the formatting properties of the row.'''
        ...
    
    ...

class RowCollection(aspose.words.NodeCollection):
    '''Provides typed access to a collection of :class:`Row` nodes.
    To learn more, visit the `Working with Tables <https://docs.aspose.com/words/net/working-with-tables/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.tables.Row:
        '''Retrieves a :class:`Row` at the given index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the collection.'''
        ...
    
    def to_array(self) -> list[aspose.words.tables.Row]:
        '''Copies all rows from the collection to a new array of rows.
        
        :returns: An array of rows.'''
        ...
    
    ...

class RowFormat:
    '''Represents all formatting for a table row.
    To learn more, visit the `Working with Tables <https://docs.aspose.com/words/net/working-with-tables/>` documentation article.'''
    
    def clear_formatting(self) -> None:
        '''Resets to default row formatting.'''
        ...
    
    @property
    def borders(self) -> aspose.words.BorderCollection:
        '''Gets the collection of default cell borders for the row.'''
        ...
    
    @property
    def height(self) -> float:
        '''Gets or sets the height of the table row in points.'''
        ...
    
    @height.setter
    def height(self, value: float):
        ...
    
    @property
    def height_rule(self) -> aspose.words.HeightRule:
        '''Gets or sets the rule for determining the height of the table row.'''
        ...
    
    @height_rule.setter
    def height_rule(self, value: aspose.words.HeightRule):
        ...
    
    @property
    def allow_break_across_pages(self) -> bool:
        '''True if the text in a table row is allowed to split across a page break.'''
        ...
    
    @allow_break_across_pages.setter
    def allow_break_across_pages(self, value: bool):
        ...
    
    @property
    def heading_format(self) -> bool:
        '''True if the row is repeated as a table heading on every page when the table spans more than one page.'''
        ...
    
    @heading_format.setter
    def heading_format(self, value: bool):
        ...
    
    ...

class Table(aspose.words.CompositeNode):
    '''Represents a table in a Word document.
    To learn more, visit the `Working with Tables <https://docs.aspose.com/words/net/working-with-tables/>` documentation article.
    
    :class:`Table` is a block-level node and can be a child of classes derived from :class:`aspose.words.Story` or
    :class:`aspose.words.InlineStory`.
    
    :class:`Table` can contain one or more :class:`Row` nodes.
    
    A minimal valid table needs to have at least one :class:`Row`.'''
    
    def __init__(self, doc: aspose.words.DocumentBase):
        '''Initializes a new instance of the :class:`Table` class.
        
        When :class:`Table` is created, it belongs to the specified document, but is not
        yet part of the document and :attr:`aspose.words.Node.parent_node` is ``None``.
        
        To append :class:`Table` to the document use :meth:`aspose.words.CompositeNode.insert_after` or :meth:`aspose.words.CompositeNode.insert_before`
        on the story where you want the table inserted.
        
        :param doc: The owner document.'''
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        '''Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`aspose.words.DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`aspose.words.DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`aspose.words.DocumentVisitor.visit_table_start`, then calls :meth:`aspose.words.Node.accept` for all child nodes of the section
        and calls :meth:`aspose.words.DocumentVisitor.visit_table_end` at the end.'''
        ...
    
    def convert_to_horizontally_merged_cells(self) -> None:
        '''Converts cells horizontally merged by width to cells merged by :attr:`CellFormat.horizontal_merge`.
        
        Table cells can be horizontally merged either using merge flags :attr:`CellFormat.horizontal_merge` or using cell width :attr:`CellFormat.width`.
        
        When table cell is merged by width property :attr:`CellFormat.horizontal_merge` is meaningless but sometimes having merge flags is more convenient way.
        
        Use this method to transforms table cells horizontally merged by width to cells merged by merge flags.'''
        ...
    
    def ensure_minimum(self) -> None:
        '''If the table has no rows, creates and appends one :class:`Row`.'''
        ...
    
    def set_borders(self, line_style: aspose.words.LineStyle, line_width: float, color: aspose.pydrawing.Color) -> None:
        '''Sets all table borders to the specified line style, width and color.
        
        :param line_style: The line style to apply.
        :param line_width: The line width to set (in points).
        :param color: The color to use for the border.'''
        ...
    
    def set_border(self, border_type: aspose.words.BorderType, line_style: aspose.words.LineStyle, line_width: float, color: aspose.pydrawing.Color, is_override_cell_borders: bool) -> None:
        '''Sets the specified table border to the specified line style, width and color.
        
        :param border_type: The table border to change.
        :param line_style: The line style to apply.
        :param line_width: The line width to set (in points).
        :param color: The color to use for the border.
        :param is_override_cell_borders: When ``True``, causes all existing explicit cell borders to be removed.'''
        ...
    
    def clear_borders(self) -> None:
        '''Removes all table and cell borders on this table.'''
        ...
    
    def set_shading(self, texture: aspose.words.TextureIndex, foreground_color: aspose.pydrawing.Color, background_color: aspose.pydrawing.Color) -> None:
        '''Sets shading to the specified values on whole table.
        
        :param texture: The texture to apply.
        :param foreground_color: The color of the texture.
        :param background_color: The color of the background fill.'''
        ...
    
    def clear_shading(self) -> None:
        '''Removes all shading on the table.'''
        ...
    
    def auto_fit(self, behavior: aspose.words.tables.AutoFitBehavior) -> None:
        '''Resizes the table and cells according to the specified auto fit behavior.
        
        This method mimics the commands available in the Auto Fit menu for a table in Microsoft Word.
        The commands available are "Auto Fit to Contents", "Auto Fit to Window" and "Fixed Column Width". In Microsoft Word
        these commands set relevant table properties and then update the table layout and Aspose.Words does the same for you.
        
        :param behavior: Specifies how to auto fit the table.'''
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        '''Returns :attr:`aspose.words.NodeType.TABLE`.'''
        ...
    
    @property
    def first_row(self) -> aspose.words.tables.Row:
        '''Returns the first :class:`Row` node in the table.'''
        ...
    
    @property
    def last_row(self) -> aspose.words.tables.Row:
        '''Returns the last :class:`Row` node in the table.'''
        ...
    
    @property
    def rows(self) -> aspose.words.tables.RowCollection:
        '''Provides typed access to the rows of the table.'''
        ...
    
    @property
    def alignment(self) -> aspose.words.tables.TableAlignment:
        '''Specifies how an inline table is aligned in the document.
        
        The default value is :attr:`TableAlignment.LEFT`.'''
        ...
    
    @alignment.setter
    def alignment(self, value: aspose.words.tables.TableAlignment):
        ...
    
    @property
    def allow_auto_fit(self) -> bool:
        '''Allows Microsoft Word and Aspose.Words to automatically resize cells in a table to fit their contents.
        
        The default value is ``True``.'''
        ...
    
    @allow_auto_fit.setter
    def allow_auto_fit(self, value: bool):
        ...
    
    @property
    def preferred_width(self) -> aspose.words.tables.PreferredWidth:
        '''Gets or sets the table preferred width.
        
        The default value is :attr:`PreferredWidth.AUTO`.'''
        ...
    
    @preferred_width.setter
    def preferred_width(self, value: aspose.words.tables.PreferredWidth):
        ...
    
    @property
    def bidi(self) -> bool:
        '''Gets or sets whether this is a right-to-left table.
        
        When ``True``, the cells in this row are laid out right to left.
        
        The default value is ``False``.'''
        ...
    
    @bidi.setter
    def bidi(self, value: bool):
        ...
    
    @property
    def left_padding(self) -> float:
        '''Gets or sets the amount of space (in points) to add to the left of the contents of cells.'''
        ...
    
    @left_padding.setter
    def left_padding(self, value: float):
        ...
    
    @property
    def right_padding(self) -> float:
        '''Gets or sets the amount of space (in points) to add to the right of the contents of cells.'''
        ...
    
    @right_padding.setter
    def right_padding(self, value: float):
        ...
    
    @property
    def top_padding(self) -> float:
        '''Gets or sets the amount of space (in points) to add above the contents of cells.'''
        ...
    
    @top_padding.setter
    def top_padding(self, value: float):
        ...
    
    @property
    def bottom_padding(self) -> float:
        '''Gets or sets the amount of space (in points) to add below the contents of cells.'''
        ...
    
    @bottom_padding.setter
    def bottom_padding(self, value: float):
        ...
    
    @property
    def cell_spacing(self) -> float:
        '''Gets or sets the amount of space (in points) between the cells.'''
        ...
    
    @cell_spacing.setter
    def cell_spacing(self, value: float):
        ...
    
    @property
    def allow_cell_spacing(self) -> bool:
        '''Gets or sets the "Allow spacing between cells" option.'''
        ...
    
    @allow_cell_spacing.setter
    def allow_cell_spacing(self, value: bool):
        ...
    
    @property
    def left_indent(self) -> float:
        '''Gets or sets the value that represents the left indent of the table.'''
        ...
    
    @left_indent.setter
    def left_indent(self, value: float):
        ...
    
    @property
    def style_options(self) -> aspose.words.tables.TableStyleOptions:
        '''Gets or sets bit flags that specify how a table style is applied to this table.'''
        ...
    
    @style_options.setter
    def style_options(self, value: aspose.words.tables.TableStyleOptions):
        ...
    
    @property
    def style(self) -> aspose.words.Style:
        '''Gets or sets the table style applied to this table.'''
        ...
    
    @style.setter
    def style(self, value: aspose.words.Style):
        ...
    
    @property
    def style_name(self) -> str:
        '''Gets or sets the name of the table style applied to this table.'''
        ...
    
    @style_name.setter
    def style_name(self, value: str):
        ...
    
    @property
    def style_identifier(self) -> aspose.words.StyleIdentifier:
        '''Gets or sets the locale independent style identifier of the table style applied to this table.'''
        ...
    
    @style_identifier.setter
    def style_identifier(self, value: aspose.words.StyleIdentifier):
        ...
    
    @property
    def text_wrapping(self) -> aspose.words.tables.TextWrapping:
        '''Gets or sets :attr:`Table.text_wrapping` for table.'''
        ...
    
    @text_wrapping.setter
    def text_wrapping(self, value: aspose.words.tables.TextWrapping):
        ...
    
    @property
    def title(self) -> str:
        '''Gets or sets title of this table.
        It provides an alternative text representation of the information contained in the table.
        
        The default value is an empty string.
        
        This property is meaningful for ISO/IEC 29500 compliant DOCX documents
        (:class:`aspose.words.saving.OoxmlCompliance`).
        When saved to pre-ISO/IEC 29500 formats, the property is ignored.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...
    
    @property
    def description(self) -> str:
        '''Gets or sets description of this table.
        It provides an alternative text representation of the information contained in the table.
        
        The default value is an empty string.
        
        This property is meaningful for ISO/IEC 29500 compliant DOCX documents
        (:class:`aspose.words.saving.OoxmlCompliance`).
        When saved to pre-ISO/IEC 29500 formats, the property is ignored.'''
        ...
    
    @description.setter
    def description(self, value: str):
        ...
    
    @property
    def distance_left(self) -> float:
        '''Gets distance between table left and the surrounding text, in points.'''
        ...
    
    @property
    def distance_right(self) -> float:
        '''Gets distance between table right and the surrounding text, in points.'''
        ...
    
    @property
    def distance_top(self) -> float:
        '''Gets distance between table top and the surrounding text, in points.'''
        ...
    
    @property
    def distance_bottom(self) -> float:
        '''Gets distance between table bottom and the surrounding text, in points.'''
        ...
    
    @property
    def relative_horizontal_alignment(self) -> aspose.words.drawing.HorizontalAlignment:
        '''Gets or sets floating table relative horizontal alignment.'''
        ...
    
    @relative_horizontal_alignment.setter
    def relative_horizontal_alignment(self, value: aspose.words.drawing.HorizontalAlignment):
        ...
    
    @property
    def relative_vertical_alignment(self) -> aspose.words.drawing.VerticalAlignment:
        '''Gets or sets floating table relative vertical alignment.'''
        ...
    
    @relative_vertical_alignment.setter
    def relative_vertical_alignment(self, value: aspose.words.drawing.VerticalAlignment):
        ...
    
    @property
    def horizontal_anchor(self) -> aspose.words.drawing.RelativeHorizontalPosition:
        '''Gets the base object from which the horizontal positioning of floating table should be calculated.
        Default value is :attr:`aspose.words.drawing.RelativeHorizontalPosition.COLUMN`.'''
        ...
    
    @horizontal_anchor.setter
    def horizontal_anchor(self, value: aspose.words.drawing.RelativeHorizontalPosition):
        ...
    
    @property
    def vertical_anchor(self) -> aspose.words.drawing.RelativeVerticalPosition:
        '''Gets the base object from which the vertical positioning of floating table should be calculated.
        Default value is :attr:`aspose.words.drawing.RelativeVerticalPosition.MARGIN`.'''
        ...
    
    @vertical_anchor.setter
    def vertical_anchor(self, value: aspose.words.drawing.RelativeVerticalPosition):
        ...
    
    @property
    def absolute_horizontal_distance(self) -> float:
        '''Gets or sets absolute horizontal floating table position specified by the table properties, in points.
        Default value is 0.'''
        ...
    
    @absolute_horizontal_distance.setter
    def absolute_horizontal_distance(self, value: float):
        ...
    
    @property
    def absolute_vertical_distance(self) -> float:
        '''Gets or sets absolute vertical floating table position specified by the table properties, in points.
        Default value is 0.'''
        ...
    
    @absolute_vertical_distance.setter
    def absolute_vertical_distance(self, value: float):
        ...
    
    @property
    def allow_overlap(self) -> bool:
        '''Gets whether a floating table shall allow other floating objects in the document
        to overlap its extents when displayed.
        Default value is ``True``.'''
        ...
    
    ...

class TableCollection(aspose.words.NodeCollection):
    '''Provides typed access to a collection of :class:`Table` nodes.
    To learn more, visit the `Working with Tables <https://docs.aspose.com/words/net/working-with-tables/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.tables.Table:
        '''Retrieves a :class:`Table` at the given index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the collection.'''
        ...
    
    def to_array(self) -> list[aspose.words.tables.Table]:
        '''Copies all tables from the collection to a new array of tables.
        
        :returns: An array of tables.'''
        ...
    
    ...

class AutoFitBehavior:
    '''Determines how Aspose.Words resizes the table when you invoke the :meth:`Table.auto_fit` method.'''
    
    AUTO_FIT_TO_CONTENTS: int
    AUTO_FIT_TO_WINDOW: int
    FIXED_COLUMN_WIDTHS: int

class CellMerge:
    '''Specifies how a cell in a table is merged with other cells.'''
    
    NONE: int
    FIRST: int
    PREVIOUS: int

class CellVerticalAlignment:
    '''Specifies vertical justification of text inside a table cell.'''
    
    TOP: int
    CENTER: int
    BOTTOM: int

class PreferredWidthType:
    '''Specifies the unit of measurement for the preferred width of a table or cell.'''
    
    AUTO: int
    PERCENT: int
    POINTS: int

class TableAlignment:
    '''Specifies alignment for an inline table.'''
    
    LEFT: int
    CENTER: int
    RIGHT: int

class TableStyleOptions:
    '''Specifies how table style is applied to a table.'''
    
    NONE: int
    FIRST_ROW: int
    LAST_ROW: int
    FIRST_COLUMN: int
    LAST_COLUMN: int
    ROW_BANDS: int
    COLUMN_BANDS: int
    DEFAULT2003: int
    DEFAULT: int

class TextWrapping:
    '''Specifies how text is wrapped around the table.'''
    
    NONE: int
    AROUND: int
    DEFAULT: int

