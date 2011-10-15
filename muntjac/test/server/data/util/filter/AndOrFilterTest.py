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

from com.vaadin.data.util.filter.AbstractFilterTest import (AbstractFilterTest,)
# from com.vaadin.data.util.filter.Or import (Or,)
# from junit.framework.Assert import (Assert,)


class AndOrFilterTest(AbstractFilterTest):
    item1 = BeanItem(1)
    item2 = BeanItem(2)

    def testNoFilterAnd(self):
        filter = And()
        Assert.assertTrue(filter.passesFilter(None, self.item1))

    def testSingleFilterAnd(self):
        filter = And(self.SameItemFilter(self.item1))
        Assert.assertTrue(filter.passesFilter(None, self.item1))
        Assert.assertFalse(filter.passesFilter(None, self.item2))

    def testTwoFilterAnd(self):
        filter1 = And(self.SameItemFilter(self.item1), self.SameItemFilter(self.item1))
        filter2 = And(self.SameItemFilter(self.item1), self.SameItemFilter(self.item2))
        Assert.assertTrue(filter1.passesFilter(None, self.item1))
        Assert.assertFalse(filter1.passesFilter(None, self.item2))
        Assert.assertFalse(filter2.passesFilter(None, self.item1))
        Assert.assertFalse(filter2.passesFilter(None, self.item2))

    def testThreeFilterAnd(self):
        filter1 = And(self.SameItemFilter(self.item1), self.SameItemFilter(self.item1), self.SameItemFilter(self.item1))
        filter2 = And(self.SameItemFilter(self.item1), self.SameItemFilter(self.item1), self.SameItemFilter(self.item2))
        Assert.assertTrue(filter1.passesFilter(None, self.item1))
        Assert.assertFalse(filter1.passesFilter(None, self.item2))
        Assert.assertFalse(filter2.passesFilter(None, self.item1))
        Assert.assertFalse(filter2.passesFilter(None, self.item2))

    def testNoFilterOr(self):
        filter = Or()
        Assert.assertFalse(filter.passesFilter(None, self.item1))

    def testSingleFilterOr(self):
        filter = Or(self.SameItemFilter(self.item1))
        Assert.assertTrue(filter.passesFilter(None, self.item1))
        Assert.assertFalse(filter.passesFilter(None, self.item2))

    def testTwoFilterOr(self):
        filter1 = Or(self.SameItemFilter(self.item1), self.SameItemFilter(self.item1))
        filter2 = Or(self.SameItemFilter(self.item1), self.SameItemFilter(self.item2))
        Assert.assertTrue(filter1.passesFilter(None, self.item1))
        Assert.assertFalse(filter1.passesFilter(None, self.item2))
        Assert.assertTrue(filter2.passesFilter(None, self.item1))
        Assert.assertTrue(filter2.passesFilter(None, self.item2))

    def testThreeFilterOr(self):
        filter1 = Or(self.SameItemFilter(self.item1), self.SameItemFilter(self.item1), self.SameItemFilter(self.item1))
        filter2 = Or(self.SameItemFilter(self.item1), self.SameItemFilter(self.item1), self.SameItemFilter(self.item2))
        Assert.assertTrue(filter1.passesFilter(None, self.item1))
        Assert.assertFalse(filter1.passesFilter(None, self.item2))
        Assert.assertTrue(filter2.passesFilter(None, self.item1))
        Assert.assertTrue(filter2.passesFilter(None, self.item2))

    def testAndEqualsHashCode(self):
        filter0 = And()
        filter0b = And()
        filter1a = And(self.SameItemFilter(self.item1))
        filter1a2 = And(self.SameItemFilter(self.item1))
        filter1b = And(self.SameItemFilter(self.item2))
        filter2a = And(self.SameItemFilter(self.item1), self.SameItemFilter(self.item1))
        filter2b = And(self.SameItemFilter(self.item1), self.SameItemFilter(self.item2))
        filter2b2 = And(self.SameItemFilter(self.item1), self.SameItemFilter(self.item2))
        other0 = Or()
        other1 = Or(self.SameItemFilter(self.item1))
        Assert.assertEquals(filter0, filter0)
        Assert.assertEquals(filter0, filter0b)
        Assert.assertFalse(filter0 == filter1a)
        Assert.assertFalse(filter0 == other0)
        Assert.assertFalse(filter0 == other1)
        Assert.assertFalse(filter1a == filter1b)
        Assert.assertFalse(filter1a == other1)
        Assert.assertFalse(filter1a == filter2a)
        Assert.assertFalse(filter2a == filter1a)
        Assert.assertFalse(filter2a == filter2b)
        Assert.assertEquals(filter2b, filter2b2)
        # hashCode()
        Assert.assertEquals(filter0.hashCode(), filter0.hashCode())
        Assert.assertEquals(filter0.hashCode(), filter0b.hashCode())
        Assert.assertEquals(filter1a.hashCode(), filter1a.hashCode())
        Assert.assertEquals(filter1a.hashCode(), filter1a2.hashCode())
        Assert.assertEquals(filter2a.hashCode(), filter2a.hashCode())
        Assert.assertEquals(filter2b.hashCode(), filter2b2.hashCode())

    def testOrEqualsHashCode(self):
        filter0 = Or()
        filter0b = Or()
        filter1a = Or(self.SameItemFilter(self.item1))
        filter1a2 = Or(self.SameItemFilter(self.item1))
        filter1b = Or(self.SameItemFilter(self.item2))
        filter2a = Or(self.SameItemFilter(self.item1), self.SameItemFilter(self.item1))
        filter2b = Or(self.SameItemFilter(self.item1), self.SameItemFilter(self.item2))
        filter2b2 = Or(self.SameItemFilter(self.item1), self.SameItemFilter(self.item2))
        other0 = And()
        other1 = And(self.SameItemFilter(self.item1))
        Assert.assertEquals(filter0, filter0)
        Assert.assertEquals(filter0, filter0b)
        Assert.assertFalse(filter0 == filter1a)
        Assert.assertFalse(filter0 == other0)
        Assert.assertFalse(filter0 == other1)
        Assert.assertFalse(filter1a == filter1b)
        Assert.assertFalse(filter1a == other1)
        Assert.assertFalse(filter1a == filter2a)
        Assert.assertFalse(filter2a == filter1a)
        Assert.assertFalse(filter2a == filter2b)
        Assert.assertEquals(filter2b, filter2b2)
        # hashCode()
        Assert.assertEquals(filter0.hashCode(), filter0.hashCode())
        Assert.assertEquals(filter0.hashCode(), filter0b.hashCode())
        Assert.assertEquals(filter1a.hashCode(), filter1a.hashCode())
        Assert.assertEquals(filter1a.hashCode(), filter1a2.hashCode())
        Assert.assertEquals(filter2a.hashCode(), filter2a.hashCode())
        Assert.assertEquals(filter2b.hashCode(), filter2b2.hashCode())

    def testAndAppliesToProperty(self):
        filter0 = And()
        filter1a = And(self.SameItemFilter(self.item1, 'a'))
        filter1b = And(self.SameItemFilter(self.item1, 'b'))
        filter2aa = And(self.SameItemFilter(self.item1, 'a'), self.SameItemFilter(self.item1, 'a'))
        filter2ab = And(self.SameItemFilter(self.item1, 'a'), self.SameItemFilter(self.item1, 'b'))
        filter3abc = And(self.SameItemFilter(self.item1, 'a'), self.SameItemFilter(self.item1, 'b'), self.SameItemFilter(self.item1, 'c'))
        # empty And does not filter out anything
        Assert.assertFalse(filter0.appliesToProperty('a'))
        Assert.assertFalse(filter0.appliesToProperty('d'))
        Assert.assertTrue(filter1a.appliesToProperty('a'))
        Assert.assertFalse(filter1a.appliesToProperty('b'))
        Assert.assertFalse(filter1b.appliesToProperty('a'))
        Assert.assertTrue(filter1b.appliesToProperty('b'))
        Assert.assertTrue(filter2aa.appliesToProperty('a'))
        Assert.assertFalse(filter2aa.appliesToProperty('b'))
        Assert.assertTrue(filter2ab.appliesToProperty('a'))
        Assert.assertTrue(filter2ab.appliesToProperty('b'))
        Assert.assertTrue(filter3abc.appliesToProperty('a'))
        Assert.assertTrue(filter3abc.appliesToProperty('b'))
        Assert.assertTrue(filter3abc.appliesToProperty('c'))
        Assert.assertFalse(filter3abc.appliesToProperty('d'))

    def testOrAppliesToProperty(self):
        filter0 = Or()
        filter1a = Or(self.SameItemFilter(self.item1, 'a'))
        filter1b = Or(self.SameItemFilter(self.item1, 'b'))
        filter2aa = Or(self.SameItemFilter(self.item1, 'a'), self.SameItemFilter(self.item1, 'a'))
        filter2ab = Or(self.SameItemFilter(self.item1, 'a'), self.SameItemFilter(self.item1, 'b'))
        filter3abc = Or(self.SameItemFilter(self.item1, 'a'), self.SameItemFilter(self.item1, 'b'), self.SameItemFilter(self.item1, 'c'))
        # empty Or filters out everything
        Assert.assertTrue(filter0.appliesToProperty('a'))
        Assert.assertTrue(filter0.appliesToProperty('d'))
        Assert.assertTrue(filter1a.appliesToProperty('a'))
        Assert.assertFalse(filter1a.appliesToProperty('b'))
        Assert.assertFalse(filter1b.appliesToProperty('a'))
        Assert.assertTrue(filter1b.appliesToProperty('b'))
        Assert.assertTrue(filter2aa.appliesToProperty('a'))
        Assert.assertFalse(filter2aa.appliesToProperty('b'))
        Assert.assertTrue(filter2ab.appliesToProperty('a'))
        Assert.assertTrue(filter2ab.appliesToProperty('b'))
        Assert.assertTrue(filter3abc.appliesToProperty('a'))
        Assert.assertTrue(filter3abc.appliesToProperty('b'))
        Assert.assertTrue(filter3abc.appliesToProperty('c'))
        Assert.assertFalse(filter3abc.appliesToProperty('d'))
