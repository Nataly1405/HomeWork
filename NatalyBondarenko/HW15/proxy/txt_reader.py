from Project.hillel_python_qa_homeworks.Nataly_Bondarenko.HW15.proxy.reader import Reader


class TxtReader(Reader):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            text = file.read()
        return text
