import pandas as pd
import os
import requests

def doi_to_csv():
    # Lee el archivo corpus.txt como una serie
    df_dois = pd.read_csv("corpus.txt", header=None, names=["DOIs"])
    dois = df_dois["DOIs"].tolist()

    # Creamos un DataFrame vacío
    documents = pd.DataFrame(columns=['file_name', 'title', 'publication_date'])

    # Creamos un DataFrame vacío
    df = pd.DataFrame(columns=['paperId', 'title', 'abstract', 'year', 'publicationDate', 'authorId', 'authorName'])

    authors_list = []  # Lista de listas de autores

    for doi in dois:
        r = requests.get(f'https://api.semanticscholar.org/v1/paper/{doi}')
        if r.status_code == 200:
            data = r.json()

            author_ids = [author.get('authorId', '') for author in data.get('authors', [])]
            author_names = [author.get('name', '') for author in data.get('authors', [])]

            authors_list.append(author_names)

            author_ids = ','.join(author_ids)
            author_names = ','.join(author_names)

            document_info = [data.get('paperId', ''), data.get('title', ''), data.get('publicationDate', '')]
            documents.loc[len(documents)] = document_info

            author_info = [data.get('paperId', ''), data.get('title', ''), data.get('abstract', ''),
                           data.get('year', ''), data.get('publicationDate', ''), author_ids, author_names]
            df.loc[len(df)] = author_info

    if not os.path.exists('./csvs'):
        os.makedirs('./csvs')

    df.to_csv('./csvs/general.csv', index=False)

    authors_list = [item for sublist in authors_list for item in sublist]

    authors_count = {i: authors_list.count(i) for i in authors_list}

    authors = pd.DataFrame(list(authors_count.items()), columns=['author', 'publications'])

    documents.to_csv('./csvs/documents.csv', index=False)
    authors.to_csv('./csvs/authors.csv', index=False)
