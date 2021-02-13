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
DISCOGS_URL = 'https://discogs.com'
MB_URL = 'https://musicbrainz.org'
WIKIDATA_URL = 'https://www.wikidata.org/wiki'
DATA_BNF_URL = 'http://data.bnf.fr/ark:/12148'

PGHOST = os.environ.get('PGHOST', 'localhost')
PGDATABASE = os.environ.get('PGDATABASE', 'musicbrainz_db')
PGUSER = os.environ.get('PGUSER', 'musicbrainz')
PGPASSWORD = os.environ.get('PGPASSWORD', 'musicbrainz')

MB_ENTITIES = [
    'area',
    'artist',
    'event',
    'instrument',
    'label',
    'place',
    'recording',
    'release',
    'release_group',
    'series',
    'work',
]

WD_MB_LINK_PROPERTIES = {
    'area': 'P982',
    'artist': 'P434',
    'event': 'P6423',
    'instrument': 'P1330',
    'label': 'P966',
    'place': 'P1004',
    'recording': 'P4404',
    'release': 'P5813',
    'release_group': 'P436',
    'series': 'P1407',
    'work': 'P435',
}


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
            f'href="{MB_URL}/{entity_type}/{mbid}">{mbid}</a>')


def mb_artist_edit_wd_link(item):
    return (
        '<a target="_blank" '
        f'href="{MB_URL}/artist/{item.mbid}/edit?'
        'edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&'
        f'edit-artist.url.99.text={WIKIDATA_URL}/{item.wd}">'
        'edit</a>')


def mb_event_edit_wd_link(item):
    return (
        '<a target="_blank" '
        f'href="{MB_URL}/event/{item.mbid}/edit?'
        'edit-event.url.99.type=b022d060-e6a8-340f-8c73-6b21b1d090b9&'
        f'edit-event.url.99.text={WIKIDATA_URL}/{item.wd}">'
        'edit</a>')


def mb_label_edit_lc_link(item):
    return (
        '<a target="_blank" '
        f'href="{MB_URL}/label/{item.mbid}/edit?'
        f'edit-label.label_code={item.lc_wd}">'
        'edit</a>')


def mb_label_edit_wd_link(item):
    return (
        '<a target="_blank" '
        f'href="{MB_URL}/label/{item.mbid}/edit?'
        'edit-label.url.99.type=75d87e83-d927-4580-ba63-44dc76256f98&'
        f'edit-label.url.99.text={WIKIDATA_URL}/{item.wd}">'
        'edit</a>')


def mb_label_edit_bnf_link(item):
    return (
        '<a target="_blank" '
        f'href="{MB_URL}/label/{item.mbid}/edit?'
        'edit-label.url.99.type=83eca2b3-5ae1-43f5-a732-56fa9a8591b1&'
        f'edit-label.url.99.text=https://catalogue.bnf.fr/ark:/12148/cb{item.bnf}">'
        'edit</a>')


def mb_releasegroup_edit_wd_link(item):
    return (
        '<a target="_blank" '
        f'href="{MB_URL}/release-group/{item.mbid}/edit?'
        'edit-release-group.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&'
        f'edit-release-group.url.99.text={WIKIDATA_URL}/{item.wd}">'
        'edit</a>')


def mb_work_edit_wd_link(item):
    return (
        '<a target="_blank" '
        f'href="{MB_URL}/work/{item.mbid}/edit?'
        'edit-work.url.99.type=587fdd8f-080e-46a9-97af-6425ebbcb3a2&'
        f'edit-work.url.99.text={WIKIDATA_URL}/{item.wd}">'
        'edit</a>')


print('Defining *sparql* helper function')


def sparql(query, endpoint="https://query.wikidata.org/sparql", **kwargs):
    wrapper = SPARQLWrapper2(endpoint)
    wrapper.setQuery(query)
    results = wrapper.query()

    def _clean_url(url):
        if not url.startswith('http'):
            return url
        if 'wikidata.org' in url or 'musicbrainz.org' in url or 'bnf.fr' in url:
            return url.split('/')[-1]
        return url

    return pd.DataFrame([
        {k: _clean_url(v.value) for k, v in result.items()}
        for result in results.bindings])


