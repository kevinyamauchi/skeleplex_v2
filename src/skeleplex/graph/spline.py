"""Utilities for fitting and working with splines."""

import json

import numpy as np
import splinebox
from splinebox.spline_curves import _prepared_dict_for_constructor


class B3Spline:
    """Model for a B3 spline.

    Parameters
    ----------
    model : Spline
        The spline model.
    """

    _backend = "splinebox"

    def __init__(self, model: splinebox.Spline):
        self._model = model

    @property
    def model(self) -> splinebox.Spline:
        """Return the underlying spline model."""
        return self._model

    @property
    def arc_length(self) -> float:
        """Return the arc length of the spline."""
        return self.model.arc_length()

    def eval(
        self, positions: np.ndarray, derivative: int = 0, atol: float = 1e-6
    ) -> np.ndarray:
        """Evaluate the spline at a set of positions.

        Parameters
        ----------
        positions : np.ndarray
            (n,) array of positions to evaluate the spline at.
            The positions are normalized to the range [0, 1].
        derivative : int
            The order of the derivative to evaluate.
            Default value is 0.
        atol : float
            The absolute tolerance for converting the normalized
            evaluation positions to positions along the spline.
            Default value is 1e-6.
        """
        # convert the normalized arc length coordinates to t
        positions_t = self.model.arc_length_to_parameter(
            positions * self.arc_length, atol=atol
        )
        return self.model.eval(positions_t, derivative=derivative)

    def __eq__(self, other_object) -> bool:
        """Check if two B3Spline objects are equal."""
        if not isinstance(other_object, B3Spline):
            return False
        return self.model == other_object.model

    def to_json_dict(self) -> dict:
        """Return a JSON serializable dictionary."""
        spline_model_dict = self.model._to_dict(version=2)
        if "__class__" in spline_model_dict:
            raise ValueError(
                "The Spline object to encode already has a '__class__' key."
            )
        spline_model_dict.update({"__class__": "splinebox.Spline"})
        return {
            "__class__": "B3Spline",
            "model": spline_model_dict,
            "backend": self._backend,
        }

    def to_json_file(self, file_path: str) -> None:
        """Save the spline to a JSON file."""
        with open(file_path, "w") as file:
            json.dump(self.to_json_dict(), file)

    @classmethod
    def from_json_dict(cls, json_dict: dict) -> "B3Spline":
        """Return a B3Spline from a JSON serializable dictionary."""
        if json_dict["backend"] != cls._backend:
            raise ValueError(
                f"Expected backend {cls._backend}, got {json_dict['backend']}."
            )

        # load the spline model
        spline_model_dict = json_dict["model"]
        spline_model_dict.pop("__class__")
        spline_kwargs = _prepared_dict_for_constructor(spline_model_dict)
        spline_model = splinebox.Spline(**spline_kwargs)

        # make the class
        return cls(model=spline_model)

    @classmethod
    def from_json_file(cls, file_path: str) -> "B3Spline":
        """Return a B3Spline from a JSON file."""
        with open(file_path) as file:
            json_dict = json.load(file)
        return cls.from_json_dict(json_dict)

    @classmethod
    def from_points(cls, points: np.ndarray, n_knots: int = 4):
        """Construct a B3 spline fit to a list of points.

        Parameters
        ----------
        points : np.ndarray
            (n, d) array of points to fit the spline to.
            These must be ordered in the positive t direction
            of the spline.
        n_knots : int
            The number of knots to use in the spline.
        """
        basis_function = splinebox.B3()
        spline = splinebox.Spline(
            M=n_knots, basis_function=basis_function, closed=False
        )
        spline.fit(points)
        return cls(model=spline)
