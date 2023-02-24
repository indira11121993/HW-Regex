from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


# Приводим все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.
for new_phone in contacts_list:
  pattern = r'(\+7|8)?\s*\(?(\d{3})\)?[-|\s]*(\d{3})[-|\s]*(\d{2})[-|\s]*(\d{2})\s*[(]*([доб.]+)*\s*(\d{4})*\)?'
  substitution = r'+7(\2)\3-\4-\5 \6\7'
  new_phone[5] = re.sub(pattern, substitution, new_phone[5])


new_contacts_list = []
new_contacts_list.append(contacts_list[0])

dict = {}

for item in contacts_list[1:]:
  lst = [item[0], item[1], item[2]]
  name = ' '.join(lst)
  name_list = name.split()
  value = dict.get(name_list[0])
  if value == None:
    new_line = ['','','','','','','']
  else:
    new_line = value

  for i in range(0, len(name_list)):
    new_line[i] = name_list[i]
  if item[3] != '':
    new_line[3] = item[3]
  if item[4] != '':
    new_line[4] = item[4]
  if item[5] != '':
    new_line[5] = item[5]
  if item[6] != '':
    new_line[6] = item[6]
  dict[new_line[0]] = new_line

for value in dict.values():
  new_contacts_list.append(value)

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts_list)