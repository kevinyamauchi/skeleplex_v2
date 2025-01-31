"""Dock widget for the Application Controls."""

from qtpy.QtWidgets import QDockWidget, QPushButton, QWidget


class AppControls(QDockWidget):
    """A dock widget for the application controls.

    This will be used as a container GUI elements
    for controlling the state of the application.
    """

    MINIMUM_WIDTH: int = 200

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent=parent)

        self.button = QPushButton("add points")
        self.button.setMinimumWidth(self.MINIMUM_WIDTH)

        self.setWidget(self.button)
