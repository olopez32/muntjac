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

import sys
import traceback
from muntjac.terminal.paintable import IRepaintRequestListener

try:
    from cStringIO import StringIO
except ImportError, e:
    from StringIO import StringIO

from muntjac.terminal.error_message import IErrorMessage


class SystemErr(RuntimeError, IErrorMessage):
    """C{SystemError} is a runtime exception caused by error in
    system. The system error can be shown to the user as it implements
    C{IErrorMessage} interface, but contains technical information
    such as stack trace and exception.

    @author: IT Mill Ltd.
    @author: Richard Lincoln
    @version @VERSION@
    """

    def __init__(self, *args):
        """Constructor for SystemError with error message and/or causing
        exception specified.

        @param args: tuple of the form
            - ()
            - (message)
              1. the textual error description.
            - (message, cause)
              1. the textual error description.
              2. the throwable causing the system error.
            - (cause)
              1. the throwable causing the system error.
        """
        # The cause of the system error.
        self._cause = None

        nargs = len(args)
        if nargs == 0:
            super(SystemErr, self).__init__()
        elif nargs == 1:
            if isinstance(args[0], Exception):
                self._cause = args[0]
                super(SystemErr, self).__init__()
            else:
                super(SystemErr, self).__init__(args[0])
        elif nargs == 2:
            message, cause = args
            super(SystemErr, self).__init__(message)
            self._cause = cause
        else:
            raise ValueError, ('too many arguments: %d' % nargs)


    def getErrorLevel(self):
        """@see: L{IErrorMessage.getErrorLevel}"""
        return IErrorMessage.SYSTEMERROR


    def paint(self, target):
        """@see: L{IPaintable.paint}"""

        target.startTag('error')
        target.addAttribute('level', 'system')

        message = self.getHtmlMessage()

        target.addXMLSection('div', message,
                'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd')

        target.endTag('error')


    def getHtmlMessage(self):
        sb = StringIO()
        message = self.message
        if message is not None:
            sb.write('<h2>')
            sb.write(message)
            sb.write('</h2>')

        # Paint the exception
        if self._cause is not None:
            sb.write('<h3>Exception</h3>')
            buff = StringIO()
            exc_type, _, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, self._cause,
                    exc_traceback, file=buff)

            sb.write('<pre>')
            sb.write(buff.getvalue())
            buff.close()
            sb.write('</pre>')

        result = sb.getvalue()
        sb.close()
        return result


    def getCause(self):
        """Gets cause for the error.

        @return: the cause.
        """
        return self._cause


    def addListener(self, listener, iface):
        if iface == IRepaintRequestListener:
            pass
        else:
            super(SystemErr).addListener(listener, iface)


    def addRepaintRequestListener(self, listener):
        self.addListener(listener, IRepaintRequestListener)


    def removeListener(self, listener, iface):
        if iface == IRepaintRequestListener:
            pass
        else:
            super(SystemErr, self).removeListener(listener, iface)


    def removeRepaintRequestListener(self, listener):
        self.removeListener(listener, IRepaintRequestListener)


    def requestRepaint(self):
        pass


    def requestRepaintRequests(self):
        pass


    def getDebugId(self):
        return None


    def setDebugId(self, idd):
        raise NotImplementedError, \
                'Setting testing id for this Paintable is not implemented'
