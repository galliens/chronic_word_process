# 当前文件名
mo = __file__[__file__.rfind('/')+1:]

# 数据结构
chaos = []


# Time
# 用来指示时间，读取文本时候会判断时间，然后把文本装进对应时间的数据结构里
class Time:
    zone = 0
    year = -10000
    month = 0
    day = 0

    @classmethod
    def reset(cls):
        Time.zone = 0
        Time.year = -100000
        Time.month = 0
        Time.day = 0

    @classmethod
    def set_zone(cls,num):
        Time.zone = num
    
    @classmethod
    def set_year(cls,num):
        Time.year = num

    @classmethod
    def set_month(cls,num):
        Time.month = num

    @classmethod
    def set_day(cls,num):
        Time.day = num
    
    @classmethod
    def display(cls):
        if Time.zone == 0:
            print('\n无时间域\n')
        elif Time.zone == 1:
            print(f'\n现在是{Time.year}年\n')
        elif Time.zone == 2:
            print(f'\n现在是{Time.year}年{Time.month}月\n')
        elif Time.zone == 3:
            print(f'\n现在是{Time.year}年{Time.month}月{Time.day}日\n')




# Year
# 表示年的类，可以用来装某年对应的文本
# 类属性
# Year.years 字典，年份-对象 int-<class Year>
# 实例属性
# self.year = int       记录年份
# self.content = list   记录内容
# self.months = dict    记录月份与对应的对象实例 int-<class Month>
# 类方法
# Year.newyear(num)                     创建一个新年份，年份是num
# Year.get_year(year)                    返回某年的实例对象
# Year.addcontent_Year(year,str)        往某年中加内容
# Year.check_year_existed(year)         检查num年是否存在
# Year.get_yearlist_ordered()           返回一个已有年份的列表
# Year.get_monthlist_ordered(year)      返回某年的已有月份列表
# Year.check_month_in_year(year,month)  检查某年是否有某月
# Year.newmonth(year,month)             在某年中创建某月的Month实例
# Year.get_month(year,month)            得到某年的某月的Month实例
class Year:
    # 所有year的字典，key-value是年份-对象 int-<class Year>
    years = {}
    def __init__(self,year):
        self.year = year
        self.content = []
        self.months = {}
    # 初始化某年
    @ classmethod
    def newyear(cls,num):
        if Year.check_year_existed(num):
            raise Exception(f'创建失败，{num}年已经存在！')
        Year.years[num] = Year(num)
    # 返回一个从小到大排序好的yearlist列表
    @classmethod
    def get_yearlist_ordered(cls):
        yearlist = list(Year.years.keys())
        return sorted(yearlist)
    # 检查某年是否已经存在
    @classmethod
    def check_year_existed(cls,year):
        yearlist = Year.get_yearlist_ordered()
        for item in yearlist:
            if item == year:
                return True
        return False
    @classmethod
    def get_year(cls,year):
        return Year.years[year]
    @classmethod
    def get_monthlist_ordered(cls,year):
        monthlist = list(Year.get_year(year).months.keys())
        return sorted(monthlist)
    @classmethod
    def check_month_in_year(cls,year,month):
        monthlist_in_year = Year.get_monthlist_ordered(year)
        for item in monthlist_in_year:
            if item == month:
                return True
        return False
    @classmethod
    def newmonth(cls,year,month):
        if Year.check_month_in_year(year,month):
            raise Exception(f'创建月份失败，{year}年中{month}月已存在！')
        Year.get_year(year).months[month] = Month(month)
    @classmethod
    def get_month(cls,year,month):
        if not Year.check_month_in_year(year,month):
            raise Exception(f'获取失败，{year}年中{month}月不存在！')
        return Year.get_year(year).months[month]
    @classmethod
    def addcontent_Year(cls,year,str):
        if not Year.check_year_existed(year):
            raise Exception(f'添加内容失败，{year}年还不存在，请创建后再往里添加内容')
        Year.get_year(year).content.append(str)








# Month 
# 表示月的类，可以用来装某年某月对应的文本
# 实例属性
# self.month = int        记录月份
# self.content = list     记录内容
# self.days = dict        记录日子以及对应的实例
# 实例方法
# self.addcontent_Month(str)      给该月份加内容
# self.get_daylist_ordered()      返回一个该月份实例的日子时序列表
# self.check_day_in_month(day)    检查该月份中是否有某日
# self.newday(day)                给某月创建某日
# self.get_day(day)               获取某日的实例对象
class Month:
    def __init__(self,month):
        self.month = month
        self.content = []
        self.days = {}
    def addcontent_Month(self,str):
        self.content.append(str)
    def get_daylist_ordered(self):
        daylist = list(self.days.keys())
        return sorted(daylist)
    def check_day_in_month(self,day):
        for item in self.get_daylist_ordered():
            if item == day:
                return True
        return False
    def newday(self,day):
        if self.check_day_in_month(day):
            raise Exception('创建day实例失败，指定day已经存在！')
        self.days[day] = Day(day)
    def get_day(self,day):
        if not self.check_day_in_month(day):
            raise Exception('获取day实例失败，指定day不存在！')
        return self.days[day]







# Day
# 表示日的类，可以用来装某年某月某日对应的文本
# 实例属性
# self.day = int        记录日子
# self.content = list   记录内容
# 实例方法
# self.addcontent_Day(str)      为Day实例添加内容
class Day:
    def __init__(self,day):
        self.day = int (day)
        self.content = []
    def addcontent_Day(self,str):
        self.content.append(str)






