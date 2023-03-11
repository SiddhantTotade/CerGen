import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class FindReplaceOptions:
    '''Specifies options for find/replace operations.
    To learn more, visit the `Find and Replace <https://docs.aspose.com/words/net/find-and-replace/>` documentation article.'''
    
    @overload
    def __init__(self):
        ...
    
    @overload
    def __init__(self, direction: aspose.words.replacing.FindReplaceDirection):
        ...
    
    @overload
    def __init__(self, replacing_callback: aspose.words.replacing.IReplacingCallback):
        ...
    
    @overload
    def __init__(self, direction: aspose.words.replacing.FindReplaceDirection, replacing_callback: aspose.words.replacing.IReplacingCallback):
        ...
    
    @property
    def apply_font(self) -> aspose.words.Font:
        '''Text formatting applied to new content.'''
        ...
    
    @property
    def apply_paragraph_format(self) -> aspose.words.ParagraphFormat:
        '''Paragraph formatting applied to new content.'''
        ...
    
    @property
    def direction(self) -> aspose.words.replacing.FindReplaceDirection:
        '''Selects direction for replace. Default value is :attr:`FindReplaceDirection.FORWARD`.'''
        ...
    
    @direction.setter
    def direction(self, value: aspose.words.replacing.FindReplaceDirection):
        ...
    
    @property
    def match_case(self) -> bool:
        '''True indicates case-sensitive comparison, false indicates case-insensitive comparison.'''
        ...
    
    @match_case.setter
    def match_case(self, value: bool):
        ...
    
    @property
    def find_whole_words_only(self) -> bool:
        '''True indicates the oldValue must be a standalone word.'''
        ...
    
    @find_whole_words_only.setter
    def find_whole_words_only(self, value: bool):
        ...
    
    @property
    def replacing_callback(self) -> aspose.words.replacing.IReplacingCallback:
        '''The user-defined method which is called before every replace occurrence.'''
        ...
    
    @replacing_callback.setter
    def replacing_callback(self, value: aspose.words.replacing.IReplacingCallback):
        ...
    
    @property
    def use_legacy_order(self) -> bool:
        '''True indicates that a text search is performed sequentially from top to bottom considering the text boxes.
        Default value is ``False``.'''
        ...
    
    @use_legacy_order.setter
    def use_legacy_order(self, value: bool):
        ...
    
    @property
    def ignore_deleted(self) -> bool:
        '''Gets or sets a boolean value indicating either to ignore text inside delete revisions.
        The default value is ``False``.'''
        ...
    
    @ignore_deleted.setter
    def ignore_deleted(self, value: bool):
        ...
    
    @property
    def ignore_inserted(self) -> bool:
        '''Gets or sets a boolean value indicating either to ignore text inside insert revisions.
        The default value is ``False``.'''
        ...
    
    @ignore_inserted.setter
    def ignore_inserted(self, value: bool):
        ...
    
    @property
    def ignore_fields(self) -> bool:
        '''Gets or sets a boolean value indicating either to ignore text inside fields.
        The default value is ``False``.
        
        This option affects whole field (all nodes between
        :attr:`aspose.words.NodeType.FIELD_START` and :attr:`aspose.words.NodeType.FIELD_END`).
        
        To ignore only field codes, please use corresponding option :attr:`FindReplaceOptions.ignore_field_codes`.'''
        ...
    
    @ignore_fields.setter
    def ignore_fields(self, value: bool):
        ...
    
    @property
    def ignore_field_codes(self) -> bool:
        '''Gets or sets a boolean value indicating either to ignore text inside field codes.
        The default value is ``False``.
        
        This option affects only field codes (it does not ignore nodes between
        :attr:`aspose.words.NodeType.FIELD_SEPARATOR` and :attr:`aspose.words.NodeType.FIELD_END`).
        
        To ignore whole field, please use corresponding option :attr:`FindReplaceOptions.ignore_fields`.'''
        ...
    
    @ignore_field_codes.setter
    def ignore_field_codes(self, value: bool):
        ...
    
    @property
    def ignore_footnotes(self) -> bool:
        '''Gets or sets a boolean value indicating either to ignore footnotes.
        The default value is ``False``.'''
        ...
    
    @ignore_footnotes.setter
    def ignore_footnotes(self, value: bool):
        ...
    
    @property
    def use_substitutions(self) -> bool:
        '''Gets or sets a boolean value indicating whether to recognize and use substitutions within replacement patterns.
        The default value is ``False``.
        
        For the details on substitution elements please refer to:
        https://docs.microsoft.com/en-us/dotnet/standard/base-types/substitutions-in-regular-expressions.'''
        ...
    
    @use_substitutions.setter
    def use_substitutions(self, value: bool):
        ...
    
    @property
    def legacy_mode(self) -> bool:
        '''Gets or sets a boolean value indicating that old find/replace algorithm is used.
        
        Use this flag if you need exactly the same behavior as before advanced find/replace feature was introduced.
        Note that old algorithm does not support advanced features such as replace with breaks, apply formatting and so on.'''
        ...
    
    @legacy_mode.setter
    def legacy_mode(self, value: bool):
        ...
    
    @property
    def ignore_structured_document_tags(self) -> bool:
        '''Gets or sets a boolean value indicating either to ignore content of :class:`aspose.words.markup.StructuredDocumentTag`.
        The default value is ``False``.
        
        When this option is set to ``True``, the content of :class:`aspose.words.markup.StructuredDocumentTag`
        will be treated as a simple text.
        
        Otherwise, :class:`aspose.words.markup.StructuredDocumentTag` will be processed as standalone Story
        and replacing pattern will be searched separately for each :class:`aspose.words.markup.StructuredDocumentTag`,
        so that if pattern crosses a :class:`aspose.words.markup.StructuredDocumentTag`, then replacement will not
        be performed for such pattern.'''
        ...
    
    @ignore_structured_document_tags.setter
    def ignore_structured_document_tags(self, value: bool):
        ...
    
    @property
    def smart_paragraph_break_replacement(self) -> bool:
        '''Gets or sets a boolean value indicating either it is allowed to replace paragraph break
        when there is no next sibling paragraph.
        
        The default value is ``False``.
        
        This option allows to replace paragraph break when there is no next sibling paragraph to which all child
        nodes can be moved, by finding any (not necessarily sibling) next paragraph after the paragraph being replaced.'''
        ...
    
    @smart_paragraph_break_replacement.setter
    def smart_paragraph_break_replacement(self, value: bool):
        ...
    
    ...

