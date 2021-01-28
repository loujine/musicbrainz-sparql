# Alignment of MusicBrainz and Wikidata Record Labels


```python
%run -i ../startup.py
import numpy as np
ENTITY_TYPE = 'label'
```

    Last notebook update: 2021-01-28
    Importing libs
    Defining database parameters
    Defining *sql* helper function
    Last database update: 2021-01-13
    
    Defining *sparql* helper function


Wikidata entities:

https://www.wikidata.org/wiki/Q18127 record label

Wikidata properties:

https://www.wikidata.org/wiki/Property:P214 VIAF

https://www.wikidata.org/wiki/Property:P268 BNF

https://www.wikidata.org/wiki/Property:P244 LoC

https://www.wikidata.org/wiki/Property:P1955 discogs ID

https://www.wikidata.org/wiki/Property:P966 MusicBrainz label ID

examples

https://www.wikidata.org/wiki/Q885833


## Record labels from Wikidata


```python
links_type_from_wd = sparql("""
SELECT distinct (count(?label) as ?cnt) ?ins ?insLabel
WHERE {
  ?label wdt:P31 ?ins;
    wdt:P966 ?mbid.
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
      <td>5310</td>
      <td>Q18127</td>
      <td>record label</td>
    </tr>
    <tr>
      <th>1</th>
      <td>766</td>
      <td>Q4830453</td>
      <td>business</td>
    </tr>
    <tr>
      <th>2</th>
      <td>340</td>
      <td>Q2442401</td>
      <td>record company</td>
    </tr>
    <tr>
      <th>3</th>
      <td>282</td>
      <td>Q1542343</td>
      <td>independent record label</td>
    </tr>
    <tr>
      <th>4</th>
      <td>174</td>
      <td>Q2608849</td>
      <td>imprint</td>
    </tr>
    <tr>
      <th>5</th>
      <td>164</td>
      <td>Q6881511</td>
      <td>enterprise</td>
    </tr>
    <tr>
      <th>6</th>
      <td>158</td>
      <td>Q2085381</td>
      <td>publisher</td>
    </tr>
    <tr>
      <th>7</th>
      <td>144</td>
      <td>Q210167</td>
      <td>video game developer</td>
    </tr>
    <tr>
      <th>8</th>
      <td>114</td>
      <td>Q5354754</td>
      <td>talent agency</td>
    </tr>
    <tr>
      <th>9</th>
      <td>102</td>
      <td>Q41298</td>
      <td>magazine</td>
    </tr>
    <tr>
      <th>10</th>
      <td>95</td>
      <td>Q658255</td>
      <td>subsidiary</td>
    </tr>
    <tr>
      <th>11</th>
      <td>90</td>
      <td>Q1917775</td>
      <td>music publishing company</td>
    </tr>
    <tr>
      <th>12</th>
      <td>82</td>
      <td>Q1320047</td>
      <td>book publisher</td>
    </tr>
    <tr>
      <th>13</th>
      <td>80</td>
      <td>Q43229</td>
      <td>organization</td>
    </tr>
    <tr>
      <th>14</th>
      <td>54</td>
      <td>Q783794</td>
      <td>company</td>
    </tr>
    <tr>
      <th>15</th>
      <td>52</td>
      <td>Q1137109</td>
      <td>video game publisher</td>
    </tr>
    <tr>
      <th>16</th>
      <td>43</td>
      <td>Q14350</td>
      <td>radio station</td>
    </tr>
    <tr>
      <th>17</th>
      <td>41</td>
      <td>Q1762059</td>
      <td>film production company</td>
    </tr>
    <tr>
      <th>18</th>
      <td>33</td>
      <td>Q1047437</td>
      <td>copyright collective</td>
    </tr>
    <tr>
      <th>19</th>
      <td>31</td>
      <td>Q35127</td>
      <td>website</td>
    </tr>
    <tr>
      <th>20</th>
      <td>30</td>
      <td>Q167270</td>
      <td>trademark</td>
    </tr>
    <tr>
      <th>21</th>
      <td>26</td>
      <td>Q12540664</td>
      <td>distributor</td>
    </tr>
    <tr>
      <th>22</th>
      <td>26</td>
      <td>Q20739124</td>
      <td>entertainment company</td>
    </tr>
    <tr>
      <th>23</th>
      <td>25</td>
      <td>Q219577</td>
      <td>holding company</td>
    </tr>
    <tr>
      <th>24</th>
      <td>22</td>
      <td>Q1616075</td>
      <td>television station</td>
    </tr>
    <tr>
      <th>25</th>
      <td>21</td>
      <td>Q1107679</td>
      <td>animation studio</td>
    </tr>
    <tr>
      <th>26</th>
      <td>21</td>
      <td>Q1002697</td>
      <td>periodical</td>
    </tr>
    <tr>
      <th>27</th>
      <td>18</td>
      <td>Q3719391</td>
      <td>sheet music publisher</td>
    </tr>
    <tr>
      <th>28</th>
      <td>18</td>
      <td>Q163740</td>
      <td>nonprofit organization</td>
    </tr>
    <tr>
      <th>29</th>
      <td>17</td>
      <td>Q15265344</td>
      <td>broadcaster</td>
    </tr>
    <tr>
      <th>30</th>
      <td>17</td>
      <td>Q215380</td>
      <td>musical group</td>
    </tr>
    <tr>
      <th>31</th>
      <td>17</td>
      <td>Q11032</td>
      <td>newspaper</td>
    </tr>
    <tr>
      <th>32</th>
      <td>16</td>
      <td>Q1110794</td>
      <td>daily newspaper</td>
    </tr>
    <tr>
      <th>33</th>
      <td>16</td>
      <td>Q708676</td>
      <td>charitable organization</td>
    </tr>
    <tr>
      <th>34</th>
      <td>16</td>
      <td>Q32178211</td>
      <td>music organization</td>
    </tr>
    <tr>
      <th>35</th>
      <td>15</td>
      <td>Q1824338</td>
      <td>music magazine</td>
    </tr>
    <tr>
      <th>36</th>
      <td>14</td>
      <td>Q10689397</td>
      <td>television production company</td>
    </tr>
    <tr>
      <th>37</th>
      <td>14</td>
      <td>Q726870</td>
      <td>brick and mortar</td>
    </tr>
    <tr>
      <th>38</th>
      <td>14</td>
      <td>Q778575</td>
      <td>conglomerate</td>
    </tr>
    <tr>
      <th>39</th>
      <td>13</td>
      <td>Q2001305</td>
      <td>television channel</td>
    </tr>
    <tr>
      <th>40</th>
      <td>12</td>
      <td>Q1802587</td>
      <td>German public state broadcaster</td>
    </tr>
    <tr>
      <th>41</th>
      <td>12</td>
      <td>Q431289</td>
      <td>brand</td>
    </tr>
    <tr>
      <th>42</th>
      <td>12</td>
      <td>Q1331793</td>
      <td>media company</td>
    </tr>
    <tr>
      <th>43</th>
      <td>12</td>
      <td>Q1001388</td>
      <td>budget label</td>
    </tr>
    <tr>
      <th>44</th>
      <td>11</td>
      <td>Q2243978</td>
      <td>record shop</td>
    </tr>
    <tr>
      <th>45</th>
      <td>11</td>
      <td>Q1589009</td>
      <td>privately held company</td>
    </tr>
    <tr>
      <th>46</th>
      <td>11</td>
      <td>Q1660312</td>
      <td>major label</td>
    </tr>
  </tbody>
</table>
</div>




```python
# linked to MB label
links_from_wd = sparql("""
SELECT (?label AS ?wd) ?mbid ?labelLabel ?lc ?viaf ?discogs
WHERE {
  ?label wdt:P966 ?mbid .
  OPTIONAL { ?label wdt:P7320 ?lc . }
#  OPTIONAL { ?label wdt:P214 ?viaf . }
#  OPTIONAL { ?label wdt:P1955 ?discogs . }
#  OPTIONAL { ?label wdt:P268 ?bnf . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
ORDER BY ASC(?labelLabel)
""")
links_from_wd.rename(columns={'labelLabel': 'name'}, inplace=True)
links_from_wd.lc = links_from_wd.lc.apply(
    lambda lc: lc if isinstance(lc, str) else '')
