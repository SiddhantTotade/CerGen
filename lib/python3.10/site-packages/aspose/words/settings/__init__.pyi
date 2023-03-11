import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class CompatibilityOptions:
    '''Contains compatibility options (that is, the user preferences entered on the **Compatibility**
    tab of the **Options** dialog in Microsoft Word).
    To learn more, visit the `Detect File Format and Check Format Compatibility <https://docs.aspose.com/words/net/detect-file-format-and-check-format-compatibility/>` documentation article.'''
    
    def optimize_for(self, version: aspose.words.settings.MsWordVersion) -> None:
        '''Allows to optimize the document contents as well as default Aspose.Words behavior to a particular versions of MS Word.
        
        Use this method to prevent MS Word from displaying "Compatibility mode" ribbon upon document loading.
        (Note that you may also need to set the :attr:`aspose.words.saving.OoxmlSaveOptions.compliance` property to
        :attr:`aspose.words.saving.OoxmlCompliance.ISO29500_2008_TRANSITIONAL` or higher.)'''
        ...
    
    @property
    def no_tab_hang_ind(self) -> bool:
        '''Do Not Create Custom Tab Stop for Hanging Indent.'''
        ...
    
    @no_tab_hang_ind.setter
    def no_tab_hang_ind(self, value: bool):
        ...
    
    @property
    def no_space_raise_lower(self) -> bool:
        '''Do Not Increase Line Height for Raised/Lowered Text.'''
        ...
    
    @no_space_raise_lower.setter
    def no_space_raise_lower(self, value: bool):
        ...
    
    @property
    def suppress_sp_bf_after_pg_brk(self) -> bool:
        '''Do Not Use Space Before On First Line After a Page Break.'''
        ...
    
    @suppress_sp_bf_after_pg_brk.setter
    def suppress_sp_bf_after_pg_brk(self, value: bool):
        ...
    
    @property
    def wrap_trail_spaces(self) -> bool:
        '''Line Wrap Trailing Spaces.'''
        ...
    
    @wrap_trail_spaces.setter
    def wrap_trail_spaces(self, value: bool):
        ...
    
    @property
    def print_col_black(self) -> bool:
        '''Print Colors as Black And White without Dithering.'''
        ...
    
    @print_col_black.setter
    def print_col_black(self, value: bool):
        ...
    
    @property
    def no_column_balance(self) -> bool:
        '''Do Not Balance Text Columns within a Section.'''
        ...
    
    @no_column_balance.setter
    def no_column_balance(self, value: bool):
        ...
    
    @property
    def conv_mail_merge_esc(self) -> bool:
        '''Treat Backslash Quotation Delimiter as Two Quotation Marks.'''
        ...
    
    @conv_mail_merge_esc.setter
    def conv_mail_merge_esc(self, value: bool):
        ...
    
    @property
    def suppress_top_spacing(self) -> bool:
        '''Ignore Minimum and Exact Line Height for First Line on Page.'''
        ...
    
    @suppress_top_spacing.setter
    def suppress_top_spacing(self, value: bool):
        ...
    
    @property
    def use_single_borderfor_contiguous_cells(self) -> bool:
        '''Use Simplified Rules For Table Border Conflicts.'''
        ...
    
    @use_single_borderfor_contiguous_cells.setter
    def use_single_borderfor_contiguous_cells(self, value: bool):
        ...
    
    @property
    def transparent_metafiles(self) -> bool:
        '''Specifies not to blank the area behind metafile pictures.'''
        ...
    
    @transparent_metafiles.setter
    def transparent_metafiles(self, value: bool):
        ...
    
    @property
    def show_breaks_in_frames(self) -> bool:
        '''Display Page/Column Breaks Present in Frames.'''
        ...
    
    @show_breaks_in_frames.setter
    def show_breaks_in_frames(self, value: bool):
        ...
    
    @property
    def swap_borders_facing_pgs(self) -> bool:
        '''Swap Paragraph Borders on Odd Numbered Pages.'''
        ...
    
    @swap_borders_facing_pgs.setter
    def swap_borders_facing_pgs(self, value: bool):
        ...
    
    @property
    def do_not_leave_backslash_alone(self) -> bool:
        '''Convert Backslash To Yen Sign When Entered.'''
        ...
    
    @do_not_leave_backslash_alone.setter
    def do_not_leave_backslash_alone(self, value: bool):
        ...
    
    @property
    def do_not_expand_shift_return(self) -> bool:
        '''Don't Justify Lines Ending in Soft Line Break.'''
        ...
    
    @do_not_expand_shift_return.setter
    def do_not_expand_shift_return(self, value: bool):
        ...
    
    @property
    def ul_trail_space(self) -> bool:
        '''Underline All Trailing Spaces.'''
        ...
    
    @ul_trail_space.setter
    def ul_trail_space(self, value: bool):
        ...
    
    @property
    def balance_single_byte_double_byte_width(self) -> bool:
        '''Balance Single Byte and Double Byte Characters.'''
        ...
    
    @balance_single_byte_double_byte_width.setter
    def balance_single_byte_double_byte_width(self, value: bool):
        ...
    
    @property
    def suppress_spacing_at_top_of_page(self) -> bool:
        '''Ignore Minimum Line Height for First Line on Page.'''
        ...
    
    @suppress_spacing_at_top_of_page.setter
    def suppress_spacing_at_top_of_page(self, value: bool):
        ...
    
    @property
    def spacing_in_whole_points(self) -> bool:
        '''Only Expand/Condense Text By Whole Points.'''
        ...
    
    @spacing_in_whole_points.setter
    def spacing_in_whole_points(self, value: bool):
        ...
    
    @property
    def print_body_text_before_header(self) -> bool:
        '''Print Body Text before Header/Footer Contents.'''
        ...
    
    @print_body_text_before_header.setter
    def print_body_text_before_header(self, value: bool):
        ...
    
    @property
    def no_leading(self) -> bool:
        '''Do Not Add Leading Between Lines of Text.'''
        ...
    
    @no_leading.setter
    def no_leading(self, value: bool):
        ...
    
    @property
    def space_for_ul(self) -> bool:
        '''Add Additional Space Below Baseline For Underlined East Asian Text.'''
        ...
    
    @space_for_ul.setter
    def space_for_ul(self, value: bool):
        ...
    
    @property
    def mw_small_caps(self) -> bool:
        '''Emulate Word 5.x for the Macintosh Small Caps Formatting.'''
        ...
    
    @mw_small_caps.setter
    def mw_small_caps(self, value: bool):
        ...
    
    @property
    def suppress_top_spacing_wp(self) -> bool:
        '''Emulate WordPerfect 5.x Line Spacing.'''
        ...
    
    @suppress_top_spacing_wp.setter
    def suppress_top_spacing_wp(self, value: bool):
        ...
    
    @property
    def truncate_font_heights_like_wp6(self) -> bool:
        '''Emulate WordPerfect 6.x Font Height Calculation.'''
        ...
    
    @truncate_font_heights_like_wp6.setter
    def truncate_font_heights_like_wp6(self, value: bool):
        ...
    
    @property
    def sub_font_by_size(self) -> bool:
        '''Increase Priority Of Font Size During Font Substitution.'''
        ...
    
    @sub_font_by_size.setter
    def sub_font_by_size(self, value: bool):
        ...
    
    @property
    def line_wrap_like_word6(self) -> bool:
        '''Emulate Word 6.0 Line Wrapping for East Asian Text.'''
        ...
    
    @line_wrap_like_word6.setter
    def line_wrap_like_word6(self, value: bool):
        ...
    
    @property
    def do_not_suppress_paragraph_borders(self) -> bool:
        '''Do Not Suppress Paragraph Borders Next To Frames.'''
        ...
    
    @do_not_suppress_paragraph_borders.setter
    def do_not_suppress_paragraph_borders(self, value: bool):
        ...
    
    @property
    def no_extra_line_spacing(self) -> bool:
        '''Do Not Center Content on Lines With Exact Line Height.'''
        ...
    
    @no_extra_line_spacing.setter
    def no_extra_line_spacing(self, value: bool):
        ...
    
    @property
    def suppress_bottom_spacing(self) -> bool:
        '''Ignore Exact Line Height for Last Line on Page.'''
        ...
    
    @suppress_bottom_spacing.setter
    def suppress_bottom_spacing(self, value: bool):
        ...
    
    @property
    def wp_space_width(self) -> bool:
        '''Specifies whether to set the width of a space as is done in WordPerfect 5.x.'''
        ...
    
    @wp_space_width.setter
    def wp_space_width(self, value: bool):
        ...
    
    @property
    def wp_justification(self) -> bool:
        '''Emulate WordPerfect 6.x Paragraph Justification.'''
        ...
    
    @wp_justification.setter
    def wp_justification(self, value: bool):
        ...
    
    @property
    def use_printer_metrics(self) -> bool:
        '''Use Printer Metrics To Display Documents.
        
        Printer Metrics may differ depending on drivers used.
        For instance, Windows "Microsoft OpenXPS Class Driver 2" and "Microsoft Print to PDF" provide slightly different metrics.
        Therefore, the final document's layout may change if this option is enabled.'''
        ...
    
    @use_printer_metrics.setter
    def use_printer_metrics(self, value: bool):
        ...
    
    @property
    def shape_layout_like_ww8(self) -> bool:
        '''Emulate Word 97 Text Wrapping Around Floating Objects.'''
        ...
    
    @shape_layout_like_ww8.setter
    def shape_layout_like_ww8(self, value: bool):
        ...
    
    @property
    def footnote_layout_like_ww8(self) -> bool:
        '''Emulate Word 6.x/95/97 Footnote Placement.'''
        ...
    
    @footnote_layout_like_ww8.setter
    def footnote_layout_like_ww8(self, value: bool):
        ...
    
    @property
    def do_not_use_html_paragraph_auto_spacing(self) -> bool:
        '''Use Fixed Paragraph Spacing for HTML Auto Setting.'''
        ...
    
    @do_not_use_html_paragraph_auto_spacing.setter
    def do_not_use_html_paragraph_auto_spacing(self, value: bool):
        ...
    
    @property
    def adjust_line_height_in_table(self) -> bool:
        '''Add Document Grid Line Pitch To Lines in Table Cells.'''
        ...
    
    @adjust_line_height_in_table.setter
    def adjust_line_height_in_table(self, value: bool):
        ...
    
    @property
    def forget_last_tab_alignment(self) -> bool:
        '''Ignore Width of Last Tab Stop When Aligning Paragraph If It Is Not Left Aligned.'''
        ...
    
    @forget_last_tab_alignment.setter
    def forget_last_tab_alignment(self, value: bool):
        ...
    
    @property
    def auto_space_like_word95(self) -> bool:
        '''Emulate Word 95 Full-Width Character Spacing.'''
        ...
    
    @auto_space_like_word95.setter
    def auto_space_like_word95(self, value: bool):
        ...
    
    @property
    def align_tables_row_by_row(self) -> bool:
        '''Align Table Rows Independently.'''
        ...
    
    @align_tables_row_by_row.setter
    def align_tables_row_by_row(self, value: bool):
        ...
    
    @property
    def layout_raw_table_width(self) -> bool:
        '''Ignore Space Before Table When Deciding If Table Should Wrap Floating Object.'''
        ...
    
    @layout_raw_table_width.setter
    def layout_raw_table_width(self, value: bool):
        ...
    
    @property
    def layout_table_rows_apart(self) -> bool:
        '''Allow Table Rows to Wrap Inline Objects Independently.'''
        ...
    
    @layout_table_rows_apart.setter
    def layout_table_rows_apart(self, value: bool):
        ...
    
    @property
    def use_word97_line_break_rules(self) -> bool:
        '''Emulate Word 97 East Asian Line Breaking.'''
        ...
    
    @use_word97_line_break_rules.setter
    def use_word97_line_break_rules(self, value: bool):
        ...
    
    @property
    def do_not_break_wrapped_tables(self) -> bool:
        '''Do Not Allow Floating Tables To Break Across Pages.'''
        ...
    
    @do_not_break_wrapped_tables.setter
    def do_not_break_wrapped_tables(self, value: bool):
        ...
    
    @property
    def do_not_snap_to_grid_in_cell(self) -> bool:
        '''Do Not Snap to Document Grid in Table Cells with Objects.'''
        ...
    
    @do_not_snap_to_grid_in_cell.setter
    def do_not_snap_to_grid_in_cell(self, value: bool):
        ...
    
    @property
    def select_fld_with_first_or_last_char(self) -> bool:
        '''Select Field When First or Last Character Is Selected.'''
        ...
    
    @select_fld_with_first_or_last_char.setter
    def select_fld_with_first_or_last_char(self, value: bool):
        ...
    
    @property
    def apply_breaking_rules(self) -> bool:
        '''Use Legacy Ethiopic and Amharic Line Breaking Rules.'''
        ...
    
    @apply_breaking_rules.setter
    def apply_breaking_rules(self, value: bool):
        ...
    
    @property
    def do_not_wrap_text_with_punct(self) -> bool:
        '''Do Not Allow Hanging Punctuation With Character Grid.'''
        ...
    
    @do_not_wrap_text_with_punct.setter
    def do_not_wrap_text_with_punct(self, value: bool):
        ...
    
    @property
    def do_not_use_east_asian_break_rules(self) -> bool:
        '''Do Not Compress Compressible Characters When Using Document Grid.'''
        ...
    
    @do_not_use_east_asian_break_rules.setter
    def do_not_use_east_asian_break_rules(self, value: bool):
        ...
    
    @property
    def use_word2002_table_style_rules(self) -> bool:
        '''Emulate Word 2002 Table Style Rules.'''
        ...
    
    @use_word2002_table_style_rules.setter
    def use_word2002_table_style_rules(self, value: bool):
        ...
    
    @property
    def grow_autofit(self) -> bool:
        '''Allow Tables to AutoFit Into Page Margins.'''
        ...
    
    @grow_autofit.setter
    def grow_autofit(self, value: bool):
        ...
    
    @property
    def use_normal_style_for_list(self) -> bool:
        '''Do Not Automatically Apply List Paragraph Style To Bulleted/Numbered Text.'''
        ...
    
    @use_normal_style_for_list.setter
    def use_normal_style_for_list(self, value: bool):
        ...
    
    @property
    def do_not_use_indent_as_numbering_tab_stop(self) -> bool:
        '''Ignore Hanging Indent When Creating Tab Stop After Numbering.'''
        ...
    
    @do_not_use_indent_as_numbering_tab_stop.setter
    def do_not_use_indent_as_numbering_tab_stop(self, value: bool):
        ...
    
    @property
    def use_alt_kinsoku_line_break_rules(self) -> bool:
        '''Use Alternate Set of East Asian Line Breaking Rules.'''
        ...
    
    @use_alt_kinsoku_line_break_rules.setter
    def use_alt_kinsoku_line_break_rules(self, value: bool):
        ...
    
    @property
    def allow_space_of_same_style_in_table(self) -> bool:
        '''Allow Contextual Spacing of Paragraphs in Tables.'''
        ...
    
    @allow_space_of_same_style_in_table.setter
    def allow_space_of_same_style_in_table(self, value: bool):
        ...
    
    @property
    def do_not_suppress_indentation(self) -> bool:
        '''Do Not Ignore Floating Objects When Calculating Paragraph Indentation.'''
        ...
    
    @do_not_suppress_indentation.setter
    def do_not_suppress_indentation(self, value: bool):
        ...
    
    @property
    def do_not_autofit_constrained_tables(self) -> bool:
        '''Do Not AutoFit Tables To Fit Next To Wrapped Objects.'''
        ...
    
    @do_not_autofit_constrained_tables.setter
    def do_not_autofit_constrained_tables(self, value: bool):
        ...
    
    @property
    def autofit_to_first_fixed_width_cell(self) -> bool:
        '''Allow Table Columns To Exceed Preferred Widths of Constituent Cells.
        
        The option is called "Use Word 2003 table autofit rules" in MS Word 2013 user interface.
        It actually affects how the grid is calculated for fixed layout tables, too (for some cases).'''
        ...
    
    @autofit_to_first_fixed_width_cell.setter
    def autofit_to_first_fixed_width_cell(self, value: bool):
        ...
    
    @property
    def underline_tab_in_num_list(self) -> bool:
        '''Underline Following Character Following Numbering.'''
        ...
    
    @underline_tab_in_num_list.setter
    def underline_tab_in_num_list(self, value: bool):
        ...
    
    @property
    def display_hangul_fixed_width(self) -> bool:
        '''Always Use Fixed Width for Hangul Characters.'''
        ...
    
    @display_hangul_fixed_width.setter
    def display_hangul_fixed_width(self, value: bool):
        ...
    
    @property
    def split_pg_break_and_para_mark(self) -> bool:
        '''Always Move Paragraph Mark to Page after a Page Break.'''
        ...
    
    @split_pg_break_and_para_mark.setter
    def split_pg_break_and_para_mark(self, value: bool):
        ...
    
    @property
    def do_not_vert_align_cell_with_sp(self) -> bool:
        '''Don't Vertically Align Cells Containing Floating Objects.'''
        ...
    
    @do_not_vert_align_cell_with_sp.setter
    def do_not_vert_align_cell_with_sp(self, value: bool):
        ...
    
    @property
    def do_not_break_constrained_forced_table(self) -> bool:
        '''Don't Break Table Rows Around Floating Tables.'''
        ...
    
    @do_not_break_constrained_forced_table.setter
    def do_not_break_constrained_forced_table(self, value: bool):
        ...
    
    @property
    def do_not_vert_align_in_txbx(self) -> bool:
        '''Ignore Vertical Alignment in Textboxes.'''
        ...
    
    @do_not_vert_align_in_txbx.setter
    def do_not_vert_align_in_txbx(self, value: bool):
        ...
    
    @property
    def use_ansi_kerning_pairs(self) -> bool:
        '''Use ANSI Kerning Pairs from Fonts.'''
        ...
    
    @use_ansi_kerning_pairs.setter
    def use_ansi_kerning_pairs(self, value: bool):
        ...
    
    @property
    def cached_col_balance(self) -> bool:
        '''Use Cached Paragraph Information for Column Balancing.'''
        ...
    
    @cached_col_balance.setter
    def cached_col_balance(self, value: bool):
        ...
    
    @property
    def use_fe_layout(self) -> bool:
        '''Do Not Bypass East Asian/Complex Script Layout Code.'''
        ...
    
    @use_fe_layout.setter
    def use_fe_layout(self, value: bool):
        ...
    
    @property
    def override_table_style_font_size_and_justification(self) -> bool:
        '''Specifies how the style hierarchy of the document is evaluated.'''
        ...
    
    @override_table_style_font_size_and_justification.setter
    def override_table_style_font_size_and_justification(self, value: bool):
        ...
    
    @property
    def disable_open_type_font_formatting_features(self) -> bool:
        ...
    
    @disable_open_type_font_formatting_features.setter
    def disable_open_type_font_formatting_features(self, value: bool):
        ...
    
    @property
    def swap_inside_and_outside_for_mirror_indents_and_relative_positioning(self) -> bool:
        ...
    
    @swap_inside_and_outside_for_mirror_indents_and_relative_positioning.setter
    def swap_inside_and_outside_for_mirror_indents_and_relative_positioning(self, value: bool):
        ...
    
    @property
    def use_word2010_table_style_rules(self) -> bool:
        ...
    
    @use_word2010_table_style_rules.setter
    def use_word2010_table_style_rules(self, value: bool):
        ...
    
    @property
    def ui_compat_97_to_2003(self) -> bool:
        '''True to disable UI functionality which is not compatible with Word97-2003.
        Default value is ``False``.
        
        Controls the Word97-2003 compatibility setting that disables UI functionality which
        is not compatible with Word97-2003.
        When ``True``, 'w:uiCompat97To2003' XML element is written to '\\word\\settings.xml'
        document package part.
        Default value is ``False``. When set to ``False``, this element is not written.
        
        Technically this property is not part of compatibility options, but we have put it here for API convenience.'''
        ...
    
    @ui_compat_97_to_2003.setter
    def ui_compat_97_to_2003(self, value: bool):
        ...
    
    ...

