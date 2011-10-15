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
# from com.vaadin.data.util.filter.Compare.Equal import (Equal,)
# from com.vaadin.data.util.filter.Compare.Greater import (Greater,)
# from com.vaadin.data.util.filter.Compare.GreaterOrEqual import (GreaterOrEqual,)
# from com.vaadin.data.util.filter.Compare.Less import (Less,)
# from com.vaadin.data.util.filter.Compare.LessOrEqual import (LessOrEqual,)
# from java.util.Date import (Date,)
# from junit.framework.Assert import (Assert,)


class CompareFilterTest(AbstractFilterTest):
    itemNull = None
    itemEmpty = None
    itemA = None
    itemB = None
    itemC = None
    equalB = Equal(AbstractFilterTest.PROPERTY1, 'b')
    greaterB = Greater(AbstractFilterTest.PROPERTY1, 'b')
    lessB = Less(AbstractFilterTest.PROPERTY1, 'b')
    greaterEqualB = GreaterOrEqual(AbstractFilterTest.PROPERTY1, 'b')
    lessEqualB = LessOrEqual(AbstractFilterTest.PROPERTY1, 'b')
    equalNull = Equal(AbstractFilterTest.PROPERTY1, None)
    greaterNull = Greater(AbstractFilterTest.PROPERTY1, None)
    lessNull = Less(AbstractFilterTest.PROPERTY1, None)
    greaterEqualNull = GreaterOrEqual(AbstractFilterTest.PROPERTY1, None)
    lessEqualNull = LessOrEqual(AbstractFilterTest.PROPERTY1, None)

    def setUp(self):
        super(CompareFilterTest, self).setUp()
        self.itemNull = PropertysetItem()
        self.itemNull.addItemProperty(self.PROPERTY1, ObjectProperty(None, str))
        self.itemEmpty = PropertysetItem()
        self.itemEmpty.addItemProperty(self.PROPERTY1, ObjectProperty('', str))
        self.itemA = PropertysetItem()
        self.itemA.addItemProperty(self.PROPERTY1, ObjectProperty('a', str))
        self.itemB = PropertysetItem()
        self.itemB.addItemProperty(self.PROPERTY1, ObjectProperty('b', str))
        self.itemC = PropertysetItem()
        self.itemC.addItemProperty(self.PROPERTY1, ObjectProperty('c', str))

    def tearDown(self):
        super(CompareFilterTest, self).tearDown()
        self.itemNull = None
        self.itemEmpty = None
        self.itemA = None
        self.itemB = None

    def testCompareString(self):
        Assert.assertFalse(self.equalB.passesFilter(None, self.itemEmpty))
        Assert.assertFalse(self.equalB.passesFilter(None, self.itemA))
        Assert.assertTrue(self.equalB.passesFilter(None, self.itemB))
        Assert.assertFalse(self.equalB.passesFilter(None, self.itemC))
        Assert.assertFalse(self.greaterB.passesFilter(None, self.itemEmpty))
        Assert.assertFalse(self.greaterB.passesFilter(None, self.itemA))
        Assert.assertFalse(self.greaterB.passesFilter(None, self.itemB))
        Assert.assertTrue(self.greaterB.passesFilter(None, self.itemC))
        Assert.assertTrue(self.lessB.passesFilter(None, self.itemEmpty))
        Assert.assertTrue(self.lessB.passesFilter(None, self.itemA))
        Assert.assertFalse(self.lessB.passesFilter(None, self.itemB))
        Assert.assertFalse(self.lessB.passesFilter(None, self.itemC))
        Assert.assertFalse(self.greaterEqualB.passesFilter(None, self.itemEmpty))
        Assert.assertFalse(self.greaterEqualB.passesFilter(None, self.itemA))
        Assert.assertTrue(self.greaterEqualB.passesFilter(None, self.itemB))
        Assert.assertTrue(self.greaterEqualB.passesFilter(None, self.itemC))
        Assert.assertTrue(self.lessEqualB.passesFilter(None, self.itemEmpty))
        Assert.assertTrue(self.lessEqualB.passesFilter(None, self.itemA))
        Assert.assertTrue(self.lessEqualB.passesFilter(None, self.itemB))
        Assert.assertFalse(self.lessEqualB.passesFilter(None, self.itemC))

    def testCompareWithNull(self):
        # null comparisons: null is less than any other value
        Assert.assertFalse(self.equalB.passesFilter(None, self.itemNull))
        Assert.assertTrue(self.greaterB.passesFilter(None, self.itemNull))
        Assert.assertFalse(self.lessB.passesFilter(None, self.itemNull))
        Assert.assertTrue(self.greaterEqualB.passesFilter(None, self.itemNull))
        Assert.assertFalse(self.lessEqualB.passesFilter(None, self.itemNull))
        Assert.assertTrue(self.equalNull.passesFilter(None, self.itemNull))
        Assert.assertFalse(self.greaterNull.passesFilter(None, self.itemNull))
        Assert.assertFalse(self.lessNull.passesFilter(None, self.itemNull))
        Assert.assertTrue(self.greaterEqualNull.passesFilter(None, self.itemNull))
        Assert.assertTrue(self.lessEqualNull.passesFilter(None, self.itemNull))
        Assert.assertFalse(self.equalNull.passesFilter(None, self.itemA))
        Assert.assertFalse(self.greaterNull.passesFilter(None, self.itemA))
        Assert.assertTrue(self.lessNull.passesFilter(None, self.itemA))
        Assert.assertFalse(self.greaterEqualNull.passesFilter(None, self.itemA))
        Assert.assertTrue(self.lessEqualNull.passesFilter(None, self.itemA))

    def testCompareInteger(self):
        negative = -1
        zero = 0
        positive = 1
        itemNegative = PropertysetItem()
        itemNegative.addItemProperty(self.PROPERTY1, ObjectProperty(negative, int))
        itemZero = PropertysetItem()
        itemZero.addItemProperty(self.PROPERTY1, ObjectProperty(zero, int))
        itemPositive = PropertysetItem()
        itemPositive.addItemProperty(self.PROPERTY1, ObjectProperty(positive, int))
        equalZero = Equal(self.PROPERTY1, zero)
        Assert.assertFalse(equalZero.passesFilter(None, itemNegative))
        Assert.assertTrue(equalZero.passesFilter(None, itemZero))
        Assert.assertFalse(equalZero.passesFilter(None, itemPositive))
        isPositive = Greater(self.PROPERTY1, zero)
        Assert.assertFalse(isPositive.passesFilter(None, itemNegative))
        Assert.assertFalse(isPositive.passesFilter(None, itemZero))
        Assert.assertTrue(isPositive.passesFilter(None, itemPositive))
        isNegative = Less(self.PROPERTY1, zero)
        Assert.assertTrue(isNegative.passesFilter(None, itemNegative))
        Assert.assertFalse(isNegative.passesFilter(None, itemZero))
        Assert.assertFalse(isNegative.passesFilter(None, itemPositive))
        isNonNegative = GreaterOrEqual(self.PROPERTY1, zero)
        Assert.assertFalse(isNonNegative.passesFilter(None, itemNegative))
        Assert.assertTrue(isNonNegative.passesFilter(None, itemZero))
        Assert.assertTrue(isNonNegative.passesFilter(None, itemPositive))
        isNonPositive = LessOrEqual(self.PROPERTY1, zero)
        Assert.assertTrue(isNonPositive.passesFilter(None, itemNegative))
        Assert.assertTrue(isNonPositive.passesFilter(None, itemZero))
        Assert.assertFalse(isNonPositive.passesFilter(None, itemPositive))

    def testCompareDate(self):
        now = Date()
        # new Date() is only accurate to the millisecond, so repeating it gives
        # the same date
        earlier = Date(now.getTime() - 1)
        later = Date(now.getTime() + 1)
        itemEarlier = PropertysetItem()
        itemEarlier.addItemProperty(self.PROPERTY1, ObjectProperty(earlier, Date))
        itemNow = PropertysetItem()
        itemNow.addItemProperty(self.PROPERTY1, ObjectProperty(now, Date))
        itemLater = PropertysetItem()
        itemLater.addItemProperty(self.PROPERTY1, ObjectProperty(later, Date))
        equalNow = Equal(self.PROPERTY1, now)
        Assert.assertFalse(equalNow.passesFilter(None, itemEarlier))
        Assert.assertTrue(equalNow.passesFilter(None, itemNow))
        Assert.assertFalse(equalNow.passesFilter(None, itemLater))
        after = Greater(self.PROPERTY1, now)
        Assert.assertFalse(after.passesFilter(None, itemEarlier))
        Assert.assertFalse(after.passesFilter(None, itemNow))
        Assert.assertTrue(after.passesFilter(None, itemLater))
        before = Less(self.PROPERTY1, now)
        Assert.assertTrue(before.passesFilter(None, itemEarlier))
        Assert.assertFalse(before.passesFilter(None, itemNow))
        Assert.assertFalse(before.passesFilter(None, itemLater))
        afterOrNow = GreaterOrEqual(self.PROPERTY1, now)
        Assert.assertFalse(afterOrNow.passesFilter(None, itemEarlier))
        Assert.assertTrue(afterOrNow.passesFilter(None, itemNow))
        Assert.assertTrue(afterOrNow.passesFilter(None, itemLater))
        beforeOrNow = LessOrEqual(self.PROPERTY1, now)
        Assert.assertTrue(beforeOrNow.passesFilter(None, itemEarlier))
        Assert.assertTrue(beforeOrNow.passesFilter(None, itemNow))
        Assert.assertFalse(beforeOrNow.passesFilter(None, itemLater))

    def testCompareAppliesToProperty(self):
        filterA = Equal('a', 1)
        filterB = Equal('b', 1)
        Assert.assertTrue(filterA.appliesToProperty('a'))
        Assert.assertFalse(filterA.appliesToProperty('b'))
        Assert.assertFalse(filterB.appliesToProperty('a'))
        Assert.assertTrue(filterB.appliesToProperty('b'))

    def testCompareEqualsHashCode(self):
        # most checks with Equal filter, then only some with others
        equalNull2 = Equal(self.PROPERTY1, None)
        equalNullProperty2 = Equal(self.PROPERTY2, None)
        equalEmpty = Equal(self.PROPERTY1, '')
        equalEmpty2 = Equal(self.PROPERTY1, '')
        equalEmptyProperty2 = Equal(self.PROPERTY2, '')
        equalA = Equal(self.PROPERTY1, 'a')
        equalB2 = Equal(self.PROPERTY1, 'b')
        equalBProperty2 = Equal(self.PROPERTY2, 'b')
        greaterEmpty = Greater(self.PROPERTY1, '')
        # equals()
        Assert.assertEquals(self.equalNull, self.equalNull)
        Assert.assertEquals(self.equalNull, equalNull2)
        Assert.assertFalse(self.equalNull == equalNullProperty2)
        Assert.assertFalse(self.equalNull == equalEmpty)
        Assert.assertFalse(self.equalNull == self.equalB)
        Assert.assertEquals(equalEmpty, equalEmpty)
        Assert.assertFalse(equalEmpty == self.equalNull)
        Assert.assertEquals(equalEmpty, equalEmpty2)
        Assert.assertFalse(equalEmpty == equalEmptyProperty2)
        Assert.assertFalse(equalEmpty == self.equalB)
        Assert.assertEquals(self.equalB, self.equalB)
        Assert.assertFalse(self.equalB == self.equalNull)
        Assert.assertFalse(self.equalB == equalEmpty)
        Assert.assertEquals(self.equalB, equalB2)
        Assert.assertFalse(self.equalB == equalBProperty2)
        Assert.assertFalse(self.equalB == equalA)
        Assert.assertEquals(self.greaterB, self.greaterB)
        Assert.assertFalse(self.greaterB == self.lessB)
        Assert.assertFalse(self.greaterB == self.greaterEqualB)
        Assert.assertFalse(self.greaterB == self.lessEqualB)
        Assert.assertFalse(self.greaterNull == greaterEmpty)
        Assert.assertFalse(self.greaterNull == self.greaterB)
        Assert.assertFalse(greaterEmpty == self.greaterNull)
        Assert.assertFalse(greaterEmpty == self.greaterB)
        Assert.assertFalse(self.greaterB == self.greaterNull)
        Assert.assertFalse(self.greaterB == greaterEmpty)
        # hashCode()
        Assert.assertEquals(self.equalNull.hashCode(), equalNull2.hashCode())
        Assert.assertEquals(equalEmpty.hashCode(), equalEmpty2.hashCode())
        Assert.assertEquals(self.equalB.hashCode(), equalB2.hashCode())
