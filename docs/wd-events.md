```python
%run -i ../startup.py
ENTITY_TYPE = 'event'
```

    Last notebook update: 2021-01-29
    Importing libs
    Defining database parameters
    Defining *sql* helper function
    Last database update: 2021-01-13
    
    Defining *sparql* helper function


Wikidata entities:

https://www.wikidata.org/wiki/Q182832 concert

https://www.wikidata.org/wiki/Q1573906 concert tour




Wikidata properties:

https://www.wikidata.org/wiki/Property:P276 location

https://www.wikidata.org/wiki/Property:P580 start time

https://www.wikidata.org/wiki/Property:P585 point in time

https://www.wikidata.org/wiki/Property:P710 participant

https://www.wikidata.org/wiki/Property:P1651 youtube ID

https://www.wikidata.org/wiki/Property:P6423 MusicBrainz event ID





examples

https://www.wikidata.org/wiki/Q898154

https://www.wikidata.org/wiki/Q25408640

## Events from Wikidata


```python
sparql("""
SELECT (COUNT(?event) AS ?cnt)
WHERE {
  ?event wdt:P31 wd:Q182832 .
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
      <td>5233</td>
    </tr>
  </tbody>
</table>
</div>




```python
# entity types
sparql("""
SELECT distinct (count(?event) as ?cnt) ?ins ?insLabel
WHERE {
  ?event wdt:P31 ?ins;
    wdt:P6423 ?mbid.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
group by ?ins ?insLabel
order by DESC(?cnt)
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
      <th>ins</th>
      <th>insLabel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>26</td>
      <td>Q27968043</td>
      <td>festival edition</td>
    </tr>
    <tr>
      <th>1</th>
      <td>12</td>
      <td>Q1151125</td>
      <td>Pinkpop Festival</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Q276</td>
      <td>Eurovision Song Contest</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Q868557</td>
      <td>music festival</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Q182832</td>
      <td>concert</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1</td>
      <td>Q979949</td>
      <td>International Eucharistic Congress</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1</td>
      <td>Q132241</td>
      <td>festival</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>Q618779</td>
      <td>award</td>
    </tr>
  </tbody>
</table>
</div>




```python
# linked to MB event
links_from_wd = sparql("""
SELECT (?event AS ?wd) ?mbid ?eventLabel
WHERE {
  ?event wdt:P6423 ?mbid .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
ORDER BY ASC(?eventLabel)
""")
links_from_wd.rename(columns={'eventLabel': 'name'}, inplace=True)


print('Count:', len(links_from_wd))
display_df(links_from_wd.head())
```

    Count: 37



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q12682738">Q12682738</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/07ebfee6-4372-4906-8ca5-d82edcc0b1c8">07ebfee6-4372-4906-8ca5-d82edcc0b1c8</a></td>
      <td>Q12682738</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q16913112">Q16913112</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/7ba13795-6dc7-450b-b4ff-052c6adc844e">7ba13795-6dc7-450b-b4ff-052c6adc844e</a></td>
      <td>Q16913112</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q61088805">Q61088805</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/4ec5dc62-9348-41e0-a0ca-949129d6258b">4ec5dc62-9348-41e0-a0ca-949129d6258b</a></td>
      <td>Q61088805</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q61117076">Q61117076</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/acaea9ba-9de5-4518-acc7-3dc38924fb38">acaea9ba-9de5-4518-acc7-3dc38924fb38</a></td>
      <td>Q61117076</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q171784">Q171784</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/3b38dc60-f35f-4335-96cc-e1e2e13e1ffd">3b38dc60-f35f-4335-96cc-e1e2e13e1ffd</a></td>
      <td>Eurovision Song Contest 1956</td>
    </tr>
  </tbody>
</table>


Event before 1920:


```python
sparql("""
SELECT (?event AS ?wd) ?date ?eventLabel ?mbidam

WHERE {
  ?event wdt:P31* wd:Q182832 .
  OPTIONAL { ?event wdt:P6423 ?mbid . }
  ?event wdt:P585 ?date .
  FILTER (year(?date) < 1920) .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
ORDER BY ASC(?date)
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
      <th>wd</th>
      <th>date</th>
      <th>eventLabel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Q1748028</td>
      <td>1783-03-23T00:00:00Z</td>
      <td>Q1748028</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Q19979612</td>
      <td>1808-12-22T00:00:00Z</td>
      <td>Beethoven concert of 22 December 1808</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Q62736575</td>
      <td>1825-03-21T00:00:00Z</td>
      <td>British première of Beethoven's Symphony No. 9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Q59811862</td>
      <td>1902-01-27T00:00:00Z</td>
      <td>Q59811862</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Q2291501</td>
      <td>1913-03-31T00:00:00Z</td>
      <td>Skandalkonzert</td>
    </tr>
  </tbody>
</table>
</div>



## Events from MusicBrainz with wikidata links


```python
links_from_mb = sql("""
SELECT
    url.url AS wd,
    event.gid AS mbid,
    event.name
FROM event
JOIN l_event_url AS leu ON leu.entity0 = event.id
JOIN url                ON leu.entity1 = url.id
WHERE
    url.url LIKE '%%wikidata.org%%'
ORDER BY event.name
;
""")
links_from_mb.wd = links_from_mb.wd.apply(lambda s: s.split('/')[-1])
links_from_mb.mbid = links_from_mb.mbid.apply(str)

print('Count:', len(links_from_mb))
display_df(links_from_mb.head())
```

    Count: 302



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4617578">Q4617578</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/5eb9c50e-7ef2-42d3-90db-2a76dcdb99bb">5eb9c50e-7ef2-42d3-90db-2a76dcdb99bb</a></td>
      <td>10th International Jean Sibelius Violin Competition</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q2636776">Q2636776</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/1d488776-dc23-4bb3-ae13-3ca71999fbe5">1d488776-dc23-4bb3-ae13-3ca71999fbe5</a></td>
      <td>11th International Jean Sibelius Violin Competition</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4581712">Q4581712</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/da2651a2-c945-43f4-8e5b-099767fee350">da2651a2-c945-43f4-8e5b-099767fee350</a></td>
      <td>1984年度十大勁歌金曲頒獎典禮</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4582345">Q4582345</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/30d9210b-afd6-4e9b-ba43-eeb8429239d4">30d9210b-afd6-4e9b-ba43-eeb8429239d4</a></td>
      <td>1985年度十大勁歌金曲頒獎典禮</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4583059">Q4583059</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/db242565-e5e3-43ec-acfa-cbec827f8154">db242565-e5e3-43ec-acfa-cbec827f8154</a></td>
      <td>1986年度十大勁歌金曲頒獎典禮</td>
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

    Count: 36



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1074246">Q1074246</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/b6139248-912f-4bf0-a3c3-42b91ac89c7c">b6139248-912f-4bf0-a3c3-42b91ac89c7c</a></td>
      <td>Animelo Summer Live 2015 -THE GATE-</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1074246">Q1074246</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/2fcfb07b-dfbb-4a71-a0c6-cf0d2bd4b243">2fcfb07b-dfbb-4a71-a0c6-cf0d2bd4b243</a></td>
      <td>Animelo Summer Live 2016 刻-TOKI-</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1074246">Q1074246</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/29f70590-45b4-4bd3-a2ad-260fe6b04944">29f70590-45b4-4bd3-a2ad-260fe6b04944</a></td>
      <td>Animelo Summer Live 2017 -THE CARD-</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1133749">Q1133749</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/57881f3d-0d3e-4188-9c85-59c25ec3515a">57881f3d-0d3e-4188-9c85-59c25ec3515a</a></td>
      <td>Rock in Rio 4</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1133749">Q1133749</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/884b21f8-0d67-4433-a774-e9d7ecde2807">884b21f8-0d67-4433-a774-e9d7ecde2807</a></td>
      <td>Rock in Rio 5</td>
    </tr>
  </tbody>
</table>



```python
duplicate_mb = links_from_mb[['wd', 'mbid', 'name']].groupby('mbid').filter(
    lambda row: len(row.mbid) > 1).sort_values('mbid')

print('Count:', len(duplicate_mb))
display_df(duplicate_mb.head())
```

    Count: 2



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q7300590">Q7300590</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/c6665c04-a110-4aa7-84f4-ae314218b060">c6665c04-a110-4aa7-84f4-ae314218b060</a></td>
      <td>Reading Festival 2012</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1137962">Q1137962</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/c6665c04-a110-4aa7-84f4-ae314218b060">c6665c04-a110-4aa7-84f4-ae314218b060</a></td>
      <td>Reading Festival 2012</td>
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
      <th>name_mb</th>
      <th>_merge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q12682738">Q12682738</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/07ebfee6-4372-4906-8ca5-d82edcc0b1c8">07ebfee6-4372-4906-8ca5-d82edcc0b1c8</a></td>
      <td>Q12682738</td>
      <td>Juara Lagu ’86</td>
      <td>both</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q16913112">Q16913112</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/7ba13795-6dc7-450b-b4ff-052c6adc844e">7ba13795-6dc7-450b-b4ff-052c6adc844e</a></td>
      <td>Q16913112</td>
      <td>XXII Congreso Eucarístico Internacional</td>
      <td>both</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q61088805">Q61088805</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/4ec5dc62-9348-41e0-a0ca-949129d6258b">4ec5dc62-9348-41e0-a0ca-949129d6258b</a></td>
      <td>Q61088805</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q61117076">Q61117076</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/acaea9ba-9de5-4518-acc7-3dc38924fb38">acaea9ba-9de5-4518-acc7-3dc38924fb38</a></td>
      <td>Q61117076</td>
      <td>Anugerah Juara Lagu 33</td>
      <td>both</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q171784">Q171784</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/3b38dc60-f35f-4335-96cc-e1e2e13e1ffd">3b38dc60-f35f-4335-96cc-e1e2e13e1ffd</a></td>
      <td>Eurovision Song Contest 1956</td>
      <td>Eurovision Song Contest 1956</td>
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

    Count: 267



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
      <td>10th International Jean Sibelius Violin Competition</td>
      <td><a target="_blank" href="https://musicbrainz.org/event/5eb9c50e-7ef2-42d3-90db-2a76dcdb99bb">5eb9c50e-7ef2-42d3-90db-2a76dcdb99bb</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4617578">Q4617578</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>11th International Jean Sibelius Violin Competition</td>
      <td><a target="_blank" href="https://musicbrainz.org/event/1d488776-dc23-4bb3-ae13-3ca71999fbe5">1d488776-dc23-4bb3-ae13-3ca71999fbe5</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q2636776">Q2636776</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td>1984年度十大勁歌金曲頒獎典禮</td>
      <td><a target="_blank" href="https://musicbrainz.org/event/da2651a2-c945-43f4-8e5b-099767fee350">da2651a2-c945-43f4-8e5b-099767fee350</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4581712">Q4581712</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td>1985年度十大勁歌金曲頒獎典禮</td>
      <td><a target="_blank" href="https://musicbrainz.org/event/30d9210b-afd6-4e9b-ba43-eeb8429239d4">30d9210b-afd6-4e9b-ba43-eeb8429239d4</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4582345">Q4582345</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td>1986年度十大勁歌金曲頒獎典禮</td>
      <td><a target="_blank" href="https://musicbrainz.org/event/db242565-e5e3-43ec-acfa-cbec827f8154">db242565-e5e3-43ec-acfa-cbec827f8154</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4583059">Q4583059</a></td>
    </tr>
  </tbody>
</table>



```python
# link in wd but missing in mb
links_to_add_to_mb = merge.loc[lambda x : x['_merge']=='left_only'][[
    'name_wd', 'wd', 'mbid']]
links_to_add_to_mb['edit_link'] = links_to_add_to_mb.apply(
    mb_event_edit_wd_link, axis=1)

print('Count:', len(links_to_add_to_mb))
display_df(links_to_add_to_mb.head())
```

    Count: 2



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name_wd</th>
      <th>wd</th>
      <th>mbid</th>
      <th>edit_link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Q61088805</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q61088805">Q61088805</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/4ec5dc62-9348-41e0-a0ca-949129d6258b">4ec5dc62-9348-41e0-a0ca-949129d6258b</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/4ec5dc62-9348-41e0-a0ca-949129d6258b/edit?edit-event.url.99.type=b022d060-e6a8-340f-8c73-6b21b1d090b9&edit-event.url.99.text=https://www.wikidata.org/wiki/Q61088805">edit</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jazz à Juan</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q744640">Q744640</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/7e1e18af-5793-4f44-bd7b-0a364b45acb2">7e1e18af-5793-4f44-bd7b-0a364b45acb2</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/event/7e1e18af-5793-4f44-bd7b-0a364b45acb2/edit?edit-event.url.99.type=b022d060-e6a8-340f-8c73-6b21b1d090b9&edit-event.url.99.text=https://www.wikidata.org/wiki/Q744640">edit</a></td>
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
    <title>Alignment of MusicBrainz and Wikidata Events</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>

  <body style="margin: 20px;">
    <h1>Alignment of MusicBrainz and Wikidata Events</h1>

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

with open('../docs/wd-events-report.html', 'w') as f:
    f.write(template.render(**globals())
            .replace('&lt;', '<').replace('&gt;', '>')
            .replace('class="dataframe"', 'class="table table-striped table-hover table-sm"')
            .replace('thead', 'thead class="thead-light"'))
```