#links_from_wd.discogs = links_from_wd.discogs.apply(
#    lambda discogs: discogs if isinstance(discogs, str) else '')

print('Count:', len(links_from_wd))
display_df(links_from_wd.head())
```

    Count: 7771



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wd</th>
      <th>mbid</th>
      <th>name</th>
      <th>lc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1017332">Q1017332</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/fc9526f3-dded-4ce5-8138-b8011c9d3bd2">fc9526f3-dded-4ce5-8138-b8011c9d3bd2</a></td>
      <td>Q1017332</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q102226212">Q102226212</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/d927bbc7-5db0-44cc-9b3f-efde37850194">d927bbc7-5db0-44cc-9b3f-efde37850194</a></td>
      <td>Q102226212</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q102276807">Q102276807</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/af5e3a19-b40b-4269-b15b-9cb2686fde43">af5e3a19-b40b-4269-b15b-9cb2686fde43</a></td>
      <td>Q102276807</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10316316">Q10316316</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/1b4f4f26-37e5-4e19-be79-3515c9ce5961">1b4f4f26-37e5-4e19-be79-3515c9ce5961</a></td>
      <td>Q10316316</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10316316">Q10316316</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/a32f2beb-5297-4f3e-b0b4-d42ddbbf9a2b">a32f2beb-5297-4f3e-b0b4-d42ddbbf9a2b</a></td>
      <td>Q10316316</td>
      <td></td>
    </tr>
  </tbody>
</table>


## Labels from MusicBrainz with wikidata links


```python
links_from_mb = sql("""
SELECT
    url.url AS wd,
    label.gid AS mbid,
    label.name,
    label.label_code AS lc
FROM 
    label
    JOIN l_label_url AS llu ON llu.entity0 = label.id
    JOIN url                ON llu.entity1 = url.id
WHERE
    url.url LIKE '%%wikidata.org%%'
ORDER BY
    label.name
;
""")
links_from_mb.wd = links_from_mb.wd.apply(lambda s: s.split('/')[-1])
links_from_mb.mbid = links_from_mb.mbid.apply(str)
links_from_mb.lc = links_from_mb.lc.apply(
    lambda lc: '' if np.isnan(lc) else str(int(lc)))

