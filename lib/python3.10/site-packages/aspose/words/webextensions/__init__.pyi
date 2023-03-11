import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class TaskPane:
    '''Represents an add-in task pane object.
    To learn more, visit the `Work with Office Add-ins <https://docs.aspose.com/words/net/work-with-office-add-ins/>` documentation article.'''
    
    def __init__(self):
        ...
    
    @property
    def row(self) -> int:
        '''Specifies the index, enumerating from the outside to the inside, of this task pane among other persisted
        task panes docked in the same default location.'''
        ...
    
    @row.setter
    def row(self, value: int):
        ...
    
    @property
    def width(self) -> float:
        '''Specifies the default width value for this task pane instance.'''
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def is_locked(self) -> bool:
        '''Specifies whether the task pane is locked to the document in the UI and cannot be closed by the user.'''
        ...
    
    @is_locked.setter
    def is_locked(self, value: bool):
        ...
    
    @property
    def is_visible(self) -> bool:
        '''Specifies whether the task pane shows as visible by default when the document opens.'''
        ...
    
    @is_visible.setter
    def is_visible(self, value: bool):
        ...
    
    @property
    def dock_state(self) -> aspose.words.webextensions.TaskPaneDockState:
        '''Specifies the last-docked location of this task pane object.'''
        ...
    
    @dock_state.setter
    def dock_state(self, value: aspose.words.webextensions.TaskPaneDockState):
        ...
    
    @property
    def web_extension(self) -> aspose.words.webextensions.WebExtension:
        '''Represents an web extension object.'''
        ...
    
    ...

