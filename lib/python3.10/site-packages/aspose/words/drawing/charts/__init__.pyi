import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class AxisBound:
    '''Represents minimum or maximum bound of axis values.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.
    
    Bound can be specified as a numeric, datetime or a special "auto" value.
    
    The instances of this class are immutable.'''
    
    @overload
    def __init__(self):
        '''Creates a new instance indicating that axis bound should be determined automatically by a word-processing
        application.'''
        ...
    
    @overload
    def __init__(self, value: float):
        '''Creates an axis bound represented as a number.'''
        ...
    
    @overload
    def __init__(self, datetime: datetime.datetime):
        '''Creates an axis bound represented as datetime value.'''
        ...
    
    @property
    def is_auto(self) -> bool:
        '''Returns a flag indicating that axis bound should be determined automatically.'''
        ...
    
    @property
    def value(self) -> float:
        '''Returns numeric value of axis bound.'''
        ...
    
    @property
    def value_as_date(self) -> datetime.datetime:
        '''Returns value of axis bound represented as datetime.'''
        ...
    
    ...

class AxisDisplayUnit:
    '''Provides access to the scaling options of the display units for the value axis.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    def __init__(self):
        ...
    
    @property
    def unit(self) -> aspose.words.drawing.charts.AxisBuiltInUnit:
        '''Gets or sets the scaling value of the display units as one of the predefined values.
        
        Default value is :attr:`AxisBuiltInUnit.NONE`. The :attr:`AxisBuiltInUnit.CUSTOM` and
        :attr:`AxisBuiltInUnit.PERCENTAGE` values are not available in some chart types; see
        :class:`AxisBuiltInUnit` for more information.'''
        ...
    
    @unit.setter
    def unit(self, value: aspose.words.drawing.charts.AxisBuiltInUnit):
        ...
    
    @property
    def custom_unit(self) -> float:
        '''Gets or sets a user-defined divisor to scale display units on the value axis.
        
        The property is not supported by MS Office 2016 new charts. Default value is 1.
        
        Setting this property sets the :attr:`AxisDisplayUnit.unit` property to
        :attr:`AxisBuiltInUnit.CUSTOM`.'''
        ...
    
    @custom_unit.setter
    def custom_unit(self, value: float):
        ...
    
    @property
    def document(self) -> aspose.words.DocumentBase:
        '''Returns the Document the title holder belongs.'''
        ...
    
    ...

class AxisScaling:
    '''Represents the scaling options of the axis.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    def __init__(self):
        ...
    
    @property
    def type(self) -> aspose.words.drawing.charts.AxisScaleType:
        '''Gets or sets scaling type of the axis.
        
        The :attr:`AxisScaleType.LINEAR` value is the only that is allowed in MS Office 2016 new charts.'''
        ...
    
    @type.setter
    def type(self, value: aspose.words.drawing.charts.AxisScaleType):
        ...
    
    @property
    def log_base(self) -> float:
        '''Gets or sets the logarithmic base for a logarithmic axis.
        
        The property is not supported by MS Office 2016 new charts.
        
        Valid range of a floating point value is greater than or equal to 2 and less than or
        equal to 1000. The property has effect only if :attr:`AxisScaling.type` is set to
        :attr:`AxisScaleType.LOGARITHMIC`.
        
        Setting this property sets the :attr:`AxisScaling.type` property to :attr:`AxisScaleType.LOGARITHMIC`.'''
        ...
    
    @log_base.setter
    def log_base(self, value: float):
        ...
    
    @property
    def minimum(self) -> aspose.words.drawing.charts.AxisBound:
        '''Gets or sets minimum value of the axis.
        
        The default value is "auto".'''
        ...
    
    @minimum.setter
    def minimum(self, value: aspose.words.drawing.charts.AxisBound):
        ...
    
    @property
    def maximum(self) -> aspose.words.drawing.charts.AxisBound:
        '''Gets or sets the maximum value of the axis.
        
        The default value is "auto".'''
        ...
    
    @maximum.setter
    def maximum(self, value: aspose.words.drawing.charts.AxisBound):
        ...
    
    ...

