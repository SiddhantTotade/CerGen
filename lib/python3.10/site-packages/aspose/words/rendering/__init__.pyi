import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class NodeRendererBase:
    '''Base class for :class:`ShapeRenderer` and :class:`OfficeMathRenderer`.
    To learn more, visit the `Working with Shapes <https://docs.aspose.com/words/net/working-with-shapes/>` documentation article.'''
    
    @overload
    def get_size_in_pixels(self, scale: float, dpi: float) -> aspose.pydrawing.Size:
        '''Calculates the size of the shape in pixels for a specified zoom factor and resolution.
        
        This method converts :attr:`NodeRendererBase.size_in_points` into size in pixels and it is useful
        when you want to create a bitmap for rendering the shape neatly onto the bitmap.
        
        :param scale: The zoom factor (1.0 is 100%).
        :param dpi: The resolution (horizontal and vertical) to convert from points to pixels (dots per inch).
        :returns: The size of the shape in pixels.'''
        ...
    
    @overload
    def get_size_in_pixels(self, scale: float, horizontal_dpi: float, vertical_dpi: float) -> aspose.pydrawing.Size:
        '''Calculates the size of the shape in pixels for a specified zoom factor and resolution.
        
        This method converts :attr:`NodeRendererBase.size_in_points` into size in pixels and it is useful
        when you want to create a bitmap for rendering the shape neatly onto the bitmap.
        
        :param scale: The zoom factor (1.0 is 100%).
        :param horizontal_dpi: The horizontal resolution to convert from points to pixels (dots per inch).
        :param vertical_dpi: The vertical resolution to convert from points to pixels (dots per inch).
        :returns: The size of the shape in pixels.'''
        ...
    
    @overload
    def get_bounds_in_pixels(self, scale: float, dpi: float) -> aspose.pydrawing.Rectangle:
        '''Calculates the bounds of the shape in pixels for a specified zoom factor and resolution.
        
        This method converts :attr:`NodeRendererBase.bounds_in_points` into rectangle in pixels.
        
        :param scale: The zoom factor (1.0 is 100%).
        :param dpi: The resolution (horizontal and vertical) to convert from points to pixels (dots per inch).
        :returns: The actual (as rendered on the page) bounding box of the shape in pixels.'''
        ...
    
    @overload
    def get_bounds_in_pixels(self, scale: float, horizontal_dpi: float, vertical_dpi: float) -> aspose.pydrawing.Rectangle:
        '''Calculates the bounds of the shape in pixels for a specified zoom factor and resolution.
        
        This method converts :attr:`NodeRendererBase.bounds_in_points` into rectangle in pixels.
        
        :param scale: The zoom factor (1.0 is 100%).
        :param horizontal_dpi: The horizontal resolution to convert from points to pixels (dots per inch).
        :param vertical_dpi: The vertical resolution to convert from points to pixels (dots per inch).
        :returns: The actual (as rendered on the page) bounding box of the shape in pixels.'''
        ...
    
    @overload
    def get_opaque_bounds_in_pixels(self, scale: float, dpi: float) -> aspose.pydrawing.Rectangle:
        '''Calculates the opaque bounds of the shape in pixels for a specified zoom factor and resolution.
        
        This method converts :attr:`NodeRendererBase.opaque_bounds_in_points` into rectangle in pixels and it is useful
        when you want to create a bitmap for rendering the shape with only opaque part of the shape.
        
        :param scale: The zoom factor (1.0 is 100%).
        :param dpi: The resolution to convert from points to pixels (dots per inch).
        :returns: The opaque rectangle of the shape in pixels.'''
        ...
    
    @overload
    def get_opaque_bounds_in_pixels(self, scale: float, horizontal_dpi: float, vertical_dpi: float) -> aspose.pydrawing.Rectangle:
        '''Calculates the opaque bounds of the shape in pixels for a specified zoom factor and resolution.
        
        This method converts :attr:`NodeRendererBase.opaque_bounds_in_points` into rectangle in pixels and it is useful
        when you want to create a bitmap for rendering the shape with only opaque part of the shape.
        
        :param scale: The zoom factor (1.0 is 100%).
        :param horizontal_dpi: The horizontal resolution to convert from points to pixels (dots per inch).
        :param vertical_dpi: The vertical resolution to convert from points to pixels (dots per inch).
        :returns: The opaque rectangle of the shape in pixels.'''
        ...
    
    @overload
    def save(self, file_name: str, save_options: aspose.words.saving.ImageSaveOptions) -> None:
        '''Renders the shape into an image and saves into a file.
        
        :param file_name: The name for the image file. If a file with the specified name already exists, the existing file is overwritten.
        :param save_options: Specifies the options that control how the shape is rendered and saved. Can be ``None``.'''
        ...
    
    @overload
    def save(self, stream: io.BytesIO, save_options: aspose.words.saving.ImageSaveOptions) -> None:
        '''Renders the shape into an image and saves into a stream.
        
        :param stream: The stream where to save the image of the shape.
        :param save_options: Specifies the options that control how the shape is rendered and saved. Can be ``None``.
                             If this is ``None``, the image will be saved in the PNG format.'''
        ...
    
    @property
    def size_in_points(self) -> aspose.pydrawing.SizeF:
        '''Gets the actual size of the shape in points.
        
        This property returns the size of the actual (as rendered on the page) bounding box of the shape.
        The size takes into account shape rotation (if any).'''
        ...
    
    @property
    def bounds_in_points(self) -> aspose.pydrawing.RectangleF:
        '''Gets the actual bounds of the shape in points.
        
        This property returns the actual (as rendered on the page) bounding box of the shape.
        The bounds takes into account shape rotation (if any).'''
        ...
    
    @property
    def opaque_bounds_in_points(self) -> aspose.pydrawing.RectangleF:
        '''Gets the opaque bounds of the shape in points.
        
        This property returns the opaque (i.e. transparent parts of the shape are ignored) bounding box of the shape.
        The bounds takes the shape rotation into account.'''
        ...
    
    ...

