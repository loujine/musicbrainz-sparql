# Alignment of MusicBrainz and Wikidata instruments


```python
%run -i ../startup.py
ENTITY_TYPE = 'instrument'
```

    Last notebook update: 2021-01-28
    Importing libs
    Defining database parameters
    Defining *sql* helper function
    Last database update: 2021-01-13
    
    Defining *sparql* helper function


## Instruments from Wikidata

Wikidata entities which are musical instruments or families of musical instruments:


```python
# instance of musical instrument
wd_musical_instruments = sparql("""
SELECT ?instrument ?instrumentLabel ?HornbostelSachs
WHERE {
  { ?instrument wdt:P31* wd:Q34379 . }
  UNION
  { ?instrument wdt:P31 wd:Q1254773 . }
  OPTIONAL
  { ?instrument wdt:P1762 ?HornbostelSachs . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
""")
wd_musical_instruments.rename(columns={
    'instrument': 'wd', 'instrumentLabel': 'name'}, inplace=True)
wd_musical_instruments.head()
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
      <th>name</th>
      <th>HornbostelSachs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Q55724333</td>
      <td>friction drums with free stick</td>
      <td>231.13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Q55724337</td>
      <td>rotating friction drums</td>
      <td>232.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Q55724342</td>
      <td>friction drums with tied stick</td>
      <td>231.2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Q55724561</td>
      <td>stationary friction drums with friction cord</td>
      <td>232.1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Q55724566</td>
      <td>single-skin stationary drums with friction cord</td>
      <td>232.11</td>
    </tr>
  </tbody>
</table>
</div>



Entities with "instrumental" links to MB:


```python
# linked to MB instrument
links_from_wd = sparql("""
SELECT (?instrument AS ?wd) ?mbid ?instrumentLabel
WHERE {
  ?instrument wdt:P1330 ?mbid .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
ORDER BY ASC(?instrumentLabel)
""")
links_from_wd.rename(columns={'instrumentLabel': 'name'}, inplace=True)

display_df(links_from_wd.head())
```


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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10751910">Q10751910</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/1c70cc38-deee-4a84-9b16-7a81c0f43aed">1c70cc38-deee-4a84-9b16-7a81c0f43aed</a></td>
      <td>Q10751910</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q13094251">Q13094251</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/f6b76abc-fdef-444c-97b1-27b12e3e3c0b">f6b76abc-fdef-444c-97b1-27b12e3e3c0b</a></td>
      <td>Q13094251</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q13094253">Q13094253</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/176ce29f-bcf0-47f5-beda-c97ef6df6480">176ce29f-bcf0-47f5-beda-c97ef6df6480</a></td>
      <td>Q13094253</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q13094254">Q13094254</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/14acd267-2e1b-459d-b41e-058d2c106345">14acd267-2e1b-459d-b41e-058d2c106345</a></td>
      <td>Q13094254</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q13094255">Q13094255</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/4ac4b541-116d-40c1-93c7-160153ca53ac">4ac4b541-116d-40c1-93c7-160153ca53ac</a></td>
      <td>Q13094255</td>
    </tr>
  </tbody>
</table>


### Wikidata instruments with several MusicBrainz links

Probably needs cleanup


```python
set([wd for wd in links_from_wd.wd
     if links_from_wd.wd.to_list().count(wd) > 1])
```




    {'Q1398629'}




```python
set([mbid for mbid in links_from_wd.mbid
     if links_from_wd.mbid.to_list().count(mbid) > 1])
```




    {'291e2d38-cdc9-4b9e-b592-5d653f32da6c',
     'd5b46baa-37fc-46cc-b99f-c455ce6e6a9c'}



## Instruments from MusicBrainz with wikidata links


```python
links_from_mb = sql("""
SELECT
    url.url AS wd,
    instrument.gid AS mbid,
    instrument.name
FROM url
JOIN l_instrument_url AS llu ON llu.entity1 = url.id
JOIN instrument              ON llu.entity0 = instrument.id
WHERE
    url.url LIKE '%%wikidata.org%%'
ORDER BY instrument.name
;
""")
links_from_mb.wd = links_from_mb.wd.apply(lambda s: s.split('/')[-1])
links_from_mb.mbid = links_from_mb.mbid.apply(str)
display_df(links_from_mb.head())
```


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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q678090">Q678090</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/d5cc3c69-218e-449a-b80d-8bd7a61311a1">d5cc3c69-218e-449a-b80d-8bd7a61311a1</a></td>
      <td>12 string guitar</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4118803">Q4118803</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/21468ce3-bad3-4f48-a2ff-01e6b0bc9ca2">21468ce3-bad3-4f48-a2ff-01e6b0bc9ca2</a></td>
      <td>17-string bass koto</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1024685">Q1024685</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/33b6ba89-8265-4d8f-bbdc-ecff41e29e8c">33b6ba89-8265-4d8f-bbdc-ecff41e29e8c</a></td>
      <td>Afuche/Cabasa</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q18639099">Q18639099</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/26b4608d-acc3-46f3-b509-d83bd798e122">26b4608d-acc3-46f3-b509-d83bd798e122</a></td>
      <td>Anglo concertina</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q2145031">Q2145031</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/e618d02c-41c0-475c-be70-7ef0f92da7d0">e618d02c-41c0-475c-be70-7ef0f92da7d0</a></td>
      <td>Appalachian dulcimer</td>
    </tr>
  </tbody>
</table>


### MusicBrainz instruments with several Wikidata links

Probably needs cleanup


```python
set([wd for wd in links_from_mb.wd
     if links_from_mb.wd.to_list().count(wd) > 1])
```




    {'Q1398629', 'Q5266546'}




```python
set([mbid for mbid in links_from_mb.mbid
     if links_from_mb.mbid.to_list().count(mbid) > 1])
