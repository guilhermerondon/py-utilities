import csv
import vobject

# Usando apenas o nome do arquivo já que está na mesma pasta
with open('contato.vcf', 'r', encoding='latin-1') as vcf_file:
    vcf_data = vobject.readComponents(vcf_file.read())

with open('contato.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Nome', 'Telefone'])  # Cabeçalho

    for vcard in vcf_data:
        nome = vcard.fn.value if 'fn' in vcard.contents else ''
        telefone = vcard.tel.value if 'tel' in vcard.contents else ''
        csv_writer.writerow([nome, telefone])  # Somente nome e telefone
