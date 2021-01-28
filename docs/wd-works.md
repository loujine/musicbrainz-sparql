```python
%run -i ../startup.py
ENTITY_TYPE = 'work'
```

    Last notebook update: 2021-01-28
    Importing libs
    Defining database parameters
    Defining *sql* helper function
    Last database update: 2021-01-13
    
    Defining *sparql* helper function


Wikidata entities:

https://www.wikidata.org/wiki/Q2188189 musical work

Wikidata properties:

https://www.wikidata.org/wiki/Property:P86 composer

https://www.wikidata.org/wiki/Property:P870 instrumentation

https://www.wikidata.org/wiki/Property:P214 VIAF

https://www.wikidata.org/wiki/Property:P268 BNF

https://www.wikidata.org/wiki/Property:P244 LoC

https://www.wikidata.org/wiki/Property:P839 IMSLP

https://www.wikidata.org/wiki/Property:P435 MusicBrainz work ID

https://www.wikidata.org/wiki/Property:P1994 AllMusic composition ID

https://www.wikidata.org/wiki/Property:P5229 Carnegie Hall work ID

https://www.wikidata.org/wiki/Property:P6080 Discogs composition ID (obsoleted by discogs in October 2019)

examples

https://www.wikidata.org/wiki/Q3478907

## Works from Wikidata


```python
links_type_from_wd = sparql("""
SELECT distinct (count(?work) as ?cnt) ?ins ?insLabel
WHERE {
  ?work wdt:P31 ?ins;
    wdt:P435 ?mbid.
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
group by ?ins ?insLabel
order by DESC(?cnt)
""")
links_type_from_wd[links_type_from_wd.cnt.astype(int) > 10]
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
      <th>cnt</th>
      <th>ins</th>
      <th>insLabel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>12075</td>
      <td>Q134556</td>
      <td>single</td>
    </tr>
    <tr>
      <th>1</th>
      <td>12020</td>
      <td>Q7366</td>
      <td>song</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5297</td>
      <td>Q207628</td>
      <td>musical composition</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1165</td>
      <td>Q1344</td>
      <td>opera</td>
    </tr>
    <tr>
      <th>4</th>
      <td>679</td>
      <td>Q7889</td>
      <td>video game</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>105</th>
      <td>12</td>
      <td>Q1667921</td>
      <td>novel series</td>
    </tr>
    <tr>
      <th>106</th>
      <td>12</td>
      <td>Q2302678</td>
      <td>clarinet concerto</td>
    </tr>
    <tr>
      <th>107</th>
      <td>12</td>
      <td>Q30340773</td>
      <td>quintet</td>
    </tr>
    <tr>
      <th>108</th>
      <td>11</td>
      <td>Q211025</td>
      <td>march</td>
    </tr>
    <tr>
      <th>109</th>
      <td>11</td>
      <td>Q541947</td>
      <td>anthem</td>
    </tr>
  </tbody>
</table>
<p>110 rows × 3 columns</p>
</div>




```python
sparql("""
SELECT (COUNT(?work) AS ?cnt)
WHERE {
  ?work wdt:P435 ?mbid.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
""")
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
      <th>cnt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>34385</td>
    </tr>
  </tbody>
</table>
</div>




