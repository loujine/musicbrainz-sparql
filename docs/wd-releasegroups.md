```python
%run -i ../startup.py
ENTITY_TYPE = 'release-group'
```

    Last notebook update: 2021-01-31
    Importing libs
    Defining database parameters
    Defining *sql* helper function
    Last database update: 2021-01-13
    
    Defining *sparql* helper function


Wikidata entities:

https://www.wikidata.org/wiki/Q482994 album

Wikidata properties:

https://www.wikidata.org/wiki/Property:P175 performer

https://www.wikidata.org/wiki/Property:P214 VIAF

https://www.wikidata.org/wiki/Property:P268 BNF

https://www.wikidata.org/wiki/Property:P244 LoC

https://www.wikidata.org/wiki/Property:P1954 discogs master ID

https://www.wikidata.org/wiki/Property:P436 MusicBrainz RG ID

examples

https://www.wikidata.org/wiki/Q7713309


## Release Groups from Wikidata


```python
links_type_from_wd = sparql("""
SELECT distinct (count(?rg) as ?cnt) ?ins ?insLabel
WHERE {
  ?rg wdt:P31 ?ins;
    wdt:P436 ?mbid.
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
group by ?ins ?insLabel
order by DESC(?cnt)
""")
links_type_from_wd[links_type_from_wd.cnt.astype(int) > 50]
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
      <td>112430</td>
      <td>Q482994</td>
      <td>album</td>
    </tr>
    <tr>
      <th>1</th>
      <td>26516</td>
      <td>Q134556</td>
      <td>single</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8615</td>
      <td>Q222910</td>
      <td>compilation album</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8315</td>
      <td>Q208569</td>
      <td>studio album</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7049</td>
      <td>Q209939</td>
      <td>live album</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6706</td>
      <td>Q169930</td>
      <td>extended play</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3295</td>
      <td>Q7366</td>
      <td>song</td>
    </tr>
    <tr>
      <th>7</th>
      <td>942</td>
      <td>Q11424</td>
      <td>film</td>
    </tr>
    <tr>
      <th>8</th>
      <td>658</td>
      <td>Q4176708</td>
      <td>soundtrack album</td>
    </tr>
    <tr>
      <th>9</th>
      <td>653</td>
      <td>Q963099</td>
      <td>remix album</td>
    </tr>
    <tr>
      <th>10</th>
      <td>349</td>
      <td>Q7889</td>
      <td>video game</td>
    </tr>
    <tr>
      <th>11</th>
      <td>209</td>
      <td>Q20737336</td>
      <td>collaborative album</td>
    </tr>
    <tr>
      <th>12</th>
      <td>176</td>
      <td>Q20089094</td>
      <td>live video album</td>
    </tr>
    <tr>
      <th>13</th>
      <td>174</td>
      <td>Q723849</td>
      <td>greatest hits album</td>
    </tr>
    <tr>
      <th>14</th>
      <td>171</td>
      <td>Q2743</td>
      <td>musical theatre</td>
    </tr>
    <tr>
      <th>15</th>
      <td>165</td>
      <td>Q394970</td>
      <td>box set</td>
    </tr>
    <tr>
      <th>16</th>
      <td>121</td>
      <td>Q2619673</td>
      <td>DJ mix</td>
    </tr>
    <tr>
      <th>17</th>
      <td>110</td>
      <td>Q1242743</td>
      <td>double album</td>
    </tr>
    <tr>
      <th>18</th>
      <td>110</td>
      <td>Q1892995</td>
      <td>mixtape</td>
    </tr>
    <tr>
      <th>19</th>
      <td>91</td>
      <td>Q368281</td>
      <td>split album</td>
    </tr>
    <tr>
      <th>20</th>
      <td>86</td>
      <td>Q217199</td>
      <td>soundtrack</td>
    </tr>
    <tr>
      <th>21</th>
      <td>85</td>
      <td>Q2068728</td>
      <td>hit record</td>
    </tr>
    <tr>
      <th>22</th>
      <td>83</td>
      <td>Q207628</td>
      <td>musical composition</td>
    </tr>
    <tr>
      <th>23</th>
      <td>81</td>
      <td>Q10590726</td>
      <td>video album</td>
    </tr>
    <tr>
      <th>24</th>
      <td>76</td>
      <td>Q7302866</td>
      <td>audio track</td>
    </tr>
    <tr>
      <th>25</th>
      <td>66</td>
      <td>Q55873388</td>
      <td>Christmas-themed album</td>
    </tr>
    <tr>
      <th>26</th>
      <td>63</td>
      <td>Q7725634</td>
      <td>literary work</td>
    </tr>
    <tr>
      <th>27</th>
      <td>58</td>
      <td>Q47461344</td>
      <td>written work</td>
    </tr>
    <tr>
      <th>28</th>
      <td>57</td>
      <td>Q59854802</td>
      <td>live extended play</td>
    </tr>
    <tr>
      <th>29</th>
      <td>56</td>
      <td>Q29652773</td>
      <td>film soundtrack</td>
    </tr>
  </tbody>
</table>
</div>




```python
# linked to MB RG
links_from_wd = sparql("""
SELECT distinct (count(?rg) as ?cnt)
WHERE {
  ?rg wdt:P436 ?mbid .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
ORDER BY ASC(?rgLabel)
""")
links_from_wd
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
      <td>174974</td>
    </tr>
  </tbody>
