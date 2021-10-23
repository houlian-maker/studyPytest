import openpyxl
from openpyxl.worksheet.worksheet import Worksheet


def read_excel(file_path, sheet_name):
    r"""    excel工具方法
            读取 excel 数据
     """
    # 打开文件
    workbook = openpyxl.load_workbook(file_path)
    # 选择表格,根据名称选择sheet文件
    sheet: Worksheet = workbook[sheet_name]
    # 获取sheet里面的数据,cell代表的是单元格，可以传入行，和列的数据,获取里面的数据
    # 获取说有的数据:generator,生成器，
    values = list(sheet.values)
    # 关闭文件
    workbook.close()
    title = values[0]
    rows = values[1:]
    # dict_values=translate(values)
    # 列表迭代器
    new_value = [dict(zip(title, row)) for row in rows]
    return new_value