```




    {'291e2d38-cdc9-4b9e-b592-5d653f32da6c',
     'b0f83029-6d38-4f6f-bd30-db44e427f497',
     'd5b46baa-37fc-46cc-b99f-c455ce6e6a9c'}



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10751910">Q10751910</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/1c70cc38-deee-4a84-9b16-7a81c0f43aed">1c70cc38-deee-4a84-9b16-7a81c0f43aed</a></td>
      <td>Q10751910</td>
      <td>cò ke</td>
      <td>both</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q13094251">Q13094251</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/f6b76abc-fdef-444c-97b1-27b12e3e3c0b">f6b76abc-fdef-444c-97b1-27b12e3e3c0b</a></td>
      <td>Q13094251</td>
      <td>kendhang batangan</td>
      <td>both</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q13094253">Q13094253</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/176ce29f-bcf0-47f5-beda-c97ef6df6480">176ce29f-bcf0-47f5-beda-c97ef6df6480</a></td>
      <td>Q13094253</td>
      <td>kendhang ketipung</td>
      <td>both</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q13094254">Q13094254</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/14acd267-2e1b-459d-b41e-058d2c106345">14acd267-2e1b-459d-b41e-058d2c106345</a></td>
      <td>Q13094254</td>
      <td>kendhang gendhing</td>
      <td>both</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q13094255">Q13094255</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/4ac4b541-116d-40c1-93c7-160153ca53ac">4ac4b541-116d-40c1-93c7-160153ca53ac</a></td>
      <td>Q13094255</td>
      <td>kendhang wayangan</td>
      <td>both</td>
    </tr>
  </tbody>
</table>



```python
# link in mb but missing in wd
links_to_add_to_wd = merge.loc[lambda x : x['_merge']=='right_only'][['name_mb', 'mbid', 'wd']]
display_df(links_to_add_to_wd)
```


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
      <td>Pierrot ensemble</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/51e92fd2-e56e-4576-8547-acb63e8b8446">51e92fd2-e56e-4576-8547-acb63e8b8446</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q7192570">Q7192570</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>baglamas</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/d4d5309f-166e-4e14-9887-06692f2c1027">d4d5309f-166e-4e14-9887-06692f2c1027</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q528239">Q528239</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td>bağlama</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/2dd967cd-104e-4696-8a70-0f6fd37779e7">2dd967cd-104e-4696-8a70-0f6fd37779e7</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q717773">Q717773</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td>bedug</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/9063d25e-87e4-4adc-81d4-8fdee23bd26f">9063d25e-87e4-4adc-81d4-8fdee23bd26f</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q3624317">Q3624317</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td>bīn</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/efa5b047-95e7-4ebb-9987-b07208a1ac27">efa5b047-95e7-4ebb-9987-b07208a1ac27</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5266546">Q5266546</a></td>
    </tr>
    <tr>
      <th>5</th>
      <td>diatonic button accordion</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/842d3d24-f638-47e6-a239-8578723db09c">842d3d24-f638-47e6-a239-8578723db09c</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q379269">Q379269</a></td>
    </tr>
    <tr>
      <th>6</th>
      <td>dilruba</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/57deb1b0-b7fe-4616-b9cb-bbd59bc0acd8">57deb1b0-b7fe-4616-b9cb-bbd59bc0acd8</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q17190172">Q17190172</a></td>
    </tr>
    <tr>
      <th>7</th>
      <td>gendèr barung</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/60cd46dd-45d5-47ff-8d7e-a501e9c7938c">60cd46dd-45d5-47ff-8d7e-a501e9c7938c</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q74581228">Q74581228</a></td>
    </tr>
    <tr>
      <th>8</th>
      <td>kempul</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/e0350378-0d4b-49d5-ad81-8f74e1b54efc">e0350378-0d4b-49d5-ad81-8f74e1b54efc</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q6387169">Q6387169</a></td>
    </tr>
    <tr>
      <th>9</th>
      <td>lira da braccio</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/6060f9c4-10ee-48b7-a2d8-e97f944afa70">6060f9c4-10ee-48b7-a2d8-e97f944afa70</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q584967">Q584967</a></td>
    </tr>
    <tr>
      <th>10</th>
      <td>piano duo</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/0a49e297-8430-44cd-be7b-1fd22560b6e1">0a49e297-8430-44cd-be7b-1fd22560b6e1</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q43136500">Q43136500</a></td>
    </tr>
    <tr>
      <th>11</th>
      <td>piano four hands</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c3f3aacc-d9c0-4b6e-92e8-05df9af50e17">c3f3aacc-d9c0-4b6e-92e8-05df9af50e17</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q227484">Q227484</a></td>
    </tr>
    <tr>
      <th>12</th>
      <td>piano quartet</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ffa61786-07ed-48ed-b7bb-a17d248fba8c">ffa61786-07ed-48ed-b7bb-a17d248fba8c</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1746025">Q1746025</a></td>
    </tr>
    <tr>
      <th>13</th>
      <td>pluriarc</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/d43c2380-efe5-4488-b08f-777296d0c95c">d43c2380-efe5-4488-b08f-777296d0c95c</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q3392660">Q3392660</a></td>
    </tr>
    <tr>
      <th>14</th>
      <td>rammana</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/551e553a-cadd-4363-8723-f72aab5431d0">551e553a-cadd-4363-8723-f72aab5431d0</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q16033036">Q16033036</a></td>
    </tr>
    <tr>
      <th>15</th>
      <td>saron barung</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/5b159ed5-2c58-4200-accb-c2ac5c9ace7f">5b159ed5-2c58-4200-accb-c2ac5c9ace7f</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q13096799">Q13096799</a></td>
    </tr>
    <tr>
      <th>16</th>
      <td>saron demung</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/81da5ec5-4a2f-4481-b01d-fb8ab9ea116d">81da5ec5-4a2f-4481-b01d-fb8ab9ea116d</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4262704">Q4262704</a></td>
    </tr>
    <tr>
      <th>17</th>
      <td>saron panerus</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/2656be9c-b531-4cbb-a5b5-30454054343c">2656be9c-b531-4cbb-a5b5-30454054343c</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q20585538">Q20585538</a></td>
    </tr>
    <tr>
      <th>18</th>
      <td>saron peking</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/b3fe02dc-f412-464e-b216-8c3fe45de456">b3fe02dc-f412-464e-b216-8c3fe45de456</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q13095883">Q13095883</a></td>
    </tr>
    <tr>
      <th>19</th>
      <td>scraped idiophone</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/dbd1ec09-34fd-412e-b73b-124e46cf7cdf">dbd1ec09-34fd-412e-b73b-124e46cf7cdf</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q50825269">Q50825269</a></td>
    </tr>
    <tr>
      <th>20</th>
      <td>string trio</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/6efec29d-013a-4687-b710-fe25800eb358">6efec29d-013a-4687-b710-fe25800eb358</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q29787068">Q29787068</a></td>
    </tr>
    <tr>
      <th>21</th>
      <td>tape</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/672c19ec-0ca3-4ece-9f6b-7f1c0018a0e6">672c19ec-0ca3-4ece-9f6b-7f1c0018a0e6</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q193663">Q193663</a></td>
    </tr>
    <tr>
      <th>22</th>
      <td>viol consort</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/e46bffd3-15a3-426a-923f-705839128609">e46bffd3-15a3-426a-923f-705839128609</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1492889">Q1492889</a></td>
    </tr>
    <tr>
      <th>23</th>
      <td>voice synthesizer</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/b0f83029-6d38-4f6f-bd30-db44e427f497">b0f83029-6d38-4f6f-bd30-db44e427f497</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q16346">Q16346</a></td>
    </tr>
  </tbody>
</table>


24 links in MB that are not in WD


```python
# link in wd but missing in mb
links_to_add_to_mb = merge.loc[lambda x : x['_merge']=='left_only'][['name_wd', 'wd', 'mbid']]
display_df(links_to_add_to_mb)
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name_wd</th>
      <th>wd</th>
      <th>mbid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rebana</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q3181140">Q3181140</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/551e553a-cadd-4363-8723-f72aab5431d0">551e553a-cadd-4363-8723-f72aab5431d0</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>akkordolia</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4701390">Q4701390</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/bd5fa79a-ea6f-4e11-9463-f6f43cca363c">bd5fa79a-ea6f-4e11-9463-f6f43cca363c</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td>bell</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q101401">Q101401</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c95c7129-d180-4218-afea-4b74ef70e2be">c95c7129-d180-4218-afea-4b74ef70e2be</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td>bellows-blown bagpipe</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q63619194">Q63619194</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/d4cbc6fd-5e68-4cf4-afeb-dd2fb4df3c2d">d4cbc6fd-5e68-4cf4-afeb-dd2fb4df3c2d</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td>dilrupa</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5277044">Q5277044</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/57deb1b0-b7fe-4616-b9cb-bbd59bc0acd8">57deb1b0-b7fe-4616-b9cb-bbd59bc0acd8</a></td>
    </tr>
    <tr>
      <th>5</th>
      <td>fretless bass</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q932855">Q932855</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/12f20f43-c71d-4476-8ada-b968aab50900">12f20f43-c71d-4476-8ada-b968aab50900</a></td>
    </tr>
    <tr>
      <th>6</th>
      <td>lap slide guitar</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q6488060">Q6488060</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c0ea0405-ae3f-4851-bf85-277fadff80e2">c0ea0405-ae3f-4851-bf85-277fadff80e2</a></td>
    </tr>
    <tr>
      <th>7</th>
      <td>scraped idiophone</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1644824">Q1644824</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/dbd1ec09-34fd-412e-b73b-124e46cf7cdf">dbd1ec09-34fd-412e-b73b-124e46cf7cdf</a></td>
    </tr>
    <tr>
      <th>8</th>
      <td>tromboon</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q840638">Q840638</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ee499c78-26df-4698-ab97-c4120276eb1a">ee499c78-26df-4698-ab97-c4120276eb1a</a></td>
    </tr>
  </tbody>
