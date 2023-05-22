import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
import time


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_first = QHBoxLayout()
        self.hbox_input = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_result)
        self.vbox.addLayout(self.hbox_first)

        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_fourth)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        # Кнопки

        # Result layer
        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        # First layer
        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_div = QPushButton("/", self)
        self.hbox_first.addWidget(self.b_div)

        # Second layer
        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_minus = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_minus)

        # Third layer
        self.b_7 = QPushButton("7", self)
        self.hbox_third.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_third.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_third.addWidget(self.b_9)

        self.b_plus = QPushButton("+", self)
        self.hbox_third.addWidget(self.b_plus)

        # Fourth layer
        self.b_point = QPushButton(".", self)
        self.hbox_fourth.addWidget(self.b_point)

        self.b_0 = QPushButton("0", self)
        self.hbox_fourth.addWidget(self.b_0)

        self.b_erase = QPushButton("<-", self)
        self.hbox_fourth.addWidget(self.b_erase)

        self.b_multiply = QPushButton("*", self)
        self.hbox_fourth.addWidget(self.b_multiply)

        self.op = '+'
        self.num_1 = 0
        self.num_2 = 0

        # События
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_result.clicked.connect(self._result)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))

        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))

        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiply.clicked.connect(lambda: self._operation("*"))
        self.b_div.clicked.connect(lambda: self._operation("/"))

        self.b_point.clicked.connect(lambda: self._button("."))
        self.b_erase.clicked.connect(self._erase_text)

    # Обработка ввода
    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    # Обработка операций
    def _operation(self, op):
        if self.input.text() == '':
            self.num_1 = 0
        else:
            self.num_1 = float(self.input.text())

        self.op = op
        self.input.setText("")

    # Обработка результа
    def _result(self):
        if self.input.text() == '':
            self.num_2 = 0
        else:
            self.num_2 = float(self.input.text())

        if self.op == "+":
            self.input.setText(str(self.num_1 + self.num_2))

        elif self.op == "-":
            self.input.setText(str(self.num_1 - self.num_2))

        elif self.op == "/":
            if self.num_2 != 0:
                self.input.setText(str(self.num_1 / self.num_2))
            else:
                print('error')
                self.input.setText(str(''))

        elif self.op == "*":
            self.input.setText(str(self.num_1 * self.num_2))

    def _erase_text(self):
        self.input.setText('')


app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())
