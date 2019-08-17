import re
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 按年份查询 main_1
# x轴：日期
def dates(year, date):
	month = [1,2,3,4,5,6,7,8,9,10,11,12]
	for i in month:
		if i == 1 or i == 3 or i == 5 or  i == 7 or  i == 8 or  i == 10 or  i == 12 :
			for date_num in range(1,32):
				date.append('{}月{}日'.format(i, date_num))
		elif i == 4 or i == 6 or i ==  9 or i == 11 :
			for date_num2 in range(1,31):
				date.append('{}月{}日'.format(i, date_num2))
		elif i == 2 and (year%4==0 or year%100==0):
			for date_num3 in range(1,30) :
				date.append('{}月{}日'.format(i, date_num3))
		else:
			for date_num4 in range(1,29) :
				date.append('{}月{}日'.format(i, date_num4))

# 从文档读取数据
def search_data(data):
	# 开始查询的位置
	how_much = 0
	for y in range(1961, year):
		if y % 4 == 0 or y % 100 == 0 :
			how_much += 366
		else:
			how_much += 365

	d = []
	for line in open(r'D:\pycodes\PYTHON\水文\梅县日降水量.txt', encoding='utf-8'):
		d.append(line.strip('\t\n'))
	if year % 4 == 0 or year % 100 == 0 :
		h2 = how_much + 366          #闰年
		d = d[how_much:h2]           #开始和结束的位置
	else:
		h2 = how_much + 365          #平年
		d = d[how_much:h2]
	for da in d:
		result = re.findall(re.compile(r'\d\++\D+\d|\d+\D+\d+|\d+'),da)
		for i in result:
			i = float(i)      # str转float
			data.append(i)


def draw(date, data):
	my_style = LS('#333366', base_style=LCS)
	my_config = pygal.Config()
	my_config.label_font_size = 14
	my_config.width = 1000

	chart = pygal.Bar(my_config, style=my_style,x_label_rotation=20, show_minor_x_labels=False)
	chart.title = '梅县{}年 日降水量'.format(year)
	N = 20
	chart.x_labels = date
	chart.x_labels_major = date[::N]
	chart.add('日降水量'.format(year), data)
	chart.render_to_file('梅县{}.svg'.format(year))

def main_1():
	date = []
	data = []
	dates(year,date)
	search_data(data)
	draw(date, data)


#按月查询
def dates2(input_month_year,input_month,date2):
	if input_month == 1 or input_month == 3 or input_month == 5 or \
	input_month == 7 or input_month == 8 or input_month == 10 or input_month == 12 :
		for i in range(1,32):
			date2.append('{}月{}号'.format(input_month,i))
	elif input_month == 4 or input_month == 6 or input_month == 9 or input_month == 11 :
		for i in range(1,31):
			date2.append('{}月{}号'.format(input_month,i))
	elif input_month == 2 and(input_month_year%4 == 0 or input_month_year%100 == 0):
		for i in range(1,30):
			date2.append('{}月{}号'.format(input_month,i))
	else:
		for i in range(1,29):
			date2.append('{}月{}号'.format(input_month,i))

def search_data2(date2, data2):
	how_much = 0
	for y in range(1961, input_month_year):
		if y % 4 == 0 or y % 100 == 0 :
			how_much += 366
		else:
			how_much += 365
	for i in range(1,input_month):
		if i == 1 or i == 3 or i == 5 or  i == 7 or  i == 8 or  i == 10 or  i == 12 :
			how_much += 31
		elif i == 4 or i == 6 or i ==  9 or i == 11 :
			how_much += 30
		elif i == 2 and (input_month_year%4==0 or input_month_year%100==0):
			how_much += 29
		else:
			how_much += 28 
	d = []
	for line in open(r'D:\pycodes\PYTHON\水文\梅县日降水量.txt', encoding='utf-8'):
		d.append(line.strip('\t\n'))
	h2 = how_much + len(date2)
	d = d[how_much:h2]
	for da in d:
		result = re.findall(re.compile(r'\d\++\D+\d|\d+\D+\d+|\d+'),da)
		for i in result:
			i = float(i)
			data2.append(i)

def draw2(date2, data2):
	my_style = LS('#333366', base_style=LCS)
	my_config = pygal.Config()
	my_config.label_font_size = 14
	my_config.width = 1000

	chart = pygal.Bar(my_config, style=my_style,x_label_rotation=20, show_minor_x_labels=False)
	chart.title = '梅县{}年{}月降水量'.format(input_month_year, input_month)
	N = 5
	chart.x_labels = date2
	chart.x_labels_major = date2[::N]
	chart.add('梅县{}年{}月降水量'.format(input_month_year, input_month),data2)
	chart.render_to_file('梅县{}年{}月降水量.svg'.format(input_month_year, input_month))

def main_2():
	date2 = []
	data2 = []
	dates2(input_month_year,input_month,date2)
	search_data2(date2, data2)
	draw2(date2, data2)


print('*****广东梅州市梅县区 1961年--2016年 日降水量查询*****')
user_input = input('按年份查询 1，按月份查询2（例198812）:')
if user_input == '1':
	r = input('请输入年份：')
	year = int(r[:4])
	main_1()
elif user_input == '2':
	r = input('请输入年份月份：')
	input_month_year = int(r[:4])
	input_month = int(r[4:7])
	main_2()
