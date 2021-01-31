# Doremus / MusicBrainz links statistics

Count links in either direction between MusicBrainz and BNF


```python
from pprint import pprint
%run -i ../startup.py
endpoint = 'http://data.doremus.org/sparql'
```

    Last notebook update: 2021-02-01
    Importing libs
    Defining database parameters
    Defining *sql* helper function
    Last database update: 2021-01-13
    
    Defining *sparql* helper function



```python
links_from_mb = {}
for entity_type in MB_ENTITIES:
    links_from_mb[entity_type] = mb_entity_count(entity_type, url_pattern='doremus.org')

pprint(links_from_mb)
```

    {'area': 0,
     'artist': 0,
     'event': 0,
     'instrument': 0,
     'label': 0,
     'place': 0,
     'recording': 0,
     'release': 0,
     'release_group': 0,
     'series': 0,
     'work': 0}



```python
links_from_doremus = {}
for entity_type in MB_ENTITIES:
    links_from_doremus[entity_type] = doremus_entity_count(entity_type)
   
pprint(links_from_doremus)
```

    {'area': 0,
     'artist': 3727,
     'event': 0,
     'instrument': 0,
     'label': 0,
     'place': 0,
     'recording': 0,
     'release': 0,
     'release_group': 0,
     'series': 0,
     'work': 0}



```python
link_count = pd.DataFrame({'from_mb': links_from_mb, 'from_doremus': links_from_doremus})
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
      <th>from_doremus</th>
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
      <td>0</td>
      <td>3727</td>
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
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>place</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>recording</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>release</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>release_group</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>series</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>work</th>
      <td>0</td>
      <td>0</td>
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
    <title>Alignment of MusicBrainz and Doremus entities</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>

  <body style="margin: 20px;">
    <h1>Alignment of MusicBrainz and Doremus entities</h1>

    <p>Latest MB database update: {{ MB_DATABASE_VERSION }}</p>
    <p>Latest update: {{ date.today().isoformat() }}</p>

    <h2>Count links in either direction between MusicBrainz and Doremus</h2>
    {{ df_to_html(link_count, reindex=False) }}
  </body>
</html>
""")

with open('../docs/doremus-statistics-report.html', 'w') as f:
    f.write(template.render(**globals())
            .replace('&lt;', '<').replace('&gt;', '>')
            .replace('class="dataframe"', 'class="table table-striped table-hover table-sm"')
            .replace('thead', 'thead class="thead-light"'))
```
