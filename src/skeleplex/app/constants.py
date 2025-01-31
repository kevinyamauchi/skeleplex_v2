"""Constants for the application."""

from enum import Enum


class CommandId(str, Enum):
    """Command identifiers for the application."""

    OPEN = "skeleplex.open"
    CLOSE = "skeleplex.close"
    SAVE = "skeleplex.save"
    QUIT = "skeleplex.quit"
    ADD_POINTS = "skeleplex.add_points"

    UNDO = "skeleplex.undo"
    REDO = "skeleplex.redo"

    def __str__(self) -> str:
        """String representation."""
        return self.value


class MenuId(str, Enum):
    """Menu identifiers for the application."""

    FILE = "skeleplex/file"
    EDIT = "skeleplex/edit"
    DATA = "skeleplex/data"

    def __str__(self) -> str:
        """String representation."""
        return self.value