class Chart:
    '''Provides access to the chart shape properties.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def series(self) -> aspose.words.drawing.charts.ChartSeriesCollection:
        '''Provides access to series collection.'''
        ...
    
    @property
    def title(self) -> aspose.words.drawing.charts.ChartTitle:
        '''Provides access to the chart title properties.'''
        ...
    
    @property
    def legend(self) -> aspose.words.drawing.charts.ChartLegend:
        '''Provides access to the chart legend properties.'''
        ...
    
    @property
    def axis_x(self) -> aspose.words.drawing.charts.ChartAxis:
        '''Provides access to properties of the X axis of the chart.'''
        ...
    
    @property
    def axis_y(self) -> aspose.words.drawing.charts.ChartAxis:
        '''Provides access to properties of the Y axis of the chart.'''
        ...
    
    @property
    def axis_z(self) -> aspose.words.drawing.charts.ChartAxis:
        '''Provides access to properties of the Z axis of the chart.'''
        ...
    
    @property
    def source_full_name(self) -> str:
        '''Gets the path and name of an xls/xlsx file this chart is linked to.'''
        ...
    
    @source_full_name.setter
    def source_full_name(self, value: str):
        ...
    
    ...

class ChartAxis:
    '''Represents the axis options of the chart.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def type(self) -> aspose.words.drawing.charts.ChartAxisType:
        '''Returns type of the axis.'''
        ...
    
    @property
    def category_type(self) -> aspose.words.drawing.charts.AxisCategoryType:
        '''Gets or sets type of the category axis.
        
        Only text categories (:attr:`AxisCategoryType.CATEGORY`) are allowed in MS Office 2016 new charts.'''
        ...
    
    @category_type.setter
    def category_type(self, value: aspose.words.drawing.charts.AxisCategoryType):
        ...
    
    @property
    def crosses(self) -> aspose.words.drawing.charts.AxisCrosses:
        '''Specifies how this axis crosses the perpendicular axis.
        
        Default value is :attr:`AxisCrosses.AUTOMATIC`.
        
        The property is not supported by MS Office 2016 new charts.'''
        ...
    
    @crosses.setter
    def crosses(self, value: aspose.words.drawing.charts.AxisCrosses):
        ...
    
    @property
    def crosses_at(self) -> float:
        '''Specifies where on the perpendicular axis the axis crosses.
        
        The property has effect only if :attr:`ChartAxis.crosses` are set to :attr:`AxisCrosses.CUSTOM`.
        It is not supported by MS Office 2016 new charts.
        
        The units are determined by the type of axis. When the axis is a value axis, the value of the property
        is a decimal number on the value axis. When the axis is a time category axis, the value is defined as
        an integer number of days relative to the base date (30/12/1899). For a text category axis, the value is
        an integer category number, starting with 1 as the first category.'''
        ...
    
    @crosses_at.setter
    def crosses_at(self, value: float):
        ...
    
    @property
    def reverse_order(self) -> bool:
        '''Returns or sets a flag indicating whether values of axis should be displayed in reverse order, i.e.
        from max to min.
        
        The property is not supported by MS Office 2016 new charts. Default value is ``False``.'''
        ...
    
    @reverse_order.setter
    def reverse_order(self, value: bool):
        ...
    
    @property
    def major_tick_mark(self) -> aspose.words.drawing.charts.AxisTickMark:
        '''Returns or sets the major tick marks.'''
        ...
    
    @major_tick_mark.setter
    def major_tick_mark(self, value: aspose.words.drawing.charts.AxisTickMark):
        ...
    
    @property
    def minor_tick_mark(self) -> aspose.words.drawing.charts.AxisTickMark:
        '''Returns or sets the minor tick marks for the axis.'''
        ...
    
    @minor_tick_mark.setter
    def minor_tick_mark(self, value: aspose.words.drawing.charts.AxisTickMark):
        ...
    
    @property
    def tick_label_position(self) -> aspose.words.drawing.charts.AxisTickLabelPosition:
        '''Returns or sets the position of the tick labels on the axis.
        
        The property is not supported by MS Office 2016 new charts.'''
        ...
    
    @tick_label_position.setter
    def tick_label_position(self, value: aspose.words.drawing.charts.AxisTickLabelPosition):
        ...
    
    @property
    def major_unit(self) -> float:
        '''Returns or sets the distance between major tick marks.
        
        Valid range of a value is greater than zero. The property has effect for time category and
        value axes.
        
        Setting this property sets the :attr:`ChartAxis.major_unit_is_auto` property to ``False``.'''
        ...
    
    @major_unit.setter
    def major_unit(self, value: float):
        ...
    
    @property
    def major_unit_is_auto(self) -> bool:
        '''Gets or sets a flag indicating whether default distance between major tick marks shall be used.
        
        The property has effect for time category and value axes.'''
        ...
    
    @major_unit_is_auto.setter
    def major_unit_is_auto(self, value: bool):
        ...
    
    @property
    def major_unit_scale(self) -> aspose.words.drawing.charts.AxisTimeUnit:
        '''Returns or sets the scale value for major tick marks on the time category axis.
        
        The property has effect only for time category axes.'''
        ...
    
    @major_unit_scale.setter
    def major_unit_scale(self, value: aspose.words.drawing.charts.AxisTimeUnit):
        ...
    
    @property
    def minor_unit(self) -> float:
        '''Returns or sets the distance between minor tick marks.
        
        Valid range of a value is greater than zero. The property has effect for time category and
        value axes.
        
        Setting this property sets the :attr:`ChartAxis.minor_unit_is_auto` property to ``False``.'''
        ...
    
    @minor_unit.setter
    def minor_unit(self, value: float):
        ...
    
    @property
    def minor_unit_is_auto(self) -> bool:
        '''Gets or sets a flag indicating whether default distance between minor tick marks shall be used.
        
        The property has effect for time category and value axes.'''
        ...
    
    @minor_unit_is_auto.setter
    def minor_unit_is_auto(self, value: bool):
        ...
    
    @property
    def minor_unit_scale(self) -> aspose.words.drawing.charts.AxisTimeUnit:
        '''Returns or sets the scale value for minor tick marks on the time category axis.
        
        The property has effect only for time category axes.'''
        ...
    
    @minor_unit_scale.setter
    def minor_unit_scale(self, value: aspose.words.drawing.charts.AxisTimeUnit):
        ...
    
    @property
    def base_time_unit(self) -> aspose.words.drawing.charts.AxisTimeUnit:
        '''Returns or sets the smallest time unit that is represented on the time category axis.
        
        The property has effect only for time category axes.'''
        ...
    
    @base_time_unit.setter
    def base_time_unit(self, value: aspose.words.drawing.charts.AxisTimeUnit):
        ...
    
    @property
    def number_format(self) -> aspose.words.drawing.charts.ChartNumberFormat:
        '''Returns a :class:`ChartNumberFormat` object that allows defining number formats for the axis.'''
        ...
    
    @property
    def tick_label_offset(self) -> int:
        '''Gets or sets the distance of labels from the axis.
        
        The property represents a percentage of the default label offset.
        
        Valid range is from 0 to 1000 percent inclusive. Default value is 100%.
        
        The property has effect only for category axes. It is not supported by MS Office 2016 new charts.'''
        ...
    
    @tick_label_offset.setter
    def tick_label_offset(self, value: int):
        ...
    
    @property
    def display_unit(self) -> aspose.words.drawing.charts.AxisDisplayUnit:
        '''Specifies the scaling value of the display units for the value axis.
        
        The property has effect only for value axes.'''
        ...
    
    @property
    def axis_between_categories(self) -> bool:
        '''Gets or sets a flag indicating whether the value axis crosses the category axis between categories.
        
        The property has effect only for value axes. It is not supported by MS Office 2016 new charts.'''
        ...
    
    @axis_between_categories.setter
    def axis_between_categories(self, value: bool):
        ...
    
    @property
    def scaling(self) -> aspose.words.drawing.charts.AxisScaling:
        '''Provides access to the scaling options of the axis.'''
        ...
    
    @property
    def tick_label_spacing(self) -> int:
        '''Gets or sets the interval, at which tick labels are drawn.
        
        The property has effect for text category and series axes. It is not supported by MS Office 2016
        new charts. Valid range of a value is greater than or equal to 1.
        
        Setting this property sets the :attr:`ChartAxis.tick_label_spacing_is_auto` property to ``False``.'''
        ...
    
    @tick_label_spacing.setter
    def tick_label_spacing(self, value: int):
        ...
    
    @property
    def tick_label_spacing_is_auto(self) -> bool:
        '''Gets or sets a flag indicating whether automatic interval of drawing tick labels shall be used.
        
        Default value is ``True``.
        
        The property has effect for text category and series axes. It is not supported by MS Office 2016
        new charts.'''
        ...
    
    @tick_label_spacing_is_auto.setter
    def tick_label_spacing_is_auto(self, value: bool):
        ...
    
    @property
    def tick_label_alignment(self) -> aspose.words.ParagraphAlignment:
        '''Gets or sets text alignment of axis tick labels.
        
        This property has effect only for multi-line labels.
        
        Default value is :attr:`aspose.words.ParagraphAlignment.CENTER`.
        
        .'''
        ...
    
    @tick_label_alignment.setter
    def tick_label_alignment(self, value: aspose.words.ParagraphAlignment):
        ...
    
    @property
    def tick_mark_spacing(self) -> int:
        '''Gets or sets the interval, at which tick marks are drawn.
        
        The property has effect for text category and series axes. It is not supported by MS Office 2016
        new charts.
        
        Valid range of a value is greater than or equal to 1.'''
        ...
    
    @tick_mark_spacing.setter
    def tick_mark_spacing(self, value: int):
        ...
    
    @property
    def hidden(self) -> bool:
        '''Gets or sets a flag indicating whether this axis is hidden or not.
        
        Default value is ``False``.'''
        ...
    
    @hidden.setter
    def hidden(self, value: bool):
        ...
    
    @property
    def document(self) -> aspose.words.DocumentBase:
        '''Returns the Document the title holder belongs.'''
        ...
    
    ...

