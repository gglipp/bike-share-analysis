import csv
from datetime import datetime


def print_first_point(filename):
    """
    本函数会输出并返回指定的 csv 文件 （含页眉行）的第一个数据点（即文件的第二行）。
    """
    # 输出城市名以供参考
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))

    with open(filename, 'r') as f_in:
        ## 待办：用 csv 库来设置一个 DictReader 对象。#tml           ##
        trip_reader = csv.DictReader(f_in)

        ## 待办：对 DictReader 对象使用函数     ##
        ## 从而读取数据文件的第一条骑行记录并将其存储为一个变量     ##
        ## 见 https://docs.python.org/3/library/csv.html#reader-objects ##
        first_trip = trip_reader.__next__()

        ## 待办：用 pprint 库来输出第一条骑行记录。 ##
        ## 见 https://docs.python.org/3/library/pprint.html     ##

    # 输出城市名和第一条骑行记录以备测试
    return (city, first_trip)


# 各城市的文件列表
data_files = ['./data/NYC-CitiBike-2016.csv',
              './data/Chicago-Divvy-2016.csv',
              './data/Washington-CapitalBikeshare-2016.csv', ]

# 输出各文件的第一条骑行记录，并将其储存在字典中
example_trips = {}
for data_file in data_files:
    city, first_trip = print_first_point(data_file)
    example_trips[city] = first_trip

nyc = example_trips["NYC"]
chicago = example_trips["Chicago"]
washington = example_trips["Washington"]

print(example_trips["NYC"])
time = example_trips["NYC"].get("starttime")
print(time)
dt = datetime.strptime(time, "%m/%d/%Y %H:%M:%S")
print(dt.strftime("%#m %#H %#A"))
print(type(dt.strftime("%#m %#H %#A")))
print(dt.strftime("%#m %#H %#A").split(" "))

print("======================")
print(example_trips["Chicago"])
time2 = example_trips["Chicago"].get("starttime")
print(time2)
dt2 = datetime.strptime(time2, "%m/%d/%Y %H:%M")
print(dt2.strftime("%#m %#H %#A"))

print("=====================")
print(example_trips["Washington"])
time3 = example_trips["Washington"].get("Start date")
print(time3)
dt3 = datetime.strptime(time3, "%m/%d/%Y %H:%M")
print(dt3.strftime("%#m %#H %#A"))

print("========================")
print(nyc.get("usertype"))
print(chicago.get("usertype"))
print(washington.get("Member Type"))

a = '123.42132'
print(float(a))
print(float('%.2f' % float(a)))
print(format(float(a),".2f"))
print(type(format(float(a),".2f")))