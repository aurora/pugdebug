# -*- coding: utf-8 -*-

"""
    pugdebug - a standalone PHP debugger
    =========================
    copyright: (c) 2015 Robert Basic
    license: GNU GPL v3, see LICENSE for more details
"""

__author__="robertbasic"

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget

from pugdebug.gui.file_browser import PugdebugFileBrowserWindow
from pugdebug.gui.settings import PugdebugSettingsWindow
from pugdebug.gui.workarea import PugdebugWorkareaWindow

class PugdebugMainWindow(QMainWindow):

    def __init__(self):
        super(PugdebugMainWindow, self).__init__()
        self.setObjectName("pugdebug")
        self.setWindowTitle("pugdebug")

        self.central_widget_layout = QGridLayout()

        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.central_widget_layout)

        self.setCentralWidget(self.central_widget)

        self.setup_gui_elements()

    def setup_gui_elements(self):
        self.setup_file_browser_window()
        self.setup_settings_window()

        self.setup_workarea_window()

    def setup_workarea_window(self):
        self.workarea_window = PugdebugWorkareaWindow(self)
        self.central_widget_layout.addWidget(self.workarea_window, 0, 1, 2, 1)

    def setup_file_browser_window(self):
        self.file_browser_window = PugdebugFileBrowserWindow(self)
        self.central_widget_layout.addWidget(self.file_browser_window, 0, 0, 1, 1)

    def setup_settings_window(self):
        self.settings_window = PugdebugSettingsWindow(self)
        self.central_widget_layout.addWidget(self.settings_window, 1, 0, 1, 1)