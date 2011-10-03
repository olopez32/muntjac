# -*- coding: utf-8 -*-


class ComboBoxPlainExample(VerticalLayout, Property.ValueChangeListener):
    _cities = ['Berlin', 'Brussels', 'Helsinki', 'Madrid', 'Oslo', 'Paris', 'Stockholm']

    def __init__(self):
        # Shows a notification when a selection is made.
        self.setSpacing(True)
        l = ComboBox('Please select a city')
        _0 = True
        i = 0
        while True:
            if _0 is True:
                _0 = False
            else:
                i += 1
            if not (i < len(self._cities)):
                break
            l.addItem(self._cities[i])
        l.setFilteringMode(Filtering.FILTERINGMODE_OFF)
        l.setImmediate(True)
        l.addListener(self)
        self.addComponent(l)

    def valueChange(self, event):
        self.getWindow().showNotification('Selected city: ' + event.getProperty())