</table>


9 links in WD that are not in MB

In those mismatches, some are not recognized because of redirects on WD side: Q54995817 to Q4138014, Q16033036 to Q3181140

## Instruments from MusicBrainz without wikidata links


```python
no_links_from_mb = sql("""
SELECT
    gid AS mbid,
    name
FROM
    instrument
WHERE
    id NOT IN (
        SELECT
            instrument.id
        FROM url
        JOIN l_instrument_url AS llu ON llu.entity1 = url.id
        JOIN instrument              ON llu.entity0 = instrument.id
        WHERE
            url.url LIKE '%%wikidata.org%%'
    )
;
""")
no_links_from_mb.mbid = no_links_from_mb.mbid.apply(str)
display_df(no_links_from_mb)
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mbid</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/f711b03f-86c6-4e67-86eb-c6716ddbe1c1">f711b03f-86c6-4e67-86eb-c6716ddbe1c1</a></td>
      <td>kös</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/872b72a2-541c-4115-b7ce-2dfed3e84884">872b72a2-541c-4115-b7ce-2dfed3e84884</a></td>
      <td>bin-sitar</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/a66b7f37-5aa2-43b8-85eb-0dea87aae930">a66b7f37-5aa2-43b8-85eb-0dea87aae930</a></td>
      <td>gramorimba</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c9fb1652-1a07-4f3d-b886-ec961efcc7c8">c9fb1652-1a07-4f3d-b886-ec961efcc7c8</a></td>
      <td>segunda</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/f0ddf0ec-e8ac-4765-acef-0687af2b2f32">f0ddf0ec-e8ac-4765-acef-0687af2b2f32</a></td>
      <td>fourth flute</td>
    </tr>
    <tr>
      <th>5</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/bd5a399f-c18e-41ad-af23-a01353c51d7c">bd5a399f-c18e-41ad-af23-a01353c51d7c</a></td>
      <td>ki pah</td>
    </tr>
    <tr>
      <th>6</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/39b5634a-4802-4a66-a27a-58f37677c197">39b5634a-4802-4a66-a27a-58f37677c197</a></td>
      <td>primero</td>
    </tr>
    <tr>
      <th>7</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/44055718-26b6-4a25-9e76-5067ae5b9862">44055718-26b6-4a25-9e76-5067ae5b9862</a></td>
      <td>ding tac ta</td>
    </tr>
    <tr>
      <th>8</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/1156c575-2165-4799-be3f-023ff1fc7655">1156c575-2165-4799-be3f-023ff1fc7655</a></td>
      <td>daruan</td>
    </tr>
    <tr>
      <th>9</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ec478db3-c490-4fca-a688-0bdd9fb55806">ec478db3-c490-4fca-a688-0bdd9fb55806</a></td>
      <td>heike biwa</td>
    </tr>
    <tr>
      <th>10</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/7a5b3204-0200-426c-88d5-3f26a225b757">7a5b3204-0200-426c-88d5-3f26a225b757</a></td>
      <td>hmông flute</td>
    </tr>
    <tr>
      <th>11</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/91eb1744-96d8-4c54-8aa2-f97ed7d88950">91eb1744-96d8-4c54-8aa2-f97ed7d88950</a></td>
      <td>foot stomps</td>
    </tr>
    <tr>
      <th>12</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/837c7244-ece8-47ff-b215-78f4aa4f227d">837c7244-ece8-47ff-b215-78f4aa4f227d</a></td>
      <td>treble violin</td>
    </tr>
    <tr>
      <th>13</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/12f20f43-c71d-4476-8ada-b968aab50900">12f20f43-c71d-4476-8ada-b968aab50900</a></td>
      <td>electric fretless guitar</td>
    </tr>
    <tr>
      <th>14</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/e798a2bd-a578-4c28-8eea-6eca2d8b2c5d">e798a2bd-a578-4c28-8eea-6eca2d8b2c5d</a></td>
      <td>horn</td>
    </tr>
    <tr>
      <th>15</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/b6aa8ec7-3ede-4f8b-92f1-45f4568e3261">b6aa8ec7-3ede-4f8b-92f1-45f4568e3261</a></td>
      <td>khong wong</td>
    </tr>
    <tr>
      <th>16</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/40243f27-1011-491b-8b06-28c48749b960">40243f27-1011-491b-8b06-28c48749b960</a></td>
      <td>farfisa</td>
    </tr>
    <tr>
      <th>17</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ce8bf63e-ffb2-44e9-a886-16ca6522525f">ce8bf63e-ffb2-44e9-a886-16ca6522525f</a></td>
      <td>đing buốt</td>
    </tr>
    <tr>
      <th>18</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/0e7c8402-0603-4aff-880b-bb7eedbf5c01">0e7c8402-0603-4aff-880b-bb7eedbf5c01</a></td>
      <td>traditional basque ensemble</td>
    </tr>
    <tr>
      <th>19</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/db36bd83-0606-42b9-91a0-d759ba52d0da">db36bd83-0606-42b9-91a0-d759ba52d0da</a></td>
      <td>trumpet family</td>
    </tr>
    <tr>
      <th>20</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/3c5349ca-cf82-4537-851f-1957ac88bced">3c5349ca-cf82-4537-851f-1957ac88bced</a></td>
      <td>electric lap steel guitar</td>
    </tr>
    <tr>
      <th>21</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/809f4e7f-918f-4e7e-884a-dc7faa4e52c1">809f4e7f-918f-4e7e-884a-dc7faa4e52c1</a></td>
      <td>gendèr wayang</td>
    </tr>
    <tr>
      <th>22</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/5888d65d-9d65-4d13-8454-3d68be9b3e55">5888d65d-9d65-4d13-8454-3d68be9b3e55</a></td>
      <td>acoustic fretless guitar</td>
    </tr>
    <tr>
      <th>23</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/a3c58697-eae3-454c-90c5-5f911a24376a">a3c58697-eae3-454c-90c5-5f911a24376a</a></td>
      <td>daire</td>
    </tr>
    <tr>
      <th>24</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/f02ca577-d1ec-4c02-97c8-a15afff6bbfa">f02ca577-d1ec-4c02-97c8-a15afff6bbfa</a></td>
      <td>daluo</td>
    </tr>
    <tr>
      <th>25</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/3933adfe-f55b-47fd-b085-c9983d15cc9d">3933adfe-f55b-47fd-b085-c9983d15cc9d</a></td>
      <td>five-string banjo</td>
    </tr>
    <tr>
      <th>26</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/371dd55f-5251-4905-a8b2-2d2acf352376">371dd55f-5251-4905-a8b2-2d2acf352376</a></td>
      <td>keyed brass instruments</td>
    </tr>
    <tr>
      <th>27</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ac16043b-4727-40f9-bb2a-cb30ab4ce7a2">ac16043b-4727-40f9-bb2a-cb30ab4ce7a2</a></td>
      <td>chikuzen biwa</td>
    </tr>
    <tr>
      <th>28</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ca17a349-e0e3-4b9b-b74d-898a2b54b43e">ca17a349-e0e3-4b9b-b74d-898a2b54b43e</a></td>
      <td>syrinx</td>
    </tr>
    <tr>
      <th>29</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/53174999-953d-482b-9240-23acf2452fc9">53174999-953d-482b-9240-23acf2452fc9</a></td>
      <td>wavedrum</td>
    </tr>
    <tr>
      <th>30</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/34c1af71-f7fc-4e34-a46a-5c29ee4c019b">34c1af71-f7fc-4e34-a46a-5c29ee4c019b</a></td>
      <td>folk harp</td>
    </tr>
    <tr>
      <th>31</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/e5781903-d6ef-4480-a158-60300265577c">e5781903-d6ef-4480-a158-60300265577c</a></td>
      <td>natural brass instruments</td>
    </tr>
    <tr>
      <th>32</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/88f0d4fb-e7cc-4825-9d05-bcf974953790">88f0d4fb-e7cc-4825-9d05-bcf974953790</a></td>
      <td>disk drive</td>
    </tr>
    <tr>
      <th>33</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/87d5bd6a-8d14-4ed0-befa-b90379536634">87d5bd6a-8d14-4ed0-befa-b90379536634</a></td>
      <td>nylon guitar</td>
    </tr>
    <tr>
      <th>34</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/bc542c3c-5cf6-4c31-b75f-a03d660cad75">bc542c3c-5cf6-4c31-b75f-a03d660cad75</a></td>
      <td>German harp</td>
    </tr>
    <tr>
      <th>35</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/4a5da835-0f0d-4010-b013-76d0a48f8578">4a5da835-0f0d-4010-b013-76d0a48f8578</a></td>
      <td>slide brass instruments</td>
    </tr>
    <tr>
      <th>36</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/7aed0189-ff99-4b43-8ff0-52ca5626d0b7">7aed0189-ff99-4b43-8ff0-52ca5626d0b7</a></td>
      <td>ankle rattlers</td>
    </tr>
    <tr>
      <th>37</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/81b68590-5c82-47a3-9790-1570ca60f711">81b68590-5c82-47a3-9790-1570ca60f711</a></td>
      <td>fundeh</td>
    </tr>
    <tr>
      <th>38</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ce9452ac-917f-4cab-ab13-75996816202b">ce9452ac-917f-4cab-ab13-75996816202b</a></td>
      <td>saz</td>
    </tr>
    <tr>
      <th>39</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/fe2e16fc-81b7-44e7-a96a-c3afac308a04">fe2e16fc-81b7-44e7-a96a-c3afac308a04</a></td>
      <td>valve trombone</td>
    </tr>
    <tr>
      <th>40</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/65116580-10f5-4123-9d86-5e379cd9ab83">65116580-10f5-4123-9d86-5e379cd9ab83</a></td>
      <td>wire-strung harp</td>
    </tr>
    <tr>
      <th>41</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/92ec69b8-c35c-4d44-9e99-953d229d6e87">92ec69b8-c35c-4d44-9e99-953d229d6e87</a></td>
      <td>pang gu ly hu hmông</td>
    </tr>
    <tr>
      <th>42</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/d2f041b9-b6a6-4973-badd-1b07a37192c9">d2f041b9-b6a6-4973-badd-1b07a37192c9</a></td>
      <td>valved brass instruments</td>
    </tr>
    <tr>
      <th>43</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/27a9b513-5218-404f-a285-02d89aa358df">27a9b513-5218-404f-a285-02d89aa358df</a></td>
      <td>chacha</td>
    </tr>
    <tr>
      <th>44</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/2561db4d-1018-4a40-9b15-93bcbd0887d4">2561db4d-1018-4a40-9b15-93bcbd0887d4</a></td>
      <td>pōrutu</td>
    </tr>
    <tr>
      <th>45</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ba6af31f-8b2f-4c5e-903e-882f88f6d3a6">ba6af31f-8b2f-4c5e-903e-882f88f6d3a6</a></td>
      <td>soprano violin</td>
    </tr>
    <tr>
      <th>46</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/de564c42-80db-4040-96c4-269ad9e063ac">de564c42-80db-4040-96c4-269ad9e063ac</a></td>
      <td>satsuma biwa</td>
    </tr>
    <tr>
      <th>47</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/5f0a32fa-82b2-49da-a9ee-78cad9cf756d">5f0a32fa-82b2-49da-a9ee-78cad9cf756d</a></td>
      <td>tanbou ka</td>
    </tr>
    <tr>
      <th>48</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ce0a1033-3e33-4d7f-8230-1fb53a57651d">ce0a1033-3e33-4d7f-8230-1fb53a57651d</a></td>
      <td>xiaoluo</td>
    </tr>
    <tr>
      <th>49</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/44c74dce-8a26-4837-9c19-918b412c6a6a">44c74dce-8a26-4837-9c19-918b412c6a6a</a></td>
      <td>tràm plè</td>
    </tr>
    <tr>
      <th>50</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/741715c4-1756-43f8-b56f-a4aca1dc2cfd">741715c4-1756-43f8-b56f-a4aca1dc2cfd</a></td>
      <td>żafżafa</td>
    </tr>
    <tr>
      <th>51</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/9478e40f-bab3-4fcb-a52a-f3df65770bfa">9478e40f-bab3-4fcb-a52a-f3df65770bfa</a></td>
      <td>żummara</td>
    </tr>
    <tr>
      <th>52</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/b0acbf59-ffba-4e2f-8104-31aed56fa364">b0acbf59-ffba-4e2f-8104-31aed56fa364</a></td>
      <td>tef</td>
    </tr>
    <tr>
      <th>53</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/8045f4a3-7f12-4de4-957d-26908a2714eb">8045f4a3-7f12-4de4-957d-26908a2714eb</a></td>
      <td>trắng jâu</td>
    </tr>
    <tr>
      <th>54</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/fd5caadd-efab-487a-8954-cd243396fbe2">fd5caadd-efab-487a-8954-cd243396fbe2</a></td>
      <td>trắng lu</td>
    </tr>
    <tr>
      <th>55</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/2c27736b-e774-4f8e-8290-604d3c468870">2c27736b-e774-4f8e-8290-604d3c468870</a></td>
      <td>đàn tứ dây</td>
    </tr>
    <tr>
      <th>56</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/d4cbc6fd-5e68-4cf4-afeb-dd2fb4df3c2d">d4cbc6fd-5e68-4cf4-afeb-dd2fb4df3c2d</a></td>
      <td>bellow-blown bagpipes</td>
    </tr>
    <tr>
      <th>57</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/023adf58-6aa2-4659-8760-3b36f81d0352">023adf58-6aa2-4659-8760-3b36f81d0352</a></td>
      <td>chamber organ</td>
    </tr>
    <tr>
      <th>58</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/f1e042f5-2a09-47b1-9cdf-1018d239d330">f1e042f5-2a09-47b1-9cdf-1018d239d330</a></td>
      <td>rhythm sticks</td>
    </tr>
    <tr>
      <th>59</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/63f030d8-f116-4f11-9dee-0cb1cfeb8445">63f030d8-f116-4f11-9dee-0cb1cfeb8445</a></td>
      <td>pí thiu</td>
    </tr>
    <tr>
      <th>60</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/e8e99279-0774-404a-9973-d4b06c759fc4">e8e99279-0774-404a-9973-d4b06c759fc4</a></td>
      <td>shudraga</td>
    </tr>
    <tr>
      <th>61</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/76e5cc5f-aa37-4be3-a035-9e7518250ee5">76e5cc5f-aa37-4be3-a035-9e7518250ee5</a></td>
      <td>ti bwa</td>
    </tr>
    <tr>
      <th>62</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/0b9d87fa-93fa-4956-8b6a-a419566cc915">0b9d87fa-93fa-4956-8b6a-a419566cc915</a></td>
      <td>electric bass guitar</td>
    </tr>
    <tr>
      <th>63</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/35e94803-4462-407a-8a01-3e474a45aaaf">35e94803-4462-407a-8a01-3e474a45aaaf</a></td>
      <td>tenor trombone</td>
    </tr>
    <tr>
      <th>64</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ffe6c3f3-12a2-42e7-8cde-7ae24ff83fc5">ffe6c3f3-12a2-42e7-8cde-7ae24ff83fc5</a></td>
      <td>trống bông</td>
    </tr>
    <tr>
      <th>65</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/2fb619eb-c5b3-495a-967a-b747b976a7d9">2fb619eb-c5b3-495a-967a-b747b976a7d9</a></td>
      <td>bowed piano</td>
    </tr>
    <tr>
      <th>66</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/8a4a2afb-609e-4316-b7fa-4a687aada9ee">8a4a2afb-609e-4316-b7fa-4a687aada9ee</a></td>
      <td>brushes</td>
    </tr>
    <tr>
      <th>67</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/117dacfc-0ad0-4e90-81a4-a28b4c03929b">117dacfc-0ad0-4e90-81a4-a28b4c03929b</a></td>
      <td>Spanish acoustic guitar</td>
    </tr>
    <tr>
      <th>68</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c0ea0405-ae3f-4851-bf85-277fadff80e2">c0ea0405-ae3f-4851-bf85-277fadff80e2</a></td>
      <td>Hawaiian guitar</td>
    </tr>
    <tr>
      <th>69</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/74e8088e-d5b0-44bc-853a-74aa8c8aa5aa">74e8088e-d5b0-44bc-853a-74aa8c8aa5aa</a></td>
      <td>finger cymbals</td>
    </tr>
    <tr>
      <th>70</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/96bec768-bee7-4b67-816e-3b4743df98ec">96bec768-bee7-4b67-816e-3b4743df98ec</a></td>
      <td>fretless bass</td>
    </tr>
    <tr>
      <th>71</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/310cb712-c512-419f-9b61-ab77325b6636">310cb712-c512-419f-9b61-ab77325b6636</a></td>
      <td>Tibetan water drum</td>
    </tr>
    <tr>
      <th>72</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c95c7129-d180-4218-afea-4b74ef70e2be">c95c7129-d180-4218-afea-4b74ef70e2be</a></td>
      <td>bell</td>
    </tr>
    <tr>
      <th>73</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/a2d87653-559a-4c8e-9cb0-f72effb8df8f">a2d87653-559a-4c8e-9cb0-f72effb8df8f</a></td>
      <td>vacuum cleaner</td>
    </tr>
    <tr>
      <th>74</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/f83c4b45-3584-401a-90bf-4ec80e7add78">f83c4b45-3584-401a-90bf-4ec80e7add78</a></td>
      <td>bağlama (saz) family</td>
    </tr>
    <tr>
      <th>75</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/e6571d23-5d79-4216-99d6-06e14e737da1">e6571d23-5d79-4216-99d6-06e14e737da1</a></td>
      <td>bass synthesizer</td>
    </tr>
    <tr>
      <th>76</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/7631a763-6c36-4fc6-b04a-1021cd60e7e5">7631a763-6c36-4fc6-b04a-1021cd60e7e5</a></td>
      <td>pūkaea</td>
    </tr>
    <tr>
      <th>77</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/5c5cf664-4685-4089-bce0-b8c7e16ac698">5c5cf664-4685-4089-bce0-b8c7e16ac698</a></td>
      <td>rehu</td>
    </tr>
    <tr>
      <th>78</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/98837460-d363-4af3-920c-cc016b48d98d">98837460-d363-4af3-920c-cc016b48d98d</a></td>
      <td>pūmotomoto</td>
    </tr>
    <tr>
      <th>79</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/68064791-4108-4c97-812f-990c45d1ba0d">68064791-4108-4c97-812f-990c45d1ba0d</a></td>
      <td>nguru</td>
    </tr>
    <tr>
      <th>80</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/2e345a93-045e-403a-80a9-4c6835c3a49e">2e345a93-045e-403a-80a9-4c6835c3a49e</a></td>
      <td>pūrerehua</td>
    </tr>
    <tr>
      <th>81</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/23af87b9-81a5-45ed-9d2e-cf4c64bfd932">23af87b9-81a5-45ed-9d2e-cf4c64bfd932</a></td>
      <td>piano spinet</td>
    </tr>
    <tr>
      <th>82</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/b6649fb6-d4cc-477e-ae8d-39145fb46d06">b6649fb6-d4cc-477e-ae8d-39145fb46d06</a></td>
      <td>poi āwhiowhio</td>
    </tr>
    <tr>
      <th>83</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/b6c87b0e-5f2b-49a4-bc0e-457e0e4951b9">b6c87b0e-5f2b-49a4-bc0e-457e0e4951b9</a></td>
      <td>saduk</td>
    </tr>
    <tr>
      <th>84</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/d0feefd4-147a-4ed9-a07c-c267b436f47f">d0feefd4-147a-4ed9-a07c-c267b436f47f</a></td>
      <td>temür khuur</td>
    </tr>
    <tr>
      <th>85</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/26ed69bd-3828-4c49-8e74-0fb4399a06d3">26ed69bd-3828-4c49-8e74-0fb4399a06d3</a></td>
      <td>khulsan khuur</td>
    </tr>
    <tr>
      <th>86</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/5ed5bf1f-ca26-4aeb-b4dd-88a52b1a17e7">5ed5bf1f-ca26-4aeb-b4dd-88a52b1a17e7</a></td>
      <td>pahū pounamu</td>
    </tr>
    <tr>
      <th>87</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/f68936f2-194c-4bcd-94a9-81e1dd947b8d">f68936f2-194c-4bcd-94a9-81e1dd947b8d</a></td>
      <td>guitar family</td>
    </tr>
    <tr>
      <th>88</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/925959ba-97d4-4e6f-b9dc-3ba8c4a773c4">925959ba-97d4-4e6f-b9dc-3ba8c4a773c4</a></td>
      <td>pahū</td>
    </tr>
    <tr>
      <th>89</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/3158f700-4e47-4cc5-b641-228b0c5e5a4a">3158f700-4e47-4cc5-b641-228b0c5e5a4a</a></td>
      <td>pākuru</td>
    </tr>
    <tr>
      <th>90</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/37ebafcb-34d7-436e-ba6e-b8646086f665">37ebafcb-34d7-436e-ba6e-b8646086f665</a></td>
      <td>chuurqin</td>
    </tr>
    <tr>
      <th>91</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/30aeef52-3ebf-405e-9baa-ef6c6f3ef6d5">30aeef52-3ebf-405e-9baa-ef6c6f3ef6d5</a></td>
      <td>repeater</td>
    </tr>
    <tr>
      <th>92</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/6bcb239b-e739-4d47-81e7-c2eec8e7b1ea">6bcb239b-e739-4d47-81e7-c2eec8e7b1ea</a></td>
      <td>chirimía and drum</td>
    </tr>
    <tr>
      <th>93</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/90bd690b-f86d-4ea3-b87d-f945b1ab9e38">90bd690b-f86d-4ea3-b87d-f945b1ab9e38</a></td>
      <td>tōkere</td>
    </tr>
    <tr>
      <th>94</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/908b5372-2a64-4248-8c27-3e9c76951aa1">908b5372-2a64-4248-8c27-3e9c76951aa1</a></td>
      <td>porotiti</td>
    </tr>
    <tr>
      <th>95</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c2bfcf82-356c-4606-9dd7-51efd1b11bec">c2bfcf82-356c-4606-9dd7-51efd1b11bec</a></td>
      <td>gut guitar</td>
    </tr>
    <tr>
      <th>96</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/bfa5b262-34cf-418b-a9c5-b629a24a96ee">bfa5b262-34cf-418b-a9c5-b629a24a96ee</a></td>
      <td>English flageolet</td>
    </tr>
    <tr>
      <th>97</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/205acba3-c6aa-4e47-be4c-2be043cfd511">205acba3-c6aa-4e47-be4c-2be043cfd511</a></td>
      <td>plucked idiophone</td>
    </tr>
    <tr>
      <th>98</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/bac20474-624a-46ce-a517-871eea3486b1">bac20474-624a-46ce-a517-871eea3486b1</a></td>
      <td>bouzar / gouzouki</td>
    </tr>
    <tr>
      <th>99</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/6dadb008-cb59-40cb-8b3a-a07942ffb818">6dadb008-cb59-40cb-8b3a-a07942ffb818</a></td>
      <td>viololyra</td>
    </tr>
    <tr>
      <th>100</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/cc996d06-87dc-420e-9ed7-a52867ca6e1e">cc996d06-87dc-420e-9ed7-a52867ca6e1e</a></td>
      <td>vibrandoneon</td>
    </tr>
    <tr>
      <th>101</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/68a64027-1bc3-4057-bd51-165697322aca">68a64027-1bc3-4057-bd51-165697322aca</a></td>
      <td>kamalen ngɔni</td>
    </tr>
    <tr>
      <th>102</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/a11e9091-1182-4d79-90a1-dcaa282e4a98">a11e9091-1182-4d79-90a1-dcaa282e4a98</a></td>
      <td>jeli ngɔni</td>
    </tr>
    <tr>
      <th>103</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/f7e7dd09-eef7-4c66-a226-c8eb6ba378e1">f7e7dd09-eef7-4c66-a226-c8eb6ba378e1</a></td>
      <td>pūpakapaka</td>
    </tr>
    <tr>
      <th>104</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/a4f10af3-d440-4ee7-9093-c60a121df41a">a4f10af3-d440-4ee7-9093-c60a121df41a</a></td>
      <td>kōauau ponga ihu</td>
    </tr>
    <tr>
      <th>105</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/fdc68c28-cc0c-4ae6-bd9e-dd0b68e3cf1a">fdc68c28-cc0c-4ae6-bd9e-dd0b68e3cf1a</a></td>
      <td>hue puruwai</td>
    </tr>
    <tr>
      <th>106</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/fdcacb6d-7f3d-446d-aa65-fff4c9afb7f6">fdcacb6d-7f3d-446d-aa65-fff4c9afb7f6</a></td>
      <td>hue puruhau</td>
    </tr>
    <tr>
      <th>107</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/0c5e5de9-605c-4487-b454-ef70ef8c1996">0c5e5de9-605c-4487-b454-ef70ef8c1996</a></td>
      <td>rōria</td>
    </tr>
    <tr>
      <th>108</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/1b425878-18c7-4bcd-9129-bed989295e5f">1b425878-18c7-4bcd-9129-bed989295e5f</a></td>
      <td>te kū</td>
    </tr>
    <tr>
      <th>109</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/e5408785-e228-4919-9e79-6f997bcdfea5">e5408785-e228-4919-9e79-6f997bcdfea5</a></td>
      <td>tube zither</td>
    </tr>
    <tr>
      <th>110</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/0a06dd9a-92d6-4891-a699-2b116a3d3f37">0a06dd9a-92d6-4891-a699-2b116a3d3f37</a></td>
      <td>other instruments</td>
    </tr>
    <tr>
      <th>111</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/3b7be43c-0b3b-42dd-8560-d61e41f6bd61">3b7be43c-0b3b-42dd-8560-d61e41f6bd61</a></td>
      <td>saron wayang</td>
    </tr>
    <tr>
      <th>112</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c588cc24-e139-44a9-8a48-7963eb693dd1">c588cc24-e139-44a9-8a48-7963eb693dd1</a></td>
      <td>kendhang indung</td>
    </tr>
    <tr>
      <th>113</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ed1628bd-8541-4874-b8ca-2cec8b4c5140">ed1628bd-8541-4874-b8ca-2cec8b4c5140</a></td>
      <td>baandu</td>
    </tr>
    <tr>
      <th>114</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/292a95fd-9bc7-4052-aa6e-844c8f4f4905">292a95fd-9bc7-4052-aa6e-844c8f4f4905</a></td>
      <td>kendhang kulanter</td>
    </tr>
  </tbody>
</table>


## Alignment suggestions

### Exact match

Exact match between instrument names in WD and MB:


```python
no_links_merge = pd.merge(no_links_from_mb, wd_musical_instruments, 
                 on='name', how='inner', indicator=False)
