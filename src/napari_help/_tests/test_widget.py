from napari_help import help_widget


def test_example_q_widget(make_napari_viewer):
    viewer = make_napari_viewer()

    # create our widget, passing in the viewer
    widget = help_widget()
    viewer.window.add_dock_widget(widget)