print('Count:', len(links_from_mb))
display_df(links_from_mb.head())
```

    Count: 7033



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wd</th>
      <th>mbid</th>
      <th>name</th>
      <th>lc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q315760">Q315760</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/893364ff-1830-4694-833d-93751f14f984">893364ff-1830-4694-833d-93751f14f984</a></td>
      <td>!K7</td>
      <td>7306</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4544982">Q4544982</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/becff808-7fa6-4f85-ab15-0444bca5d04c">becff808-7fa6-4f85-ab15-0444bca5d04c</a></td>
      <td>+1 Records</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q58209721">Q58209721</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/3129e8bf-cd5c-428d-b79a-51f77445a3f9">3129e8bf-cd5c-428d-b79a-51f77445a3f9</a></td>
      <td>1 Numara Plakçılık</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4545734">Q4545734</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/7441004d-1165-4c04-b029-7c8d59c5912a">7441004d-1165-4c04-b029-7c8d59c5912a</a></td>
      <td>1-2-3-4 Go! Records</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q3983384">Q3983384</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/5a8514dd-22d2-4def-a48d-3a8b71a8e24f">5a8514dd-22d2-4def-a48d-3a8b71a8e24f</a></td>
      <td>10 Records</td>
      <td>3098</td>
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

    Count: 622



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1011446">Q1011446</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/2f8b7a22-70c3-457c-bb57-194236f9435e">2f8b7a22-70c3-457c-bb57-194236f9435e</a></td>
      <td>Gold Record</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1011446">Q1011446</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/3737052c-6104-4c0c-9fff-cab022fc8800">3737052c-6104-4c0c-9fff-cab022fc8800</a></td>
      <td>Gold Record</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10263636">Q10263636</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/6ca8e712-4a92-4f9a-b180-16bd7d157176">6ca8e712-4a92-4f9a-b180-16bd7d157176</a></td>
      <td>Dance World Attack</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10263636">Q10263636</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/bd0487d9-1740-4426-8740-85a7a2375c33">bd0487d9-1740-4426-8740-85a7a2375c33</a></td>
      <td>DWA (Dance World Attack)</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10290705">Q10290705</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/d2e62ad3-2530-4322-9e72-0d3830aaee82">d2e62ad3-2530-4322-9e72-0d3830aaee82</a></td>
      <td>Gospel Records</td>
    </tr>
  </tbody>
</table>



```python
duplicate_mb = links_from_mb[['wd', 'mbid', 'name']].groupby('mbid').filter(
    lambda row: len(row.mbid) > 1).sort_values('mbid')

