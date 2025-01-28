"""Utilities for fitting and working with splines."""

import numpy as np
import splinebox


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
