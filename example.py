import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from graphic import Ui_MainWindow
from itertools import *
from math import *

class Effect(QMainWindow):

    def __init__(self):
        super(Effect, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_btn_calculate)

    def on_btn_calculate(self):
        self.ui.lineEdit_p_2.setText(f"-")
        text_m = self.ui.lineEdit_m.text()
        text_S = self.ui.lineEdit_S.text()
        n_shots = int(self.ui.lineEdit_m_2.text())
        m = self._get_input_data(text_m)
        S = self._get_input_data(text_S)
        n, G = self.get_G(n_shots, S, m)

    def get_G(self, n_shots, S, m):

        n = np.arange(0, n_shots + 1)
        G = []
        M = 0.  # среднее необходимое число попаданий
        P_ = 0.  # вероятность поражения для предущего выстрела (для 0 она 0)

        for i in n:
            H = self.get_combinations(i, m)
            P = self.get_probability(H, S)
            M += i * (P - P_)
            G.append(P)
            P_ = P
            if P == 1.:
                n = np.arange(0, i + 1, 1)
                M = ceil(M)
                self.ui.lineEdit_p_2.setText(f"{M}")
                break

        if P != 1.:
            self.ui.lineEdit_p.setText(f"Цель не уничтожена гарантированно: P={P}")

        return n, np.array(G)

    def get_combinations(self, n_shots, m):

        n_section = len(m)

        range_number = ''
        for elem in (str(i) for i in range(1, n_section + 1)):
            range_number += elem

        combinations_sorted = []
        ma = np.zeros(n_section)
        for i in product(range_number, repeat=n_shots):
            combination = [int(a) for a in i]
            for i in range(1, n_section + 1):
                ma[i - 1] = combination.count(i)
            if list(ma < m).count(False) == 0:
                combinations_sorted.append(combination)

        return combinations_sorted

    def get_probability(self, combinations, S):

        probability = 0  # вероятность поражения

        for i in combinations:
            probability_combination = 1.0
            for j in i:
                if j == 1:
                    probability_combination *= S[0]
                if j == 2:
                    probability_combination *= S[1]
                if j == 3:
                    probability_combination *= S[2]
                if j == 4:
                    probability_combination *= S[3]
                if j == 5:
                    probability_combination *= S[4]
                if j == 6:
                    probability_combination *= S[5]
                if j == 7:
                    probability_combination *= S[6]
                if j == 8:
                    probability_combination *= S[7]
                if j == 9:
                    probability_combination *= S[8]
                if j == 10:
                    probability_combination *= S[9]
            probability += probability_combination if probability_combination != 1.0 else 0

        if probability != 0.0:
            m = len(combinations[0])
            self.ui.lineEdit_p.setText(f'при m={m} P={1 - probability}')
            return (1 - probability)
        elif len(combinations) == 0:
            self.ui.lineEdit_p.setText('P=1.0')
            return (1 - probability)
        else:
            self.ui.lineEdit_p.setText('m=0 P=0.0')
            return probability

    def _get_input_data(self, a):
        res_data = []
        data = ''
        for i in range(len(a)):
            if a[i].isdigit() or a[i] == '.':
                data += a[i]
                if i == (len(a) - 1):
                    res_data.append(float(data))
            elif data != '':
                res_data.append(float(data))
                data = ''
        return res_data

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Effect()
    window.show()

    sys.exit(app.exec())