print('Count:', len(duplicate_mb))
display_df(duplicate_mb.head())
```

    Count: 18



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q50021153">Q50021153</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/158b407e-26d7-48d9-b6ba-639861e1bffc">158b407e-26d7-48d9-b6ba-639861e1bffc</a></td>
      <td>Zafiro</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q50020430">Q50020430</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/158b407e-26d7-48d9-b6ba-639861e1bffc">158b407e-26d7-48d9-b6ba-639861e1bffc</a></td>
      <td>Zafiro</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q55908907">Q55908907</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/1ff104ed-0536-4dfd-b3f4-2b053ea66f32">1ff104ed-0536-4dfd-b3f4-2b053ea66f32</a></td>
      <td>Capitol Records Nashville</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q5035920">Q5035920</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/1ff104ed-0536-4dfd-b3f4-2b053ea66f32">1ff104ed-0536-4dfd-b3f4-2b053ea66f32</a></td>
      <td>Capitol Records Nashville</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q8602939">Q8602939</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/5b34c929-fd09-4b57-a8bf-1e8eb0f21c12">5b34c929-fd09-4b57-a8bf-1e8eb0f21c12</a></td>
      <td>Lost Highway Records</td>
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
      <th>lc_wd</th>
      <th>name_mb</th>
      <th>lc_mb</th>
      <th>_merge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1017332">Q1017332</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/fc9526f3-dded-4ce5-8138-b8011c9d3bd2">fc9526f3-dded-4ce5-8138-b8011c9d3bd2</a></td>
      <td>Q1017332</td>
      <td></td>
      <td>BuschFunk</td>
      <td>6312</td>
      <td>both</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q102226212">Q102226212</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/d927bbc7-5db0-44cc-9b3f-efde37850194">d927bbc7-5db0-44cc-9b3f-efde37850194</a></td>
      <td>Q102226212</td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q102276807">Q102276807</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/af5e3a19-b40b-4269-b15b-9cb2686fde43">af5e3a19-b40b-4269-b15b-9cb2686fde43</a></td>
      <td>Q102276807</td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10316316">Q10316316</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/1b4f4f26-37e5-4e19-be79-3515c9ce5961">1b4f4f26-37e5-4e19-be79-3515c9ce5961</a></td>
      <td>Q10316316</td>
      <td></td>
      <td>星光唱片</td>
      <td></td>
      <td>both</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10316316">Q10316316</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/a32f2beb-5297-4f3e-b0b4-d42ddbbf9a2b">a32f2beb-5297-4f3e-b0b4-d42ddbbf9a2b</a></td>
      <td>Q10316316</td>
      <td></td>
      <td>Star Records Ltd.</td>
      <td></td>
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

    Count: 589



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
      <td>125</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/13b6890a-0b41-4271-9f18-51d2f344cb2c">13b6890a-0b41-4271-9f18-51d2f344cb2c</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4548425">Q4548425</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>20|20|20</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/b1a86e1f-02c7-42c4-a741-fd3fd6e1c1a1">b1a86e1f-02c7-42c4-a741-fd3fd6e1c1a1</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q98226934">Q98226934</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td>3517 Records</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/3032dfb9-6bbc-4baa-8819-62d2bff7bc84">3032dfb9-6bbc-4baa-8819-62d2bff7bc84</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q96515410">Q96515410</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td>407 Records</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/4e61e8b0-7328-4e78-a663-a2d5bfbd0d17">4e61e8b0-7328-4e78-a663-a2d5bfbd0d17</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q63133237">Q63133237</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td>50/50innertainment</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/1bd94d7c-0dd4-45a5-824c-dd434d36fd32">1bd94d7c-0dd4-45a5-824c-dd434d36fd32</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q23055027">Q23055027</a></td>
    </tr>
  </tbody>
</table>



```python
# link in wd but missing in mb
links_to_add_to_mb = merge.loc[lambda x : x['_merge']=='left_only'][[
    'name_wd', 'wd', 'mbid']]