</table>
</div>



That's too many to be fetched. Try the artists with a discogs link


```python
links_from_wd = sparql("""
SELECT distinct (count(?rg) as ?cnt)
WHERE {
  ?rg wdt:P436 ?mbid .
  ?rg wdt:P1954 ?discogs .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
""")
links_from_wd
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
      <td>95963</td>
    </tr>
  </tbody>
</table>
</div>




```python
links_from_wd = sparql("""
SELECT (?rg AS ?wd) ?mbid ?rgLabel ?discogs
WHERE {
  ?rg wdt:P436 ?mbid .
  ?rg wdt:P1954 ?discogs .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
ORDER BY ASC(?rgLabel)
""")
links_from_wd.rename(columns={'rgLabel': 'name'}, inplace=True)

print('Count:', len(links_from_wd))
display_df(links_from_wd.head())
```

    Count: 95963



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wd</th>
      <th>mbid</th>
      <th>name</th>
      <th>discogs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100701398">Q100701398</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/b88cf8ff-ac40-31a0-8722-cf7c215c27df">b88cf8ff-ac40-31a0-8722-cf7c215c27df</a></td>
      <td>Q100701398</td>
      <td><a target="_blank" href="https://discogs.com/release-group/3088228">3088228</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1009874">Q1009874</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/7280e3be-30b9-3b14-ab47-a33448916e09">7280e3be-30b9-3b14-ab47-a33448916e09</a></td>
      <td>Q1009874</td>
      <td><a target="_blank" href="https://discogs.com/release-group/632312">632312</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100998836">Q100998836</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/0c536afe-dbc4-4af7-8c6d-79899dd813f3">0c536afe-dbc4-4af7-8c6d-79899dd813f3</a></td>
      <td>Q100998836</td>
      <td><a target="_blank" href="https://discogs.com/release-group/1729268">1729268</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1016612">Q1016612</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/f19754b3-88d1-3cfe-937e-d28b560e59c5">f19754b3-88d1-3cfe-937e-d28b560e59c5</a></td>
      <td>Q1016612</td>
      <td><a target="_blank" href="https://discogs.com/release-group/517422">517422</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q102128610">Q102128610</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/818bf59a-3982-4486-97e5-8b0748c71aee">818bf59a-3982-4486-97e5-8b0748c71aee</a></td>
      <td>Q102128610</td>
      <td><a target="_blank" href="https://discogs.com/release-group/1521602">1521602</a></td>
    </tr>
  </tbody>
</table>


## Release Groups from MusicBrainz with wikidata links


```python
links_from_mb = sql("""
SELECT
    url.url AS wd,
    release_group.gid AS mbid,
    release_group.name
FROM 
    release_group
    JOIN l_release_group_url AS lau ON lau.entity0 = release_group.id
    JOIN url                 ON lau.entity1 = url.id
WHERE
    url.url LIKE '%%wikidata.org%%'
ORDER BY
    release_group.name
;
""")
links_from_mb.wd = links_from_mb.wd.apply(lambda s: s.split('/')[-1])
links_from_mb.mbid = links_from_mb.mbid.apply(str)