def wd_entity_count(entity_type, prop):
    df = sparql(f"""
        SELECT (count(?{entity_type}) as ?cnt)
        WHERE {{
          ?{entity_type} wdt:{prop} ?mbid .
        }}
    """)
    return int(df.cnt[0])


# helper function to build canonical URLs
def wd_link(wdid):
    return ('<a target="_blank" '
            f'href="{WIKIDATA_URL}/{wdid}">{wdid}</a>')


def bnf_link(bnf):
    return ('<a target="_blank" '
            f'href="{DATA_BNF_URL}/{bnf}">{bnf}</a>')


def discogs_link(entity_type, id):
    type = {
        'release-group': 'master',
    }.get(entity_type, entity_type)
    return ('<a target="_blank" '
            f'href="{DISCOGS_URL}/{type}/{id}">{id}</a>')


def df_to_html(original_df, reindex=True, **kwargs):
    entity_type = kwargs.get('entity_type',
                             globals().get('ENTITY_TYPE', 'artist'))
    df = original_df.copy()
    if reindex:
        df.index = range(len(df))
    if 'wd' in df.columns:
        df.wd = df.wd.apply(wd_link)
    if 'bnf' in df.columns:
        df.bnf = df.bnf.apply(bnf_link)
    if 'mbid' in df.columns:
        df.mbid = df.mbid.apply(lambda mbid: _mb_link(entity_type, mbid))
    if 'discogs' in df.columns:
        df.discogs = df.discogs.apply(lambda id: discogs_link(entity_type, id))
    return df.to_html(escape=False, **kwargs)


def display_df(df, **kwargs):
    display(HTML(df_to_html(df, **kwargs)))


def partial_query(entity, url_pattern):
    link_table = f"l_{entity + '_url' if entity < 'url' else 'url_' + entity}"
    entity_idx, url_idx = (0, 1) if entity < 'url' else (1, 0)
    return f"""
    FROM
        url
        JOIN {link_table} AS link ON link.entity{url_idx} = url.id
        JOIN {entity} ON link.entity{entity_idx} = {entity}.id
    WHERE
        url.url LIKE '%%{url_pattern}%%'
    """


def mb_entity_count(entity, url_pattern='wikidata.org'):
    df = sql(f"""
    SELECT
        COUNT({entity}.gid) AS cnt
    {partial_query(entity, url_pattern)}
    ;
    """)
    return int(df.cnt[0])


def mb_entity_list(entity, url_pattern='wikidata.org'):
    df = sql(f"""
    SELECT
        url.url AS wd,
        {entity}.gid AS mbid,
        {entity}.name
    {partial_query(entity, url_pattern)}
    ORDER BY
        {entity}.name
    ;
    """)
    df.wd = df.wd.apply(lambda s: s.split('/')[-1])
    df.mbid = df.mbid.apply(str)
    return df


def bnf_entity_count(entity_type):
    type = {
        'release_group': 'release-group'
    }.get(entity_type, entity_type)
    df = sparql(f"""
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

        SELECT (COUNT(?concept) AS ?cnt)
        WHERE {{
            ?concept skos:exactMatch ?mb .
            FILTER (regex (?mb, 'musicbrainz.org/{type}/'))
        }}
    """, endpoint='http://data.bnf.fr/sparql')
    return int(df.cnt[0])


def doremus_entity_count(entity_type):
    type = {
        'release_group': 'release-group'
    }.get(entity_type, entity_type)
    df = sparql(f"""
        SELECT (COUNT(?concept) AS ?cnt)
        WHERE {{
            ?concept owl:sameAs ?mb .
            FILTER (regex (?mb, 'musicbrainz.org/{type}/'))
        }}
    """, endpoint='http://data.doremus.org/sparql')
    return int(df.cnt[0])


def mb_releasegroup_edit_bnf_link(item):
    return (
        '<a target="_blank" '
        f'href="{MB_URL}/release-group/{item.mbid}/edit?'
        'edit-release-group.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&'
        f'edit-release-group.url.99.text={DATA_BNF_URL}/{item.bnf}">'
        'edit</a>')


def mb_work_edit_bnf_link(item):
    return (
        '<a target="_blank" '
        f'href="{MB_URL}/work/{item.mbid}/edit?'
        'edit-work.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&'
        f'edit-work.url.99.text={DATA_BNF_URL}/{item.bnf}">'
        'edit</a>')
