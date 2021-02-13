```python
%run -i ../startup.py
ENTITY_TYPE = 'release-group'
endpoint='http://data.bnf.fr/sparql'
```

    Last notebook update: 2021-02-08
    Importing libs
    Defining database parameters
    Defining *sql* helper function
    Last database update: 2021-01-13
    
    Defining *sparql* helper function


## Release Groups from BNF


```python
# linked to MB RG
bnf_entity_count(ENTITY_TYPE)
```




    205




```python
links_from_bnf = sparql(f"""
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT (?rg AS ?bnf) ?mbid ?name
WHERE {{
  ?rg skos:exactMatch ?mbid .
  ?rg skos:prefLabel ?name .
  FILTER (regex (?mbid, 'musicbrainz.org/release-group/'))
}}
""", endpoint='http://data.bnf.fr/sparql')

print('Count:', len(links_from_bnf))
display_df(links_from_bnf.head())
```

    Count: 205



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
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb121110184">cb121110184</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/da9d7460-395c-3b3a-92fa-4b15e8680bb3">da9d7460-395c-3b3a-92fa-4b15e8680bb3</a></td>
      <td>Zur Psychopathologie des Alltagslebens</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13915256q">cb13915256q</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/dca4865a-9d5e-3bf1-acd0-13cfe8f6f8f7">dca4865a-9d5e-3bf1-acd0-13cfe8f6f8f7</a></td>
      <td>Don Giovanni. KV 527</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb119446876">cb119446876</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/5fc2d466-e22d-4460-806a-76cb08c893f5">5fc2d466-e22d-4460-806a-76cb08c893f5</a></td>
      <td>The Canterbury tales</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb16599036w">cb16599036w</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/0611a3fa-2e9d-3bbf-871f-f264c6bf1561">0611a3fa-2e9d-3bbf-871f-f264c6bf1561</a></td>
      <td>StarCraft : jeu vidéo</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13177432m">cb13177432m</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/6d1a8775-9814-393d-91ca-e6fc46945eb1">6d1a8775-9814-393d-91ca-e6fc46945eb1</a></td>
      <td>Le cinquième élément : film</td>
    </tr>
  </tbody>
</table>



```python
links_to_add_to_mb = links_from_bnf
links_to_add_to_mb['edit_link'] = links_to_add_to_mb.apply(
    mb_releasegroup_edit_bnf_link, axis=1)

print('Count:', len(links_to_add_to_mb))
display_df(links_to_add_to_mb.head())
```

    Count: 205



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>bnf</th>
      <th>mbid</th>
      <th>name</th>
      <th>edit_link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb121110184">cb121110184</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/da9d7460-395c-3b3a-92fa-4b15e8680bb3">da9d7460-395c-3b3a-92fa-4b15e8680bb3</a></td>
      <td>Zur Psychopathologie des Alltagslebens</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/da9d7460-395c-3b3a-92fa-4b15e8680bb3/edit?edit-release-group.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-release-group.url.99.text=http://data.bnf.fr/ark:/12148/cb121110184">edit</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13915256q">cb13915256q</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/dca4865a-9d5e-3bf1-acd0-13cfe8f6f8f7">dca4865a-9d5e-3bf1-acd0-13cfe8f6f8f7</a></td>
      <td>Don Giovanni. KV 527</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/dca4865a-9d5e-3bf1-acd0-13cfe8f6f8f7/edit?edit-release-group.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-release-group.url.99.text=http://data.bnf.fr/ark:/12148/cb13915256q">edit</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb119446876">cb119446876</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/5fc2d466-e22d-4460-806a-76cb08c893f5">5fc2d466-e22d-4460-806a-76cb08c893f5</a></td>
      <td>The Canterbury tales</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/5fc2d466-e22d-4460-806a-76cb08c893f5/edit?edit-release-group.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-release-group.url.99.text=http://data.bnf.fr/ark:/12148/cb119446876">edit</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb16599036w">cb16599036w</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/0611a3fa-2e9d-3bbf-871f-f264c6bf1561">0611a3fa-2e9d-3bbf-871f-f264c6bf1561</a></td>
      <td>StarCraft : jeu vidéo</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/0611a3fa-2e9d-3bbf-871f-f264c6bf1561/edit?edit-release-group.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-release-group.url.99.text=http://data.bnf.fr/ark:/12148/cb16599036w">edit</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="http://data.bnf.fr/ark:/12148/cb13177432m">cb13177432m</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/6d1a8775-9814-393d-91ca-e6fc46945eb1">6d1a8775-9814-393d-91ca-e6fc46945eb1</a></td>
      <td>Le cinquième élément : film</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/6d1a8775-9814-393d-91ca-e6fc46945eb1/edit?edit-release-group.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-release-group.url.99.text=http://data.bnf.fr/ark:/12148/cb13177432m">edit</a></td>
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
    <title>Alignment of MusicBrainz and BNF Release Groups</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>

  <body style="margin: 20px;">
    <h1>Alignment of MusicBrainz and BNF Release Groups</h1>

    <p>Latest MB database update: {{ MB_DATABASE_VERSION }}</p>
    <p>Latest update: {{ date.today().isoformat() }}</p>

    <ol>
      <li>
        <a href="#bnf2mb">Add missing BNF links to MusicBrainz</a>
        ({{ links_to_add_to_mb.shape[0] }} rows)
      </li>
    </ol>
    
    <h2 id="bnf2mb">Add missing BNF links to MusicBrainz</h2>
    {{ df_to_html(links_to_add_to_mb) }}
    
  </body>
</html>
""")

with open('../docs/bnf-releasegroups-report.html', 'w') as f:
    f.write(template.render(**globals())
            .replace('&lt;', '<').replace('&gt;', '>')
            .replace('class="dataframe"', 'class="table table-striped table-hover table-sm"')
            .replace('thead', 'thead class="thead-light"'))
```