links_to_add_to_mb['edit_link'] = links_to_add_to_mb.apply(
    mb_label_edit_wd_link, axis=1)

print('Count:', len(links_to_add_to_mb))
display_df(links_to_add_to_mb.head())
```

    Count: 1328



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
      <td>Q102226212</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q102226212">Q102226212</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/d927bbc7-5db0-44cc-9b3f-efde37850194">d927bbc7-5db0-44cc-9b3f-efde37850194</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/d927bbc7-5db0-44cc-9b3f-efde37850194/edit?edit-label.url.99.type=75d87e83-d927-4580-ba63-44dc76256f98&edit-label.url.99.text=https://www.wikidata.org/wiki/Q102226212">edit</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>Q102276807</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q102276807">Q102276807</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/af5e3a19-b40b-4269-b15b-9cb2686fde43">af5e3a19-b40b-4269-b15b-9cb2686fde43</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/af5e3a19-b40b-4269-b15b-9cb2686fde43/edit?edit-label.url.99.type=75d87e83-d927-4580-ba63-44dc76256f98&edit-label.url.99.text=https://www.wikidata.org/wiki/Q102276807">edit</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td>Q10564076</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q10564076">Q10564076</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/14bfabf3-2cab-4f74-bac5-52c8ccce7b47">14bfabf3-2cab-4f74-bac5-52c8ccce7b47</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/14bfabf3-2cab-4f74-bac5-52c8ccce7b47/edit?edit-label.url.99.type=75d87e83-d927-4580-ba63-44dc76256f98&edit-label.url.99.text=https://www.wikidata.org/wiki/Q10564076">edit</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td>Q11175283</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q11175283">Q11175283</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/33ccae50-a5a4-46bc-85ec-f65e111e56e8">33ccae50-a5a4-46bc-85ec-f65e111e56e8</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/33ccae50-a5a4-46bc-85ec-f65e111e56e8/edit?edit-label.url.99.type=75d87e83-d927-4580-ba63-44dc76256f98&edit-label.url.99.text=https://www.wikidata.org/wiki/Q11175283">edit</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td>Q11284795</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q11284795">Q11284795</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/8c24cbcc-ff67-4f21-8b1f-6daa5366e54a">8c24cbcc-ff67-4f21-8b1f-6daa5366e54a</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/8c24cbcc-ff67-4f21-8b1f-6daa5366e54a/edit?edit-label.url.99.type=75d87e83-d927-4580-ba63-44dc76256f98&edit-label.url.99.text=https://www.wikidata.org/wiki/Q11284795">edit</a></td>
    </tr>
  </tbody>
</table>


Example:
https://musicbrainz.org/label/85bb6180-ac99-46b5-a3ec-92967e88f842 is not linked to https://www.wikidata.org/wiki/Q56809543

https://musicbrainz.org/label/86e1fce2-a61e-4d08-9d4f-b91d602f995b is linked to https://www.wikidata.org/wiki/Q24950167 that was removed in https://www.wikidata.org/w/index.php?title=Special:Log&logid=661147435

https://musicbrainz.org/label/69de915d-e7b5-4739-bd21-2de1099a0610 is linked to https://www.wikidata.org/wiki/Q4146440 and not the opposite

### Add missing Label Codes


```python
lc_to_add_to_mb = merge.loc[
    (merge._merge=='both') & (merge.lc_mb == '') & (merge.lc_wd != '')
][['mbid', 'wd', 'lc_wd']].sort_values(by='lc_wd')
lc_to_add_to_mb['edit_link'] = lc_to_add_to_mb.apply(
    mb_label_edit_lc_link, axis=1)

