import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QButtonGroup,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QGroupBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Byte Converter")
        # self.setFixedSize(QSize(800, 600))
        self.setup_main_widget()

    def setup_main_widget(self):

        self.mainWidget = QWidget()
        self.mainLayout = QHBoxLayout()

        self.setup_choice_units()
        self.setup_input()
        self.setup_output()
        # self.setup_buttons()

        # self.mainLayout.addWidget(self.inputWidget)
        # self.mainLayout.addWidget(self.outputLayout)
        # self.mainLayout.addWidget(self.buttonLayout)

        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

    def setup_input(self):

        leftWidget = QWidget(self)
        leftLayout = QVBoxLayout()

        inputBox = QGroupBox("Input")
        inputLayout = QVBoxLayout()
        self.inputNumber = QLineEdit(self)
        self.inputNumber.setPlaceholderText("Enter a number")
        inputLayout.addWidget(self.inputNumber)
        inputBox.setLayout(inputLayout)

        unitGroup = QGroupBox("Units")
        unitLayout = QVBoxLayout()
        unitLayout.addWidget(self.unitWidget)
        unitGroup.setLayout(unitLayout)

        leftLayout.addWidget(inputBox)
        leftLayout.addWidget(unitGroup)
        leftWidget.setLayout(leftLayout)

        self.mainLayout.addWidget(leftWidget)

    def setup_output(self):

        rightWidget = QWidget(self)
        rightLayout = QVBoxLayout()

        self.bitOutput = QLabel("Bits: ")
        self.byteOutput = QLabel("Bytes: ")
        self.kibiByteOutput = QLabel("Kibibytes: ")
        self.kilobyteOutput = QLabel("Kilobytes: ")
        self.megabyteOutput = QLabel("Megabytes: ")
        self.gigabyteOutput = QLabel("Gigabytes: ")
        self.terabyteOutput = QLabel("Terabytes: ")

        outputGroup = QGroupBox("Output")
        outputLayout = QVBoxLayout()
        outputLayout.addWidget(self.bitOutput)
        outputLayout.addWidget(self.byteOutput)
        outputLayout.addWidget(self.kibiByteOutput)
        outputLayout.addWidget(self.kilobyteOutput)
        outputLayout.addWidget(self.megabyteOutput)
        outputLayout.addWidget(self.gigabyteOutput)
        outputLayout.addWidget(self.terabyteOutput)
        outputGroup.setLayout(outputLayout)

        self.convertButton = QPushButton("Convert")
        self.convertButton.clicked.connect(self.convertDate)

        rightLayout.addWidget(outputGroup)
        rightLayout.addWidget(self.convertButton)
        rightWidget.setLayout(rightLayout)

        self.mainLayout.addWidget(rightWidget)

    def setup_choice_units(self):

        self.unitWidget = QWidget()
        unitLayout = QVBoxLayout()

        self.unitButtons = QButtonGroup(self)
        bitButton = QRadioButton("Bit")
        byteButton = QRadioButton("Byte")
        kibiByteButton = QRadioButton("Kibibyte")
        kilobyteButton = QRadioButton("Kilobyte")
        megabyteButton = QRadioButton("Megabyte")
        gigabyteButton = QRadioButton("Gigabyte")
        terabyteButton = QRadioButton("Terabyte")

        self.unitButtons.addButton(bitButton, 0)
        self.unitButtons.addButton(byteButton, 1)
        self.unitButtons.addButton(kibiByteButton, 2)
        self.unitButtons.addButton(kilobyteButton, 3)
        self.unitButtons.addButton(megabyteButton, 4)
        self.unitButtons.addButton(gigabyteButton, 5)
        self.unitButtons.addButton(terabyteButton, 6)

        unitLayout.addWidget(bitButton)
        unitLayout.addWidget(byteButton)
        unitLayout.addWidget(kibiByteButton)
        unitLayout.addWidget(kilobyteButton)
        unitLayout.addWidget(megabyteButton)
        unitLayout.addWidget(gigabyteButton)
        unitLayout.addWidget(terabyteButton)

        bitButton.setChecked(True)  # Set default unit to bit

        self.unitWidget.setLayout(unitLayout)

    def byte_converter(self, bytes):
        conversions = {
            "bit": bytes * 8,
            "byte": bytes,
            "kibi": bytes / 1024,
            "kB": bytes / 1000,
            "mB": bytes / 1000**2,
            "gB": bytes / 1000**3,
            "tB": bytes / 1000**4,
        }
        return conversions

    def input_to_bytes(self, input_value, selected_unit):
        if selected_unit == 0:
            return input_value / 8
        elif selected_unit == 1:
            return input_value
        elif selected_unit == 2:
            return input_value * 1024
        elif selected_unit == 3:
            return input_value * 1000
        elif selected_unit == 4:
            return input_value * 1000**2
        elif selected_unit == 5:
            return input_value * 1000**3
        elif selected_unit == 6:
            return input_value * 1000**4
        else:
            print(f"Selected unit: {selected_unit}")

    def convertDate(self):

        try:
            input_value = float(self.inputNumber.text())
            selected_unit = self.unitButtons.checkedId()
            conversions = self.byte_converter(self.input_to_bytes(input_value, selected_unit))

            self.bitOutput.setText(f"Bits: {conversions['bit']}")
            self.byteOutput.setText(f"Bytes: {conversions['byte']}")
            self.kibiByteOutput.setText(f"Kibibytes: {conversions['kibi']}")
            self.kilobyteOutput.setText(f"Kilobytes: {conversions['kB']}")
            self.megabyteOutput.setText(f"Megabytes: {conversions['mB']}")
            self.gigabyteOutput.setText(f"Gigabytes: {conversions['gB']}")
            self.terabyteOutput.setText(f"Terabytes: {conversions['tB']}")

        except ValueError:
            self.bitOutput.setText("Bits: 'Error: Invalid input'")
            self.byteOutput.setText("Bytes: ")
            self.kibiByteOutput.setText("Kibibytes: ")
            self.kilobyteOutput.setText("Kilobytes: ")
            self.megabyteOutput.setText("Megabytes: ")
            self.gigabyteOutput.setText("Gigabytes: ")
            self.terabyteOutput.setText("Terabytes: ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
