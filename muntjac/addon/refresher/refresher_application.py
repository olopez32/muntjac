# @MUNTJAC_COPYRIGHT@
# @MUNTJAC_LICENSE@

from time import sleep

from threading import Thread

from muntjac.application import Application
from muntjac.ui.window import Window
from muntjac.ui.label import Label
from muntjac.addon.refresher.refresher import Refresher, RefreshListener


class RefresherApplication(Application):

    def __init__(self):
        super(RefresherApplication, self).__init__()

        self._databaseResult = None
        self._content = None


    def init(self):
        mainWindow = Window('Refresher Database Example')
        self.setMainWindow(mainWindow)
        # present with a loading contents.
        self._content = Label('please wait while the database is queried')
        mainWindow.addComponent(self._content)
        # the Refresher polls automatically
        refresher = Refresher()
        refresher.addListener(DatabaseListener(self))
        mainWindow.addComponent(refresher)
        DatabaseQueryProcess(self).start()



class DatabaseListener(RefreshListener):

    def __init__(self, app):
        self._app = app

    def refresh(self, source):
        if self._app._databaseResult is not None:
            # stop polling
            source.setEnabled(False)
            # replace the "loading" with the actual fetched result
            self._app._content.setValue('Database result was: ' +
                                        self._app._databaseResult)


class DatabaseQueryProcess(Thread):

    def __init__(self, app):
        super(DatabaseQueryProcess, self).__init__()
        self._app = app

    def run(self):
        self._app._databaseResult = self.veryHugeDatabaseCalculation()

    def veryHugeDatabaseCalculation(self):
        # faux long lasting database query
        try:
            sleep(2000)
        except KeyboardInterrupt:
            pass  # ignore

        return 'huge!'


if __name__ == '__main__':
    from muntjac.main import muntjac
    muntjac(RefresherApplication, nogui=True, debug=True,
            contextRoot='.')
