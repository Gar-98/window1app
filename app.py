'''Подключение модулей'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint


'''Функции'''
def pos():
    message = QMessageBox() #создали мини-окно
    message.setText('Уведомление о победе') #установили текст в мини-окне
    message.exec_() #окно должно закрываться, когда мы нажмем на крестик

def neg():
    message = QMessageBox() #создали мини-окно
    message.setText('Уведомление о поражении') #установили текст в мини-окне
    message.exec_() #окно должно закрываться, когда мы нажмем на крестик



'''Создание приложения и окна'''
app = QApplication([]) #создали приложение
win = QWidget() #создали окно



'''Настройка окна'''
win.setWindowTitle('Вопрос года') #задали заголовок окна
win.resize(400, 300) #установили размер окна



'''Создание виджетов'''
question = QLabel('Сколько будет 2+2*2')
ans1 = QRadioButton('Ответ1')
ans2 = QRadioButton('Ответ2')
ans3 = QRadioButton('Ответ3')
ans4 = QRadioButton('Ответ4')




'''Создание шампуров'''
main_vert = QVBoxLayout()
hor_1 = QHBoxLayout()
hor_2 = QHBoxLayout()


'''Сборка'''
hor_1.addWidget(ans1, alignment = Qt.AlignCenter)
hor_1.addWidget(ans2, alignment = Qt.AlignCenter)

hor_2.addWidget(ans3, alignment = Qt.AlignCenter)
hor_2.addWidget(ans4, alignment = Qt.AlignCenter)

main_vert.addWidget(question, alignment = Qt.AlignCenter)
main_vert.addLayout(hor_1)
main_vert.addLayout(hor_2)
win.setLayout(main_vert) #шампур в окно



'''Подписки'''
ans1.clicked.connect(pos) 
ans2.clicked.connect(neg) 
ans3.clicked.connect(neg) 
ans4.clicked.connect(neg) 



'''Показываем окно'''
win.show() #показали окно
app.exec_() #приложение открыто, пока не нажата кнопка выхода(крестик)






