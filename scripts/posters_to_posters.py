import csv
import argparse

parser = argparse.ArgumentParser(description='convert to MiniConf papers')
parser.add_argument('--public', type=str, default='extractor/all_posters.csv',
                    help='public file')
parser.add_argument('--out', type=str, default='../sitedata/posters.csv')

args = parser.parse_args()


# print(args.accumulate(args.integers))

def convert():
    cols_in = "title,link,authors".split(',')

    out = "UID,title,authors,abstract,keywords,session,pdf_local,ieee_link"

    with open(args.public, 'r') as f, open(args.out, 'w') as t:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(t, fieldnames=out.split(','))

        writer.writeheader()

        for row in reader:
            writer.writerow({
                'UID': row['link'].replace('/','_').replace('.','_'),
                'title': row['title'],
                'authors': row['authors'].replace(',','|'),
                'abstract': 'lorem ipsum',
                'keywords': 'posters',
                'session': 'posters',
                'pdf_local': row['link'],
                # 'ieee_link': row['Link']
            })


if __name__ == '__main__':
    convert()