class TaskPaneCollection:
    '''Specifies a list of persisted task pane objects.
    To learn more, visit the `Work with Office Add-ins <https://docs.aspose.com/words/net/work-with-office-add-ins/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.webextensions.TaskPane:
        ...
    
    def __setitem__(self, index: int, value: aspose.words.webextensions.TaskPane):
        ...
    
    def add(self, item: aspose.words.webextensions.TaskPane) -> None:
        ...
    
    def clear(self) -> None:
        ...
    
    def remove(self, index: int) -> None:
        ...
    
    @property
    def count(self) -> int:
        ...
    
    ...

class WebExtension:
    '''Represents a web extension object.
    To learn more, visit the `Work with Office Add-ins <https://docs.aspose.com/words/net/work-with-office-add-ins/>` documentation article.'''
    
    @property
    def id(self) -> str:
        '''Uniquely identifies the web extension instance in the current document.'''
        ...
    
    @id.setter
    def id(self, value: str):
        ...
    
    @property
    def is_frozen(self) -> bool:
        '''Specifies whether the user can interact with the web extension or not.'''
        ...
    
    @is_frozen.setter
    def is_frozen(self, value: bool):
        ...
    
    @property
    def reference(self) -> aspose.words.webextensions.WebExtensionReference:
        '''Specifies the primary reference to an web extension.'''
        ...
    
    @property
    def bindings(self) -> aspose.words.webextensions.WebExtensionBindingCollection:
        '''Specifies a list of web extension bindings.'''
        ...
    
    @property
    def alternate_references(self) -> aspose.words.webextensions.WebExtensionReferenceCollection:
        '''Specifies alternate references to a web extension.'''
        ...
    
    @property
    def properties(self) -> aspose.words.webextensions.WebExtensionPropertyCollection:
        '''Represents a set of web extension custom properties.'''
        ...
    
    ...

class WebExtensionBinding:
    '''Specifies a binding relationship between a web extension and the data in the document.
    To learn more, visit the `Work with Office Add-ins <https://docs.aspose.com/words/net/work-with-office-add-ins/>` documentation article.'''
    
    def __init__(self, id: str, binding_type: aspose.words.webextensions.WebExtensionBindingType, app_ref: str):
        '''Creates web extension binding with specified parameters.
        
        :param id: Binding identifier.
        :param binding_type: Binding type.
        :param app_ref: Binding key used to map the binding entry in this list with the bound data in the document.'''
        ...
    
    @property
    def id(self) -> str:
        '''Specifies the binding identifier.'''
        ...
    
    @id.setter
    def id(self, value: str):
        ...
    
    @property
    def binding_type(self) -> aspose.words.webextensions.WebExtensionBindingType:
        '''Specifies the binding type.'''
        ...
    
    @binding_type.setter
    def binding_type(self, value: aspose.words.webextensions.WebExtensionBindingType):
        ...
    
    @property
    def app_ref(self) -> str:
        '''Specifies the binding key used to map the binding entry in this list with the bound data in the document.'''
        ...
    
    @app_ref.setter
    def app_ref(self, value: str):
        ...
    
    ...

class WebExtensionBindingCollection:
    '''Specifies a list of web extension bindings.
    To learn more, visit the `Work with Office Add-ins <https://docs.aspose.com/words/net/work-with-office-add-ins/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.webextensions.WebExtensionBinding:
        ...
    
    def __setitem__(self, index: int, value: aspose.words.webextensions.WebExtensionBinding):
        ...
    
    def add(self, item: aspose.words.webextensions.WebExtensionBinding) -> None:
        ...
    
    def clear(self) -> None:
        ...
    
    def remove(self, index: int) -> None:
        ...
    
    @property
    def count(self) -> int:
        ...
    
    ...

class WebExtensionProperty:
    '''Specifies a web extension custom property.
    To learn more, visit the `Work with Office Add-ins <https://docs.aspose.com/words/net/work-with-office-add-ins/>` documentation article.'''
    
    def __init__(self, name: str, value: str):
        '''Creates web extension custom property with specified name and value.
        
        :param name: Property name.
        :param value: Property value.'''
        ...
    
    @property
    def name(self) -> str:
        '''Specifies a custom property name'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def value(self) -> str:
        '''Specifies a custom property value.'''
        ...
    
    @value.setter
    def value(self, value: str):
        ...
    
    ...

class WebExtensionPropertyCollection:
    '''Specifies a set of web extension custom properties.
    To learn more, visit the `Work with Office Add-ins <https://docs.aspose.com/words/net/work-with-office-add-ins/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.webextensions.WebExtensionProperty:
        ...
    
    def __setitem__(self, index: int, value: aspose.words.webextensions.WebExtensionProperty):
        ...
    
    def add(self, item: aspose.words.webextensions.WebExtensionProperty) -> None:
        ...
    
    def clear(self) -> None:
        ...
    
    def remove(self, index: int) -> None:
        ...
    
    @property
    def count(self) -> int:
        ...
    
    ...

class WebExtensionReference:
    '''Represents the reference to a web extension. The reference is used to identify the provider location and version of the
    extension.
    To learn more, visit the `Work with Office Add-ins <https://docs.aspose.com/words/net/work-with-office-add-ins/>` documentation article.'''
    
    def __init__(self):
        ...
    
    @property
    def id(self) -> str:
        '''Identifier associated with the web extension within a catalog provider.'''
        ...
    
    @id.setter
    def id(self, value: str):
        ...
    
    @property
    def version(self) -> str:
        '''Specifies the version of the web extension.'''
        ...
    
    @version.setter
    def version(self, value: str):
        ...
    
    @property
    def store(self) -> str:
        '''Specifies the instance of the marketplace where the web extension is stored.'''
        ...
    
    @store.setter
    def store(self, value: str):
        ...
    
    @property
    def store_type(self) -> aspose.words.webextensions.WebExtensionStoreType:
        '''Specifies the type of marketplace.'''
        ...
    
    @store_type.setter
    def store_type(self, value: aspose.words.webextensions.WebExtensionStoreType):
        ...
    
    ...

class WebExtensionReferenceCollection:
    '''Specifies a list of web extension references.
    To learn more, visit the `Work with Office Add-ins <https://docs.aspose.com/words/net/work-with-office-add-ins/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.webextensions.WebExtensionReference:
        ...
    
    def __setitem__(self, index: int, value: aspose.words.webextensions.WebExtensionReference):
        ...
    
    def add(self, item: aspose.words.webextensions.WebExtensionReference) -> None:
        ...
    
    def clear(self) -> None:
        ...
    
    def remove(self, index: int) -> None:
        ...
    
    @property
    def count(self) -> int:
        ...
    
    ...

class TaskPaneDockState:
    '''Enumerates available locations of task pane object.'''
    
    RIGHT: int
    LEFT: int

class WebExtensionBindingType:
    '''Enumerates available types of binding between a web extension and the data in the document.'''
    
    MATRIX: int
    TABLE: int
    TEXT: int
    DEFAULT: int

class WebExtensionStoreType:
    '''Enumerates available types of a web extension store.'''
    
    SP_CATALOG: int
    OMEX: int
    SP_APP: int
    EXCHANGE: int
    FILE_SYSTEM: int
    REGISTRY: int
    EX_CATALOG: int
    DEFAULT: int