display_df(no_links_merge)
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mbid</th>
      <th>name</th>
      <th>wd</th>
      <th>HornbostelSachs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ca17a349-e0e3-4b9b-b74d-898a2b54b43e">ca17a349-e0e3-4b9b-b74d-898a2b54b43e</a></td>
      <td>syrinx</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10902606">Q10902606</a></td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c95c7129-d180-4218-afea-4b74ef70e2be">c95c7129-d180-4218-afea-4b74ef70e2be</a></td>
      <td>bell</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q101401">Q101401</a></td>
      <td>111.242</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c95c7129-d180-4218-afea-4b74ef70e2be">c95c7129-d180-4218-afea-4b74ef70e2be</a></td>
      <td>bell</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q96309259">Q96309259</a></td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/e5408785-e228-4919-9e79-6f997bcdfea5">e5408785-e228-4919-9e79-6f997bcdfea5</a></td>
      <td>tube zither</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q30034781">Q30034781</a></td>
      <td>312</td>
    </tr>
  </tbody>
</table>


### With fuzzy-matching library

Using fuzzy-matching to find close instrument names:


```python
import fuzzymatcher

match = fuzzymatcher.fuzzy_left_join(
    no_links_from_mb, wd_musical_instruments[['wd', 'name']], 
    left_on='name', right_on='name')[['best_match_score', 'mbid', 
                                      'name_left', 'name_right', 'wd']]
match = match[match['best_match_score'] > 0.09].sort_values(by='best_match_score', 
                                                            ascending=False)
```


