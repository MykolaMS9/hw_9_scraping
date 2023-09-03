import json
import pathlib

from models import Authors, Qoutes
import connect


def load_from_json(filename):
    with open(filename, encoding='utf-8') as file:
        file_data = json.load(file)
    return file_data


def main():
    working_path = pathlib.Path.cwd().parent
    authors_filename = working_path / 'bs_4' / 'authors.json'
    quotes_filename = working_path / 'bs_4' / 'quotes.json'

    print('Writing authors to mongodb...')
    for author in load_from_json(authors_filename):
        try:
            authors_obj = Authors(
                fullname=author['fullname'],
                born_date=author['born_date'],
                born_location=author['born_location'],
                description=author['description']
            ).save()
        except:
            pass

    author_objs = Authors.objects()

    def fin(fullname):
        for val in author_objs:
            if val.to_mongo().to_dict()['fullname'] == fullname:
                return val.to_mongo().to_dict()['_id']

    print('Writing quotes to mongodb...')
    for quote_f in load_from_json(quotes_filename):
        try:
            quote_ = Qoutes(
                author=fin(quote_f['author']),
                quote=quote_f['quote'],
                tags=quote_f['tags']
            ).save()
        except:
            pass


if __name__ == '__main__':
    main()
    print('Done')