print('Count:', len(links_from_mb))
display_df(links_from_mb.head())
```

    Count: 115750



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q66092288">Q66092288</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/46a4376d-7fdd-416a-9b26-f38273e13f76">46a4376d-7fdd-416a-9b26-f38273e13f76</a></td>
      <td>!</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q2705922">Q2705922</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/e2e3f68e-4b21-3296-88f5-39d50f53cc72">e2e3f68e-4b21-3296-88f5-39d50f53cc72</a></td>
      <td>!!!</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q3596098">Q3596098</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/c00126c7-6b6f-3857-8f4e-8e4b2aba635c">c00126c7-6b6f-3857-8f4e-8e4b2aba635c</a></td>
      <td>!!Destroy‐Oh‐Boy!!</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5577828">Q5577828</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/3f762d15-18ba-3883-a7b4-73a0c9f39f46">3f762d15-18ba-3883-a7b4-73a0c9f39f46</a></td>
      <td>!!Going Places!!</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5037656">Q5037656</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/dcacff75-c1ed-36f9-b139-425cf2612574">dcacff75-c1ed-36f9-b139-425cf2612574</a></td>
      <td>!Caramba!</td>
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

    Count: 940



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1028031">Q1028031</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/dcd22f78-aac2-37c6-b55e-96cba448e259">dcd22f78-aac2-37c6-b55e-96cba448e259</a></td>
      <td>Driving Home for Christmas / Hello Friend (Re-Recorded)</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1028031">Q1028031</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/124f7c14-40f0-3746-9a9b-fdb74fd5387b">124f7c14-40f0-3746-9a9b-fdb74fd5387b</a></td>
      <td>Driving Home for Christmas: The Christmas EP</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1028055">Q1028055</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/7f697ec7-d422-3690-9788-f837dce3777e">7f697ec7-d422-3690-9788-f837dce3777e</a></td>
      <td>Greatest Hits</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1028055">Q1028055</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/5410586d-698c-38cc-b26f-b61577f4c32d">5410586d-698c-38cc-b26f-b61577f4c32d</a></td>
      <td>Greatest Hits</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10280819">Q10280819</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/cb4d06c2-94fc-3e75-9ee7-1d4a9182e044">cb4d06c2-94fc-3e75-9ee7-1d4a9182e044</a></td>
      <td>Feijoada acidente? - Brasil</td>
    </tr>
  </tbody>
</table>



```python
duplicate_mb = links_from_mb[['wd', 'mbid', 'name']].groupby('mbid').filter(
    lambda row: len(row.mbid) > 1).sort_values('mbid')