```python
display_df(match, index=False)
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>best_match_score</th>
      <th>mbid</th>
      <th>name_left</th>
      <th>name_right</th>
      <th>wd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.459847</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/e5408785-e228-4919-9e79-6f997bcdfea5">e5408785-e228-4919-9e79-6f997bcdfea5</a></td>
      <td>tube zither</td>
      <td>tube zither</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q30034781">Q30034781</a></td>
    </tr>
    <tr>
      <td>0.282946</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/3c5349ca-cf82-4537-851f-1957ac88bced">3c5349ca-cf82-4537-851f-1957ac88bced</a></td>
      <td>electric lap steel guitar</td>
      <td>Lap steel</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q94994651">Q94994651</a></td>
    </tr>
    <tr>
      <td>0.246483</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ca17a349-e0e3-4b9b-b74d-898a2b54b43e">ca17a349-e0e3-4b9b-b74d-898a2b54b43e</a></td>
      <td>syrinx</td>
      <td>syrinx</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10902606">Q10902606</a></td>
    </tr>
    <tr>
      <td>0.206346</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/e798a2bd-a578-4c28-8eea-6eca2d8b2c5d">e798a2bd-a578-4c28-8eea-6eca2d8b2c5d</a></td>
      <td>horn</td>
      <td>Horn</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q94994539">Q94994539</a></td>
    </tr>
    <tr>
      <td>0.193824</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c95c7129-d180-4218-afea-4b74ef70e2be">c95c7129-d180-4218-afea-4b74ef70e2be</a></td>
      <td>bell</td>
      <td>bell</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q101401">Q101401</a></td>
    </tr>
    <tr>
      <td>0.130599</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/872b72a2-541c-4115-b7ce-2dfed3e84884">872b72a2-541c-4115-b7ce-2dfed3e84884</a></td>
      <td>bin-sitar</td>
      <td>Sitar</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q79485179">Q79485179</a></td>
    </tr>
    <tr>
      <td>0.130280</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/371dd55f-5251-4905-a8b2-2d2acf352376">371dd55f-5251-4905-a8b2-2d2acf352376</a></td>
      <td>keyed brass instruments</td>
      <td>brass instrument</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q180744">Q180744</a></td>
    </tr>
    <tr>
      <td>0.125435</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/837c7244-ece8-47ff-b215-78f4aa4f227d">837c7244-ece8-47ff-b215-78f4aa4f227d</a></td>
      <td>treble violin</td>
      <td>Violin</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q80002939">Q80002939</a></td>
    </tr>
    <tr>
      <td>0.114376</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/e5781903-d6ef-4480-a158-60300265577c">e5781903-d6ef-4480-a158-60300265577c</a></td>
      <td>natural brass instruments</td>
      <td>brass instrument</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q180744">Q180744</a></td>
    </tr>
    <tr>
      <td>0.104660</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/7a5b3204-0200-426c-88d5-3f26a225b757">7a5b3204-0200-426c-88d5-3f26a225b757</a></td>
      <td>hmông flute</td>
      <td>flute</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q11405">Q11405</a></td>
    </tr>
    <tr>
      <td>0.104342</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/d2f041b9-b6a6-4973-badd-1b07a37192c9">d2f041b9-b6a6-4973-badd-1b07a37192c9</a></td>
      <td>valved brass instruments</td>
      <td>brass instrument</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q180744">Q180744</a></td>
    </tr>
    <tr>
      <td>0.097538</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/205acba3-c6aa-4e47-be4c-2be043cfd511">205acba3-c6aa-4e47-be4c-2be043cfd511</a></td>
      <td>plucked idiophone</td>
      <td>idiophone</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q12639">Q12639</a></td>
    </tr>
    <tr>
      <td>0.094626</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/f0ddf0ec-e8ac-4765-acef-0687af2b2f32">f0ddf0ec-e8ac-4765-acef-0687af2b2f32</a></td>
      <td>fourth flute</td>
      <td>flute</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q11405">Q11405</a></td>
    </tr>
    <tr>
      <td>0.094540</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/87d5bd6a-8d14-4ed0-befa-b90379536634">87d5bd6a-8d14-4ed0-befa-b90379536634</a></td>
      <td>nylon guitar</td>
      <td>Guitar</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q79485088">Q79485088</a></td>
    </tr>
    <tr>
      <td>0.094540</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c0ea0405-ae3f-4851-bf85-277fadff80e2">c0ea0405-ae3f-4851-bf85-277fadff80e2</a></td>
      <td>Hawaiian guitar</td>
      <td>Guitar</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q79485088">Q79485088</a></td>
    </tr>
    <tr>
      <td>0.094540</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c2bfcf82-356c-4606-9dd7-51efd1b11bec">c2bfcf82-356c-4606-9dd7-51efd1b11bec</a></td>
      <td>gut guitar</td>
      <td>Guitar</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q79485088">Q79485088</a></td>
    </tr>
    <tr>
      <td>0.091077</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/db36bd83-0606-42b9-91a0-d759ba52d0da">db36bd83-0606-42b9-91a0-d759ba52d0da</a></td>
      <td>trumpet family</td>
      <td>trumpet</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q8338">Q8338</a></td>
    </tr>
    <tr>
      <td>0.090461</td>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/2fb619eb-c5b3-495a-967a-b747b976a7d9">2fb619eb-c5b3-495a-967a-b747b976a7d9</a></td>
      <td>bowed piano</td>
      <td>piano</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5994">Q5994</a></td>
    </tr>
  </tbody>
</table>


### With record linkage library


```python
import recordlinkage

