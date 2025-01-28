import numpy as np

from skeleplex.graph.spline import B3Spline


def test_uniform_sampling():
    # make three points that go from x=0 to x=1
    points = np.array(
        [
            [0, 0, 0],
            [0.25, 0, 0],
            [0.5, 0, 0],
            [0.75, 0, 0],
            [1, 0, 0],
        ]
    )

    # fit a spline to the points
    spline = B3Spline.from_points(points)

    # sample the spline uniformly in arc length
    sample_points = np.linspace(0, 1, 11, endpoint=True)
    spline_points = spline.eval(sample_points)

    expected_points = np.column_stack((sample_points, np.zeros((11, 2))))
    np.testing.assert_allclose(spline_points, expected_points, atol=1e-6)
