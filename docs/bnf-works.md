```python
%run -i ../startup.py
ENTITY_TYPE = 'work'
endpoint='http://data.bnf.fr/sparql'
```

    Last notebook update: 2021-02-13
    Importing libs
    Defining database parameters
    Defining *sql* helper function
    Last database update: 2021-01-13
    
    Defining *sparql* helper function


## Works from BNF


```python
# linked to MB works
bnf_entity_count(ENTITY_TYPE)
```




    2839




```python
links_from_bnf = sparql(f"""
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT (?work AS ?bnf) ?mbid ?name
WHERE {{
  ?work skos:exactMatch ?mbid .
  ?work skos:prefLabel ?name .
  FILTER (regex (?mbid, 'musicbrainz.org/work/'))
}}
""", endpoint='http://data.bnf.fr/sparql')

print('Count:', len(links_from_bnf))
display_df(links_from_bnf.head())
```

    Count: 2839



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>bnf</th>
      <th>mbid</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb11944701x">cb11944701x</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/9c73bb0c-c20c-4fc9-828e-baf9a3e2892c">9c73bb0c-c20c-4fc9-828e-baf9a3e2892c</a></td>
      <td>Vita nuova</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb11939496m">cb11939496m</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/d8e99500-f056-4d82-b819-971e713ca84a">d8e99500-f056-4d82-b819-971e713ca84a</a></td>
      <td>Der Zauberberg</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13927446n">cb13927446n</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/43b3d2c0-210e-3124-a97c-e97dd9564f1e">43b3d2c0-210e-3124-a97c-e97dd9564f1e</a></td>
      <td>L'Internationale</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13927446n">cb13927446n</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/45dd2d44-95b3-4cfa-8484-45416a7db8e7">45dd2d44-95b3-4cfa-8484-45416a7db8e7</a></td>
      <td>L'Internationale</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13920574g">cb13920574g</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/0b1f0523-969a-44eb-8ee5-001b0f30343b">0b1f0523-969a-44eb-8ee5-001b0f30343b</a></td>
      <td>Otello</td>
    </tr>
  </tbody>
</table>


## Works from MB with BNF links


```python
links_from_mb = sql("""
SELECT
    url.url AS bnf,
    work.gid AS mbid,
    work.name
FROM work
JOIN l_url_work AS luw ON luw.entity1 = work.id
JOIN url               ON luw.entity0 = url.id
WHERE
    url.url LIKE '%%bnf.fr%%'
ORDER BY work.name
;
""")
links_from_mb.bnf = links_from_mb.bnf.apply(lambda s: s.split('/')[-1])
links_from_mb.mbid = links_from_mb.mbid.apply(str)

print('Count:', len(links_from_mb))
display_df(links_from_mb.head())
```

    Count: 1002



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>bnf</th>
      <th>mbid</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13912155c">cb13912155c</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/26a22ba5-cff7-478e-bf92-ad594d4f590f">26a22ba5-cff7-478e-bf92-ad594d4f590f</a></td>
      <td>"El Fuego", ensalada for 4 voices</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13912906c">cb13912906c</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/e130ee21-7930-4c17-8ccf-cb0192cd3ba4">e130ee21-7930-4c17-8ccf-cb0192cd3ba4</a></td>
      <td>"Ohne Titel"</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb166320720">cb166320720</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/e8c10bc4-c39e-461a-b077-9b59a95774ee">e8c10bc4-c39e-461a-b077-9b59a95774ee</a></td>
      <td>"Wer ist so würdig als du", Wq. 222, H. 831</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb166009413">cb166009413</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/38f09a04-1808-4777-b710-a27beb95e73c">38f09a04-1808-4777-b710-a27beb95e73c</a></td>
      <td>12 chansons Op. 11 : 12.Embarquez-vous!</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb139121990">cb139121990</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/32663f37-e1d4-489f-b429-0da57dbb293b">32663f37-e1d4-489f-b429-0da57dbb293b</a></td>
      <td>15 portraits d'enfants d'Auguste Renoir</td>
    </tr>
  </tbody>
</table>


