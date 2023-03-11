import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class OfficeMath(aspose.words.CompositeNode):
    '''Represents an Office Math object such as function, equation, matrix or alike. Can contain child elements
    including runs of mathematical text, bookmarks, comments, other :class:`OfficeMath` instances and some other nodes.
    To learn more, visit the `Working with OfficeMath <https://docs.aspose.com/words/net/working-with-officemath/>` documentation article.
    
    In this version of Aspose.Words, :class:`OfficeMath` nodes do not provide public methods
    and properties to create or modify a :class:`OfficeMath` object. In this version you are not able to instantiate
    :mod:`aspose.words.math` nodes or modify existing except deleting them.
    
    :class:`OfficeMath` can only be a child of :class:`aspose.words.Paragraph`.'''
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        '''Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`aspose.words.DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`aspose.words.DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`aspose.words.DocumentVisitor.visit_office_math_start`, then calls :meth:`aspose.words.Node.accept` for all
        child nodes of the Office Math and calls :meth:`aspose.words.DocumentVisitor.visit_office_math_end` at the end.'''
        ...
    
    def get_math_renderer(self) -> aspose.words.rendering.OfficeMathRenderer:
        '''Creates and returns an object that can be used to render this equation into an image.
        
        This method just invokes the :class:`aspose.words.rendering.OfficeMathRenderer` constructor and passes
        this object as a parameter.
        
        :returns: The renderer object for this equation.'''
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        '''Returns :attr:`aspose.words.NodeType.OFFICE_MATH`.'''
        ...
    
    @property
    def parent_paragraph(self) -> aspose.words.Paragraph:
        '''Retrieves the parent :class:`aspose.words.Paragraph` of this node.'''
        ...
    
    @property
    def math_object_type(self) -> aspose.words.math.MathObjectType:
        '''Gets type :attr:`OfficeMath.math_object_type` of this Office Math object.'''
        ...
    
    @property
    def equation_xml_encoding(self) -> str:
        '''Gets/sets an encoding that was used to encode equation XML, if this office math object is read from
        equation XML.'''
        ...
    
    @equation_xml_encoding.setter
    def equation_xml_encoding(self, value: str):
        ...
    
    @property
    def justification(self) -> aspose.words.math.OfficeMathJustification:
        '''Gets/sets Office Math justification.
        
        Justification cannot be set to the Office Math with display format type :attr:`OfficeMathDisplayType.INLINE`.
        
        Inline justification cannot be set to the Office Math with display format type :attr:`OfficeMathDisplayType.DISPLAY`.
        
        Corresponding :attr:`OfficeMath.display_type` has to be set before setting Office Math justification.'''
        ...
    
    @justification.setter
    def justification(self, value: aspose.words.math.OfficeMathJustification):
        ...
    
    @property
    def display_type(self) -> aspose.words.math.OfficeMathDisplayType:
        '''Gets/sets Office Math display format type which represents whether an equation is displayed inline with the text
        or displayed on its own line.
        
        Display format type has effect for top level Office Math only.
        
        Returned display format type is always :attr:`OfficeMathDisplayType.INLINE` for nested Office Math.'''
        ...
    
    @display_type.setter
    def display_type(self, value: aspose.words.math.OfficeMathDisplayType):
        ...
    
    ...

class MathObjectType:
    '''Specifies type of an Office Math object.'''
    
    O_MATH: int
    O_MATH_PARA: int
    ACCENT: int
    BAR: int
    BORDER_BOX: int
    BOX: int
    DELIMITER: int
    DEGREE: int
    ARGUMENT: int
    ARRAY: int
    FRACTION: int
    DENOMINATOR: int
    NUMERATOR: int
    FUNCTION: int
    FUNCTION_NAME: int
    GROUP_CHARACTER: int
    LIMIT: int
    LOWER_LIMIT: int
    UPPER_LIMIT: int
    MATRIX: int
    MATRIX_ROW: int
    N_ARY: int
    PHANTOM: int
    RADICAL: int
    SUBSCRIPT_PART: int
    SUPERSCRIPT_PART: int
    PRE_SUB_SUPERSCRIPT: int
    SUBSCRIPT: int
    SUB_SUPERSCRIPT: int
    SUPERCRIPT: int

class OfficeMathDisplayType:
    '''Specifies the display format type of the equation.'''
    
    DISPLAY: int
    INLINE: int

class OfficeMathJustification:
    '''Specifies the justification of the equation.'''
    
    CENTER_GROUP: int
    CENTER: int
    LEFT: int
    RIGHT: int
    INLINE: int
    DEFAULT: int

