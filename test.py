# import matplotlib.pyplot as plt
# import openpyxl.utils
# import pandas as pd
# from openpyxl import load_workbook
# from matplotlib.animation import FuncAnimation

# fig, ax = plt.subplots()
# line, = ax.plot([], [], 'r-')

# # 设置图表参数
# ax.set_xlim(0, 10)
# ax.set_ylim(0, 100)
# ax.grid(True)

# def get_latest_data():
#     # 获取最新数据
#     # 这里只是一个示例，实际应根据需求修改
#     import random
#     return [random.randint(0, 100) for _ in range(10)]

# def update_data(frame):
#     new_data = get_latest_data()

#     # 更新折线图
#     x_data = list(range(len(new_data)))
#     line.set_data(x_data, new_data)
#     # 重新绘制图表
#     plt.draw()

# # 设置刷新时间和间隔
# interval = 1000 # 刷新间隔，单位为毫秒
# frames = 10 # 总帧数

# # 创建动画
# ani = FuncAnimation(fig, update_data, frames=frames, interval=interval)
# plt.show()

# file = pd.read_csv(r"C:\Users\shiqideng\OneDrive\桌面\test\5400\Library\2022 09 07 14H 43M\2022 09 07 14H 43M Electropherogram.csv")
# file = file[file["Size (bp)"] <= 6000]
# new_file = file.iloc[:,0:2]

# # 获取0到100的区间内y值的最大值
# LM_max_value_in_range = new_file[new_file["Size (bp)"] <= 100][new_file.columns[1]].max()
# UM_max_value_in_range = new_file[new_file["Size (bp)"] >= 4700][new_file.columns[1]].max()

# # 找到对应的最大值的x坐标
# LM_max_x = new_file[new_file[new_file.columns[1]] == LM_max_value_in_range]["Size (bp)"].values[0]
# UM_max_x = new_file[new_file[new_file.columns[1]] == UM_max_value_in_range]["Size (bp)"].values[0]

# # 绘制折线图
# new_file.plot(kind="line", x="Size (bp)", xlabel="Size(bp)", ylabel="RFU", color="k", linewidth=0.5)

# # 添加标记
# plt.annotate("LM", xy=(LM_max_x, LM_max_value_in_range), xytext=(-5, 5), textcoords="offset points",
#              arrowprops=dict(facecolor='red', edgecolor='red', arrowstyle="->"), fontsize=10, color='red')
# plt.annotate("UM", xy=  (UM_max_x, UM_max_value_in_range), xytext=(-5, 5), textcoords="offset points",
#              arrowprops=dict(facecolor='red', edgecolor='red', arrowstyle="->"), fontsize=10, color='red')

# for position in [0, 100, 4700, 5500]:
#     plt.axvline(x=position, color='r', linestyle='--', linewidth=0.5)

# plt.show()

# def clear_and_merge_excel(df, output_file="./test.xlsx", cells_to_clear=['NaN', "备注", "空列", "原始质量浓度", "原始摩尔浓度"], merge_range="G1:H1", header_title="片段大小"):
#     try:
#         with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
#             df.to_excel(writer, sheet_name="Sheet1", index=False)

#         # 加载并处理Excel文件
#         wb = load_workbook(output_file)
#         sheet = wb.active

#         # 高效地清空指定单元格内容
#         for cell_value in cells_to_clear:
#             for row in sheet.iter_rows():
#                 for cell in row:
#                     if cell.value == cell_value:
#                         cell.value = ""

#         # 合并单元格
#         sheet.merge_cells(merge_range)
#         sheet[merge_range.split(":")[0]] = header_title

#         # 保存修改
#         wb.save(output_file)
#     except Exception as e:
#         print(f"Error occurred: {e}")
#         # 根据实际情况，可以选择重新抛出异常或者进行其他错误处理

# # 使用示例
# column = {"文库号":["ED241109202","ED241109203","ED241109204","ED241109205","ED241109206"],
#            "片段大小":[1481.00,1454.00,1497.00,1270.00,1261.00],
#            "质量浓度":[2024.21,872.31,538.91,963.23,543.19],
#            "摩尔浓度":[860.00,899.30,2484.40,1299.20,876.10],
#            "结果":["文库偏大","文库偏小","接头二聚体污染","峰图过宽","多峰"],
#            "判定":["失败","成功","成功","失败","失败"],
#            "片段描述":["","","","",""],
#            "备注":["待反馈","成功","失败","待反馈","成功"],
#            "空列":["","","","",""],
#            "原始质量浓度":[2024.21,872.31,538.91,963.23,543.19],
#            "原始摩尔浓度":[860.00,899.30,2484.40,1299.20,876.10],
#            "稀释倍数":[1,1,1,1,1]}
# # 创建DataFrame并写入Excel
# df = pd.DataFrame.from_dict(column)
# clear_and_merge_excel(df)

