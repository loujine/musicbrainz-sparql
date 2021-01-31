# Wikidata / MusicBrainz links statistics

Count links in either direction between MusicBrainz and Wikidata


```python
from pprint import pprint
%run -i ../startup.py
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
    links_from_mb[entity_type] = mb_entity_count(entity_type)

pprint(links_from_mb)
```

    {'area': 118295,
     'artist': 200132,
     'event': 302,
     'instrument': 890,
     'label': 7033,
     'place': 7901,
     'recording': 2,
     'release': 1,
     'release_group': 115750,
     'series': 1367,
     'work': 31842}



```python
links_from_wd = {}
for entity_type, prop in WD_MB_LINK_PROPERTIES.items():
    links_from_wd[entity_type] = wd_entity_count(entity_type, prop)
   
pprint(links_from_wd)
```

    {'area': 118295,
     'artist': 200132,
     'event': 302,
     'instrument': 890,
     'label': 7033,
     'place': 7901,
     'recording': 2,
     'release': 1,
     'release_group': 115750,
     'series': 1367,
     'work': 31842}



```python
link_count = pd.DataFrame({'from_mb': links_from_mb, 'from_wd': links_from_wd})
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
      <th>from_wd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>area</th>
      <td>118295</td>
      <td>28472</td>
    </tr>
    <tr>
      <th>artist</th>
      <td>200132</td>
      <td>220497</td>
    </tr>
    <tr>
      <th>event</th>
      <td>302</td>
      <td>37</td>
    </tr>
    <tr>
      <th>instrument</th>
      <td>890</td>
      <td>875</td>
    </tr>
    <tr>
      <th>label</th>
      <td>7033</td>
      <td>7772</td>
    </tr>
    <tr>
      <th>place</th>
      <td>7901</td>
      <td>7265</td>
    </tr>
    <tr>
      <th>recording</th>
      <td>2</td>
      <td>8198</td>
    </tr>
    <tr>
      <th>release</th>
      <td>1</td>
      <td>1064</td>
    </tr>
    <tr>
      <th>release_group</th>
      <td>115750</td>
      <td>174976</td>
    </tr>
    <tr>
      <th>series</th>
      <td>1367</td>
      <td>1229</td>
    </tr>
    <tr>
      <th>work</th>
      <td>31842</td>
      <td>34406</td>
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
    <title>Alignment of MusicBrainz and Wikidata entities</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>

  <body style="margin: 20px;">
    <h1>Alignment of MusicBrainz and Wikidata entities</h1>

    <p>Latest MB database update: {{ MB_DATABASE_VERSION }}</p>
    <p>Latest update: {{ date.today().isoformat() }}</p>

    <h2>Count links in either direction between MusicBrainz and Wikidata</h2>
    {{ df_to_html(link_count, reindex=False) }}
  </body>
</html>
""")

with open('../docs/wd-statistics-report.html', 'w') as f:
    f.write(template.render(**globals())
            .replace('&lt;', '<').replace('&gt;', '>')
            .replace('class="dataframe"', 'class="table table-striped table-hover table-sm"')
            .replace('thead', 'thead class="thead-light"'))
```
