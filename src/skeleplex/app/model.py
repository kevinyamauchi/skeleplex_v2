"""The main application model."""

import numpy as np
from app_model import Application
from app_model.types import Action, MenuRule
from cellier.models.data_stores.points import PointsMemoryStore
from cellier.models.nodes.points_node import PointsNode, PointsUniformMaterial

from skeleplex.app.actions import ACTIONS
from skeleplex.app.cellier import make_viewer_controller, make_viewer_model
from skeleplex.app.constants import CommandId, MenuId
from skeleplex.app.qt import MainWindow


class SkelePlexApp(Application):
    """The main application class."""

    def __init__(self) -> None:
        super().__init__("SkelePlex")

        # ACTIONS is a list of Action objects.
        for action in ACTIONS:
            self.register_action(action)
        self._register_data_actions()

        self._main_window = MainWindow(app=self)
        # This will build a menu bar based on these menus
        self._main_window.setModelMenuBar([MenuId.FILE, MenuId.EDIT, MenuId.DATA])

        # make the viewer model
        self._viewer_model, self._main_viewer_scene_id = make_viewer_model()
        self._viewer_controller = make_viewer_controller(
            viewer_model=self._viewer_model, parent_widget=self._main_window
        )

        for canvas in self._viewer_controller._canvas_widgets.values():
            # add the canvas widgets
            self._main_window.setCentralWidget(canvas)

    def _register_data_actions(self) -> None:
        """Register actions for adding/removing data to/from the viewer."""
        # add points
        self.register_action(
            Action(
                id=CommandId.ADD_POINTS,
                title="Add points",
                icon="fa6-solid:folder-open",
                callback=self.add_points,
                menus=[MenuRule(id=MenuId.DATA)],
            )
        )

    def add_points(self) -> None:
        """Add points to the main viewer."""
        # make the coordinates
        coordinates = 20 * np.random.random((100, 3))

        # make the points store
        points_store = PointsMemoryStore(coordinates=coordinates)

        # make the points material
        points_material_3d = PointsUniformMaterial(
            size=1, color=(1, 1, 1, 1), size_coordinate_space="data"
        )

        # make the points model
        points_visual_3d = PointsNode(
            name="points_node_3d",
            data_store_id=points_store.id,
            material=points_material_3d,
        )
        self._viewer_controller.add_data_store(data_store=points_store)
        self._viewer_controller.add_visual(
            visual_model=points_visual_3d, scene_id=self._main_viewer_scene_id
        )

        self._viewer_controller.reslice_scene(scene_id=self._main_viewer_scene_id)

    def show(self) -> None:
        """Show the app."""
        self._main_window.show()