class HyphenationOptions:
    '''Allows to configure document hyphenation options.
    To learn more, visit the `Working with Hyphenation <https://docs.aspose.com/words/net/working-with-hyphenation/>` documentation article.'''
    
    def __init__(self):
        ...
    
    @property
    def auto_hyphenation(self) -> bool:
        '''Gets or sets value determining whether automatic hyphenation is turned on for the document.
        Default value for this property is ``False``.'''
        ...
    
    @auto_hyphenation.setter
    def auto_hyphenation(self, value: bool):
        ...
    
    @property
    def consecutive_hyphen_limit(self) -> int:
        '''Gets or sets the maximum number of consecutive lines that can end with hyphens.
        Default value for this property is 0.
        
        If value of this property is set to 0, any number of consecutive lines can end with hyphens.
        
        The property does not have effect when saving to fixed page formats e.g. PDF.'''
        ...
    
    @consecutive_hyphen_limit.setter
    def consecutive_hyphen_limit(self, value: int):
        ...
    
    @property
    def hyphenation_zone(self) -> int:
        '''Gets or sets the distance in 1/20 of a point from the right margin within which you do not want
        to hyphenate words.
        Default value for this property is 360 (0.25 inch).'''
        ...
    
    @hyphenation_zone.setter
    def hyphenation_zone(self, value: int):
        ...
    
    @property
    def hyphenate_caps(self) -> bool:
        '''Gets or sets value determining whether words written in all capital letters are hyphenated.
        Default value for this property is ``True``.'''
        ...
    
    @hyphenate_caps.setter
    def hyphenate_caps(self, value: bool):
        ...
    
    ...

