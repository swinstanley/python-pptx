# encoding: utf-8

"""
Legend of a chart.
"""

from __future__ import absolute_import, print_function, unicode_literals

from ..enum.chart import XL_LEGEND_POSITION


class Legend(object):
    """
    Represents the legend in a chart. A chart can have at most one legend.
    """
    def __init__(self, legend_elm):
        super(Legend, self).__init__()
        self._element = legend_elm

    @property
    def horz_offset(self):
        """
        Adjustment of the x position of the legend from its default.
        Expressed as a float between -1.0 and 1.0 representing a fraction of
        the chart width. Negative values move the legend left, positive
        values move it to the right. |None| if no setting is specified.
        """
        return self._element.horz_offset

    @horz_offset.setter
    def horz_offset(self, value):
        self._element.horz_offset = value

    @property
    def include_in_layout(self):
        """
        Read/write boolean specifying whether the legend should occupy the
        chart layout space, causing it to overlap the chart.
        """
        overlay = self._element.overlay
        if overlay is None:
            return True
        return overlay.val

    @include_in_layout.setter
    def include_in_layout(self, value):
        self._element.get_or_add_overlay().val = bool(value)

    @property
    def position(self):
        """
        Read/write :ref:`XlLegendPosition` enumeration value specifying the
        general region of the chart in which to place the legend.
        """
        legendPos = self._element.legendPos
        if legendPos is None:
            return XL_LEGEND_POSITION.RIGHT
        return legendPos.val

    @position.setter
    def position(self, position):
        self._element.get_or_add_legendPos().val = position