## Data alignment


```python
merge = pd.merge(links_from_bnf, links_from_mb, 
                 on=['bnf', 'mbid'], suffixes=('_bnf', '_mb'),
                 how='outer', indicator=True)
display_df(merge.head())
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>bnf</th>
      <th>mbid</th>
      <th>name_bnf</th>
      <th>edit_link</th>
      <th>name_mb</th>
      <th>_merge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb11944701x">cb11944701x</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/9c73bb0c-c20c-4fc9-828e-baf9a3e2892c">9c73bb0c-c20c-4fc9-828e-baf9a3e2892c</a></td>
      <td>Vita nuova</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/9c73bb0c-c20c-4fc9-828e-baf9a3e2892c/edit?edit-work.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-work.url.99.text=http://data.bnf.fr/ark:/12148/cb11944701x">edit</a></td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb11939496m">cb11939496m</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/d8e99500-f056-4d82-b819-971e713ca84a">d8e99500-f056-4d82-b819-971e713ca84a</a></td>
      <td>Der Zauberberg</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/d8e99500-f056-4d82-b819-971e713ca84a/edit?edit-work.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-work.url.99.text=http://data.bnf.fr/ark:/12148/cb11939496m">edit</a></td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13927446n">cb13927446n</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/43b3d2c0-210e-3124-a97c-e97dd9564f1e">43b3d2c0-210e-3124-a97c-e97dd9564f1e</a></td>
      <td>L'Internationale</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/43b3d2c0-210e-3124-a97c-e97dd9564f1e/edit?edit-work.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-work.url.99.text=http://data.bnf.fr/ark:/12148/cb13927446n">edit</a></td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13927446n">cb13927446n</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/45dd2d44-95b3-4cfa-8484-45416a7db8e7">45dd2d44-95b3-4cfa-8484-45416a7db8e7</a></td>
      <td>L'Internationale</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/45dd2d44-95b3-4cfa-8484-45416a7db8e7/edit?edit-work.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-work.url.99.text=http://data.bnf.fr/ark:/12148/cb13927446n">edit</a></td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13920574g">cb13920574g</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/0b1f0523-969a-44eb-8ee5-001b0f30343b">0b1f0523-969a-44eb-8ee5-001b0f30343b</a></td>
      <td>Otello</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/0b1f0523-969a-44eb-8ee5-001b0f30343b/edit?edit-work.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-work.url.99.text=http://data.bnf.fr/ark:/12148/cb13920574g">edit</a></td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
  </tbody>
</table>



```python
# link in mb but missing in bnf
links_to_add_to_bnf = merge.loc[lambda x : x['_merge']=='right_only'][[
    'name_mb', 'mbid', 'bnf']]

print('Count:', len(links_to_add_to_bnf))
display_df(links_to_add_to_bnf.head())
```

    Count: 721



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name_mb</th>
      <th>mbid</th>
      <th>bnf</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>"El Fuego", ensalada for 4 voices</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/26a22ba5-cff7-478e-bf92-ad594d4f590f">26a22ba5-cff7-478e-bf92-ad594d4f590f</a></td>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13912155c">cb13912155c</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>"Ohne Titel"</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/e130ee21-7930-4c17-8ccf-cb0192cd3ba4">e130ee21-7930-4c17-8ccf-cb0192cd3ba4</a></td>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13912906c">cb13912906c</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td>"Wer ist so würdig als du", Wq. 222, H. 831</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/e8c10bc4-c39e-461a-b077-9b59a95774ee">e8c10bc4-c39e-461a-b077-9b59a95774ee</a></td>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb166320720">cb166320720</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td>12 chansons Op. 11 : 12.Embarquez-vous!</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/38f09a04-1808-4777-b710-a27beb95e73c">38f09a04-1808-4777-b710-a27beb95e73c</a></td>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb166009413">cb166009413</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td>15 portraits d'enfants d'Auguste Renoir</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/32663f37-e1d4-489f-b429-0da57dbb293b">32663f37-e1d4-489f-b429-0da57dbb293b</a></td>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb139121990">cb139121990</a></td>
    </tr>
  </tbody>
</table>



```python
# link in bnf but missing in mb
links_to_add_to_mb = merge.loc[lambda x : x['_merge']=='left_only'][[
    'name_bnf', 'bnf', 'mbid']]