```python
# linked to MB work
links_from_wd = sparql("""
SELECT (?work AS ?wd) ?mbid ?workLabel (GROUP_CONCAT(?categoryLabel; SEPARATOR=", ") AS ?workType)
WHERE {
  ?work wdt:P435 ?mbid .
  ?work wdt:P31 ?category .
  ?category rdfs:label ?categoryLabel FILTER(LANG(?categoryLabel) = "en")
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
GROUP BY ?work ?mbid ?workLabel
ORDER BY ASC(?workType) ASC(?workLabel)
""")
links_from_wd.rename(columns={'workLabel': 'name'}, inplace=True)
print('Count:', len(links_from_wd))
display_df(links_from_wd.head())
```

    Count: 33886



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wd</th>
      <th>mbid</th>
      <th>name</th>
      <th>workType</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5151283">Q5151283</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/0d6b1470-53a5-4885-9aaf-2157a43566a1">0d6b1470-53a5-4885-9aaf-2157a43566a1</a></td>
      <td>Come, Thou Long Expected Jesus</td>
      <td>Advent song, Christmas hymn</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5151283">Q5151283</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/3b4fb873-1df3-3a82-b5ab-2a9325bf1875">3b4fb873-1df3-3a82-b5ab-2a9325bf1875</a></td>
      <td>Come, Thou Long Expected Jesus</td>
      <td>Advent song, Christmas hymn</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5151283">Q5151283</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/87c901cf-fd2f-479d-ad07-668b405c1ee0">87c901cf-fd2f-479d-ad07-668b405c1ee0</a></td>
      <td>Come, Thou Long Expected Jesus</td>
      <td>Advent song, Christmas hymn</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5151283">Q5151283</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/9ce6cf52-e963-455b-97ae-598b99547f91">9ce6cf52-e963-455b-97ae-598b99547f91</a></td>
      <td>Come, Thou Long Expected Jesus</td>
      <td>Advent song, Christmas hymn</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q16147392">Q16147392</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/3ae52335-d8c7-45d3-9940-ff6cc7de0b63">3ae52335-d8c7-45d3-9940-ff6cc7de0b63</a></td>
      <td>All Things Bright and Beautiful</td>
      <td>Anglican hymn</td>
    </tr>
  </tbody>
</table>


## Works from MusicBrainz with wikidata links


```python
links_from_mb = sql("""
SELECT
    url.url AS wd,
    work.gid AS mbid,
    work.name
FROM work
JOIN l_url_work AS luw ON luw.entity1 = work.id
JOIN url               ON luw.entity0 = url.id
WHERE
    url.url LIKE '%%wikidata.org%%'
ORDER BY work.name
;
""")
links_from_mb.wd = links_from_mb.wd.apply(lambda s: s.split('/')[-1])
links_from_mb.mbid = links_from_mb.mbid.apply(str)

print('Count:', len(links_from_mb))
display_df(links_from_mb.head())
```

    Count: 31842



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wd</th>
      <th>mbid</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1195883">Q1195883</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/a0c2aa81-3185-412d-93f2-eefe4606c70e">a0c2aa81-3185-412d-93f2-eefe4606c70e</a></td>
      <td>"Der Morgen und der Abend" 12 Musikstücke für das Hornwerk "Salzburger Stier" der Festung Hohensalzburg</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1339833">Q1339833</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/054f14c0-8edf-43b5-8946-88f9bd6c3dc1">054f14c0-8edf-43b5-8946-88f9bd6c3dc1</a></td>
      <td>"Geistervariationen" in E-flat major for piano solo, WoO 24</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10513545">Q10513545</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/76fdbe87-6c69-4c54-a6de-97a2dd3d2517">76fdbe87-6c69-4c54-a6de-97a2dd3d2517</a></td>
      <td>"Ô meilleur des hommes! Celui qui t'aime est le véritable croyant"</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q3879355">Q3879355</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/55b4b32d-0908-4500-8ec5-f14b77953e92">55b4b32d-0908-4500-8ec5-f14b77953e92</a></td>
      <td>#1 Crush</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q945195">Q945195</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/187f83e3-1a1f-3623-8e71-109442414cb0">187f83e3-1a1f-3623-8e71-109442414cb0</a></td>
      <td>#9 Dream</td>
    </tr>
  </tbody>
</table>


## Duplicate links


