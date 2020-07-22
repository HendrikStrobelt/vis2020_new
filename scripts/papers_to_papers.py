import csv
import argparse

parser = argparse.ArgumentParser(description='convert to MiniConf papers')
parser.add_argument('--public', type=str, default='extractor/all_papers.csv',
                    help='public file')
parser.add_argument('--out', type=str, default='../sitedata/papers.csv')

args = parser.parse_args()


# print(args.accumulate(args.integers))

def convert():
    cols_in = ['Conference',
               'Year',
               'Title',
               'DOI',
               'Link',
               'FirstPage',
               'LastPage',
               'PaperType',
               'Abstract',
               'AuthorNames-Deduped',
               'AuthorNames',
               'AuthorAffiliation',
               'InternalReferences',
               'AuthorKeywords',
               'AminerCitationCount_02-2020',
               'AminerCitationCount_06-2020',
               'XploreCitationCount - 2020-01',
               'PubsCited',
               'Award',
               'pdf_local']

    out = "UID,title,authors,abstract,keywords,session,pdf_local,ieee_link"

    with open(args.public, 'r') as f, open(args.out, 'w') as t:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(t, fieldnames=out.split(','))

        writer.writeheader()

        for row in reader:
            writer.writerow({
                'UID': row['DOI'].replace('/','_'),
                'title': row['Title'],
                'authors': row['AuthorNames-Deduped'].replace(';','|'),
                'abstract': row['Abstract'],
                'keywords': row['AuthorKeywords'].lower().replace(',','|'),
                'session': row['Conference'],
                'pdf_local': row['pdf_local'].replace('papers/',''),
                'ieee_link': row['Link']
            })


if __name__ == '__main__':
    convert()
