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


class ListSet(list):
    """ListSet is an internal Vaadin class which implements a combination of a List
    and a Set. The main purpose of this class is to provide a list with a fast
    {@link #contains(Object)} method. Each inserted object must by unique (as
    specified by {@link #equals(Object)}). The {@link #set(int, Object)} method
    allows duplicates because of the way {@link Collections#sort(java.util.List)}
    works.

    This class is subject to change and should not be used outside Vaadin core.
    """

    def __init__(self, *args):
        self._itemSet = None

        # Contains a map from an element to the number of duplicates it has. Used
        # to temporarily allow duplicates in the list.
        self._duplicates = dict()

        nargs = len(args)
        if nargs == 0:
            super(ListSet, self).__init__()
            self._itemSet = set()
        elif nargs == 1:
            if isinstance(args[0], int):
                initialCapacity, = args
                super(ListSet, self).__init__(initialCapacity)
                self._itemSet = set(initialCapacity)
            else:
                c, = args
                super(ListSet, self).__init__(c)
                self._itemSet = set(len(c))
                self._itemSet.union(c)
        else:
            raise ValueError, 'too many arguments'

    # Delegate contains operations to the set

    def contains(self, o):
        return o in self._itemSet


    def containsAll(self, c):
        for cc in c:
            if cc not in self._itemSet:
                return False
        else:
            return True

    # Methods for updating the set when the list is updated.
    def add(self, *args):
        """None
        ---
        Works as java.util.ArrayList#add(int, java.lang.Object) but returns
        immediately if the element is already in the ListSet.
        """
        nargs = len(args)
        if nargs == 1:
            e, = args
            if e in self:
                # Duplicates are not allowed
                return False
            if super(ListSet, self).add(e):
                self._itemSet.add(e)
                return True
            else:
                return False
        elif nargs == 2:
            index, element = args
            if element in self:
                # Duplicates are not allowed
                return
            super(ListSet, self).insert(index, element)
            self._itemSet.add(element)
        else:
            raise ValueError, 'invalid number of arguments'


    def addAll(self, *args):
        nargs = len(args)
        if nargs == 1:
            c, = args
            modified = False
            for e in i:
                if e in self:
                    continue
                if self.add(e):
                    self._itemSet.add(e)
                    modified = True
            return modified
        elif nargs == 2:
            index, c = args
            self.ensureCapacity(len(self) + len(c))
            modified = False
            for e in c:
                if e in self:
                    continue
                self.add(index, e)
                index += 1
                self._itemSet.add(e)
                modified = True
            return modified
        else:
            raise ValueError, 'invalid number of arguments'


    def clear(self):
        super(ListSet, self).clear()
        self._itemSet.clear()


    def indexOf(self, o):
        if o not in self:
            return -1
        return super(ListSet, self).index(o)


    def lastIndexOf(self, o):
        if o not in self:
            return -1
        return super(ListSet, self).rindex(o)


    def remove(self, o):
        if isinstance(o, int):
            index = o
            e = super(ListSet, self).remove(index)
            if e is not None:
                self._itemSet.remove(e)
            return e

        else:
            if super(ListSet, self).remove(o):
                self._itemSet.remove(o)
                return True
            else:
                return False


    def removeRange(self, fromIndex, toIndex):
        toRemove = set()
        for idx in range(fromIndex, toIndex):
            toRemove.add(self.get(idx))
        super(ListSet, self).removeRange(fromIndex, toIndex)
        for r in toRemove:
            self._itemSet.remove(r)


    def set(self, index, element):  #@PydevCodeAnalysisIgnore
        if element in self:
            # Element already exist in the list
            if self.get(index) == element:
                # At the same position, nothing to be done
                return element
            else:
                # Adding at another position. We assume this is a sort
                # operation and temporarily allow it.
                # We could just remove (null) the old element and keep the list
                # unique. This would require finding the index of the old
                # element (indexOf(element)) which is not a fast operation in a
                # list. So we instead allow duplicates temporarily.
                self.addDuplicate(element)

        old = super(ListSet, self).set(index, element)
        self.removeFromSet(old)
        self._itemSet.add(element)
        return old


    def removeFromSet(self, e):
        """Removes "e" from the set if it no longer exists in the list.

        @param e
        """
        dupl = self._duplicates.get(e)
        if dupl is not None:
            # A duplicate was present so we only decrement the duplicate count
            # and continue
            if dupl == 1:
                # This is what always should happen. A sort sets the items one
                # by one, temporarily breaking the uniqueness requirement.
                del self._duplicates[e]
            else:
                self._duplicates[e] = dupl - 1
        else:
            # The "old" value is no longer in the list.
            self._itemSet.remove(e)


    def addDuplicate(self, element):
        """Marks the "element" can be found more than once from the list.
        Allowed in {@link #set(int, Object)} to make sorting work.

        @param element
        """
        nr = self._duplicates.get(element)
        if nr is None:
            nr = 1
        else:
            nr += 1

        # Store the number of duplicates of this element so we know later on if
        # we should remove an element from the set or if it was a duplicate (in
        # removeFromSet)
        self._duplicates[element] = nr


    def clone(self):
        v = super(ListSet, self).clone()
        v.itemSet = set(self._itemSet)
        return v
