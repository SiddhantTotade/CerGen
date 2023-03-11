import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class Frameset:
    '''Represents a frames page or a single frame on a frames page.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/net/programming-with-documents/>` documentation article.
    
    If the :attr:`Frameset.child_framesets` property contains items, this instance is a frames page, otherwise it is
    a single frame.'''
    
    def __init__(self):
        ...
    
    @property
    def frame_default_url(self) -> str:
        '''Gets or sets the web page URL or document file name to display in this frame.'''
        ...
    
    @frame_default_url.setter
    def frame_default_url(self, value: str):
        ...
    
    @property
    def is_frame_link_to_file(self) -> bool:
        '''Gets or sets a value indicating whether the web page or document file name specified in the
        :attr:`Frameset.frame_default_url` property is an external resource the frame is linked with.'''
        ...
    
    @is_frame_link_to_file.setter
    def is_frame_link_to_file(self, value: bool):
        ...
    
    @property
    def child_framesets(self) -> aspose.words.framesets.FramesetCollection:
        '''Gets the collection of child frames and frames pages.'''
        ...
    
    ...

class FramesetCollection:
    '''Represents a collection of instances of the :class:`Frameset` class.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/net/programming-with-documents/>` documentation article.'''
    
    def __init__(self):
        ...
    
    def __getitem__(self, index: int) -> aspose.words.framesets.Frameset:
        '''Gets a frame or frames page at the specified index.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of frames or frames pages contained in the collection.'''
        ...
    
    ...

