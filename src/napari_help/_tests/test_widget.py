from napari_help import HelpWidget


def test_example_q_widget(make_napari_viewer):
    viewer = make_napari_viewer()

    # create our widget, passing in the viewer
    widget = HelpWidget(viewer=viewer)
    viewer.window.add_dock_widget(widget)
