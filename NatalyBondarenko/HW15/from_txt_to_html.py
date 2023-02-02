class FromTxtToHtml:
    def __init__(self, file_path):
        self.__file_path = file_path

    def from_txt_to_html(self):
        with open(self.__file_path, 'r') as file:
            lines = file.readlines()
        header = lines[0].replace('\n', '').split(',')
        data = [item.replace('\n', '').split(',') for item in lines[1:]]
        result = [dict(zip(header, worker_data)) for worker_data in data]
        new_list = []
        for line in result:
            new_list.append(''.join([f'<{item}>{value}</{item}>\n' for (item, value) in line.items()]))
        return ''.join(new_list)


if __name__ == '__main__':
    html = FromTxtToHtml('worker_information.txt').from_txt_to_html()
    print(html)
