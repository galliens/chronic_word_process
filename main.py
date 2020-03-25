# # -*- coding: utf-8 -*-
# import ds_and_func as yo
# import os
# import pprint
# # 本文件所在目录以及文件名的字符串
# mydir = __file__[:__file__.rfind('/')+1]
# me = __file__[__file__.rfind('/')+1:]



# print('\n'+'*'*40+'程序开始了'+'*'*40+'\n')
# # 获取当前目录所有文件
# filelist = os.listdir(mydir)
# # 如果有output文件则提示错误并退出
# for file in filelist:
#     if file == 'output':
#         while a = input('本文件夹中已经存在名为output的文件，请问如何处理 \
#             1. 删除 \
#                 2. 关闭程序，我自己处理完再来')



# # 控制是否输出处理过程
# fileprocess_output = input('请问是否显示处理文件过程:\n1. 显示过程\n2. 不显示过程\n3. 我不搞了，给爷把程序退了\n\n')
# if fileprocess_output == '3':
#     exit('\n本程序已经关闭！')
# while (fileprocess_output != '1') and (fileprocess_output != '2') :
#     if fileprocess_output == '3':
#         exit('\n本程序已经关闭！')
#     fileprocess_output = input('请输入 1 或者 2 或者 3！\n请问是否显示处理文件过程:\n1. 显示过程\n2. 不显示过程\n3. 我不搞了，给爷把程序退了\n\n')



# for file in filelist:
# # 去掉.开头的隐藏文件
# # 去掉自己
# # 去掉yo模块的文件
# # 去掉README.md
#     if file[0] == '.':
#         if fileprocess_output == '1':
#             print(f'{file}是.开头的隐藏文件，跳过\n')
#         continue
#     if file == me :
#         if fileprocess_output == '1':
#             print(f'{file}是我自己，我就不整自己了\n')
#         continue
#     if file == yo.mo :
#         if fileprocess_output == '1':
#             print(f'{file}是我兄弟模块，我就不整他了\n')
#         continue
#     if file == 'README.md' :
#         if fileprocess_output == '1':
#             print(f'{file}是本程序说明文件，我就不整他了\n')
#         continue
# # 打开文件开始操作
#     try:
#         with open(file,'r',encoding='utf-8') as thefile:
#             yo.Time.reset()
#             if fileprocess_output == '1':
#                 print('\n现在开始整合',file,'文件\n')
#             process = thefile.readlines()
#             for line in process:
#                 if line == '\n':
#                     continue
#                 time_judge = line[:16]  # 每行前面的切片
#                 result = yo.line_set_time(time_judge)
#                 # yo.Time.display()
#                 # print(result[1])
#                 if result[0] == 8:
#                     line = line[8:]
#                     while line[0] == ' ':
#                         line = line [1:]
#                     if line == '\n':
#                         continue
#                     yo.put_in(line)
#                 if result[0] == 0:
#                     yo.put_in(line)
#             if fileprocess_output == '1':
#                 print(file,'文件已整合完毕！\n')
#     except IsADirectoryError:
#         if fileprocess_output == '1':
#             print(file,'是一个目录，跳过\n')
#         continue

# shuchu = input(' \
# 请选择输出格式:\n \
# 1. 简式markdown格式\n \
# 2. 繁式markdown格式\n \
# 3. 8数字单行输出\n \
# ')
# while (shuchu != '1') and (shuchu != '2') and (shuchu != '3'):
#     shuchu = input(' \
# 请输入规定的数字！\n\n \
# 请选择输出格式:\n \
# 1. 简式markdown格式\n \
# 2. 繁式markdown格式\n \
# 3. 8数字单行输出\n \
# ')


# # 输出
# # 1,markdown 简单输出
# if shuchu == '1':
#     yearlist = yo.Year.get_yearlist_ordered()
#     with open('output','w') as f:
#         for year in yearlist:
#             f.write('## %d年\n\n'%year)
#             if yo.Year.years[year].content != []:
#                 for line in yo.Year.years[year].content:
#                     f.write(f'{line}\n')
#             for month in yo.Year.get_monthlist_ordered(year):
#                 f.write('### %d月\n\n'%month)
#                 if yo.Year.get_month(year,month).content != []:
#                     for line in yo.Year.get_month(year,month).content:
#                         f.write(f'{line}\n')
#                 for day in yo.Year.get_month(year,month).get_daylist_ordered():
#                     f.write('#### %d日\n\n'%day)
#                     for line in yo.Year.get_month(year,month).get_day(day).content:
#                         f.write(f'{line}\n')

# # 2，markdown繁式输出
# if shuchu == '2':
#     yearlist = yo.Year.get_yearlist_ordered()
#     with open('output','w') as f:
#         for year in yearlist:
#             f.write('## %d年\n\n'%year)
#             if yo.Year.years[year].content != []:
#                 for line in yo.Year.years[year].content:
#                     f.write(f'{line}\n')
#             for month in yo.Year.get_monthlist_ordered(year):
#                 f.write('### %d年%d月\n\n'%(year,month))
#                 if yo.Year.get_month(year,month).content != []:
#                     for line in yo.Year.get_month(year,month).content:
#                         f.write(f'{line}\n')
#                 for day in yo.Year.get_month(year,month).get_daylist_ordered():
#                     f.write('#### %d年%d月%d日\n\n'%(year,month,day))
#                     for line in yo.Year.get_month(year,month).get_day(day).content:
#                         f.write(f'{line}\n')

# # 3，8数字单行输出
# try:
#     if shuchu == '3':
#         yearlist = yo.Year.get_yearlist_ordered()
#         with open('output','w') as f:
#             for year in yearlist:
#                 if yo.Year.years[year].content != []:
#                     for line in yo.Year.years[year].content:
#                         f.write('%-8d '%year)
#                         f.write(f'{line}\n')
#                 for month in yo.Year.get_monthlist_ordered(year):
#                     if yo.Year.get_month(year,month).content != []:
#                         for line in yo.Year.get_month(year,month).content:
#                             f.write('%d-%2d   '%(year,month))
#                             f.write(f'{line}\n')
#                     for day in yo.Year.get_month(year,month).get_daylist_ordered():
#                         for line in yo.Year.get_month(year,month).get_day(day).content:
#                             f.write('%d-%2d-%2d '%(year,month,day))
#                             f.write(f'{line}\n')
# except:
#     print('输出过程发生错误，已将output文件删除！')
#     exit()



# print('\n'+'*'*40+'程序结束了'+'*'*40+'\n')


while (a = input