class MailMergeSettings:
    '''Specifies all of the mail merge information for a document.
    To learn more, visit the `Mail Merge and Reporting <https://docs.aspose.com/words/net/mail-merge-and-reporting/>` documentation article.
    
    You can use this object to specify a mail merge data source for a document and this information
    (along with the available data fields) will appear in Microsoft Word when the user opens this document.
    Or you can use this object to query mail merge settings that the user has specified in Microsoft Word
    for this document.
    
    You do not normally need to create objects of this class directly because Mail merge settings
    of a document are always available via the :attr:`aspose.words.Document.mail_merge_settings` property.
    
    To detect whether this document is a mail merge main document, check the value of the
    :attr:`MailMergeSettings.main_document_type` property.
    
    To remove mail merge settings and data source information from a document you can use the
    :meth:`MailMergeSettings.clear` method. Aspose.Words will not write mail merge settings to a document if
    the :attr:`MailMergeSettings.main_document_type` property is set to :attr:`MailMergeMainDocumentType.NOT_A_MERGE_DOCUMENT`
    or the :attr:`MailMergeSettings.data_type` property is set to :attr:`MailMergeDataType.NONE`.
    
    The best way to learn how to use the properties of this object is to create a document with a desired
    data source manually in Microsoft Word and then open that document using Aspose.Words and examine the properties
    of the :attr:`aspose.words.Document.mail_merge_settings` and :attr:`MailMergeSettings.odso` objects. This is
    a good approach to take if you want to learn how to programmatically configure a data source, for example.
    
    Aspose.Words preserves mail merge information when loading, saving and converting documents
    between different formats, but does not use this information when performing its own mail merge
    using the :class:`aspose.words.mailmerging.MailMerge` object.'''
    
    def __init__(self):
        ...
    
    def clear(self) -> None:
        '''Clears the mail merge settings in such a way that when the document is saved,
        no mail merge settings will be saved and it will become a normal document.'''
        ...
    
    def clone(self) -> aspose.words.settings.MailMergeSettings:
        '''Returns a deep clone of this object.'''
        ...
    
    @property
    def active_record(self) -> int:
        '''Specifies the one-based index of the record from the data source which shall be displayed in Microsoft Word. The default value is 1.'''
        ...
    
    @active_record.setter
    def active_record(self, value: int):
        ...
    
    @property
    def address_field_name(self) -> str:
        '''Specifies the column within the data source that contains e-mail addresses. The default value is an empty string.'''
        ...
    
    @address_field_name.setter
    def address_field_name(self, value: str):
        ...
    
    @property
    def check_errors(self) -> aspose.words.settings.MailMergeCheckErrors:
        '''Specifies the type of error reporting which shall be conducted by Microsoft Word when performing a mail merge.
        The default value is :attr:`MailMergeCheckErrors.DEFAULT`.'''
        ...
    
    @check_errors.setter
    def check_errors(self, value: aspose.words.settings.MailMergeCheckErrors):
        ...
    
    @property
    def connect_string(self) -> str:
        '''Specifies the connection string used to connect to an external data source. The default value is an empty string.'''
        ...
    
    @connect_string.setter
    def connect_string(self, value: str):
        ...
    
    @property
    def data_source(self) -> str:
        '''Specifies the path to the mail-merge data source. The default value is an empty string.'''
        ...
    
    @data_source.setter
    def data_source(self, value: str):
        ...
    
    @property
    def data_type(self) -> aspose.words.settings.MailMergeDataType:
        '''Specifies the type of the mail-merge data source and the method of data access.
        The default value is :attr:`MailMergeDataType.DEFAULT`.'''
        ...
    
    @data_type.setter
    def data_type(self, value: aspose.words.settings.MailMergeDataType):
        ...
    
    @property
    def destination(self) -> aspose.words.settings.MailMergeDestination:
        '''Specifies how Microsoft Word will output the results of a mail merge.
        The default value is :attr:`MailMergeDestination.DEFAULT`.'''
        ...
    
    @destination.setter
    def destination(self, value: aspose.words.settings.MailMergeDestination):
        ...
    
    @property
    def do_not_supress_blank_lines(self) -> bool:
        '''Specifies how an application performing the mail merge shall handle blank lines in the merged documents resulting from the mail merge.
        The default value is ``False``.'''
        ...
    
    @do_not_supress_blank_lines.setter
    def do_not_supress_blank_lines(self, value: bool):
        ...
    
    @property
    def header_source(self) -> str:
        '''Specifies the path to the mail-merge header source.
        The default value is an empty string.'''
        ...
    
    @header_source.setter
    def header_source(self, value: str):
        ...
    
    @property
    def link_to_query(self) -> bool:
        '''Not sure about this one.
        The Microsoft Word Automation Reference suggests that this specifies that the query is executed every time the document
        is opened in Microsoft Word. But the OOXML specification suggests that this specifies that the query contains a reference
        to an external query file which contains the actual query.
        The default value is ``False``.'''
        ...
    
    @link_to_query.setter
    def link_to_query(self, value: bool):
        ...
    
    @property
    def mail_as_attachment(self) -> bool:
        '''Specifies that the documents produced during a mail merge operation should be emailed as an attachment rather
        than the body of the actual e-mail. The default value is ``False``.'''
        ...
    
    @mail_as_attachment.setter
    def mail_as_attachment(self, value: bool):
        ...
    
    @property
    def mail_subject(self) -> str:
        '''Specifies the text which shall appear in the subject line of the e-mails or faxes produced during mail merge.
        The default value is an empty string.'''
        ...
    
    @mail_subject.setter
    def mail_subject(self, value: str):
        ...
    
    @property
    def main_document_type(self) -> aspose.words.settings.MailMergeMainDocumentType:
        '''Specifies the mail-merge main document type.
        The default value is :attr:`MailMergeMainDocumentType.DEFAULT`.
        
        The main document is the document that contains information that is the same for each version of the merged document.'''
        ...
    
    @main_document_type.setter
    def main_document_type(self, value: aspose.words.settings.MailMergeMainDocumentType):
        ...
    
    @property
    def odso(self) -> aspose.words.settings.Odso:
        '''Gets or sets the object that specifies the Office Data Source Object (ODSO) settings.
        
        This object is never ``None``.'''
        ...
    
    @odso.setter
    def odso(self, value: aspose.words.settings.Odso):
        ...
    
    @property
    def query(self) -> str:
        '''Contains the Structured Query Language string that shall be run against the specified external data source to
        return the set of records which shall be imported into the document when the mail merge operation is performed.
        The default value is an empty string.'''
        ...
    
    @query.setter
    def query(self, value: str):
        ...
    
    @property
    def view_merged_data(self) -> bool:
        '''Specifies that Microsoft Word shall display the data from the specified external data source where merge fields
        have been inserted (e.g. preview merged data). The default value is ``False``.'''
        ...
    
    @view_merged_data.setter
    def view_merged_data(self, value: bool):
        ...
    
    ...