print('Count:', len(duplicate_mb))
display_df(duplicate_mb.head())
```

    Count: 185



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q69715896">Q69715896</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/0402ea05-c920-30c3-9559-94a6ebd783a3">0402ea05-c920-30c3-9559-94a6ebd783a3</a></td>
      <td>My Generation</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q69709269">Q69709269</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/0402ea05-c920-30c3-9559-94a6ebd783a3">0402ea05-c920-30c3-9559-94a6ebd783a3</a></td>
      <td>My Generation</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q15971649">Q15971649</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/05c9b920-d313-3220-b997-f8ed16ebeaae">05c9b920-d313-3220-b997-f8ed16ebeaae</a></td>
      <td>17: Greatest Hits</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q565500">Q565500</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/05c9b920-d313-3220-b997-f8ed16ebeaae">05c9b920-d313-3220-b997-f8ed16ebeaae</a></td>
      <td>17: Greatest Hits</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q9363343">Q9363343</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/0a11885b-3fcf-3d41-9e54-2f16582190af">0a11885b-3fcf-3d41-9e54-2f16582190af</a></td>
      <td>Zmierzch Bogów</td>
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
      <th>discogs</th>
      <th>name_mb</th>
      <th>_merge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100701398">Q100701398</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/b88cf8ff-ac40-31a0-8722-cf7c215c27df">b88cf8ff-ac40-31a0-8722-cf7c215c27df</a></td>
      <td>Q100701398</td>
      <td><a target="_blank" href="https://discogs.com/release-group/3088228">3088228</a></td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1009874">Q1009874</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/7280e3be-30b9-3b14-ab47-a33448916e09">7280e3be-30b9-3b14-ab47-a33448916e09</a></td>
      <td>Q1009874</td>
      <td><a target="_blank" href="https://discogs.com/release-group/632312">632312</a></td>
      <td>Bunte Scherben</td>
      <td>both</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100998836">Q100998836</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/0c536afe-dbc4-4af7-8c6d-79899dd813f3">0c536afe-dbc4-4af7-8c6d-79899dd813f3</a></td>
      <td>Q100998836</td>
      <td><a target="_blank" href="https://discogs.com/release-group/1729268">1729268</a></td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1016612">Q1016612</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/f19754b3-88d1-3cfe-937e-d28b560e59c5">f19754b3-88d1-3cfe-937e-d28b560e59c5</a></td>
      <td>Q1016612</td>
      <td><a target="_blank" href="https://discogs.com/release-group/517422">517422</a></td>
      <td>Burli</td>
      <td>both</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q102128610">Q102128610</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/818bf59a-3982-4486-97e5-8b0748c71aee">818bf59a-3982-4486-97e5-8b0748c71aee</a></td>
      <td>Q102128610</td>
      <td><a target="_blank" href="https://discogs.com/release-group/1521602">1521602</a></td>
      <td>NaN</td>
      <td>left_only</td>
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

    Count: 51875



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
      <td>!</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/46a4376d-7fdd-416a-9b26-f38273e13f76">46a4376d-7fdd-416a-9b26-f38273e13f76</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q66092288">Q66092288</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>"... The Truth Is a Fucking Lie..."</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/63451c2c-c39d-3d30-b7e2-c6608708db4d">63451c2c-c39d-3d30-b7e2-c6608708db4d</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q13416956">Q13416956</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td>"10"</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/0cc5b1f4-6df9-35df-becf-cb7e954eb893">0cc5b1f4-6df9-35df-becf-cb7e954eb893</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q184591">Q184591</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td>"77"</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/180f5161-23f7-49a0-beec-09555d4a654e">180f5161-23f7-49a0-beec-09555d4a654e</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q11880947">Q11880947</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td>"A" e o "Z"</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/5baebed3-fcab-30ec-8eda-1eccf5921b22">5baebed3-fcab-30ec-8eda-1eccf5921b22</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q3285394">Q3285394</a></td>
    </tr>
  </tbody>
</table>



```python
# link in wd but missing in mb
links_to_add_to_mb = merge.loc[lambda x : x['_merge']=='left_only'][[
    'name_wd', 'wd', 'mbid']]
links_to_add_to_mb['edit_link'] = links_to_add_to_mb.apply(
    mb_artist_edit_wd_link, axis=1)

print('Count:', len(links_to_add_to_mb))
display_df(links_to_add_to_mb.head())
```

    Count: 32046



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
      <td>Q100701398</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100701398">Q100701398</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/b88cf8ff-ac40-31a0-8722-cf7c215c27df">b88cf8ff-ac40-31a0-8722-cf7c215c27df</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/b88cf8ff-ac40-31a0-8722-cf7c215c27df/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q100701398">edit</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>Q100998836</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100998836">Q100998836</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/0c536afe-dbc4-4af7-8c6d-79899dd813f3">0c536afe-dbc4-4af7-8c6d-79899dd813f3</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/0c536afe-dbc4-4af7-8c6d-79899dd813f3/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q100998836">edit</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td>Q102128610</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q102128610">Q102128610</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/818bf59a-3982-4486-97e5-8b0748c71aee">818bf59a-3982-4486-97e5-8b0748c71aee</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/818bf59a-3982-4486-97e5-8b0748c71aee/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q102128610">edit</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td>Q10217180</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10217180">Q10217180</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/307af7b8-67ef-38a4-95df-cc366ef636b6">307af7b8-67ef-38a4-95df-cc366ef636b6</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/307af7b8-67ef-38a4-95df-cc366ef636b6/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q10217180">edit</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td>Q102338667</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q102338667">Q102338667</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/d95a18d0-af86-367f-bf31-8b43abc0c824">d95a18d0-af86-367f-bf31-8b43abc0c824</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/d95a18d0-af86-367f-bf31-8b43abc0c824/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q102338667">edit</a></td>
    </tr>
  </tbody>
</table>


## Data alignment through Discogs

TBD on wd entries with discogs links and no mb link


```python
# linked to Discogs master
discogs_links_from_wd = sparql("""
SELECT (?rg AS ?wd) ?rgLabel ?discogs
WHERE {
  ?rg wdt:P1954 ?discogs .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
  MINUS {
    ?rg wdt:P436 ?mbid .  
  }
}
ORDER BY ASC(?rgLabel)
""")
discogs_links_from_wd.rename(columns={'rgLabel': 'name'}, inplace=True)

