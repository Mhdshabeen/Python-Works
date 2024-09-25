

class editor:

    def __init__(self,name,vendor):

        self.name=name
        self.vendor=vendor

    def open(self):

        print(self.name,"open")

    def execute(self):

        print(self.name,"execute")

class vscode(editor):

    def __init__(self, name, vendor):
        super().__init__(name, vendor)

vscode_instance=vscode("Visualstudio code","Vs vendor")

vscode_instance.open()

class pycharm(editor):

    def __init__(self, name, vendor):
        super().__init__(name, vendor)

pycharm_instance=pycharm("pycharm",'pycharm vendor')

pycharm_instance.open()