```python
duplicate_wd = links_from_mb[[
    'wd', 'mbid', 'name']].groupby('wd').filter(
    lambda row: len(row.mbid) > 1).sort_values('wd')

print('Count:', len(duplicate_wd))
display_df(duplicate_wd.head())
```

    Count: 1652



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wd</th>
      <th>mbid</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1000352">Q1000352</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/948cc231-12a7-4b13-8022-e7e6e75ee8ba">948cc231-12a7-4b13-8022-e7e6e75ee8ba</a></td>
      <td>Reckless</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1000352">Q1000352</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/35765848-0832-402c-91b5-8b505919e271">35765848-0832-402c-91b5-8b505919e271</a></td>
      <td>Reckless: Steinernes Fleisch</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1027675">Q1027675</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/447b9b10-f278-4b13-b55a-8a925811260c">447b9b10-f278-4b13-b55a-8a925811260c</a></td>
      <td>Got to Give It Up</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1027675">Q1027675</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/ba2dfdad-4591-3de3-9e1f-f9f0a1071f76">ba2dfdad-4591-3de3-9e1f-f9f0a1071f76</a></td>
      <td>Got to Give It Up</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1028491">Q1028491</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/e8e21649-afb6-338f-9c89-ac48dfe8df0a">e8e21649-afb6-338f-9c89-ac48dfe8df0a</a></td>
      <td>Camelot</td>
    </tr>
  </tbody>
</table>



```python
duplicate_mb = links_from_mb[['wd', 'mbid', 'name']].groupby('mbid').filter(
    lambda row: len(row.mbid) > 1).sort_values('mbid')

print('Count:', len(duplicate_mb))
display_df(duplicate_mb.head())
```

    Count: 38



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wd</th>
      <th>mbid</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q62565775">Q62565775</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/088c2a4a-e9c3-46ee-ae23-8acb4d4294e4">088c2a4a-e9c3-46ee-ae23-8acb4d4294e4</a></td>
      <td>Deutschland</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q62566152">Q62566152</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/088c2a4a-e9c3-46ee-ae23-8acb4d4294e4">088c2a4a-e9c3-46ee-ae23-8acb4d4294e4</a></td>
      <td>Deutschland</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q29158512">Q29158512</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/0b5def1a-3892-4716-a7a2-2ee02b10c55f">0b5def1a-3892-4716-a7a2-2ee02b10c55f</a></td>
      <td>Images, Livre 1, L. 110, CD 105</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1132712">Q1132712</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/0b5def1a-3892-4716-a7a2-2ee02b10c55f">0b5def1a-3892-4716-a7a2-2ee02b10c55f</a></td>
      <td>Images, Livre 1, L. 110, CD 105</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q512715">Q512715</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/1319ddc3-910a-4c93-afc7-c5e5973f3b78">1319ddc3-910a-4c93-afc7-c5e5973f3b78</a></td>
      <td>Préludes, Livre I, L. 117, CD 125</td>
    </tr>
  </tbody>
</table>


## Data alignment


```python
merge = pd.merge(links_from_wd, links_from_mb, 
                 on=['wd', 'mbid'], suffixes=('_wd', '_mb'),
                 how='outer', indicator=True)
display_df(merge.head())
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wd</th>
      <th>mbid</th>
      <th>name_wd</th>
      <th>workType</th>
      <th>name_mb</th>
      <th>_merge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5151283">Q5151283</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/0d6b1470-53a5-4885-9aaf-2157a43566a1">0d6b1470-53a5-4885-9aaf-2157a43566a1</a></td>
      <td>Come, Thou Long Expected Jesus</td>
      <td>Advent song, Christmas hymn</td>
      <td>Come, Thou Long Expected Jesus</td>
      <td>both</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5151283">Q5151283</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/3b4fb873-1df3-3a82-b5ab-2a9325bf1875">3b4fb873-1df3-3a82-b5ab-2a9325bf1875</a></td>
      <td>Come, Thou Long Expected Jesus</td>
      <td>Advent song, Christmas hymn</td>
      <td>Come, Thou Long Expected Jesus</td>
      <td>both</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5151283">Q5151283</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/87c901cf-fd2f-479d-ad07-668b405c1ee0">87c901cf-fd2f-479d-ad07-668b405c1ee0</a></td>
      <td>Come, Thou Long Expected Jesus</td>
      <td>Advent song, Christmas hymn</td>
      <td>Come, Thou Long Expected Jesus</td>
      <td>both</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5151283">Q5151283</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/9ce6cf52-e963-455b-97ae-598b99547f91">9ce6cf52-e963-455b-97ae-598b99547f91</a></td>
      <td>Come, Thou Long Expected Jesus</td>
      <td>Advent song, Christmas hymn</td>
      <td>Come, Thou Long Expected Jesus</td>
      <td>both</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q331595">Q331595</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/09d0b344-1396-4985-a3aa-d4b4db7e2b33">09d0b344-1396-4985-a3aa-d4b4db7e2b33</a></td>
      <td>Veni, Veni Emmanuel</td>
      <td>Advent song, Christmas hymn</td>
      <td>O Come, O Come, Emmanuel</td>
      <td>both</td>
    </tr>
  </tbody>
</table>



```python
# link in mb but missing in wd
links_to_add_to_wd = merge.loc[lambda x : x['_merge']=='right_only'][[
    'name_mb', 'mbid', 'wd']]