class OfficeMathRenderer(aspose.words.rendering.NodeRendererBase):
    '''Provides methods to render an individual :class:`aspose.words.math.OfficeMath`
    to a raster or vector image or to a Graphics object.
    To learn more, visit the `Working with OfficeMath <https://docs.aspose.com/words/net/working-with-officemath/>` documentation article.'''
    
    def __init__(self, math: aspose.words.math.OfficeMath):
        '''Initializes a new instance of this class.
        
        :param math: The :class:`aspose.words.math.OfficeMath` object that you want to render.'''
        ...
    
    ...

class PageInfo:
    '''Represents information about a particular document page.
    To learn more, visit the `Rendering <https://docs.aspose.com/words/net/rendering/>` documentation article.
    
    The page width and height returned by this object represent the "final" size of the page e.g. they are
    already rotated to the correct orientation.'''
    
    @overload
    def get_size_in_pixels(self, scale: float, dpi: float) -> aspose.pydrawing.Size:
        '''Calculates the page size in pixels for a specified zoom factor and resolution.
        
        :param scale: The zoom factor (1.0 is 100%).
        :param dpi: The resolution (horizontal and vertical) to convert from points to pixels (dots per inch).
        :returns: The size of the page in pixels.'''
        ...
    
    @overload
    def get_size_in_pixels(self, scale: float, horizontal_dpi: float, vertical_dpi: float) -> aspose.pydrawing.Size:
        '''Calculates the page size in pixels for a specified zoom factor and resolution.
        
        :param scale: The zoom factor (1.0 is 100%).
        :param horizontal_dpi: The horizontal resolution to convert from points to pixels (dots per inch).
        :param vertical_dpi: The vertical resolution to convert from points to pixels (dots per inch).
        :returns: The size of the page in pixels.'''
        ...
    
    @property
    def paper_size(self) -> aspose.words.PaperSize:
        '''Gets the paper size as enumeration.'''
        ...
    
    @property
    def width_in_points(self) -> float:
        '''Gets the width of the page in points.'''
        ...
    
    @property
    def height_in_points(self) -> float:
        '''Gets the height of the page in points.'''
        ...
    
    @property
    def size_in_points(self) -> aspose.pydrawing.SizeF:
        '''Gets the page size in points.'''
        ...
    
    @property
    def paper_tray(self) -> int:
        '''Gets the paper tray (bin) for this page as specified in the document.
        The value is implementation (printer) specific.'''
        ...
    
    @property
    def landscape(self) -> bool:
        '''Returns ``True`` if the page orientation specified in the document for this page is landscape.'''
        ...
    
    ...

class ShapeRenderer(aspose.words.rendering.NodeRendererBase):
    '''Provides methods to render an individual :class:`aspose.words.drawing.Shape` or :class:`aspose.words.drawing.GroupShape`
    to a raster or vector image or to a Graphics object.
    To learn more, visit the `Working with Shapes <https://docs.aspose.com/words/net/working-with-shapes/>` documentation article.'''
    
    def __init__(self, shape: aspose.words.drawing.ShapeBase):
        '''Initializes a new instance of this class.
        
        :param shape: The DrawinML shape object that you want to render.'''
        ...
    
    ...

class ThumbnailGeneratingOptions:
    '''Can be used to specify additional options when generating thumbnail for a document.
    
    User can call method :meth:`aspose.words.Document.update_thumbnail` to generate
    :attr:`aspose.words.properties.BuiltInDocumentProperties.thumbnail` for a document.'''
    
    def __init__(self):
        ...
    
    @property
    def generate_from_first_page(self) -> bool:
        '''Specifies whether to generate thumbnail from first page of the document or first image.
        
        Default is ``True``, which means thumbnail will be generated from first page of the document.
        If value is ``False`` and there is no image in the document, thumbnail will be generated
        from first page of the document.'''
        ...
    
    @generate_from_first_page.setter
    def generate_from_first_page(self, value: bool):
        ...
    
    @property
    def thumbnail_size(self) -> aspose.pydrawing.Size:
        '''Size of generated thumbnail in pixels.
        Default is 600x900.'''
        ...
    
    @thumbnail_size.setter
    def thumbnail_size(self, value: aspose.pydrawing.Size):
        ...
    
    ...

