import wpf
import seaborn as sns

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'ECOLOGDataIronPythonViewer.xaml')
    

if __name__ == '__main__':
    Application().Run(MyWindow())