class IReplacingCallback:
    '''Implement this interface if you want to have your own custom method called during a find and replace operation.'''
    
    def replacing(self, args: aspose.words.replacing.ReplacingArgs) -> aspose.words.replacing.ReplaceAction:
        '''A user defined method that is called during a replace operation for each match found just before a replace is made.
        
        :returns: A :class:`ReplaceAction` value that specifies the action to be taken for the current match.'''
        ...
    
    ...

class ReplacingArgs:
    '''Provides data for a custom replace operation.
    To learn more, visit the `Find and Replace <https://docs.aspose.com/words/net/find-and-replace/>` documentation article.'''
    
    @property
    def match_node(self) -> aspose.words.Node:
        '''Gets the node that contains the beginning of the match.'''
        ...
    
    @property
    def match_offset(self) -> int:
        '''Gets the zero-based starting position of the match from the start of
        the node that contains the beginning of the match.'''
        ...
    
    @property
    def replacement(self) -> str:
        '''Gets or sets the replacement string.'''
        ...
    
    @replacement.setter
    def replacement(self, value: str):
        ...
    
    @property
    def group_name(self) -> str:
        '''Identifies, by name, a captured group in the Aspose.Words.Replacing.ReplacingArgs.Match
        that is to be replaced with the :attr:`ReplacingArgs.replacement` string.
        
        When group name is ``None``, :attr:`ReplacingArgs.group_index` is used to identify the group.
        
        Default is ``None``.'''
        ...
    
    @group_name.setter
    def group_name(self, value: str):
        ...
    
    @property
    def group_index(self) -> int:
        '''Identifies, by index, a captured group in the Aspose.Words.Replacing.ReplacingArgs.Match
        that is to be replaced with the :attr:`ReplacingArgs.replacement` string.
        
        :attr:`ReplacingArgs.group_index` has effect only when :attr:`ReplacingArgs.group_name` is ``None``.
        
        Default is zero.'''
        ...
    
    @group_index.setter
    def group_index(self, value: int):
        ...
    
    ...

class FindReplaceDirection:
    '''Specifies direction for replace operations.'''
    
    FORWARD: int
    BACKWARD: int

class ReplaceAction:
    '''Allows the user to specify what happens to the current match during a replace operation.'''
    
    REPLACE: int
    SKIP: int
    STOP: int