print('Count:', len(lc_to_add_to_mb))
display_df(lc_to_add_to_mb)
```

    Count: 20



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mbid</th>
      <th>wd</th>
      <th>lc_wd</th>
      <th>edit_link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/81f4e3cc-0dfd-47e9-8caa-2ae80e5cb496">81f4e3cc-0dfd-47e9-8caa-2ae80e5cb496</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q726251">Q726251</a></td>
      <td>00192</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/81f4e3cc-0dfd-47e9-8caa-2ae80e5cb496/edit?edit-label.label_code=00192">edit</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/2baaef8d-d357-408e-8dfe-e7ff0e569969">2baaef8d-d357-408e-8dfe-e7ff0e569969</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q935090">Q935090</a></td>
      <td>00253</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/2baaef8d-d357-408e-8dfe-e7ff0e569969/edit?edit-label.label_code=00253">edit</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/48e00f72-583c-4fbc-babb-31cd6c42a11c">48e00f72-583c-4fbc-babb-31cd6c42a11c</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q89683651">Q89683651</a></td>
      <td>00896</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/48e00f72-583c-4fbc-babb-31cd6c42a11c/edit?edit-label.label_code=00896">edit</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/d97da6f0-c0ba-4a60-8fd5-fb8edab24d32">d97da6f0-c0ba-4a60-8fd5-fb8edab24d32</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q2998569">Q2998569</a></td>
      <td>01078</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/d97da6f0-c0ba-4a60-8fd5-fb8edab24d32/edit?edit-label.label_code=01078">edit</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/053e37d6-0374-4ae7-bbe2-cf4472f6e22b">053e37d6-0374-4ae7-bbe2-cf4472f6e22b</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q937185">Q937185</a></td>
      <td>01181</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/053e37d6-0374-4ae7-bbe2-cf4472f6e22b/edit?edit-label.label_code=01181">edit</a></td>
    </tr>
    <tr>
      <th>5</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/158b407e-26d7-48d9-b6ba-639861e1bffc">158b407e-26d7-48d9-b6ba-639861e1bffc</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q50021153">Q50021153</a></td>
      <td>01619</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/158b407e-26d7-48d9-b6ba-639861e1bffc/edit?edit-label.label_code=01619">edit</a></td>
    </tr>
    <tr>
      <th>6</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/360f0149-5510-400b-a281-cb2d735f9f8e">360f0149-5510-400b-a281-cb2d735f9f8e</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1780995">Q1780995</a></td>
      <td>03066</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/360f0149-5510-400b-a281-cb2d735f9f8e/edit?edit-label.label_code=03066">edit</a></td>
    </tr>
    <tr>
      <th>7</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/ed181c75-809b-4ea3-a58e-12b2e435ea3a">ed181c75-809b-4ea3-a58e-12b2e435ea3a</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1046707">Q1046707</a></td>
      <td>03272</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/ed181c75-809b-4ea3-a58e-12b2e435ea3a/edit?edit-label.label_code=03272">edit</a></td>
    </tr>
    <tr>
      <th>8</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/2564aad6-155c-4a81-a537-03f69bce60ba">2564aad6-155c-4a81-a537-03f69bce60ba</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q13396798">Q13396798</a></td>
      <td>05668</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/2564aad6-155c-4a81-a537-03f69bce60ba/edit?edit-label.label_code=05668">edit</a></td>
    </tr>
    <tr>
      <th>9</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/e34fbcc3-4ecd-408f-ba48-ba4530a12577">e34fbcc3-4ecd-408f-ba48-ba4530a12577</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q98097397">Q98097397</a></td>
      <td>10906</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/e34fbcc3-4ecd-408f-ba48-ba4530a12577/edit?edit-label.label_code=10906">edit</a></td>
    </tr>
    <tr>
      <th>10</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/8acdd8f2-7fbb-4634-9b5f-adaa5254b032">8acdd8f2-7fbb-4634-9b5f-adaa5254b032</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4867000">Q4867000</a></td>
      <td>12762</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/8acdd8f2-7fbb-4634-9b5f-adaa5254b032/edit?edit-label.label_code=12762">edit</a></td>
    </tr>
    <tr>
      <th>11</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/2f624cc8-ccfc-4ca7-939c-dbbdad2d781b">2f624cc8-ccfc-4ca7-939c-dbbdad2d781b</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1734690">Q1734690</a></td>
      <td>16986</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/2f624cc8-ccfc-4ca7-939c-dbbdad2d781b/edit?edit-label.label_code=16986">edit</a></td>
    </tr>
    <tr>
      <th>12</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/d1208b98-107f-4052-954d-a65af60d0612">d1208b98-107f-4052-954d-a65af60d0612</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1022791">Q1022791</a></td>
      <td>21226</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/d1208b98-107f-4052-954d-a65af60d0612/edit?edit-label.label_code=21226">edit</a></td>
    </tr>
    <tr>
      <th>13</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/cfcfda4d-b5b4-48d6-be64-655db21f5d5e">cfcfda4d-b5b4-48d6-be64-655db21f5d5e</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q61888082">Q61888082</a></td>
      <td>21775</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/cfcfda4d-b5b4-48d6-be64-655db21f5d5e/edit?edit-label.label_code=21775">edit</a></td>
    </tr>
    <tr>
      <th>14</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/e39b8545-dcc6-44a9-a7b3-e564fa56e30f">e39b8545-dcc6-44a9-a7b3-e564fa56e30f</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q6940121">Q6940121</a></td>
      <td>24535</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/e39b8545-dcc6-44a9-a7b3-e564fa56e30f/edit?edit-label.label_code=24535">edit</a></td>
    </tr>
    <tr>
      <th>15</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/696ee2f4-c486-4e7a-80f4-cfd85193677a">696ee2f4-c486-4e7a-80f4-cfd85193677a</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q375229">Q375229</a></td>
      <td>34682</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/696ee2f4-c486-4e7a-80f4-cfd85193677a/edit?edit-label.label_code=34682">edit</a></td>
    </tr>
    <tr>
      <th>16</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/ebff23f2-5c49-4b7e-8735-cbe13c2705e3">ebff23f2-5c49-4b7e-8735-cbe13c2705e3</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q16834801">Q16834801</a></td>
      <td>50450</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/ebff23f2-5c49-4b7e-8735-cbe13c2705e3/edit?edit-label.label_code=50450">edit</a></td>
    </tr>
    <tr>
      <th>17</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/cef333af-c032-41a9-a391-181d482f92b4">cef333af-c032-41a9-a391-181d482f92b4</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q6101742">Q6101742</a></td>
      <td>83574</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/cef333af-c032-41a9-a391-181d482f92b4/edit?edit-label.label_code=83574">edit</a></td>
    </tr>
    <tr>
      <th>18</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/bab0d362-fc09-476a-aa33-0fee8efee0fa">bab0d362-fc09-476a-aa33-0fee8efee0fa</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q831335">Q831335</a></td>
      <td>LC 00098</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/bab0d362-fc09-476a-aa33-0fee8efee0fa/edit?edit-label.label_code=LC 00098">edit</a></td>
    </tr>
    <tr>
      <th>19</th>
      <td><a target="_blank" href="https://musicbrainz.org/label/9b6dec85-599a-481f-9642-62fd1d3999fe">9b6dec85-599a-481f-9642-62fd1d3999fe</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q59469453">Q59469453</a></td>
      <td>LC 0227</td>
      <td><a target="_blank" href="https://musicbrainz.org/label/9b6dec85-599a-481f-9642-62fd1d3999fe/edit?edit-label.label_code=LC 0227">edit</a></td>
    </tr>
  </tbody>
</table>



```python
# linked to MB label
links_from_wd_with_bnf = sparql("""
SELECT (?label AS ?wd) ?mbid ?labelLabel ?bnf
WHERE {
  ?label wdt:P966 ?mbid .
  ?label wdt:P268 ?bnf .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
ORDER BY ASC(?labelLabel)
""")
links_from_wd_with_bnf.rename(columns={'labelLabel': 'name'}, inplace=True)

