# https://docs.python.org/3/library/datetime.html
from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays


setlocale(LC_ALL, 'pt_BR.utf-8')

data = datetime(2019, 10, 8, 1, 2, 1)
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.timestamp())
print(data.fromtimestamp(1570507321.0))


new_data = data.strptime('20/04/1987 20:00:00', '%d/%m/%Y  %H:%M:%S')
new_data1 = data.strptime('21/04/1987 20:00:00', '%d/%m/%Y  %H:%M:%S')
date2 = new_data-new_data1
date3 = new_data > new_data1
# print(date3)
# print(date2.total_seconds)
# print(date2.min)
# print(date2.days)
# print(new_data.time)
# new_data = new_data + timedelta(days=5, seconds=59)
# print(new_data.total)

dt = datetime.now()
formatacao = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y  %H:%M:%S')

mes_atual = int(dt.strftime('%m'))

print(mes_atual, mdays[mes_atual])
print(formatacao)
print(formatacao2)