# Indexation step
indexer = recordlinkage.SortedNeighbourhoodIndex('name', window=9)
pairs = indexer.index(no_links_from_mb, wd_musical_instruments[['wd', 'name']])
print(len(pairs))

# Comparison step
compare_cl = recordlinkage.Compare()
compare_cl.string('name', 'name', method='jarowinkler', 
                  threshold=0.9, label='name')
features = compare_cl.compute(pairs, no_links_from_mb, wd_musical_instruments[['wd', 'name']])
print(features[features.sum(axis=1) > 0].shape)

# Classification step
linkage = []
for (idx0, idx1) in features[features.sum(axis=1) > 0].index:
    linkage.append([
        no_links_from_mb.loc[idx0]['mbid'],
        no_links_from_mb.loc[idx0]['name'],
        wd_musical_instruments.loc[idx1]['name'],
        wd_musical_instruments.loc[idx1]['wd'],
    ])
    
display_df(pd.DataFrame(linkage, columns=('mbid', 'name_left', 'name_right', 'wd')),
           index=False)
```

    681
    (5, 1)



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>mbid</th>
      <th>name_left</th>
      <th>name_right</th>
      <th>wd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/ca17a349-e0e3-4b9b-b74d-898a2b54b43e">ca17a349-e0e3-4b9b-b74d-898a2b54b43e</a></td>
      <td>syrinx</td>
      <td>syrinx</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10902606">Q10902606</a></td>
    </tr>
    <tr>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c95c7129-d180-4218-afea-4b74ef70e2be">c95c7129-d180-4218-afea-4b74ef70e2be</a></td>
      <td>bell</td>
      <td>bell</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q101401">Q101401</a></td>
    </tr>
    <tr>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/c95c7129-d180-4218-afea-4b74ef70e2be">c95c7129-d180-4218-afea-4b74ef70e2be</a></td>
      <td>bell</td>
      <td>bell</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q96309259">Q96309259</a></td>
    </tr>
    <tr>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/e5408785-e228-4919-9e79-6f997bcdfea5">e5408785-e228-4919-9e79-6f997bcdfea5</a></td>
      <td>tube zither</td>
      <td>tube zither</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q30034781">Q30034781</a></td>
    </tr>
    <tr>
      <td><a target="_blank" href="https://musicbrainz.org/instrument/db36bd83-0606-42b9-91a0-d759ba52d0da">db36bd83-0606-42b9-91a0-d759ba52d0da</a></td>
      <td>trumpet family</td>
      <td>trumpet</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q8338">Q8338</a></td>
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
    <title>Alignment of MusicBrainz and Wikidata Instruments</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>

  <body style="margin: 20px;">
    <h1>Alignment of MusicBrainz and Wikidata Instruments</h1>

    <p>Latest MB database update: {{ MB_DATABASE_VERSION }}</p>
    <p>Latest update: {{ date.today().isoformat() }}</p>
    
    <ol>
      <li><a href="#wd2mb">Add missing Wikidata links to MusicBrainz</a></li>
      <li><a href="#mb2wd">Add missing MusicBrainz links to Wikidata</a></li>
      <li><a href="#alignment">Missing alignment suggestions</a>
    </ol>
    
    <h2 id="wd2mb">Add missing Wikidata links to MusicBrainz</h2>
    {{ df_to_html(links_to_add_to_mb) }}

    <h2 id="mb2wd">Add missing MusicBrainz links to Wikidata</h2>
    {{ df_to_html(links_to_add_to_wd) }}

    <h2 id="alignment">Missing alignment suggestions</h2>
    
    <h3>Alignment on exact names</h3>
    {{ df_to_html(no_links_merge) }}
    
    <h3>Alignment on fuzzy matching</h3>
    {{ df_to_html(match) }}    
  
  </body>
</html>
""")

with open('../docs/wd-instruments-report.html', 'w') as f:
    f.write(template.render(**globals())
            .replace('&lt;', '<').replace('&gt;', '>')
            .replace('class="dataframe"', 'class="table table-striped table-hover table-sm"')
            .replace('thead', 'thead class="thead-light"'))
```
