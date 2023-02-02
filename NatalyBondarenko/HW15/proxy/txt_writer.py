from Project.hillel_python_qa_homeworks.Nataly_Bondarenko.HW15.proxy.writer import Writer


class TxtWriter(Writer):
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, new_data):
        with open(self.file_path, 'w') as file:
            text = file.write(new_data)
        return text