class ChartDataLabel:
    '''Represents data label on a chart point or trendline.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.
    
    On a series, the :class:`ChartDataLabel` object is a member of the :class:`ChartDataLabelCollection`.
    The :class:`ChartDataLabelCollection` contains a :class:`ChartDataLabel` object for each point.'''
    
    def clear_format(self) -> None:
        '''Clears format of this data label. The properties are set to the default values defined in the parent data
        label collection.'''
        ...
    
    @property
    def index(self) -> int:
        '''Specifies the index of the containing element.
        This index shall determine which of the parent's children collection this element applies to.
        Default value is 0.'''
        ...
    
    @property
    def show_category_name(self) -> bool:
        '''Allows to specify if category name is to be displayed for the data labels on a chart.
        Default value is ``False``.'''
        ...
    
    @show_category_name.setter
    def show_category_name(self, value: bool):
        ...
    
    @property
    def show_bubble_size(self) -> bool:
        '''Allows to specify if bubble size is to be displayed for the data labels on a chart.
        Applies only to Bubble charts.
        Default value is ``False``.'''
        ...
    
    @show_bubble_size.setter
    def show_bubble_size(self, value: bool):
        ...
    
    @property
    def show_legend_key(self) -> bool:
        '''Allows to specify if legend key is to be displayed for the data labels on a chart.
        Default value is ``False``.'''
        ...
    
    @show_legend_key.setter
    def show_legend_key(self, value: bool):
        ...
    
    @property
    def show_percentage(self) -> bool:
        '''Allows to specify if percentage value is to be displayed for the data labels on a chart.
        Default value is ``False``.'''
        ...
    
    @show_percentage.setter
    def show_percentage(self, value: bool):
        ...
    
    @property
    def show_series_name(self) -> bool:
        '''Returns or sets a Boolean to indicate the series name display behavior for the data labels on a chart.
        ``True`` to show the series name; ``False`` to hide. By default ``False``.'''
        ...
    
    @show_series_name.setter
    def show_series_name(self, value: bool):
        ...
    
    @property
    def show_value(self) -> bool:
        '''Allows to specify if values are to be displayed in the data labels.
        Default value is ``False``.'''
        ...
    
    @show_value.setter
    def show_value(self, value: bool):
        ...
    
    @property
    def show_leader_lines(self) -> bool:
        '''Allows to specify if data label leader lines need be shown.
        Default value is ``False``.
        
        Applies to Pie charts only.
        Leader lines create a visual connection between a data label and its corresponding data point.'''
        ...
    
    @show_leader_lines.setter
    def show_leader_lines(self, value: bool):
        ...
    
    @property
    def show_data_labels_range(self) -> bool:
        '''Allows to specify if values from data labels range to be displayed in the data labels.
        Default value is ``False``.'''
        ...
    
    @show_data_labels_range.setter
    def show_data_labels_range(self, value: bool):
        ...
    
    @property
    def separator(self) -> str:
        '''Gets or sets string separator used for the data labels on a chart.
        The default is a comma, except for pie charts showing only category name and percentage, when a line break
        shall be used instead.'''
        ...
    
    @separator.setter
    def separator(self, value: str):
        ...
    
    @property
    def is_visible(self) -> bool:
        '''Returns ``True`` if this data label has something to display.'''
        ...
    
    @property
    def number_format(self) -> aspose.words.drawing.charts.ChartNumberFormat:
        '''Returns number format of the parent element.'''
        ...
    
    @property
    def is_hidden(self) -> bool:
        '''Gets/sets a flag indicating whether this label is hidden.
        The default value is ``False``.'''
        ...
    
    @is_hidden.setter
    def is_hidden(self, value: bool):
        ...
    
    @property
    def font(self) -> aspose.words.Font:
        '''Provides access to the font formatting of this data label.'''
        ...
    
    ...