links_to_add_to_mb['edit_link'] = links_to_add_to_mb.apply(
    mb_work_edit_bnf_link, axis=1)

print('Count:', len(links_to_add_to_mb))
display_df(links_to_add_to_mb.head())
```

    Count: 2558



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name_bnf</th>
      <th>bnf</th>
      <th>mbid</th>
      <th>edit_link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Vita nuova</td>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb11944701x">cb11944701x</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/9c73bb0c-c20c-4fc9-828e-baf9a3e2892c">9c73bb0c-c20c-4fc9-828e-baf9a3e2892c</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/9c73bb0c-c20c-4fc9-828e-baf9a3e2892c/edit?edit-work.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-work.url.99.text=http://data.bnf.fr/ark:/12148/cb11944701x">edit</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>Der Zauberberg</td>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb11939496m">cb11939496m</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/d8e99500-f056-4d82-b819-971e713ca84a">d8e99500-f056-4d82-b819-971e713ca84a</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/d8e99500-f056-4d82-b819-971e713ca84a/edit?edit-work.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-work.url.99.text=http://data.bnf.fr/ark:/12148/cb11939496m">edit</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td>L'Internationale</td>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13927446n">cb13927446n</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/43b3d2c0-210e-3124-a97c-e97dd9564f1e">43b3d2c0-210e-3124-a97c-e97dd9564f1e</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/43b3d2c0-210e-3124-a97c-e97dd9564f1e/edit?edit-work.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-work.url.99.text=http://data.bnf.fr/ark:/12148/cb13927446n">edit</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td>L'Internationale</td>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13927446n">cb13927446n</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/45dd2d44-95b3-4cfa-8484-45416a7db8e7">45dd2d44-95b3-4cfa-8484-45416a7db8e7</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/45dd2d44-95b3-4cfa-8484-45416a7db8e7/edit?edit-work.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-work.url.99.text=http://data.bnf.fr/ark:/12148/cb13927446n">edit</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td>Otello</td>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13920574g">cb13920574g</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/0b1f0523-969a-44eb-8ee5-001b0f30343b">0b1f0523-969a-44eb-8ee5-001b0f30343b</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/0b1f0523-969a-44eb-8ee5-001b0f30343b/edit?edit-work.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-work.url.99.text=http://data.bnf.fr/ark:/12148/cb13920574g">edit</a></td>
    </tr>
  </tbody>
</table>


## Report


```python
import jinja2

template = jinja2.Template("""
<!doctype html>

<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Alignment of MusicBrainz and BNF Works</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>

  <body style="margin: 20px;">
    <h1>Alignment of MusicBrainz and BNF Works</h1>

    <p>Latest MB database update: {{ MB_DATABASE_VERSION }}</p>
    <p>Latest update: {{ date.today().isoformat() }}</p>

    <ol>
      <li>
        <a href="#bnf2mb">Add missing BNF links to MusicBrainz</a>
        ({{ links_to_add_to_mb.shape[0] }} rows)
      </li>
      <li>
        <a href="#mb2bnf">Add missing MusicBrainz links to BNF</a>
        ({{ links_to_add_to_bnf.shape[0] }} rows)
      </li>

    </ol>
    
    <h2 id="bnf2mb">Add missing BNF links to MusicBrainz</h2>
    {{ df_to_html(links_to_add_to_mb) }}

    <h2 id="mb2bnf">Add missing MusicBrainz links to BNF</h2>
    {{ df_to_html(links_to_add_to_bnf) }}
    
  </body>
</html>
""")

with open('../docs/bnf-works-report.html', 'w') as f:
    f.write(template.render(**globals())
            .replace('&lt;', '<').replace('&gt;', '>')
            .replace('class="dataframe"', 'class="table table-striped table-hover table-sm"')
            .replace('thead', 'thead class="thead-light"'))
```