class Odso:
    '''Specifies the Office Data Source Object (ODSO) settings for a mail merge data source.
    To learn more, visit the `Mail Merge and Reporting <https://docs.aspose.com/words/net/mail-merge-and-reporting/>` documentation article.
    
    ODSO seems to be the "new" way the newer Microsoft Word versions prefer to use when specifying certain
    types of data sources for a mail merge document. ODSO probably first appeared in Microsoft Word 2000.
    
    The use of ODSO is poorly documented and the best way to learn how to use the properties of this object
    is to create a document with a desired data source manually in Microsoft Word and then open that document using
    Aspose.Words and examine the properties of the :attr:`aspose.words.Document.mail_merge_settings` and
    :attr:`MailMergeSettings.odso` objects. This is a good approach to take if you want to learn how to
    programmatically configure a data source, for example.
    
    You do not normally need to create objects of this class directly because ODSO settings
    are always available via the :attr:`MailMergeSettings.odso` property.'''
    
    def __init__(self):
        ...
    
    def clone(self) -> aspose.words.settings.Odso:
        '''Returns a deep clone of this object.'''
        ...
    
    @property
    def column_delimiter(self) -> str:
        '''Specifies the character which shall be interpreted as the column delimiter used to separate columns within external data sources.
        The default value is 0 which means there is no column delimiter defined.
        
        RK I have never seen this in use.'''
        ...
    
    @column_delimiter.setter
    def column_delimiter(self, value: str):
        ...
    
    @property
    def first_row_contains_column_names(self) -> bool:
        '''Specifies that a hosting application shall treat the first row of data in the specified external data
        source as a header row containing the names of each column in the data source.
        The default value is ``False``.
        
        RK I have never seen this in use.'''
        ...
    
    @first_row_contains_column_names.setter
    def first_row_contains_column_names(self, value: bool):
        ...
    
    @property
    def data_source(self) -> str:
        '''Specifies the location of the external data source to be connected to a document to perform the mail merge.
        The default value is an empty string.'''
        ...
    
    @data_source.setter
    def data_source(self, value: str):
        ...
    
    @property
    def table_name(self) -> str:
        '''Specifies the particular set of data that a source shall be connected to within an external data source.
        The default value is an empty string.'''
        ...
    
    @table_name.setter
    def table_name(self, value: str):
        ...
    
    @property
    def data_source_type(self) -> aspose.words.settings.OdsoDataSourceType:
        '''Specifies the type of the external data source to be connected to as part of the ODSO connection information for this mail merge.
        The default value is :attr:`OdsoDataSourceType.DEFAULT`.
        
        This setting is purely a suggestion of the data source type that is being used for this mail merge.'''
        ...
    
    @data_source_type.setter
    def data_source_type(self, value: aspose.words.settings.OdsoDataSourceType):
        ...
    
    @property
    def udl_connect_string(self) -> str:
        '''Specifies the Universal Data Link (UDL) connection string used to connect to an external data source.
        The default value is an empty string.'''
        ...
    
    @udl_connect_string.setter
    def udl_connect_string(self, value: str):
        ...
    
    @property
    def field_map_datas(self) -> aspose.words.settings.OdsoFieldMapDataCollection:
        '''Gets or sets a collection of objects that specify how columns from the external data source
        are mapped to the predefined merge field names in the document.
        This object is never ``None``.'''
        ...
    
    @field_map_datas.setter
    def field_map_datas(self, value: aspose.words.settings.OdsoFieldMapDataCollection):
        ...
    
    @property
    def recipient_datas(self) -> aspose.words.settings.OdsoRecipientDataCollection:
        '''Gets or sets a collection of objects that specify inclusion/exclusion of individual records in the mail merge.
        This object is never ``None``.'''
        ...
    
    @recipient_datas.setter
    def recipient_datas(self, value: aspose.words.settings.OdsoRecipientDataCollection):
        ...
    
    ...