class ChartDataLabelCollection:
    '''Represents a collection of :class:`ChartDataLabel`.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.drawing.charts.ChartDataLabel:
        '''Returns :class:`ChartDataLabel` for the specified index.'''
        ...
    
    def clear_format(self) -> None:
        '''Clears format of all :class:`ChartDataLabel` in this collection.'''
        ...
    
    @property
    def count(self) -> int:
        '''Returns the number of :class:`ChartDataLabel` in this collection.'''
        ...
    
    @property
    def show_category_name(self) -> bool:
        '''Allows to specify whether category name is to be displayed for the data labels of the entire series.
        Default value is ``False``.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_category_name` property.'''
        ...
    
    @show_category_name.setter
    def show_category_name(self, value: bool):
        ...
    
    @property
    def show_bubble_size(self) -> bool:
        '''Allows to specify whether bubble size is to be displayed for the data labels of the entire series.
        Applies only to Bubble charts.
        Default value is ``False``.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_bubble_size` property.'''
        ...
    
    @show_bubble_size.setter
    def show_bubble_size(self, value: bool):
        ...
    
    @property
    def show_legend_key(self) -> bool:
        '''Allows to specify whether legend key is to be displayed for the data labels of the entire series.
        Default value is ``False``.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_legend_key` property.'''
        ...
    
    @show_legend_key.setter
    def show_legend_key(self, value: bool):
        ...
    
    @property
    def show_percentage(self) -> bool:
        '''Allows to specify whether percentage value is to be displayed for the data labels of the entire series.
        Default value is ``False``. Applies only to Pie charts.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_percentage` property.'''
        ...
    
    @show_percentage.setter
    def show_percentage(self, value: bool):
        ...
    
    @property
    def show_series_name(self) -> bool:
        '''Returns or sets a Boolean to indicate the series name display behavior for the data labels of the entire series.
        ``True`` to show the series name; ``False`` to hide. By default ``False``.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_series_name` property.'''
        ...
    
    @show_series_name.setter
    def show_series_name(self, value: bool):
        ...
    
    @property
    def show_value(self) -> bool:
        '''Allows to specify whether values are to be displayed in the data labels of the entire series.
        Default value is ``False``.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_value` property.'''
        ...
    
    @show_value.setter
    def show_value(self, value: bool):
        ...
    
    @property
    def show_leader_lines(self) -> bool:
        '''Allows to specify whether data label leader lines need be shown for the data labels of the entire series.
        Default value is ``False``.
        
        Applies to Pie charts only.
        Leader lines create a visual connection between a data label and its corresponding data point.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_leader_lines` property.'''
        ...
    
    @show_leader_lines.setter
    def show_leader_lines(self, value: bool):
        ...
    
    @property
    def show_data_labels_range(self) -> bool:
        '''Allows to specify whether values from data labels range to be displayed in the data labels of the entire series.
        Default value is ``False``.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.show_data_labels_range` property.'''
        ...
    
    @show_data_labels_range.setter
    def show_data_labels_range(self, value: bool):
        ...
    
    @property
    def separator(self) -> str:
        '''Gets or sets string separator used for the data labels of the entire series.
        The default is a comma, except for pie charts showing only category name and percentage, when a line break
        shall be used instead.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.separator` property.'''
        ...
    
    @separator.setter
    def separator(self, value: str):
        ...
    
    @property
    def number_format(self) -> aspose.words.drawing.charts.ChartNumberFormat:
        '''Gets an :class:`ChartNumberFormat` instance allowing to set number format for the data labels of the
        entire series.'''
        ...
    
    @property
    def font(self) -> aspose.words.Font:
        '''Provides access to the font formatting of the data labels of the entire series.
        
        Value defined for this property can be overridden for an individual data label with using the
        :attr:`ChartDataLabel.font` property.'''
        ...
    
    ...

class ChartDataPoint:
    '''Allows to specify formatting of a single data point on the chart.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.
    
    On a series, the :class:`ChartDataPoint` object is a member of the :class:`ChartDataPointCollection`.
    The :class:`ChartDataPointCollection` contains a :class:`ChartDataPoint` object for each point.'''
    
    def clear_format(self) -> None:
        '''Clears format of this data point. The properties are set to the default values defined in the parent series.'''
        ...
    
    @property
    def index(self) -> int:
        '''Index of the data point this object applies formatting to.'''
        ...
    
    @property
    def format(self) -> aspose.words.drawing.charts.ChartFormat:
        '''Provides access to fill and line formatting of this data point.'''
        ...
    
    ...

class ChartDataPointCollection:
    '''Represents collection of a :class:`ChartDataPoint`.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.drawing.charts.ChartDataPoint:
        '''Returns :class:`ChartDataPoint` for the specified index.'''
        ...
    
    def clear_format(self) -> None:
        '''Clears format of all :class:`ChartDataPoint` in this collection.'''
        ...
    
    @property
    def count(self) -> int:
        '''Returns the number of :class:`ChartDataPoint` in this collection.'''
        ...
    
    ...

class ChartFormat:
    '''Represents the formatting of a chart element.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def fill(self) -> aspose.words.drawing.Fill:
        '''Gets fill formatting for the parent chart element.'''
        ...
    
    @property
    def stroke(self) -> aspose.words.drawing.Stroke:
        '''Gets line formatting for the parent chart element.'''
        ...
    
    ...

class ChartLegend:
    '''Represents chart legend properties.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    def __init__(self):
        '''Initializes a new instance of the :class:`ChartLegend` class.'''
        ...
    
    @property
    def legend_entries(self) -> aspose.words.drawing.charts.ChartLegendEntryCollection:
        '''Returns a collection of legend entries for all series and trendlines of the parent chart.'''
        ...
    
    @property
    def position(self) -> aspose.words.drawing.charts.LegendPosition:
        '''Specifies the position of the legend on a chart.
        Default value is :attr:`LegendPosition.RIGHT`.'''
        ...
    
    @position.setter
    def position(self, value: aspose.words.drawing.charts.LegendPosition):
        ...
    
    @property
    def overlay(self) -> bool:
        '''Determines whether other chart elements shall be allowed to overlap legend.
        Default value is ``False``.'''
        ...
    
    @overlay.setter
    def overlay(self, value: bool):
        ...
    
    ...

class ChartLegendEntry:
    '''Represents a chart legend entry.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.
    
    A legend entry corresponds to a specific chart series or trendline.
    
    The text of the entry is the name of the series or trendline. The text cannot be changed.'''
    
    @property
    def is_hidden(self) -> bool:
        '''Gets or sets a value indicating whether this entry is hidden in the chart legend.
        The default value is **false**.
        
        When a chart legend entry is hidden, it does not affect the corresponding chart series or trendline that
        is still displayed on the chart.'''
        ...
    
    @is_hidden.setter
    def is_hidden(self, value: bool):
        ...
    
    @property
    def font(self) -> aspose.words.Font:
        '''Provides access to the font formatting of this legend entry.'''
        ...
    
    ...

class ChartLegendEntryCollection:
    '''Represents a collection of chart legend entries.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.drawing.charts.ChartLegendEntry:
        '''Returns :class:`ChartLegendEntry` for the specified index.'''
        ...
    
    @property
    def count(self) -> int:
        '''Returns the number of :class:`ChartLegendEntry` in this collection.'''
        ...
    
    ...

class ChartMarker:
    '''Represents a chart data marker.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def symbol(self) -> aspose.words.drawing.charts.MarkerSymbol:
        '''Gets or sets chart marker symbol.'''
        ...
    
    @symbol.setter
    def symbol(self, value: aspose.words.drawing.charts.MarkerSymbol):
        ...
    
    @property
    def size(self) -> int:
        '''Gets or sets chart marker size.
        Default value is 7.'''
        ...
    
    @size.setter
    def size(self, value: int):
        ...
    
    @property
    def format(self) -> aspose.words.drawing.charts.ChartFormat:
        '''Provides access to fill and line formatting of this marker.'''
        ...
    
    ...

class ChartNumberFormat:
    '''Represents number formatting of the parent element.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def format_code(self) -> str:
        '''Gets or sets the format code applied to a data label.
        
        Number formatting is used to change the way a value appears in data label and can be used in some very creative ways.
        The examples of number formats:
        Number - "#,##0.00"
        
        Currency - "\\"$\\"#,##0.00"
        
        Time - "[$-x-systime]h:mm:ss AM/PM"
        
        Date - "d/mm/yyyy"
        
        Percentage - "0.00%"
        
        Fraction - "# ?/?"
        
        Scientific - "0.00E+00"
        
        Text - "@"
        
        Accounting - "_-\\"$\\"\* #,##0.00_-;-\\"$\\"\* #,##0.00_-;_-\\"$\\"\* \\"-\\"??_-;_-@_-"
        
        Custom with color - "[Red]-#,##0.0"'''
        ...
    
    @format_code.setter
    def format_code(self, value: str):
        ...
    
    @property
    def is_linked_to_source(self) -> bool:
        '''Specifies whether the format code is linked to a source cell.
        Default is true.
        
        The NumberFormat will be reset to general if format code is linked to source.'''
        ...
    
    @is_linked_to_source.setter
    def is_linked_to_source(self, value: bool):
        ...
    
    ...

class ChartSeries:
    '''Represents chart series properties.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def data_points(self) -> aspose.words.drawing.charts.ChartDataPointCollection:
        '''Returns a collection of formatting objects for all data points in this series.'''
        ...
    
    @property
    def name(self) -> str:
        '''Gets or sets the name of the series, if name is not set explicitly it is generated using index.
        By default returns Series plus one based index.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def smooth(self) -> bool:
        '''Allows to specify whether the line connecting the points on the chart shall be smoothed using Catmull-Rom splines.'''
        ...
    
    @smooth.setter
    def smooth(self, value: bool):
        ...
    
    @property
    def has_data_labels(self) -> bool:
        '''Gets or sets a flag indicating whether data labels are displayed for the series.'''
        ...
    
    @has_data_labels.setter
    def has_data_labels(self, value: bool):
        ...
    
    @property
    def data_labels(self) -> aspose.words.drawing.charts.ChartDataLabelCollection:
        '''Specifies the settings for the data labels for the entire series.'''
        ...
    
    @property
    def format(self) -> aspose.words.drawing.charts.ChartFormat:
        '''Provides access to fill and line formatting of the series.'''
        ...
    
    @property
    def legend_entry(self) -> aspose.words.drawing.charts.ChartLegendEntry:
        '''Gets a legend entry for this chart series.'''
        ...
    
    ...

class ChartSeriesCollection:
    '''Represents collection of a :class:`ChartSeries`.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    def __getitem__(self, index: int) -> aspose.words.drawing.charts.ChartSeries:
        '''Returns a :class:`ChartSeries` at the specified index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the collection.'''
        ...
    
    @overload
    def add(self, series_name: str, categories: list[str], values: list[float]) -> aspose.words.drawing.charts.ChartSeries:
        '''Adds new :class:`ChartSeries` to this collection.
        Use this method to add series to any type of Bar, Column, Line and Surface charts.
        
        :returns: Recently added :class:`ChartSeries` object.'''
        ...
    
    @overload
    def add(self, series_name: str, x_values: list[float], y_values: list[float]) -> aspose.words.drawing.charts.ChartSeries:
        '''Adds new :class:`ChartSeries` to this collection.
        Use this method to add series to any type of Scatter charts.
        
        :returns: Recently added :class:`ChartSeries` object.'''
        ...
    
    @overload
    def add(self, series_name: str, dates: list[datetime.datetime], values: list[float]) -> aspose.words.drawing.charts.ChartSeries:
        '''Adds new :class:`ChartSeries` to this collection.
        Use this method to add series to any type of Area, Radar and Stock charts.'''
        ...
    
    @overload
    def add(self, series_name: str, x_values: list[float], y_values: list[float], bubble_sizes: list[float]) -> aspose.words.drawing.charts.ChartSeries:
        '''Adds new :class:`ChartSeries` to this collection.
        Use this method to add series to any type of Bubble charts.
        
        :returns: Recently added :class:`ChartSeries` object.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes a :class:`ChartSeries` at the specified index.
        
        :param index: The zero-based index of the :class:`ChartSeries` to remove.'''
        ...
    
    def clear(self) -> None:
        '''Removes all :class:`ChartSeries` from this collection.'''
        ...
    
    def add_double(self, series_name: str, x_values: list[float], y_values: list[float]) -> aspose.words.drawing.charts.ChartSeries:
        ...
    
    def add_date(self, series_name: str, dates: list[datetime.datetime], values: list[float]) -> aspose.words.drawing.charts.ChartSeries:
        ...
    
    @property
    def count(self) -> int:
        '''Returns the number of :class:`ChartSeries` in this collection.'''
        ...
    
    ...

class ChartTitle:
    '''Provides access to the chart title properties.
    To learn more, visit the `Working with Charts <https://docs.aspose.com/words/net/working-with-charts/>` documentation article.'''
    
    @property
    def text(self) -> str:
        '''Gets or sets the text of the chart title.
        If ``None`` or empty value is specified, auto generated title will be shown.
        
        Use :attr:`ChartTitle.show` option if you need to hide the Title.'''
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    @property
    def overlay(self) -> bool:
        '''Determines whether other chart elements shall be allowed to overlap title.
        By default overlay is ``False``.'''
        ...
    
    @overlay.setter
    def overlay(self, value: bool):
        ...
    
    @property
    def show(self) -> bool:
        '''Determines whether the title shall be shown for this chart.
        Default value is ``True``.'''
        ...
    
    @show.setter
    def show(self, value: bool):
        ...
    
    ...