print('Count:', len(links_to_add_to_wd))
display_df(links_to_add_to_wd.head())
```

    Count: 4692



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name_mb</th>
      <th>mbid</th>
      <th>wd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>"Ô meilleur des hommes! Celui qui t'aime est le véritable croyant"</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/76fdbe87-6c69-4c54-a6de-97a2dd3d2517">76fdbe87-6c69-4c54-a6de-97a2dd3d2517</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10513545">Q10513545</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>(Can’t Get My) Head Around You</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/a7757771-757b-4ff8-9736-7ad065bd2bd3">a7757771-757b-4ff8-9736-7ad065bd2bd3</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q2550692">Q2550692</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td>(It’s All Down to) Goodnight Vienna</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/c740d2c6-3f54-42ca-8dc5-6a0fd2f1e2f2">c740d2c6-3f54-42ca-8dc5-6a0fd2f1e2f2</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4041672">Q4041672</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td>(I’m Always Touched by Your) Presence, Dear</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/299b84fe-bf16-3e22-b2c3-edf9796e0b0d">299b84fe-bf16-3e22-b2c3-edf9796e0b0d</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q837484">Q837484</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td>(I’m Gonna) Love Me Again</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/94bbf621-3dd9-4f2b-88b5-4f3b3cebac5d">94bbf621-3dd9-4f2b-88b5-4f3b3cebac5d</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q77816604">Q77816604</a></td>
    </tr>
  </tbody>
</table>



```python
# link in wd but missing in mb
links_to_add_to_mb = merge.loc[lambda x : x['_merge']=='left_only'][[
    'name_wd', 'wd', 'mbid', 'workType']]
links_to_add_to_mb['edit_link'] = links_to_add_to_mb.apply(
    mb_work_edit_wd_link, axis=1)