# 根据一个lenth最多16的字符串来设定时间域
# 返回值：0，1，2，3，6
# 0 没改
# 1 改年
# 2 改月
# 3 改日
# 8 8数字改
def line_set_time(str):
    number = ''
    counter = 0
    nyr = [False,False,False]
# 一次检测获取信息
    for char in str:
        if char =='#':
            counter +=1
        if char.isdigit():
            number = number + char
        if char == '年':
            nyr[0] = True
        if char == '月':
            nyr[1] = True
        if char == '日' or char == '号':
            nyr[2] = True
# 年月日判定最优先            
    if nyr == [True, False, False]:
        num_nyr = ['','','']
        for char in str:
            if char == '年':
                break
            if char.isdigit():
                num_nyr[0] = num_nyr[0] + char
        Time.set_zone(1)
        if num_nyr[0] !='':
            Time.set_year(int(num_nyr[0]))
        return (1,'\n年月日检测，年改了\n')

    if nyr == [False, True, False]:
        num_nyr = ['','','']
        for char in str:
            if char == '月':
                break
            if char.isdigit():
                num_nyr[1] = num_nyr[1] + char
        Time.set_zone(2)
        if num_nyr[1] !='':
            Time.set_month(int(num_nyr[1]))
        return (2,'\n年月日检测，月改了\n')

    if nyr == [False, False, True]:
        num_nyr = ['','','']
        for char in str:
            if char == '日' or char == '号':
                break
            if char.isdigit():
                num_nyr[2] += char
        Time.set_zone(3)
        if num_nyr[2] !='':
            Time.set_day(int(num_nyr[2]))
        return (3,'\n年月日检测，日改了\n')

    if nyr == [True,True,False]:
        num_nyr = ['','','']
        s = 0
        for char in str:
            if char == '年':
                s += 1
            if char == '月':
                break
            if char.isdigit():
                num_nyr[s] += char
        Time.set_zone(2)
        if num_nyr[0] !='':
            Time.set_year(int(num_nyr[0]))
        if num_nyr[1] !='':
            Time.set_month(int(num_nyr[1]))
        return (2,'\n年月日检测，年月改了\n')

    if nyr == [False,True,True]:
        num_nyr = ['','','']
        s = 1
        for char in str:
            if char == '月':
                s += 1
            if char == '日' or char == '号':
                break
            if char.isdigit():
                num_nyr[s] += char
        Time.set_zone(3)
        if num_nyr[1] !='':
            Time.set_month(int(num_nyr[1]))
        if num_nyr[2] !='':
            Time.set_day(int(num_nyr[2]))
        return (1,'\n年月日检测，月日改了\n')

    if nyr == [True,True,True]:
        num_nyr = ['','','']
        s = 0
        for char in str:
            if (char == '年') or (char == '月'):
                s += 1
            if char == '日' or char == '号':
                break
            if char.isdigit():
                num_nyr[s] += char
        Time.set_zone(3)
        if num_nyr[0] !='':
            Time.set_year(int(num_nyr[0]))
        if num_nyr[1] !='':
            Time.set_month(int(num_nyr[1]))
        if num_nyr[2] !='':
            Time.set_day(int(num_nyr[2]))
        return (1,'\n年月日检测，年月日改了\n')
# 使用#的个数来确定年月日
    if counter == 2:
        if len(number)<5:
            Time.set_zone(1)
            Time.set_year(int(number))
        return (1,'\n#\n改了年\n')
    if counter == 3:
        if len(number) < 3:
            Time.set_zone(2)
            Time.set_month(int(number))
        return (2,'\n#\n改了月\n')
    if counter == 4:
        if len(number) < 3:
            Time.set_zone(3)
            Time.set_day(int(number))
        return (3,'\n#\n改了日\n')
# 八数字检测
    if len(number) >= 8:
        num_nyr = [number[0:4],number[4:6],number[6:8]]
        Time.set_zone(3)
        Time.set_year(int(num_nyr[0]))
        Time.set_month(int(num_nyr[1]))
        Time.set_day(int(num_nyr[2]))
        return (8,'\n年月日改了，八数字版本\n')
    

    if 0<len(number) <5:
        Time.set_zone(1)
        Time.set_year(int(number))
        return (1,'\n年改了，数字版本\n')
    return (0,'\n没检测到时间改变')

# put_in 函数
# 根据时间域把句子填装到数据结构里
def put_in(that):
    if Time.zone == 0:
        chaos.append(that)
    if Time.zone == 1:
        if not Year.check_year_existed(Time.year):      # 没那年就建那年
            Year.newyear(Time.year)
        Year.addcontent_Year(Time.year,that)
    if Time.zone == 2:
        if not Year.check_year_existed(Time.year):      # 没那年就建那年
            Year.newyear(Time.year)
        if not Year.check_month_in_year(Time.year,Time.month):  # 没那月就建那月
            Year.newmonth(Time.year,Time.month)
        Year.get_month(Time.year,Time.month).addcontent_Month(that)
    if Time.zone == 3:
        if not Year.check_year_existed(Time.year):      # 没那年就建那年
            Year.newyear(Time.year)
        if not Year.check_month_in_year(Time.year,Time.month):  # 没那月就建那月
            Year.newmonth(Time.year,Time.month)
        if not Year.get_month(Time.year,Time.month).check_day_in_month(Time.day):
            Year.get_month(Time.year,Time.month).newday(Time.day)
        Year.get_month(Time.year,Time.month).get_day(Time.day).addcontent_Day(that)
        


# def time_format(mode = 0)
#     if mode ==0:
#         if Time.zone ==1:
#             print()




