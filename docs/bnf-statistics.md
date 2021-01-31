# BNF / MusicBrainz links statistics

Count links in either direction between MusicBrainz and BNF


```python
from pprint import pprint
%run -i ../startup.py
endpoint = 'http://data.bnf.fr/sparql'
```

    Last notebook update: 2021-01-31
    Importing libs
    Defining database parameters
    Defining *sql* helper function
    Last database update: 2021-01-13
    
    Defining *sparql* helper function



```python
links_from_mb = {}
for entity_type in MB_ENTITIES:
    links_from_mb[entity_type] = mb_entity_count(entity_type, url_pattern='bnf.fr')

pprint(links_from_mb)
```

    {'area': 0,
     'artist': 34252,
     'event': 0,
     'instrument': 0,
     'label': 102,
     'place': 125,
     'recording': 2,
     'release': 457,
     'release_group': 0,
     'series': 2,
     'work': 1002}



```python
links_from_bnf = {}
for entity_type in MB_ENTITIES:
    links_from_bnf[entity_type] = bnf_entity_count(entity_type)
   
pprint(links_from_bnf)
```

    {'area': 0,
     'artist': 56759,
     'event': 0,
     'instrument': 0,
     'label': 0,
     'place': 0,
     'recording': 0,
     'release': 0,
     'release_group': 205,
     'series': 0,
     'work': 2839}



```python
link_count = pd.DataFrame({'from_mb': links_from_mb, 'from_bnf': links_from_bnf})
link_count
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>from_mb</th>
      <th>from_bnf</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>area</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>artist</th>
      <td>34252</td>
      <td>56759</td>
    </tr>
    <tr>
      <th>event</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>instrument</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>label</th>
      <td>102</td>
      <td>0</td>
    </tr>
    <tr>
      <th>place</th>
      <td>125</td>
      <td>0</td>
    </tr>
    <tr>
      <th>recording</th>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>release</th>
      <td>457</td>
      <td>0</td>
    </tr>
    <tr>
      <th>release_group</th>
      <td>0</td>
      <td>205</td>
    </tr>
    <tr>
      <th>series</th>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>work</th>
      <td>1002</td>
      <td>2839</td>
    </tr>
  </tbody>
</table>
</div>




```python
import jinja2

template = jinja2.Template("""
<!doctype html>

<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Alignment of MusicBrainz and BNF entities</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>

  <body style="margin: 20px;">
    <h1>Alignment of MusicBrainz and BNF entities</h1>

    <p>Latest MB database update: {{ MB_DATABASE_VERSION }}</p>
    <p>Latest update: {{ date.today().isoformat() }}</p>

    <h2>Count links in either direction between MusicBrainz and BNF</h2>
    {{ df_to_html(link_count, reindex=False) }}
  </body>
</html>
""")

with open('../docs/bnf-statistics-report.html', 'w') as f:
    f.write(template.render(**globals())
            .replace('&lt;', '<').replace('&gt;', '>')
            .replace('class="dataframe"', 'class="table table-striped table-hover table-sm"')
            .replace('thead', 'thead class="thead-light"'))
```
