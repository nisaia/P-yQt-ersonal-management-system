import sys
from PyQt5.QtWidgets import QDialog, QApplication
from views.reserveHotel import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonCalculateRoomRent.clicked.connect(self.computeRoomRent)

        self.show()

    def computeRoomRent(self):
        selected_date = str(self.ui.calendarWidget.selectedDate().toPyDate())
        days = self.ui.spinBox.value()
        chosen_room_type = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())

        self.ui.labelEnterdInfo.setText('Date of reservation: ' + selected_date + '.\nNumber of days: ' + str(days) + ' and room type selected: ' + chosen_room_type)

        roomRent = 0
        if chosen_room_type == "Suite": roomRent = 40
        elif chosen_room_type == "Super luxury": roomRent = 30
        elif chosen_room_type == "Super deluxe": roomRent = 20
        elif chosen_room_type == "Ordinary": roomRent = 10

        total_amount = roomRent * days

        self.ui.labelRoomRentInfo.setText('Room rent for single day for ' + chosen_room_type + ' type is: ' + str(roomRent) + '$.\nTotal room rent is: '+ str(total_amount) + '$')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())