class IChartDataPoint:
    '''Contains properties of a single data point on the chart.'''
    
    @property
    def explosion(self) -> int:
        '''Specifies the amount the data point shall be moved from the center of the pie.
        Can be negative, negative means that property is not set and no explosion should be applied.
        Applies only to Pie charts.'''
        ...
    
    @explosion.setter
    def explosion(self, value: int):
        ...
    
    @property
    def invert_if_negative(self) -> bool:
        '''Specifies whether the parent element shall inverts its colors if the value is negative.'''
        ...
    
    @invert_if_negative.setter
    def invert_if_negative(self, value: bool):
        ...
    
    @property
    def marker(self) -> aspose.words.drawing.charts.ChartMarker:
        '''Specifies a data marker. Marker is automatically created when requested.'''
        ...
    
    @property
    def bubble_3d(self) -> bool:
        '''Specifies whether the bubbles in Bubble chart should have a 3-D effect applied to them.'''
        ...
    
    @bubble_3d.setter
    def bubble_3d(self, value: bool):
        ...
    
    ...

class AxisBuiltInUnit:
    '''Specifies the display units for an axis.'''
    
    NONE: int
    CUSTOM: int
    BILLIONS: int
    HUNDRED_MILLIONS: int
    HUNDREDS: int
    HUNDRED_THOUSANDS: int
    MILLIONS: int
    TEN_MILLIONS: int
    TEN_THOUSANDS: int
    THOUSANDS: int
    TRILLIONS: int
    PERCENTAGE: int

