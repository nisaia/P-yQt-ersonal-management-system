import sys
from PyQt5.QtWidgets import QDialog, QApplication
from views.demoScrollBar import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.horizontalScrollBarSugarLevel.valueChanged.connect(self.scrollHorizontal)
        self.ui.horizontalSliderBloodPressure.valueChanged.connect(self.sliderHorizontal)
        self.ui.verticalScrollBarPulseRate.valueChanged.connect(self.scrollVertical)
        self.ui.verticalSliderCholesterolLevel.valueChanged.connect(self.sliderVertical)

        self.show()

    def scrollHorizontal(self, value):
        self.ui.lineEditResult.setText("Sugar value: " + str(value))

    def sliderHorizontal(self, value):
        self.ui.lineEditResult.setText("Blood pressure: " + str(value))

    def scrollVertical(self, value):
        self.ui.lineEditResult.setText("Pulse Rate: " + str(value))

    def sliderVertical(self, value):
        self.ui.lineEditResult.setText("Cholestorel level: " + str(value))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())