print('Count:', len(discogs_links_from_wd))
display_df(discogs_links_from_wd.head())
```

    Count: 24444



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wd</th>
      <th>name</th>
      <th>discogs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100251747">Q100251747</a></td>
      <td>Q100251747</td>
      <td><a target="_blank" href="https://discogs.com/release-group/893897">893897</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100300673">Q100300673</a></td>
      <td>Q100300673</td>
      <td><a target="_blank" href="https://discogs.com/release-group/1150563">1150563</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100316840">Q100316840</a></td>
      <td>Q100316840</td>
      <td><a target="_blank" href="https://discogs.com/release-group/6530510">6530510</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100342804">Q100342804</a></td>
      <td>Q100342804</td>
      <td><a target="_blank" href="https://discogs.com/release-group/1108665">1108665</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100378070">Q100378070</a></td>
      <td>Q100378070</td>
      <td><a target="_blank" href="https://discogs.com/release-group/275211">275211</a></td>
    </tr>
  </tbody>
</table>



```python
discogs_links_from_mb = sql("""
SELECT
    url.url AS discogs,
    release_group.gid AS mbid,
    release_group.name
FROM 
    release_group
    JOIN l_release_group_url AS lau ON lau.entity0 = release_group.id
    JOIN url                 ON lau.entity1 = url.id
WHERE
    url.url LIKE '%%discogs.com%%'
    AND lau.entity0 IN (
        SELECT
            entity0
        FROM 
            l_release_group_url
            JOIN url ON l_release_group_url.entity1 = url.id
        WHERE
            url.url LIKE '%%discogs.com%%'
    EXCEPT
        SELECT
            entity0
        FROM 
            l_release_group_url
            JOIN url ON l_release_group_url.entity1 = url.id
        WHERE
            url.url LIKE '%%wikidata.org%%'
    )
ORDER BY
    release_group.name
;
""")
discogs_links_from_mb.discogs = discogs_links_from_mb.discogs.apply(lambda s: s.split('/')[-1])
discogs_links_from_mb.mbid = discogs_links_from_mb.mbid.apply(str)

print('Count:', len(discogs_links_from_mb))
display_df(discogs_links_from_mb.head())
```

    Count: 171673



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>discogs</th>
      <th>mbid</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://discogs.com/release-group/1784550">1784550</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/dae13e8a-0d21-4151-a492-f4ec39394d81">dae13e8a-0d21-4151-a492-f4ec39394d81</a></td>
      <td>!</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://discogs.com/release-group/1793473">1793473</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/16c05add-e78e-40ee-a809-6b68a5d7d664">16c05add-e78e-40ee-a809-6b68a5d7d664</a></td>
      <td>!!</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://discogs.com/release-group/427086">427086</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/6f319a03-20ac-33c8-98a0-1ef746e78d04">6f319a03-20ac-33c8-98a0-1ef746e78d04</a></td>
      <td>!!</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://discogs.com/release-group/321441">321441</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/4cd7ca7e-d8fd-3cdb-a9c7-1caef23deab1">4cd7ca7e-d8fd-3cdb-a9c7-1caef23deab1</a></td>
      <td>!!!Here Ain't the Sonics!!!</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://discogs.com/release-group/136546">136546</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/eae71c65-4b63-4ea8-a759-40f190ba67f6">eae71c65-4b63-4ea8-a759-40f190ba67f6</a></td>
      <td>!Catch the Beat! / !Catch the Groove!</td>
    </tr>
  </tbody>
</table>



```python
discogs_merge = pd.merge(discogs_links_from_wd, discogs_links_from_mb, 
                 on=['discogs'], suffixes=('_wd', '_mb'),
                 how='inner', indicator=False)
discogs_merge['edit_link'] = discogs_merge.apply(
    mb_releasegroup_edit_wd_link, axis=1)