from DataOperation.Module import detectEncoding, getConfig
import pandas as pd
import re

def caculat(smearTable):
    smearTable = detectEncoding(smearFilePath)
    column = ["Well","Sample ID","Range","ng/uL", "nmole/L", "Avg. Size"]
    SMEARADAPTOR="100 bp to 150 bp"
    SMWAESMALLFRAG = "150 bp to 260 bp"
    SMEARAVERAGWFRAG = "200 bp to 4000 bp"
    SMEARDETERMINEFRAG = "200 bp to 6000 bp"
    # 格式化样本数据，去除无SmearPeak的样本
    smearTable = smearTable.dropna(subset=["Range"])
    smearTable = smearTable.loc[:,column]
    smearTable.fillna(0, inplace=True)

    # 获取样本名称输出一个列表
    newSmearTable = smearTable.duplicated(subset=["Sample ID"])
    newSmearTableIndex = newSmearTable[newSmearTable==False].index

    sampleIDList = smearTable.loc[newSmearTableIndex]["Sample ID"].to_list()

    # 去除列表中的空字符串
    dupSampleIDList = list(filter(lambda x: x == x, sampleIDList))
    # 设置表头
    resultDataFrameColumn = ["文库号","片段大小","质量浓度","摩尔浓度","结果","判定","片段描述","备注","空列","原始质量浓度","原始摩尔浓度","稀释倍数"]

    resultDataFrame = pd.DataFrame(columns=resultDataFrameColumn)

    for sampleID in dupSampleIDList:
        sampleDataFrame = smearTable[smearTable["Sample ID"] == sampleID]
        adaptorMolarity = sampleDataFrame.loc[smearTable["Range"]==SMEARADAPTOR,"nmole/L"].to_list()[0]
        smallFragMolarity = sampleDataFrame.loc[smearTable["Range"]==SMWAESMALLFRAG,"nmole/L"].to_list()[0]
        averageFragMolarity = sampleDataFrame.loc[smearTable["Range"]==SMEARAVERAGWFRAG,"nmole/L"].to_list()[0]
        averageFragConc = sampleDataFrame.loc[smearTable["Range"]==SMEARAVERAGWFRAG,"ng/uL"].to_list()[0]
        averageFragment = sampleDataFrame.loc[smearTable["Range"]==SMEARAVERAGWFRAG,"Avg. Size"].to_list()[0]
        determineFragment = sampleDataFrame.loc[smearTable["Range"]==SMEARDETERMINEFRAG,"Avg. Size"].to_list()[0]
        # 计算占比情况
        totalMolarity = adaptorMolarity + smallFragMolarity + averageFragMolarity
        adaptorPercentage = adaptorMolarity/totalMolarity
        smallFrafPercentage = smallFragMolarity/totalMolarity
        # 判断样品是否合格
        result = ""
        judge = ""
        # 接头二聚体情况判断
        if adaptorPercentage >= 0.03:
            if len(result) >0:
                result += ";接头二聚体污染"
            else:
                result += "接头二聚体污染"
        elif adaptorPercentage < 0.03:
            pass
        # 小片段情况判断
        if smallFrafPercentage >= 0.1:
            if len(result) >0:
                result += ";小片段污染"
            else:
                result += "小片段污染"
        elif smallFrafPercentage < 0.1:
            pass
        # 文库大小判断
        if determineFragment <260:
            if len(result) >0:
                result += ";文库偏小"
            else:
                result += "文库偏小"
        elif determineFragment > 650:
            if len(result) >0:
                result += ";文库偏大"
            else:
                result += "文库偏大"
        # 综合判断
        if len(result) == 0:
            judge += "成功"
        elif len(result) > 0:
            # 判断文库类型
            pattern = re.compile('^W')
            if pattern.match(sampleID):
                judge += "风险上机"
            else:
                judge += "待反馈"
        # 汇总结果，插入到新Dataframe中
        excelDict = {"文库号":sampleID,
                     "片段大小":averageFragment,
                     "质量浓度":averageFragConc,
                     "摩尔浓度":averageFragMolarity,
                     "结果":result,
                     "判定":judge,
                     "片段描述":"",
                     "备注":"",
                     "空列":"",
                     "原始质量浓度":averageFragConc,
                     "原始摩尔浓度":averageFragMolarity,
                     "稀释倍数":1
                    }
        newPD = pd.DataFrame(excelDict, index=[0])
        resultDataFrame = pd.concat([resultDataFrame, newPD], ignore_index=True)
    
    return resultDataFrame

smearFilePath = r"D:\Code\dataprocess\Data\test.csv"

if __name__ == "__main__":
    a = caculat(smearFilePath)
    print(a)

