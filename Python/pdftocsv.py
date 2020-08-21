"""" My mom needed a simple script to merge info from various pdf to a single file she could use in excel """
import pdfplumber
import csv
import os

with open('tabela.csv', 'w', newline='') as csvfile:
    print('tabela iniciada')

fileNames = []
for root, dirs, files in os.walk(r'.'):
    for file in files:
        if file.endswith('.pdf'):
            fileNames.append(file)
print(fileNames)

for table in fileNames:
    with pdfplumber.open(table) as pdfFile:
        print(f'usando tabela {table}')
        for i in range(len(pdfFile.pages)):
            page = pdfFile.pages[i]
            try:
                texto = page.extract_table()
                texto = [[linha[0], linha[0].split(' ')[1][-2:], linha[1].split(',')[0]] for linha in texto if 'PNEU' in linha[0]]
                # texto = [[linha[0], linha[1].split(',')[0]] for linha in texto if 'PNEU' in linha[0]]
                with open('tabela.csv', 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerows(texto)
                print(f'pagina {i} carregada')
            except:
                print(f'erro na pagina {i}')