print('Count:', len(links_to_add_to_mb))
display_df(links_to_add_to_mb.head())
```

    Count: 6735



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name_wd</th>
      <th>wd</th>
      <th>mbid</th>
      <th>workType</th>
      <th>edit_link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Veni, Veni Emmanuel</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q331595">Q331595</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/0ae49426-2891-4ed3-aec6-ee95369fd0c8">0ae49426-2891-4ed3-aec6-ee95369fd0c8</a></td>
      <td>Advent song, Christmas hymn</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/0ae49426-2891-4ed3-aec6-ee95369fd0c8/edit?edit-work.url.99.type=587fdd8f-080e-46a9-97af-6425ebbcb3a2&edit-work.url.99.text=https://www.wikidata.org/wiki/Q331595">edit</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>Veni, Veni Emmanuel</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q331595">Q331595</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/523d5269-0212-41ae-997e-294267e5ddbf">523d5269-0212-41ae-997e-294267e5ddbf</a></td>
      <td>Advent song, Christmas hymn</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/523d5269-0212-41ae-997e-294267e5ddbf/edit?edit-work.url.99.type=587fdd8f-080e-46a9-97af-6425ebbcb3a2&edit-work.url.99.text=https://www.wikidata.org/wiki/Q331595">edit</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td>Entfliehet, verschwindet, entweichet, ihr Sorgen, BWV 249a</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1249980">Q1249980</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/a5c89bd4-986d-4af4-82a0-e6d4bafc7e0c">a5c89bd4-986d-4af4-82a0-e6d4bafc7e0c</a></td>
      <td>Bach cantata</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/a5c89bd4-986d-4af4-82a0-e6d4bafc7e0c/edit?edit-work.url.99.type=587fdd8f-080e-46a9-97af-6425ebbcb3a2&edit-work.url.99.text=https://www.wikidata.org/wiki/Q1249980">edit</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ich bin in mir vergnügt, BWV 204</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q3147633">Q3147633</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/e01a83bb-d8d1-4295-b6aa-22a28cc04d85">e01a83bb-d8d1-4295-b6aa-22a28cc04d85</a></td>
      <td>Bach cantata</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/e01a83bb-d8d1-4295-b6aa-22a28cc04d85/edit?edit-work.url.99.type=587fdd8f-080e-46a9-97af-6425ebbcb3a2&edit-work.url.99.text=https://www.wikidata.org/wiki/Q3147633">edit</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td>Non sa che sia dolore, BWV 209</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q2784522">Q2784522</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/work/43fa1a90-7f72-4e45-905f-3d845d500f66">43fa1a90-7f72-4e45-905f-3d845d500f66</a></td>
      <td>Bach cantata</td>
      <td><a target="_blank" href="https://musicbrainz.org/work/43fa1a90-7f72-4e45-905f-3d845d500f66/edit?edit-work.url.99.type=587fdd8f-080e-46a9-97af-6425ebbcb3a2&edit-work.url.99.text=https://www.wikidata.org/wiki/Q2784522">edit</a></td>
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
    <title>Alignment of MusicBrainz and Wikidata Works</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>

  <body style="margin: 20px;">
    <h1>Alignment of MusicBrainz and Wikidata Works</h1>

    <p>Latest MB database update: {{ MB_DATABASE_VERSION }}</p>
    <p>Latest update: {{ date.today().isoformat() }}</p>

    <ol>
      <li>
        <a href="#wddup">MusicBrainz entities sharing a Wikidata link</a>
        ({{ duplicate_wd.shape[0] }} rows)
      </li>
      <li>
        <a href="#mbdup">Wikidata entities sharing a MusicBrainz link</a>
        ({{ duplicate_mb.shape[0] }} rows)
      </li>
      <li>
        <a href="#wd2mb">Add missing Wikidata links to MusicBrainz</a>
        ({{ links_to_add_to_mb.shape[0] }} rows)
      </li>
      <li>
        <a href="#mb2wd">Add missing MusicBrainz links to Wikidata</a>
        ({{ links_to_add_to_wd.shape[0] }} rows)
      </li>
    </ol>
    
    <h2 id="wddup">MusicBrainz entities sharing a Wikidata link</h2>
    {{ df_to_html(duplicate_wd) }}

    <h2 id="mbdup">Wikidata entities sharing a MusicBrainz link</h2>
    {{ df_to_html(duplicate_mb) }}

    <h2 id="wd2mb">Add missing Wikidata links to MusicBrainz</h2>
    {{ df_to_html(links_to_add_to_mb) }}

    <h2 id="mb2wd">Add missing MusicBrainz links to Wikidata</h2>
    {{ df_to_html(links_to_add_to_wd) }}
  </body>
</html>
""")

with open('../docs/wd-works-report.html', 'w') as f:
    f.write(template.render(**globals())
            .replace('&lt;', '<').replace('&gt;', '>')
            .replace('class="dataframe"', 'class="table table-striped table-hover table-sm"')
            .replace('thead', 'thead class="thead-light"'))
```
