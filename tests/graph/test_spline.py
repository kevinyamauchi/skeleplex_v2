import numpy as np

from skeleplex.graph.spline import B3Spline


def test_uniform_sampling(simple_spline):
    """Test uniform sampling of a spline."""
    # sample the spline uniformly in arc length
    sample_points = np.linspace(0, 1, 11, endpoint=True)
    spline_points = simple_spline.eval(sample_points)

    expected_points = np.column_stack((sample_points, np.zeros((11, 2))))
    np.testing.assert_allclose(spline_points, expected_points, atol=1e-6)


def test_spline_equality(simple_spline):
    """Test spline equality."""
    # create a new spline that is the same as the original
    new_spline = B3Spline(model=simple_spline.model)

    assert simple_spline == new_spline

    # create a different spline
    points = np.array(
        [
            [0, 0, 0],
            [0.25, 0, 0],
            [0.5, 0, 0],
            [0.75, 0, 0],
            [1, 0, 0],
        ]
    )
    different_spline = B3Spline.from_points(points, n_knots=5)
    assert simple_spline != different_spline


def test_spline_serialization(simple_spline, tmp_path):
    """Test spline serialization."""
    # save the spline to a file
    file_path = tmp_path / "spline.json"
    simple_spline.to_json_file(file_path)

    # load the spline from the file
    reloaded_spline = B3Spline.from_json_file(file_path)

    assert simple_spline == reloaded_spline


def test_spline_flipping(simple_spline):
    """Test if spline is getting flipped correctly."""

    eval_points = simple_spline.eval(np.linspace(0, 1, 4))
    flipped_spline, flipped_coords = simple_spline.flip_spline(eval_points)

    # test if the flipping changed the spline
    with np.testing.assert_raises(AssertionError):
        np.testing.assert_allclose(
            eval_points, flipped_spline.eval(np.linspace(0, 1, 4)), atol=1e-2
        )

    # test if the flipping changed the coordinates to the inverse
    np.testing.assert_allclose(
        eval_points[::-1], flipped_spline.eval(np.linspace(0, 1, 4)), atol=1e-2
    )
    # test if the coordinates are flipped
    np.testing.assert_allclose(eval_points[::-1], flipped_coords, atol=1e-2)
