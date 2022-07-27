import napari
from napari.utils.action_manager import action_manager
from qtpy.QtWidgets import QFormLayout, QLabel, QWidget


class HelpWidget(QWidget):
    def __init__(self, viewer: napari.Viewer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLayout(QFormLayout())
        self.layout().addRow("Keys:", QLabel("Actions:"))
        self.viewer = viewer
        self.viewer.layers.selection.events.active.connect(self.update_table)
        self._current = None

    def update_table(self, event):
        active = event.value
        if active is None:
            self._update_table({})
        else:
            cls = active.__class__
            if cls != self._current:
                shortcuts = action_manager._get_layer_shortcuts([cls])[cls]
                self._update_table(shortcuts)

    def _update_table(self, shortcuts):
        for i in range(self.layout().rowCount(), 1, -1):
            self.layout().removeRow(i - 1)
        for key, action in shortcuts.items():
            key = " or ".join(key.strip("{}").split(", "))
            self.layout().addRow(key, QLabel(action))
