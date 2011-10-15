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
from com.vaadin.data.util.AbstractContainerTest import (AbstractContainerTest,)
# from com.vaadin.data.Container.Hierarchical import (Hierarchical,)


class AbstractHierarchicalContainerTest(AbstractContainerTest):

    def validateHierarchicalContainer(self, container, expectedFirstItemId, expectedLastItemId, itemIdInSet, itemIdNotInSet, checkGetItemNull, expectedSize, expectedRootSize, rootsHaveChildren):
        """@param container
                   The container to validate
        @param expectedFirstItemId
                   Expected first item id
        @param expectedLastItemId
                   Expected last item id
        @param itemIdInSet
                   An item id that is in the container
        @param itemIdNotInSet
                   An item id that is not in the container
        @param checkGetItemNull
                   true if getItem() should return null for itemIdNotInSet, false
                   to skip the check (container.containsId() is checked in any
                   case)
        @param expectedSize
                   Expected number of items in the container. Not related to
                   hierarchy.
        @param expectedTraversalSize
                   Expected number of items found when traversing from the roots
                   down to all available nodes.
        @param expectedRootSize
                   Expected number of root items
        @param rootsHaveChildren
                   true if all roots have children, false otherwise (skips some
                   asserts)
        """
        self.validateContainer(container, expectedFirstItemId, expectedLastItemId, itemIdInSet, itemIdNotInSet, checkGetItemNull, expectedSize)
        # rootItemIds
        rootIds = container.rootItemIds()
        self.assertEquals(expectedRootSize, len(rootIds))
        for rootId in rootIds:
            # All roots must be in container
            self.assertTrue(container.containsId(rootId))
            # All roots must have no parent
            self.assertNull(container.getParent(rootId))
            # all roots must be roots
            self.assertTrue(container.isRoot(rootId))
            if rootsHaveChildren:
                # all roots have children allowed in this case
                self.assertTrue(container.areChildrenAllowed(rootId))
                # all roots have children in this case
                children = container.getChildren(rootId)
                self.assertNotNull(rootId + ' should have children', children)
                self.assertTrue(rootId + ' should have children', len(children) > 0)
                # getParent
                for childId in children:
                    self.assertEquals(container.getParent(childId), rootId)
        # isRoot should return false for unknown items
        self.assertFalse(container.isRoot(itemIdNotInSet))
        # hasChildren should return false for unknown items
        self.assertFalse(container.hasChildren(itemIdNotInSet))
        # areChildrenAllowed should return false for unknown items
        self.assertFalse(container.areChildrenAllowed(itemIdNotInSet))
        # removeItem of unknown items should return false
        self.assertFalse(container.removeItem(itemIdNotInSet))
        self.assertEquals(expectedSize, self.countNodes(container))
        self.validateHierarchy(container)

    def countNodes(self, *args):
        _0 = args
        _1 = len(args)
        if _1 == 1:
            container, = _0
            totalNodes = 0
            for rootId in container.rootItemIds():
                totalNodes += self.countNodes(container, rootId)
            return totalNodes
        elif _1 == 2:
            container, itemId = _0
            nodes = 1
            # This
            children = container.getChildren(itemId)
            if children is not None:
                for id in children:
                    nodes += self.countNodes(container, id)
            return nodes
        else:
            raise ARGERROR(1, 2)

    def validateHierarchy(self, *args):
        _0 = args
        _1 = len(args)
        if _1 == 1:
            container, = _0
            for rootId in container.rootItemIds():
                self.validateHierarchy(container, rootId, None)
        elif _1 == 3:
            container, itemId, parentId = _0
            children = container.getChildren(itemId)
            # getParent
            self.assertEquals(container.getParent(itemId), parentId)
            if not container.areChildrenAllowed(itemId):
                # If no children is allowed the item should have no children
                self.assertFalse(container.hasChildren(itemId))
                self.assertTrue((children is None) or (len(children) == 0))
                return
            if children is not None:
                for id in children:
                    self.validateHierarchy(container, id, itemId)
        else:
            raise ARGERROR(1, 3)

    def testHierarchicalContainer(self, container):
        self.initializeContainer(container)
        packages = 21 + 3
        expectedSize = self.sampleData.length + packages
        self.validateHierarchicalContainer(container, 'com', 'org.vaadin.test.LastClass', 'com.vaadin.terminal.ApplicationResource', 'blah', True, expectedSize, 2, True)

    def testHierarchicalSorting(self, container):
        sortable = container
        self.initializeContainer(container)
        # Must be able to sort based on PROP1 and PROP2 for this test
        self.assertTrue(sortable.getSortableContainerPropertyIds().contains(self.FULLY_QUALIFIED_NAME))
        self.assertTrue(sortable.getSortableContainerPropertyIds().contains(self.REVERSE_FULLY_QUALIFIED_NAME))
        sortable.sort([self.FULLY_QUALIFIED_NAME], [True])
        packages = 21 + 3
        expectedSize = self.sampleData.length + packages
        self.validateHierarchicalContainer(container, 'com', 'org.vaadin.test.LastClass', 'com.vaadin.terminal.ApplicationResource', 'blah', True, expectedSize, 2, True)
        sortable.sort([self.REVERSE_FULLY_QUALIFIED_NAME], [True])
        self.validateHierarchicalContainer(container, 'com.vaadin.terminal.gwt.server.ApplicationPortlet2', 'com.vaadin.data.util.ObjectProperty', 'com.vaadin.terminal.ApplicationResource', 'blah', True, expectedSize, 2, True)

    def initializeContainer(self, container):
        container.removeAllItems()
        propertyIds = list(container.getContainerPropertyIds())
        for propertyId in propertyIds:
            container.removeContainerProperty(propertyId)
        container.addContainerProperty(self.FULLY_QUALIFIED_NAME, str, '')
        container.addContainerProperty(self.SIMPLE_NAME, str, '')
        container.addContainerProperty(self.REVERSE_FULLY_QUALIFIED_NAME, str, None)
        container.addContainerProperty(self.ID_NUMBER, int, None)
        _0 = True
        i = 0
        while True:
            if _0 is True:
                _0 = False
            else:
                i += 1
            if not (i < self.sampleData.length):
                break
            id = self.sampleData[i]
            # Add path as parent
            paths = id.split('\\.')
            path = paths[0]
            # Adds "com" and other items multiple times so should return null
            # for all but the first time
            if container.addItem(path) is not None:
                self.assertTrue(container.setChildrenAllowed(path, False))
                item = container.getItem(path)
                item.getItemProperty(self.FULLY_QUALIFIED_NAME).setValue(path)
                item.getItemProperty(self.SIMPLE_NAME).setValue(self.getSimpleName(path))
                item.getItemProperty(self.REVERSE_FULLY_QUALIFIED_NAME).setValue(self.reverse(path))
                item.getItemProperty(self.ID_NUMBER).setValue(1)
            _1 = True
            j = 1
            while True:
                if _1 is True:
                    _1 = False
                else:
                    j += 1
                if not (j < len(paths)):
                    break
                parent = path
                path = path + '.' + paths[j]
                # Adds "com" and other items multiple times so should return
                # null for all but the first time
                if container.addItem(path) is not None:
                    self.assertTrue(container.setChildrenAllowed(path, False))
                    item = container.getItem(path)
                    item.getItemProperty(self.FULLY_QUALIFIED_NAME).setValue(path)
                    item.getItemProperty(self.SIMPLE_NAME).setValue(self.getSimpleName(path))
                    item.getItemProperty(self.REVERSE_FULLY_QUALIFIED_NAME).setValue(self.reverse(path))
                    item.getItemProperty(self.ID_NUMBER).setValue(1)
                self.assertTrue(container.setChildrenAllowed(parent, True))
                self.assertTrue('Failed to set ' + parent + ' as parent for ' + path, container.setParent(path, parent))
            item = container.getItem(id)
            self.assertNotNull(item)
            parent = id[:id.rfind('.')]
            self.assertTrue(container.setParent(id, parent))
            item.getItemProperty(self.FULLY_QUALIFIED_NAME).setValue(self.sampleData[i])
            item.getItemProperty(self.SIMPLE_NAME).setValue(self.getSimpleName(self.sampleData[i]))
            item.getItemProperty(self.REVERSE_FULLY_QUALIFIED_NAME).setValue(self.reverse(self.sampleData[i]))
            item.getItemProperty(self.ID_NUMBER).setValue(i % 2)