print('Count:', len(discogs_merge))
display_df(discogs_merge.head())
```

    Count: 3317



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wd</th>
      <th>name_wd</th>
      <th>discogs</th>
      <th>mbid</th>
      <th>name_mb</th>
      <th>edit_link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q101480010">Q101480010</a></td>
      <td>Q101480010</td>
      <td><a target="_blank" href="https://discogs.com/master/322472">322472</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/1d27dcca-2980-47bc-b358-a3c038bfb90d">1d27dcca-2980-47bc-b358-a3c038bfb90d</a></td>
      <td>La convenzione / Paranoia</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/1d27dcca-2980-47bc-b358-a3c038bfb90d/edit?edit-release-group.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-release-group.url.99.text=https://www.wikidata.org/wiki/Q101480010">edit</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q101510523">Q101510523</a></td>
      <td>Q101510523</td>
      <td><a target="_blank" href="https://discogs.com/master/768022">768022</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/4eba0184-9340-4fde-b1c3-b243bc75a418">4eba0184-9340-4fde-b1c3-b243bc75a418</a></td>
      <td>L'era del cinghiale bianco / Luna indiana</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/4eba0184-9340-4fde-b1c3-b243bc75a418/edit?edit-release-group.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-release-group.url.99.text=https://www.wikidata.org/wiki/Q101510523">edit</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q102350795">Q102350795</a></td>
      <td>Q102350795</td>
      <td><a target="_blank" href="https://discogs.com/master/563853">563853</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/a974458d-f876-443f-b501-f7aec0e416b8">a974458d-f876-443f-b501-f7aec0e416b8</a></td>
      <td>Big Big Hits of '62</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/a974458d-f876-443f-b501-f7aec0e416b8/edit?edit-release-group.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-release-group.url.99.text=https://www.wikidata.org/wiki/Q102350795">edit</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10278713">Q10278713</a></td>
      <td>Q10278713</td>
      <td><a target="_blank" href="https://discogs.com/master/334266">334266</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/42dc40f6-f27c-47ef-8d09-58e941046fa1">42dc40f6-f27c-47ef-8d09-58e941046fa1</a></td>
      <td>Explode</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/42dc40f6-f27c-47ef-8d09-58e941046fa1/edit?edit-release-group.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-release-group.url.99.text=https://www.wikidata.org/wiki/Q10278713">edit</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10282621">Q10282621</a></td>
      <td>Q10282621</td>
      <td><a target="_blank" href="https://discogs.com/master/293281">293281</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/f619677a-e20a-38cd-ae74-09ef523f097d">f619677a-e20a-38cd-ae74-09ef523f097d</a></td>
      <td>First / Second</td>
      <td><a target="_blank" href="https://musicbrainz.org/release-group/f619677a-e20a-38cd-ae74-09ef523f097d/edit?edit-release-group.url.99.type=b988d08c-5d86-4a57-9557-c83b399e3580&edit-release-group.url.99.text=https://www.wikidata.org/wiki/Q10282621">edit</a></td>
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
    <title>Alignment of MusicBrainz and Wikidata Release Groups</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>

  <body style="margin: 20px;">
    <h1>Alignment of MusicBrainz and Wikidata Release Groups</h1>

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
        <a href="#discogs2mb">Add missing Wikidata links to MusicBrainz (through Discogs)</a>
        ({{ discogs_merge.shape[0] }} rows)
      </li>
      <li>
        <a href="#mb2wd">Add missing MusicBrainz links to Wikidata</a>
      </li>
    </ol>
    
    <h2 id="wddup">MusicBrainz entities sharing a Wikidata link</h2>
    {{ df_to_html(duplicate_wd) }}

    <h2 id="mbdup">Wikidata entities sharing a MusicBrainz link</h2>
    {{ df_to_html(duplicate_mb) }}

    <h2 id="wd2mb">Add missing Wikidata links to MusicBrainz</h2>
    {{ df_to_html(links_to_add_to_mb) }}

    <h2 id="discogs2mb">Add missing Wikidata links to MusicBrainz (through Discogs)</h2>
    {{ df_to_html(discogs_merge) }}

    <h2 id="mb2wd">Add missing MusicBrainz links to Wikidata</h2>
    
  </body>
</html>
""")

with open('../docs/wd-releasegroups-report.html', 'w') as f:
    f.write(template.render(**globals())
            .replace('&lt;', '<').replace('&gt;', '>')
            .replace('class="dataframe"', 'class="table table-striped table-hover table-sm"')
            .replace('thead', 'thead class="thead-light"'))
```
