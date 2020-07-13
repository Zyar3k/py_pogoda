from requests import get
from json import loads
from terminaltables import AsciiTable

CITIES = ['Kielce', 'Kraków']

def main():
  url = 'https://danepubliczne.imgw.pl/api/data/synop'
  response = get(url)

  rows = [
    ['Miasto', 'Godzina pomiaru', 'Temperatura']
  ]


  for row in loads(response.text):
    if row['stacja'] in CITIES:      
      rows.append([
        row['stacja'],
        row['data_pomiaru'],
        row['temperatura']
      ])

  table = AsciiTable(rows)
  print(table.table)

if __name__ == '__main__':
  print('Pogoodynka 2020')
  main()