print('Count:', len(links_from_wd_with_bnf))
display_df(links_from_wd_with_bnf.head())
```

    Count: 459



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wd</th>
      <th>mbid</th>
      <th>name</th>
      <th>bnf</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q2982799">Q2982799</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/6bac79db-1cda-4c50-b02a-0d275807725d">6bac79db-1cda-4c50-b02a-0d275807725d</a></td>
      <td>Q2982799</td>
      <td>12454777n</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q3269707">Q3269707</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/7f8729af-19ea-4aef-a951-fee47ff2f59f">7f8729af-19ea-4aef-a951-fee47ff2f59f</a></td>
      <td>Q3269707</td>
      <td>13889093m</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q52721802">Q52721802</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/45cd3e9d-7c41-4875-a561-4df7c4e46812">45cd3e9d-7c41-4875-a561-4df7c4e46812</a></td>
      <td>Q52721802</td>
      <td>16765226w</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q77202">Q77202</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/45fe499a-d335-44a9-9f84-e17ccf97152a">45fe499a-d335-44a9-9f84-e17ccf97152a</a></td>
      <td>1C Company</td>
      <td>145534620</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q97446731">Q97446731</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/ed0d5aff-e23f-4239-950f-bae0bc201e6c">ed0d5aff-e23f-4239-950f-bae0bc201e6c</a></td>
      <td>20th Century Records</td>
      <td>13884815t</td>
    </tr>
  </tbody>
</table>



```python
links_from_mb_with_bnf = sql("""
SELECT
    url.url AS wd,
    label.gid AS mbid,
    label.name
FROM label
JOIN l_label_url AS llu             ON llu.entity0 = label.id
JOIN url                            ON llu.entity1 = url.id
WHERE
    url.url LIKE '%%bnf.fr%%'
ORDER BY label.name
;
""")
links_from_mb_with_bnf.wd = links_from_mb.wd.apply(lambda s: s.split('/')[-1])
links_from_mb_with_bnf.mbid = links_from_mb.mbid.apply(str)

