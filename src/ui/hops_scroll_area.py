from PyQt5.QtWidgets import (
    QWidget, QScrollArea, QVBoxLayout, QPushButton,
    QLineEdit, QComboBox, QHBoxLayout, QCompleter
)

from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import Qt, QRegExp


class HopsScrollArea(QWidget):
    """Widget consisting of the scrollarea for managing hops of the recipe.

    This scrollarea consists of a vboxlayout consisting of hboxlayouts. 
    """

    def __init__(self, data_grid, manager):
        """Consturctor of the class.

        Args:
            data_grid (QWidget): Calculations grid widget.
            manager (Manager_services): Manager_services class of the recipe.
        """

        super().__init__()
        self.manager = manager
        self.data_grid = data_grid
        self.all_hops = self.manager.get_all_hops()
        self.init_ui()

    def init_ui(self):
        """Initializes the widgets.
        """

        font = self.font()
        font.setPointSize(10)
        self.window().setFont(font)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(2)

        self.widget = QWidget(self.scroll_area)
        self.vertical_box = QVBoxLayout(self.widget)
        self.vertical_box.setAlignment(Qt.AlignTop)
        self.vertical_box.setSpacing(15)

        add_malt_button = QPushButton("Add new hop")
        add_malt_button.clicked.connect(self.add_new_row)
        self.vertical_box.addWidget(add_malt_button)

        self.add_new_row()

        self.scroll_area.setWidget(self.widget)
        self.setFixedSize(475, 300)

        self.setLayout(QVBoxLayout(self))
        self.layout().addWidget(self.scroll_area)

    def add_new_row(self):
        """Adds a new row to the vbox. Row consists of a lineedit, combobox and a button.
        """

        horizontal_box = QHBoxLayout()
        line_edit = QLineEdit()
        line_edit.setMaximumWidth(25)

        regex = QRegExp("[0-9]+(\\.[0-9]+)?")
        validator = QRegExpValidator(regex)
        line_edit.setValidator(validator)

        line_edit.textEdited.connect((
            lambda text: self.line_edit_signal(text, horizontal_box)))
        combo_box = self.init_combo_box(horizontal_box)
        remove_button = QPushButton("Remove")
        remove_button.setMaximumWidth(60)
        remove_button.clicked.connect(
            lambda _, horizontal_box=horizontal_box: self.remove_row(horizontal_box))

        horizontal_box.addWidget(line_edit)
        horizontal_box.addWidget(combo_box)
        horizontal_box.addWidget(remove_button)

        horizontal_box.setStretch(0, 1)
        horizontal_box.setStretch(1, 9)
        horizontal_box.setStretch(2, 1)

        self.vertical_box.addLayout(horizontal_box)

    def remove_row(self, horizontal_box):
        """Removes a row from the vbox and the corresponding ingredient from the recipe.
        Then updates the calculation values.

        Args:
            horizontal_box (QWidgget): The hbox to be removed.
        """

        index = self.get_row(horizontal_box)
        values = self.manager.ingredient_removed(index, "hops")
        self.data_grid.update_values(values)

        self.layout().removeItem(horizontal_box)

        for i in reversed(range(horizontal_box.count())):
            horizontal_box.itemAt(i).widget().setParent(None)
        horizontal_box.setParent(None)

    def get_row(self, horizontal_box):
        """Gets the row index of the horizontal box.

        Args:
            horizontal_box (hbox): The horizontal box.

        Returns:
            int: Index of the hbox on the vbox. Counting starts from top and from 0.
        """

        for i in range(self.vertical_box.count()):
            item = self.vertical_box.itemAt(i)
            if item.layout() == horizontal_box:
                return i - 1

    def init_combo_box(self, horizontal_box):
        """Initializes the combo box.

        Args:
            horizontal_box (hbox): The hbox which this combobox is a part of.

        Returns:
            combobox: This combobox.
        """

        combo_box = QComboBox()
        combo_box.setMaximumWidth(305)
        combo_box.addItem("")
        combo_box.addItems([malt.name for malt in self.all_hops])
        combo_box.activated.connect(
            lambda index: self.combo_box_signal(index, horizontal_box))

        combo_box.setEditable(True)
        combo_box.setInsertPolicy(QComboBox.NoInsert)
        combo_box.completer().setCompletionMode(QCompleter.PopupCompletion)
        combo_box.completer().setFilterMode(Qt.MatchContains)

        return combo_box

    def combo_box_signal(self, index, horizontal_box):
        """Signal of the combo box.

        Args:
            index (int): Index of the chosen item in the combo box.
            horizontal_box (hbox): Hbox which this combo box is a part of.
        """

        row_index = self.get_row(horizontal_box)
        values = self.manager.ingredient_added(
            self.all_hops[index-1], "hops", row_index)
        self.data_grid.update_values(values)

    def line_edit_signal(self, text, horizontal_box):
        """Handles the changes of this line edit.

        Converts the value into float and passes it on to the manager.

        This should not receive incorrect inputs due to line edits validator but try/except keeps
        it safe in case of an unprepared inputs.

        Args:
            text (str): The user input in the volume line edit.
        """

        try:
            index = self.get_row(horizontal_box)
            values = self.manager.ingredient_amount_changed(
                float(text), index, "hops")
            self.data_grid.update_values(values)
        except:
            pass
