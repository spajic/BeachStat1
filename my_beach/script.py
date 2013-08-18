def table_header():
    return '<table class=\'sortable\'>\n\
    <thead>\n\
	  <tr>\n\
	    <th>Ф.И.О</th>\n\
		<th>Рейтинг</th>\n\
		<th>% побед</th>\n\
		<th>Побед</th>\n\
		<th>Поражений</th>\n\
		<th>Игр</th>\n\
	  </tr>\n\
	</thead>\n\
	<tfoot>\n\
	  <tr>\n\
	    <td></td>\n\
		<td></td>\n\
		<td></td>\n\
		<td></td>\n\
		<td></td>\n\
		<td></td>\n\
	  </tr>\n\
	</tfoot>\n\
	<tbody>'

def table_footer():
    return '	</tbody>\n\
</table>'

def row_header(num):
	if num % 2 == 1:
	    return '      <tr class=\'odd\'>'
	else:
	    return '      <tr>'

def row_footer(num):
    return '      </tr>'

def pretty_float(s):
    return str( round( float(s)*100, 0 ) ).rstrip('0').rstrip('.')
	
def row_content(row):
    s = ''
    s = s + '        <td>' + row[0] + '</td>\n'                   # Имя
    s = s + '        <td class=\'numeric\'>' + pretty_float( row[1] ) + '</td>\n' # Total
    s = s + '        <td class=\'numeric\'>' + pretty_float( row[2] ) + '</td>\n' # Ratio
    s = s + '        <td class=\'numeric\'>' + row[3] + '</td>\n' # Wins
    s = s + '        <td class=\'numeric\'>' + row[4] + '</td>\n' # Loses
    s = s + '        <td class=\'numeric\'>' + row[5] + '</td>\n' # Games
    return s

f = open('C:\\Users\\1\\Dropbox\\Beach\\my_beach\\gen_day28.txt', 'w');
f.write(table_header()+'\n')

import csv
beachReader = csv.reader(
    open('C:\\Users\\1\\Dropbox\\Beach\\day28.csv'), 
	delimiter=';')
next(beachReader) # Пропускаем заголовок
n = 0
for row in beachReader:
    f.write(row_header(n) + '\n')
    f.write(row_content(row))
    f.write(row_footer(n) + '\n')
    n = n + 1
f.write(table_footer())
