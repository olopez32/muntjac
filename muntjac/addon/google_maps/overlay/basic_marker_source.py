# Copyright (C) 2011 Vaadin Ltd.
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
#
# Note: This is a modified file from Vaadin. For further information on
#       Vaadin please visit http://www.vaadin.com.

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from muntjac.addon.google_maps.overlay.marker_source \
    import IMarkerSource


class BasicMarkerSource(IMarkerSource):

    def __init__(self):
        super(BasicMarkerSource, self).__init__()
        self._markers = list()


    def getMarkers(self):
        return self._markers


    def addMarker(self, newMarker):
        if newMarker in self._markers:
            return False
        self._markers.append(newMarker)
        return True


    def getMarkerJSON(self):
        markerJSON = StringIO()

        for i, marker in enumerate(self._markers):
            markerJSON.write('{\"mid\":\"')
            markerJSON.write(str(marker.getId()))

            markerJSON.write('\",\"lat\":')
            markerJSON.write(str(marker.getLatLng()[1]))

            markerJSON.write(',\"lng\":')
            markerJSON.write(str(marker.getLatLng()[0]))

            # Escape single and double quotes
            markerJSON.write(',\"title\":\"')
            markerJSON.write(marker.getTitle().replace('\'', "\\'").replace('\"', '\\\\\"'))

            markerJSON.write('\",\"visible\":')
            markerJSON.write('true' if marker.isVisible() else 'false')

            markerJSON.write(',\"info\":')
            markerJSON.write('true' if marker.getInfoWindowContent() is not None else 'false')

            markerJSON.write(',\"draggable\":')
            markerJSON.write('true' if marker.isDraggable() else 'false')

            if marker.getIconUrl() is not None:
                markerJSON.write(',\"icon\":\"')
                markerJSON.write(marker.getIconUrl() + '\"')

                if marker.getIconAnchor() is not None:
                    markerJSON.write(',\"iconAnchorX\":')
                    markerJSON.write(str(marker.getIconAnchor()[0]))

                    markerJSON.write(',\"iconAnchorY\":')
                    markerJSON.write(str(marker.getIconAnchor()[1]))
                else:
                    markerJSON.write(',\"iconAnchorX\":')
                    markerJSON.write(str(marker.getLatLng()[0]))

                    markerJSON.write(',\"iconAnchorY\":')
                    markerJSON.write(str(marker.getLatLng()[1]))

            markerJSON.write('}')

            if i != len(self._markers) - 1:
                markerJSON.write(',')

        try:
            json = ('[' + markerJSON.getvalue() + ']').encode('utf-8')
        except Exception:
            json = ('[' + markerJSON.getvalue() + ']').encode()

        markerJSON.close()

        return json


    def registerEvents(self, map_):
        # This marker source implementation is not interested in map events
        pass


    def getMarker(self, markerId):
        # TODO: The marker collection should be a map...
        for marker in self._markers:
            if str(marker.getId()) == markerId:
                return marker
        return None