class OdsoFieldMapData:
    '''Specifies how a column in the external data source shall be mapped to the predefined merge fields within the document.
    To learn more, visit the `Mail Merge and Reporting <https://docs.aspose.com/words/net/mail-merge-and-reporting/>` documentation article.
    
    Microsoft Word provides some predefined merge field names that it allows to insert into a document as MERGEFIELD or
    use in the ADDRESSBLOCK or GREETINGLINE fields. The information specified in :class:`OdsoFieldMapData`
    allows to map one column in the external data source to a single predefined merge field.'''
    
    def __init__(self):
        ...
    
    def clone(self) -> aspose.words.settings.OdsoFieldMapData:
        '''Returns a deep clone of this object.'''
        ...
    
    @property
    def column(self) -> int:
        '''Specifies the zero-based index of the column within an external data source which shall be
        mapped to the local name of a specific MERGEFIELD field.
        The default value is 0.'''
        ...
    
    @column.setter
    def column(self, value: int):
        ...
    
    @property
    def mapped_name(self) -> str:
        '''Specifies the predefined merge field name which shall be mapped to the column number
        specified by the :attr:`OdsoFieldMapData.column` property within this field mapping.
        The default value is an empty string.'''
        ...
    
    @mapped_name.setter
    def mapped_name(self, value: str):
        ...
    
    @property
    def name(self) -> str:
        '''Specifies the column name within an external data source for the column whose
        index is specified by the :attr:`OdsoFieldMapData.column` property.
        The default value is an empty string.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def type(self) -> aspose.words.settings.OdsoFieldMappingType:
        '''Specifies if a given mail merge field has been mapped to a column in the given external data source or not.
        The default value is :attr:`OdsoFieldMappingType.DEFAULT`.'''
        ...
    
    @type.setter
    def type(self, value: aspose.words.settings.OdsoFieldMappingType):
        ...
    
    ...

class OdsoFieldMapDataCollection:
    '''A typed collection of the :class:`OdsoFieldMapData` objects.
    To learn more, visit the `Mail Merge and Reporting <https://docs.aspose.com/words/net/mail-merge-and-reporting/>` documentation article.'''
    
    def __init__(self):
        ...
    
    def __getitem__(self, index: int) -> aspose.words.settings.OdsoFieldMapData:
        '''Gets or sets an item in this collection.'''
        ...
    
    def __setitem__(self, index: int, value: aspose.words.settings.OdsoFieldMapData):
        ...
    
    def add(self, value: aspose.words.settings.OdsoFieldMapData) -> int:
        '''Adds an object to the end of this collection.
        
        :param value: The object to add. Cannot be ``None``.'''
        ...
    
    def clear(self) -> None:
        '''Removes all elements from this collection.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes the element at the specified index.
        
        :param index: The zero-based index of the element.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of elements contained in the collection.'''
        ...
    
    ...

class OdsoRecipientData:
    '''Represents information about a single record within an external data source that is to be excluded from the mail merge.
    To learn more, visit the `Mail Merge and Reporting <https://docs.aspose.com/words/net/mail-merge-and-reporting/>` documentation article.
    
    If a record shall be merged into a merged document, then no information is needed about that record.
    However, if a given record shall not be merged into a merged document, then the value of the unique key
    for that record shall be stored in the :attr:`OdsoRecipientData.unique_tag` property of this object to indicate this exclusion.'''
    
    def __init__(self):
        ...
    
    def clone(self) -> aspose.words.settings.OdsoRecipientData:
        '''Returns a deep clone of this object.'''
        ...
    
    @property
    def active(self) -> bool:
        '''Specifies whether the record from the data source shall be imported into a document when the mail merge is performed.
        The default value is ``True``.'''
        ...
    
    @active.setter
    def active(self, value: bool):
        ...
    
    @property
    def column(self) -> int:
        '''Specifies the column within the data source that contains unique data for the current record.
        The default value is 0.'''
        ...
    
    @column.setter
    def column(self, value: int):
        ...
    
    @property
    def unique_tag(self) -> bytes:
        '''Specifies the contents of a given record in the column containing unique data.
        The default value is ``None``.'''
        ...
    
    @unique_tag.setter
    def unique_tag(self, value: bytes):
        ...
    
    @property
    def hash(self) -> int:
        '''Represents the hash code for this record.
        Sometimes Microsoft Word uses :attr:`OdsoRecipientData.hash` of a whole record instead of a :attr:`OdsoRecipientData.unique_tag` value.
        The default value is 0.'''
        ...
    
    @hash.setter
    def hash(self, value: int):
        ...
    
    ...

class OdsoRecipientDataCollection:
    '''A typed collection of :class:`OdsoRecipientData`To learn more, visit the `Mail Merge and Reporting <https://docs.aspose.com/words/net/mail-merge-and-reporting/>` documentation article.'''
    
    def __init__(self):
        ...
    
    def __getitem__(self, index: int) -> aspose.words.settings.OdsoRecipientData:
        '''Gets or sets an item in this collection.'''
        ...
    
    def __setitem__(self, index: int, value: aspose.words.settings.OdsoRecipientData):
        ...
    
    def add(self, value: aspose.words.settings.OdsoRecipientData) -> int:
        '''Adds an object to the end of this collection.
        
        :param value: The object to add. Cannot be ``None``.'''
        ...
    
    def clear(self) -> None:
        '''Removes all elements from this collection.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes the element at the specified index.
        
        :param index: The zero-based index of the element.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of elements contained in the collection.'''
        ...
    
    ...

class ViewOptions:
    '''Provides various options that control how a document is shown in Microsoft Word.
    To learn more, visit the `Work with Options and Appearance of Word Documents <https://docs.aspose.com/words/net/work-with-word-document-options-and-appearance/>` documentation article.'''
    
    @property
    def view_type(self) -> aspose.words.settings.ViewType:
        '''Controls the view mode in Microsoft Word.
        
        Although Aspose.Words is able to read and write this option, its usage is application-specific.
        For example MS Word 2013 does not respect the value of this option.'''
        ...
    
    @view_type.setter
    def view_type(self, value: aspose.words.settings.ViewType):
        ...
    
    @property
    def zoom_type(self) -> aspose.words.settings.ZoomType:
        '''Gets or sets a zoom value based on the size of the window.'''
        ...
    
    @zoom_type.setter
    def zoom_type(self, value: aspose.words.settings.ZoomType):
        ...
    
    @property
    def zoom_percent(self) -> int:
        '''Gets or sets the percentage (between 10 and 500) at which you want to view your document.
        
        If value is 0 then this property uses 100 instead, else if value is less than 10 or greater
        than 500 this property throws.
        
        Although Aspose.Words is able to read and write this option, its usage is application-specific.
        For example MS Word 2013 does not respect the value of this option.'''
        ...
    
    @zoom_percent.setter
    def zoom_percent(self, value: int):
        ...
    
    @property
    def do_not_display_page_boundaries(self) -> bool:
        '''Turns off display of the space between the top of the text and the top edge of the page.'''
        ...
    
    @do_not_display_page_boundaries.setter
    def do_not_display_page_boundaries(self, value: bool):
        ...
    
    @property
    def display_background_shape(self) -> bool:
        '''Controls display of the background shape in print layout view.'''
        ...
    
    @display_background_shape.setter
    def display_background_shape(self, value: bool):
        ...
    
    @property
    def forms_design(self) -> bool:
        '''Specifies whether the document is in forms design mode.
        
        Currently works only for documents in WordML format.'''
        ...
    
    @forms_design.setter
    def forms_design(self, value: bool):
        ...
    
    ...

class WriteProtection:
    '''Specifies write protection settings for a document.
    To learn more, visit the `Protect or Encrypt a Document <https://docs.aspose.com/words/net/protect-or-encrypt-a-document/>` documentation article.
    
    Write protection specifies whether the author has recommended that
    the document is to be opened as read-only and/or require a password to modify a document.
    
    Write protection is different from document protection. Write protection is specified in
    Microsoft Word in the options of the Save As dialog box.
    
    You do not create instances of this class directly. You access document protection settings
    via the :attr:`aspose.words.Document.write_protection` property.'''
    
    def set_password(self, password: str) -> None:
        '''Sets the write protection password for the document.
        
        If a password is set, Microsoft Word will require the user to enter it or open
        the document as read-only.
        
        :param password: The password to set. Cannot be ``None``, but can be an empty string.'''
        ...
    
    def validate_password(self, password: str) -> bool:
        '''Returns ``True`` if the specified password is the same as the write-protection password the document was protected with.
        If document is not write-protected with password then returns ``False``.'''
        ...
    
    @property
    def read_only_recommended(self) -> bool:
        '''Specifies whether the document author has recommended that the document be opened as read-only.'''
        ...
    
    @read_only_recommended.setter
    def read_only_recommended(self, value: bool):
        ...
    
    @property
    def is_write_protected(self) -> bool:
        '''Returns ``True`` when a write protection password is set.'''
        ...
    
    ...

class Compatibility:
    '''Specifies names of compatibility options.'''
    
    NO_TAB_HANG_IND: int
    NO_SPACE_RAISE_LOWER: int
    SUPPRESS_SP_BF_AFTER_PG_BRK: int
    WRAP_TRAIL_SPACES: int
    PRINT_COL_BLACK: int
    NO_COLUMN_BALANCE: int
    CONV_MAIL_MERGE_ESC: int
    SUPPRESS_TOP_SPACING: int
    USE_SINGLE_BORDERFOR_CONTIGUOUS_CELLS: int
    TRANSPARENT_METAFILES: int
    SHOW_BREAKS_IN_FRAMES: int
    SWAP_BORDERS_ODD_FACING_PGS: int
    DO_NOT_LEAVE_BACKSLASH_ALONE: int
    DO_NOT_EXPAND_ON_SHIFT_RETURN: int
    UL_TRAIL_SPACE: int
    BALANCE_SINGLE_BYTE_DOUBLE_BYTE_WIDTH: int
    SUPPRESS_TOP_SPACING_AT_TOP_OF_PAGE: int
    SPACING_IN_WHOLE_POINTS: int
    PRINT_BODY_TEXT_BEFORE_HEADER: int
    NO_LEADING: int
    SPACE_FOR_UL: int
    MW_SMALL_CAPS: int
    SUPPRESS_TOP_LINE_SPACING_WP: int
    TRUNCATE_FONT_HEIGHT_LIKE_WP6: int
    SUB_FONT_BY_SIZE: int
    LINE_WRAP_LIKE_WORD6: int
    DO_NOT_SUPPRESS_PARAGRAPH_BORDER: int
    NO_EXTRA_LINE_SPACING: int
    SUPPRESS_BOTTOM_SPACING: int
    WP_SPACE_WIDTH: int
    WP_JUSTIFICATION: int
    USE_PRINTER_METRICS: int
    SHAPE_LAYOUT_LIKE_WW8: int
    FOOTNOTE_LAYOUT_LIKE_WW8: int
    DO_NOT_USE_HTML_PARAGRAPH_AUTO_SPACING: int
    ADJUST_LINE_HEIGHT_IN_TABLE: int
    FORGET_LAST_TAB_ALIGNMENT: int
    AUTO_SPACE_LIKE_WORD95: int
    ALIGN_TABLE_ROW_BY_ROW: int
    LAYOUT_RAW_TABLE_WIDTH: int
    LAYOUT_TABLE_ROWS_APART: int
    USE_WORD97_LINE_BREAK_RULES: int
    DO_NOT_BREAK_WRAPPED_TABLES: int
    DO_NOT_SNAP_TO_GRID_IN_CELL: int
    SELECT_FLD_WITH_FIRST_OR_LAST_CHAR: int
    APPLY_BREAKING_RULES: int
    DO_NOT_WRAP_TEXT_WITH_PUNCT: int
    DO_NOT_USE_EAST_ASIAN_BREAK_RULES: int
    USE_WORD2002_TABLE_STYLE_RULES: int
    GROW_AUTOFIT: int
    USE_NORMAL_STYLE_FOR_LIST: int
    DO_NOT_USE_INDENT_AS_NUMBERING_TAB_STOP: int
    USE_ALT_KINSOKU_LINE_BREAK_RULES: int
    ALLOW_SPACE_OF_SAME_STYLE_IN_TABLE: int
    DO_NOT_SUPPRESS_INDENTATION: int
    DO_NOT_AUTOFIT_CONSTRAINED_TABLES: int
    AUTOFIT_TO_FIRST_FIXED_WIDTH_CELL: int
    UNDERLINE_TAB_IN_NUM_LIST: int
    DISPLAY_HANGUL_FIXED_WIDTH: int
    SPLIT_PG_BREAK_AND_PARA_MARK: int
    DO_NOT_VERT_ALIGN_CELL_WITH_SP: int
    DO_NOT_BREAK_CONSTRAINED_FORCED_TABLE: int
    DO_NOT_VERT_ALIGN_IN_TXBX: int
    USE_ANSI_KERNING_PAIRS: int
    CACHED_COL_BALANCE: int
    USE_FE_LAYOUT: int
    UI_COMPAT_97_TO_2003: int
    OVERRIDE_TABLE_STYLE_FONT_SIZE_AND_JUSTIFICATION: int
    DISABLE_OPEN_TYPE_FONT_FORMATTING_FEATURES: int
    SWAP_INSIDE_AND_OUTSIDE_FOR_MIRROR_INDENTS_AND_RELATIVE_POSITIONING: int
    USE_WORD2010_TABLE_STYLE_RULES: int

class JustificationMode:
    '''Specifies the character spacing adjustment for a document.
    The default value is ``Expand``.'''
    
    EXPAND: int
    COMPRESS: int
    COMPRESS_KANA: int

class MailMergeCheckErrors:
    '''Specifies how Microsoft Word will report errors detected during mail merge.'''
    
    SIMULATE: int
    PAUSE_ON_ERROR: int
    COLLECT_ERRORS: int
    DEFAULT: int

class MailMergeDataType:
    '''Specifies the type of an external mail merge data source.'''
    
    NONE: int
    TEXT_FILE: int
    DATABASE: int
    SPREADSHEET: int
    QUERY: int
    ODBC: int
    NATIVE: int
    DEFAULT: int

class MailMergeDestination:
    '''Specifies the possible results which may be generated when a mail merge is carried out on a document.'''
    
    NEW_DOCUMENT: int
    PRINTER: int
    EMAIL: int
    FAX: int
    DEFAULT: int

class MailMergeMainDocumentType:
    '''Specifies the possible types for a mail merge source document.'''
    
    NOT_A_MERGE_DOCUMENT: int
    FORM_LETTERS: int
    MAILING_LABELS: int
    ENVELOPES: int
    CATALOG: int
    EMAIL: int
    FAX: int
    DEFAULT: int

class MsWordVersion:
    '''Allows Aspose.Wods to mimic MS Word version-specific application behavior.'''
    
    WORD2000: int
    WORD2002: int
    WORD2003: int
    WORD2007: int
    WORD2010: int
    WORD2013: int
    WORD2016: int
    WORD2019: int

class MultiplePagesType:
    '''Specifies how document is printed out.'''
    
    NORMAL: int
    MIRROR_MARGINS: int
    TWO_PAGES_PER_SHEET: int
    BOOK_FOLD_PRINTING: int
    BOOK_FOLD_PRINTING_REVERSE: int
    DEFAULT: int

class OdsoDataSourceType:
    '''Specifies the type of the external data source to be connected to as part of the ODSO connection information.
    
    The OOXML specification is very vague for this enum. I guess it might correspond to the WdMergeSubType
    enumeration http://msdn.microsoft.com/en-us/library/bb237801.aspx.'''
    
    TEXT: int
    DATABASE: int
    ADDRESS_BOOK: int
    DOCUMENT1: int
    DOCUMENT2: int
    NATIVE: int
    EMAIL: int
    NONE: int
    LEGACY: int
    MASTER: int
    DEFAULT: int

class OdsoFieldMappingType:
    '''Specifies the possible types used to indicate if a given mail merge field has been mapped to a column in the given external data source.'''
    
    COLUMN: int
    NULL: int
    DEFAULT: int

class ViewType:
    '''Possible values for the view mode in Microsoft Word.'''
    
    NONE: int
    READING: int
    PAGE_LAYOUT: int
    OUTLINE: int
    NORMAL: int
    WEB: int

class ZoomType:
    '''Possible values for how large or small the document appears on the screen in Microsoft Word.'''
    
    CUSTOM: int
    NONE: int
    FULL_PAGE: int
    PAGE_WIDTH: int
    TEXT_FIT: int

