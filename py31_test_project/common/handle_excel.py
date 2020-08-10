import openpyxl


class Operation_excel:
    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def wb_sh(self):
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheetname]

    def read_excel(self):
        '''读取数据方法'''
        self.wb_sh()  # 调用共有方法
        cell_data = list(self.sh.rows)  # 批量读取数据

        # 获取首行数据
        # first_li = []
        # for first_row in cell_data[0]:
        #     first_li.append(first_row.value)
        # first_li = [first_row.value for first_row in cell_data[0]]

        # 获取其他行数据
        # data = []
        # for other_row in cell_data[1:]:
        #     other_li = []
        #     for other_data in other_row:
        #         other_li.append(other_data.value)
        #     data.append(dict(zip(first_li, other_li)))

        # 列表推导式优化后
        data = [
            dict(zip([first_row.value for first_row in cell_data[0]], [other_data.value for other_data in other_row]))
            for other_row in cell_data[1:]]
        return data

    def write_excel(self, row, column, value):
        '''写入数据方法'''
        self.wb_sh()  # 调用共有方法
        self.sh.cell(row=row, column=column, value=value)
        self.wb.save(self.filename)
