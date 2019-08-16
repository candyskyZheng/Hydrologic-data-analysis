import re
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


r = input('请输入年份：')
year = int(r[:4])

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


how_much = 0
for y in range(1961, year):
	if y % 4 == 0 or y % 100 == 0 :
		how_much += 366
	else:
		how_much += 365


def search_data(data, how_much):
	d = []
	for line in open(r'D:\pycodes\PYTHON\水文\梅县日降水量.txt', encoding='utf-8'):
		d.append(line.strip('\t\n'))
	if year % 4 == 0 or year % 100 == 0 :
		h2 = how_much + 366
		d = d[how_much:h2]
	else:
		h2 = how_much + 365
		d = d[how_much:h2]
	for da in d:
		result = re.findall(re.compile(r'\d\++\D+\d|\d+\D+\d+|\d+'),da)
		for i in result:
			i = float(i)
			data.append(i)


def draw(date, data):
	my_style = LS('#333366', base_style=LCS)
	my_config = pygal.Config()
	my_config.label_font_size = 14
	my_config.width = 1000

	chart = pygal.Bar(my_config, style=my_style,x_label_rotation=20, show_minor_x_labels=False)
	chart.title = '梅县{}日降水量'.format(year)
	N = 20
	chart.x_labels = date
	chart.x_labels_major = date[::N]
	chart.add('日降水量'.format(year), data)
	chart.render_to_file('梅县{}.svg'.format(year))

def main():
	date = []
	data = []
	dates(year,date)
	search_data(data, how_much)
	draw(date, data)

main()
