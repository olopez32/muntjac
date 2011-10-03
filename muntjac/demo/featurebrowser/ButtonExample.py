
from muntjac.ui.themes import Reindeer, BaseTheme
from muntjac.ui.button import IClickListener
from muntjac.terminal.theme_resource import ThemeResource

from muntjac.terminal.external_resource import ExternalResource

from muntjac.ui import \
    (Link, VerticalLayout, HorizontalLayout, CustomComponent, Panel,
     Button, CheckBox, Label)


class ButtonExample(CustomComponent, IClickListener):
    """Shows a few variations of Buttons and Links.

    @author IT Mill Ltd.
    """

    def __init__(self):
        main = VerticalLayout()
        main.setMargin(True)
        self.setCompositionRoot(main)

        horiz = HorizontalLayout()
        horiz.setWidth('100%')
        main.addComponent(horiz)
        basic = Panel('Basic buttons')
        basic.setStyleName(Reindeer.PANEL_LIGHT)
        horiz.addComponent(basic)

        bells = Panel('w/ bells & whistles')
        bells.setStyleName(Reindeer.PANEL_LIGHT)
        horiz.addComponent(bells)

        b = Button('Basic button')
        b.addListener(self)
        basic.addComponent(b)
        b = Button('Button w/ icon + tooltip')
        b.addListener(self)
        b.setIcon(ThemeResource('icons/ok.png'))
        b.setDescription('This button does nothing, fast')
        bells.addComponent(b)

        b = CheckBox('CheckBox - a switch-button')
        b.setImmediate(True)  # checkboxes are not immediate by default
        b.addListener(self)
        basic.addComponent(b)

        b = CheckBox('CheckBox w/ icon + tooltip')
        b.setImmediate(True)  # checkboxes are not immediate by default
        b.addListener(self)
        b.setIcon(ThemeResource('icons/ok.png'))
        b.setDescription('This is a CheckBox')
        bells.addComponent(b)

        b = Button('Link-style button')
        b.addListener(self)
        b.setStyleName(BaseTheme.BUTTON_LINK)
        basic.addComponent(b)

        b = Button('Link button w/ icon + tooltip')
        b.addListener(self)
        b.setStyleName(BaseTheme.BUTTON_LINK)
        b.setIcon(ThemeResource('icons/ok.png'))
        b.setDescription('Link-style, icon+tootip, no caption')
        bells.addComponent(b)

        b = Button()
        b.addListener(self)
        b.setStyleName(BaseTheme.BUTTON_LINK)
        b.setIcon(ThemeResource('icons/ok.png'))
        b.setDescription('Link-style, icon+tootip, no caption')
        basic.addComponent(b)

        links = Panel('Links')
        links.setStyleName(Reindeer.PANEL_LIGHT)
        main.addComponent(links)
        desc = Label(('The main difference between a Link and'
            + ' a link-styled Button is that the Link works client-'
            + ' side, whereas the Button works server side.<br/> This means'
            + ' that the Button triggers some event on the server,'
            + ' while the Link is a normal web-link. <br/><br/>Note that for'
            + ' opening new windows, the Link might be a safer '
            + ' choice, since popup-blockers might interfer with '
            + ' server-initiated window opening.'))
        desc.setContentMode(Label.CONTENT_XHTML);
        links.addComponent(desc)
        l = Link('Vaadin home', ExternalResource('http://www.vaadin.com'))
        l.setDescription('Link without target name, opens in this window')
        links.addComponent(l)

        l = Link('Vaadin home (new window)',
                ExternalResource('http://www.vaadin.com'))
        l.setTargetName('_blank')
        l.setDescription('Link with target name, opens in new window')
        links.addComponent(l)

        l = Link('Vaadin home (new window, less decor)',
                ExternalResource('http://www.vaadin.com'))
        l.setTargetName('_blank')
        l.setTargetBorder(Link.TARGET_BORDER_MINIMAL)
        l.setTargetName('_blank')
        l.setDescription(('Link with target name and BORDER_MINIMAL, '
                'opens in new window with less decor'))
        links.addComponent(l)

        l = Link('Vaadin home (new 200x200 window, no decor, icon)',
                ExternalResource('http://www.vaadin.com'), '_blank',
                200, 200, Link.TARGET_BORDER_NONE)
        l.setTargetName('_blank')
        l.setDescription(('Link with target name and BORDER_NONE, '
                'opens in new window with no decor'))
        l.setIcon(ThemeResource('icons/ok.png'))
        links.addComponent(l)


    def buttonClick(self, event):
        b = event.getButton()
        self.getWindow().showNotification('Clicked' + (', value: '
            + event.getButton().getValue() if isinstance(b, CheckBox) else ''))
