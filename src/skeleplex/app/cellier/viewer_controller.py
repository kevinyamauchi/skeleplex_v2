"""Viewer controller for the Cellier renderer."""

from cellier.models.data_manager import DataManager
from cellier.models.scene import (
    Canvas,
    CoordinateSystem,
    DimsManager,
    PerspectiveCamera,
    Scene,
)
from cellier.models.viewer import SceneManager, ViewerModel
from cellier.slicer.slicer import SlicerType
from cellier.viewer_controller import ViewerController
from qtpy.QtWidgets import QWidget


def make_viewer_model() -> ViewerModel:
    """Make the viewer controller."""
    # make the data manager (empty for now)
    data_manager = DataManager(stores={})

    # make the scene coordinate system
    coordinate_system_3d = CoordinateSystem(
        name="scene_3d", axis_labels=["z", "y", "x"]
    )
    dims_3d = DimsManager(
        point=(0, 0, 0),
        margin_negative=(0, 0, 0),
        margin_positive=(0, 0, 0),
        coordinate_system=coordinate_system_3d,
        displayed_dimensions=(0, 1, 2),
    )

    # make the canvas
    camera_3d = PerspectiveCamera()
    canvas_3d = Canvas(camera=camera_3d)

    # make the scene
    main_viewer_scene = Scene(
        dims=dims_3d, visuals=[], canvases={canvas_3d.id: canvas_3d}
    )

    scene_manager = SceneManager(scenes={main_viewer_scene.id: main_viewer_scene})

    # make the viewer model
    viewer_model = ViewerModel(data=data_manager, scenes=scene_manager)

    return viewer_model, main_viewer_scene.id


def make_viewer_controller(
    viewer_model: ViewerModel, parent_widget: QWidget
) -> ViewerController:
    """Make the viewer controller."""
    return ViewerController(
        model=viewer_model,
        slicer_type=SlicerType.ASYNCHRONOUS,
        widget_parent=parent_widget,
    )
