from Project.hillel_python_qa_homeworks.Nataly_Bondarenko.HW15.proxy.txt_reader import TxtReader
from Project.hillel_python_qa_homeworks.Nataly_Bondarenko.HW15.proxy.txt_writer import TxtWriter


class TxtProxyReaderWriter:
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)
        self.__txt_writer = TxtWriter(file_path)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read()
            self.__is_actual = True
            return self.__result

    def write_file(self, new_data):
        if not new_data:
            print("Empty value is not supported. Please, insert the data.")
        else:
            self.__result = self.__txt_writer.write(new_data)
            self.__is_actual = False
            return self.__result


if __name__ == '__main__':
    proxy_reader_writer = TxtProxyReaderWriter('my_text_file.txt')
    print(proxy_reader_writer.read_file())
    proxy_reader_writer.write_file('Shabbat Shalom')
    print(proxy_reader_writer.read_file())
    proxy_reader_writer.write_file("")
    print(proxy_reader_writer.read_file())
    proxy_reader_writer.write_file('Hello everyone!')
    print(proxy_reader_writer.read_file())