print('Count:', len(links_from_mb_with_bnf))
display_df(links_from_mb_with_bnf.head())
```

    Count: 102



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q315760">Q315760</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/893364ff-1830-4694-833d-93751f14f984">893364ff-1830-4694-833d-93751f14f984</a></td>
      <td>10 Records Ltd.</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4544982">Q4544982</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/becff808-7fa6-4f85-ab15-0444bca5d04c">becff808-7fa6-4f85-ab15-0444bca5d04c</a></td>
      <td>1NC@</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q58209721">Q58209721</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/3129e8bf-cd5c-428d-b79a-51f77445a3f9">3129e8bf-cd5c-428d-b79a-51f77445a3f9</a></td>
      <td>21 Records</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4545734">Q4545734</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/7441004d-1165-4c04-b029-7c8d59c5912a">7441004d-1165-4c04-b029-7c8d59c5912a</a></td>
      <td>A&M Records</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q3983384">Q3983384</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/label/5a8514dd-22d2-4def-a48d-3a8b71a8e24f">5a8514dd-22d2-4def-a48d-3a8b71a8e24f</a></td>
      <td>ACPE</td>
    </tr>
  </tbody>
</table>


report
x missing WD link
x missing LC / diverging LC
missing discogs /div 
missing viaf / div
missing bnf / div

common LC but no direct MB/WD link
common discogs viaf bnf

wikipedia link and no wikidata link


```python
import jinja2

template = jinja2.Template("""
<!doctype html>

<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Alignment of MusicBrainz and Wikidata Record Labels</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>

  <body style="margin: 20px;">
    <h1>Alignment of MusicBrainz and Wikidata Record Labels</h1>

    <p>Latest MB database update: {{ MB_DATABASE_VERSION }}</p>
    <p>Latest update: {{ date.today().isoformat() }}</p>

    <ol>
      <li>
        <a href="#lc">Add missing Label Codes</a>
        ({{ lc_to_add_to_mb.shape[0] }} rows)
      </li>
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
    
    <h2 id="lc">Add missing Label Codes</h2>
    {{ df_to_html(lc_to_add_to_mb) }}

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

with open('../docs/wd-recordlabels-report.html', 'w') as f:
    f.write(template.render(**globals())
            .replace('&lt;', '<').replace('&gt;', '>')
            .replace('class="dataframe"', 'class="table table-striped table-hover table-sm"')
            .replace('thead', 'thead class="thead-light"'))
```