class AxisCategoryType:
    '''Specifies type of a category axis.'''
    
    AUTOMATIC: int
    CATEGORY: int
    TIME: int

class AxisCrosses:
    '''Specifies the possible crossing points for an axis.'''
    
    AUTOMATIC: int
    MAXIMUM: int
    MINIMUM: int
    CUSTOM: int

class AxisScaleType:
    '''Specifies the possible scale types for an axis.'''
    
    LINEAR: int
    LOGARITHMIC: int

class AxisTickLabelPosition:
    '''Specifies the possible positions for tick labels.'''
    
    HIGH: int
    LOW: int
    NEXT_TO_AXIS: int
    NONE: int
    DEFAULT: int

class AxisTickMark:
    '''Specifies the possible positions for tick marks.'''
    
    CROSS: int
    INSIDE: int
    OUTSIDE: int
    NONE: int

class AxisTimeUnit:
    '''Specifies the unit of time for axes.'''
    
    AUTOMATIC: int
    DAYS: int
    MONTHS: int
    YEARS: int

class ChartAxisType:
    '''Specifies type of chart axis.'''
    
    CATEGORY: int
    SERIES: int
    VALUE: int

class ChartType:
    '''Specifies type of a chart.'''
    
    AREA: int
    AREA_STACKED: int
    AREA_PERCENT_STACKED: int
    AREA_3D: int
    AREA_3D_STACKED: int
    AREA_3D_PERCENT_STACKED: int
    BAR: int
    BAR_STACKED: int
    BAR_PERCENT_STACKED: int
    BAR_3D: int
    BAR_3D_STACKED: int
    BAR_3D_PERCENT_STACKED: int
    BUBBLE: int
    BUBBLE_3D: int
    COLUMN: int
    COLUMN_STACKED: int
    COLUMN_PERCENT_STACKED: int
    COLUMN_3D: int
    COLUMN_3D_STACKED: int
    COLUMN_3D_PERCENT_STACKED: int
    COLUMN_3D_CLUSTERED: int
    DOUGHNUT: int
    LINE: int
    LINE_STACKED: int
    LINE_PERCENT_STACKED: int
    LINE_3D: int
    PIE: int
    PIE_3D: int
    PIE_OF_BAR: int
    PIE_OF_PIE: int
    RADAR: int
    SCATTER: int
    STOCK: int
    SURFACE: int
    SURFACE_3D: int

class LegendPosition:
    '''Specifies the possible positions for a chart legend.'''
    
    NONE: int
    BOTTOM: int
    LEFT: int
    RIGHT: int
    TOP: int
    TOP_RIGHT: int

class MarkerSymbol:
    '''Specifies marker symbol style.'''
    
    DEFAULT: int
    CIRCLE: int
    DASH: int
    DIAMOND: int
    DOT: int
    NONE: int
    PICTURE: int
    PLUS: int
    SQUARE: int
    STAR: int
    TRIANGLE: int
    X: int

