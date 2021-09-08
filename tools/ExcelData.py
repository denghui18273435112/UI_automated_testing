import  json

import xlrd
from xlutils.copy import copy


class get_ExcelData:
    """
    初始化中
    1 初始化文件的相对路径excel_file，并默认文件位置
    2 申明列表
    """
    def __init__(self,excel_file=get_docs_path()+os.sep+"外卖系统接口测试用例-V1.5.xls"):
        self.excel_file = excel_file
        self._data=list()
    def ExcelData(self, beginColumn=None):
        """
        1、不传入beginColumn，读取表格中所有信息
        2、传入beginColumn，读取满足条件的某一行
        :return: 重新生成字典，首行：key;数据行：value
        """
        workbook = xlrd.open_workbook(self.excel_file,formatting_info=True)     #打开表格
        sheets = workbook.sheet_names()                                          #查询此表一共有几页
        for i in range(len(sheets)):                                            # 循环
            sheet = workbook.sheet_by_name(sheets[i])                            #进入制定哪一页
            title = sheet.row_values(0)                                          #获取当前页第一行的的名称
            for col in range(1,sheet.nrows):
                col_value = sheet.row_values(col)
                if beginColumn !=None:
                    if beginColumn in sheet.cell(col,0).value:
                        self._data.append(dict(zip(title, col_value)))
                else:
                        self._data.append(dict(zip(title, col_value)))
        return self._data


def get_excelData(sheet_names, startRow, endRow):
    # 读取
    rlist=[]
    excel_file=get_docs_path()+os.sep+"外卖系统接口测试用例-V1.5.xls"
    workbook = xlrd.open_workbook(excel_file,formatting_info=True)
    sheet = workbook.sheet_by_name(sheet_names)
    for one in range(startRow-1,endRow):
        r = sheet.cell(one,9).value
        x = sheet.cell(one,11).value
        rlist.append((r,x))
    return rlist

def set_excelData():
    #写入
    rlist=[]
    excel_file=get_docs_path()+os.sep+"外卖系统接口测试用例-V1.5.xls"
    workbook = xlrd.open_workbook(excel_file,formatting_info=True)
    workbookNew = copy(workbook)
    worksheetNew = workbookNew.get_sheet(0)
    return workbookNew,worksheetNew


def get_excelData2(sheet_names,caseName):
    # 读取
    rlist=[]
    excel_file=get_docs_path()+os.sep+"外卖系统接口测试用例-V1.5.xls"
    workbook = xlrd.open_workbook(excel_file,formatting_info=True)
    sheet = workbook.sheet_by_name(sheet_names)
    inx = 0
    for one in sheet.col_values(0):
        if caseName in one:
            r = sheet.cell(inx,9).value
            y = sheet.cell(inx,10).value
            x = sheet.cell(inx,11).value
            # print("------->------->------->获取某行第9列,请求参数的数据",r)
            # print("------->------->------->获取某行第1列,预期响应的数据的数据",x)
            # print("------->------->------->",y)
            #rlist.append(r,x)
            rlist.append((
                json.loads(r),json.loads(x)
            ))
            #rlist["id"] = y
        inx+=1
    return rlist






def get_excelData3(caseName):
    rlist=[]
    excel_file=get_docs_path()+os.sep+"外卖系统接口测试用例-V1.5.xls"
    workbook = xlrd.open_workbook(excel_file,formatting_info=True)
    sheets = workbook.sheets()
    for i in range(len(sheets)):
        sheet = workbook.sheet_by_index(i)
        title = sheet.row_values(0)
        inx = 0
        for one in sheet.col_values(0):
            if caseName in one:
                r = sheet.cell(inx,9).value
                x = sheet.cell(inx,11).value
                rlist.append((
                    json.loads(r),json.loads(x)
                ))
            inx+=1
    return rlist

def ExcelData(beginColumn=None):
    """
    读取表格中的用例信息
    :param beginColumn:第一列的名称，支持模糊
    :return: 返回的数据格式字典
    """
    excel_file=get_docs_path()+os.sep+"禅道测试用例.xls"
    _data=[]
    workbook = xlrd.open_workbook(excel_file,formatting_info=True)     #打开表格
    sheets = workbook.sheet_names()                                          #查询此表一共有几页
    for i in range(len(sheets)):                                            # 循环
        sheet = workbook.sheet_by_name(sheets[i])                            #进入制定哪一页
        title = sheet.row_values(0)                                          #获取当前页第一行的的名称
        for col in range(1,sheet.nrows):
            col_value = sheet.row_values(col)
            if beginColumn !=None:
                if beginColumn in sheet.cell(col,0).value:
                    _data.append(dict(zip(title, col_value)))
            else:
                    _data.append(dict(zip(title, col_value)))
    return _data

def data_table(tesst_id,field_name=None):
    """
    遍历表格上的信息
    :param tesst_id: 测试用例表上的用例编号，支持模块查询
    :param field_name:需要的字段名称，直接使用表格的字段名称，可不填写
    :return:
    """
    if field_name==None:
        return ExcelData(tesst_id)[0]
    elif field_name!=None and field_name=="请求头" or field_name=="请求参数" or field_name=="响应预期结果":
        return json.loads(ExcelData(tesst_id)[0][field_name])
    else:
        return ExcelData(tesst_id)[0][field_name]


def data_s(data,name=None):
    """
    传入读取表格的字段，对特定的字段进行转换
    :param data:
    :param name:
    :return:
    """
    if name ==None:
        return data
    elif name!=None and name=="请求头" or name=="请求参数" or name=="响应预期结果":
        return  json.loads(data[name])
    else:
        data[name]

if __name__ == "__main__":
    print(ExcelData("test_user_add-"))



