#!/usr/bin/env python3

from datetime import date
import os

from IPython.core.display import display, HTML
import pandas as pd
import sqlalchemy
from SPARQLWrapper import SPARQLWrapper2

print('Last notebook update: {}'.format(date.today().isoformat()))

print('Importing libs')
print('Defining database parameters')
SITE_URL = 'https://musicbrainz.org'
WIKIDATA_URL = 'https://www.wikidata.org/wiki'

PGHOST = os.environ.get('PGHOST', 'localhost')
PGDATABASE = os.environ.get('PGDATABASE', 'musicbrainz_db')
PGUSER = os.environ.get('PGUSER', 'musicbrainz')
PGPASSWORD = os.environ.get('PGPASSWORD', 'musicbrainz')


print('Defining *sql* helper function')


def sql(query, **kwargs):
    """helper function for SQL queries using the %(...) syntax
    Parameters for the query must be passed as keyword arguments
    e.g. sql('SELECT * FROM artist WHERE name=%(singer)s', singer='Bob Dylan')
    """
    engine = sqlalchemy.create_engine(
        'postgresql+psycopg2://'
        '{PGUSER}:{PGPASSWORD}@{PGHOST}/{PGDATABASE}'.format(**globals()),
        isolation_level='READ UNCOMMITTED')
    return pd.read_sql(query, engine, params=kwargs)


MB_DATABASE_VERSION = None


def mb_database_version():
    global MB_DATABASE_VERSION
    if MB_DATABASE_VERSION is None:
        try:
            MB_DATABASE_VERSION = sql("""
                SELECT open_time
                FROM edit
                ORDER BY id DESC
                LIMIT 1;
            """).open_time[0].date().isoformat()
        except IndexError:
            MB_DATABASE_VERSION = sql("""
                SELECT last_updated
                FROM release
                ORDER BY id DESC
                LIMIT 1;
            """).last_updated[0].date().isoformat()
    return MB_DATABASE_VERSION


print('Last database update: {}'.format(mb_database_version()))


print()


# helper function to build canonical URLs
def _mb_link(entity_type, mbid):
    return ('<a target="_blank" '
            f'href="{SITE_URL}/{entity_type}/{mbid}">{mbid}</a>')


print('Defining *sparql* helper function')


def sparql(query, endpoint="https://query.wikidata.org/sparql", **kwargs):
    wrapper = SPARQLWrapper2(endpoint)
    wrapper.setQuery(query)
    results = wrapper.query()

    def _clean_url(url):
        if not url.startswith('http'):
            return url
        if 'wikidata.org' in url or 'musicbrainz.org' in url:
            return url.split('/')[-1]
        return url

    return pd.DataFrame([
        {k: _clean_url(v.value) for k, v in result.items()}
        for result in results.bindings])


# helper function to build canonical URLs
def wd_link(wdid):
    return ('<a target="_blank" '
            f'href="{WIKIDATA_URL}/{wdid}">{wdid}</a>')


def df_to_html(original_df, **kwargs):
    entity_type = kwargs.get('entity_type',
                             globals().get('ENTITY_TYPE', 'artist'))
    df = original_df.copy()
    df.index = range(len(df))
    if 'wd' in df.columns:
        df.wd = df.wd.apply(wd_link)
    if 'mbid' in df.columns:
        df.mbid = df.mbid.apply(lambda mbid: _mb_link(entity_type, mbid))
    return df.to_html(escape=False, **kwargs)


def display_df(df, **kwargs):
    display(HTML(df_to_html(df, **kwargs)))
