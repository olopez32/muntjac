# Copyright (C) 2010 IT Mill Ltd.
# Copyright (C) 2011 Richard Lincoln
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __pyjamas__ import (ARGERROR,)
# from com.vaadin.data.Container.Filter import (Filter,)
# from com.vaadin.data.Item import (Item,)
# from com.vaadin.data.Property import (Property,)
# from com.vaadin.data.util.ObjectProperty import (ObjectProperty,)
# from com.vaadin.data.util.PropertysetItem import (PropertysetItem,)
# from junit.framework.TestCase import (TestCase,)


class AbstractFilterTest(TestCase):
    PROPERTY1 = 'property1'
    PROPERTY2 = 'property2'

    def TestItem(AbstractFilterTest_this, *args, **kwargs):

        class TestItem(PropertysetItem):

            def __init__(self, value1, value2):
                self.addItemProperty(AbstractFilterTest_this.PROPERTY1, ObjectProperty(value1))
                self.addItemProperty(AbstractFilterTest_this.PROPERTY2, ObjectProperty(value2))

        return TestItem(*args, **kwargs)

    class NullProperty(Property):

        def getValue(self):
            return None

        def setValue(self, newValue):
            raise self.ReadOnlyException()

        def getType(self):
            return str

        def isReadOnly(self):
            return True

        def setReadOnly(self, newStatus):
            # do nothing
            pass

    class SameItemFilter(Filter):
        _item = None
        _propertyId = None

        def __init__(self, *args):
            _0 = args
            _1 = len(args)
            if _1 == 1:
                item, = _0
                self.__init__(item, '')
            elif _1 == 2:
                item, propertyId = _0
                self._item = item
                self._propertyId = propertyId
            else:
                raise ARGERROR(1, 2)

        def passesFilter(self, itemId, item):
            return self._item == item

        def appliesToProperty(self, propertyId):
            return self._propertyId == propertyId if self._propertyId is not None else True

        def equals(self, obj):
            if (obj is None) or (not (self.getClass() == obj.getClass())):
                return False
            other = obj
            return self._item == other.item and other.propertyId is None if self._propertyId is None else self._propertyId == other.propertyId

        def hashCode(self):
            return self._item.hashCode()
