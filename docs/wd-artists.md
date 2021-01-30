```python
%run -i ../startup.py
ENTITY_TYPE = 'artist'
```

    Last notebook update: 2021-01-30
    Importing libs
    Defining database parameters
    Defining *sql* helper function
    Last database update: 2021-01-13
    
    Defining *sparql* helper function


Wikidata entities:

https://www.wikidata.org/wiki/Q482994 album

Wikidata properties:

https://www.wikidata.org/wiki/Property:P214 VIAF

https://www.wikidata.org/wiki/Property:P268 BNF

https://www.wikidata.org/wiki/Property:P244 LoC

https://www.wikidata.org/wiki/Property:P1953 discogs artist ID

https://www.wikidata.org/wiki/Property:P434 MusicBrainz Artist ID

examples



## Artists from Wikidata


```python
links_type_from_wd = sparql("""
SELECT distinct (count(?artist) as ?cnt) ?ins ?insLabel
WHERE {
  ?artist wdt:P31 ?ins;
    wdt:P434 ?mbid.
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
group by ?ins ?insLabel
order by DESC(?cnt)
""")
links_type_from_wd[links_type_from_wd.cnt.astype(int) > 10]
```


    ---------------------------------------------------------------------------

    RemoteDisconnected                        Traceback (most recent call last)

    ~/mbz/musicbrainz-sparql/startup.py in <module>
    ----> 1 links_type_from_wd = sparql("""
          2 SELECT distinct (count(?artist) as ?cnt) ?ins ?insLabel
          3 WHERE {
          4   ?artist wdt:P31 ?ins;
          5     wdt:P434 ?mbid.


    ~/mbz/musicbrainz-sparql/startup.py in sparql(query, endpoint, **kwargs)
        131     wrapper = SPARQLWrapper2(endpoint)
        132     wrapper.setQuery(query)
    --> 133     results = wrapper.query()
        134 
        135     def _clean_url(url):


    ~/.virtualenvs/mbsparq/lib/python3.9/site-packages/SPARQLWrapper/SmartWrapper.py in query(self)
        310             :rtype: :class:`Bindings` instance
        311         """
    --> 312         res = super(SPARQLWrapper2, self).query()
        313 
        314         if self.queryType == SELECT:


    ~/.virtualenvs/mbsparq/lib/python3.9/site-packages/SPARQLWrapper/Wrapper.py in query(self)
       1105             :rtype: :class:`QueryResult` instance
       1106         """
    -> 1107         return QueryResult(self._query())
       1108 
       1109     def queryAndConvert(self):


    ~/.virtualenvs/mbsparq/lib/python3.9/site-packages/SPARQLWrapper/Wrapper.py in _query(self)
       1071                 response = urlopener(request, timeout=self.timeout)
       1072             else:
    -> 1073                 response = urlopener(request)
       1074             return response, self.returnFormat
       1075         except urllib.error.HTTPError as e:


    /usr/lib/python3.9/urllib/request.py in urlopen(url, data, timeout, cafile, capath, cadefault, context)
        212     else:
        213         opener = _opener
    --> 214     return opener.open(url, data, timeout)
        215 
        216 def install_opener(opener):


    /usr/lib/python3.9/urllib/request.py in open(self, fullurl, data, timeout)
        515 
        516         sys.audit('urllib.Request', req.full_url, req.data, req.headers, req.get_method())
    --> 517         response = self._open(req, data)
        518 
        519         # post-process response


    /usr/lib/python3.9/urllib/request.py in _open(self, req, data)
        532 
        533         protocol = req.type
    --> 534         result = self._call_chain(self.handle_open, protocol, protocol +
        535                                   '_open', req)
        536         if result:


    /usr/lib/python3.9/urllib/request.py in _call_chain(self, chain, kind, meth_name, *args)
        492         for handler in handlers:
        493             func = getattr(handler, meth_name)
    --> 494             result = func(*args)
        495             if result is not None:
        496                 return result


    /usr/lib/python3.9/urllib/request.py in https_open(self, req)
       1387 
       1388         def https_open(self, req):
    -> 1389             return self.do_open(http.client.HTTPSConnection, req,
       1390                 context=self._context, check_hostname=self._check_hostname)
       1391 


    /usr/lib/python3.9/urllib/request.py in do_open(self, http_class, req, **http_conn_args)
       1348             except OSError as err: # timeout error
       1349                 raise URLError(err)
    -> 1350             r = h.getresponse()
       1351         except:
       1352             h.close()


    /usr/lib/python3.9/http/client.py in getresponse(self)
       1345         try:
       1346             try:
    -> 1347                 response.begin()
       1348             except ConnectionError:
       1349                 self.close()


    /usr/lib/python3.9/http/client.py in begin(self)
        305         # read until we get a non-100 response
        306         while True:
    --> 307             version, status, reason = self._read_status()
        308             if status != CONTINUE:
        309                 break


    /usr/lib/python3.9/http/client.py in _read_status(self)
        274             # Presumably, the server closed the connection before
        275             # sending a valid response.
    --> 276             raise RemoteDisconnected("Remote end closed connection without"
        277                                      " response")
        278         try:


    RemoteDisconnected: Remote end closed connection without response



```python
# linked to MB artist
links_from_wd = sparql("""
SELECT distinct (count(?artist) as ?cnt)
WHERE {
  ?artist wdt:P434 ?mbid .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
ORDER BY ASC(?artistLabel)
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
      <td>220459</td>
    </tr>
  </tbody>
</table>
</div>



That's too many to be fetched. Try the artists with a discogs link


```python
# linked to MB artist
links_from_wd = sparql("""
SELECT distinct (count(?artist) as ?cnt)
WHERE {
  ?artist wdt:P434 ?mbid .
  ?artist wdt:P1953 ?discogs .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
ORDER BY ASC(?artistLabel)
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
      <td>139136</td>
    </tr>
  </tbody>
</table>
</div>




```python
# linked to MB work
links_from_wd = sparql("""
SELECT (?artist AS ?wd) ?mbid ?artistLabel ?discogs
WHERE {
  ?artist wdt:P434 ?mbid .
  ?artist wdt:P1953 ?discogs .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
ORDER BY ASC(?artistLabel)
""")
links_from_wd.rename(columns={'artistLabel': 'name'}, inplace=True)

print('Count:', len(links_from_wd))
display_df(links_from_wd.head())
```

    Count: 139136



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100147499">Q100147499</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/3a7d3219-41e1-4f5a-87f4-fbf5c7aed04d">3a7d3219-41e1-4f5a-87f4-fbf5c7aed04d</a></td>
      <td>Q100147499</td>
      <td>1642404</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100251627">Q100251627</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/a9639067-da3f-4747-b604-0269241d7494">a9639067-da3f-4747-b604-0269241d7494</a></td>
      <td>Q100251627</td>
      <td>5776203</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100315776">Q100315776</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/d7c66a58-a91e-48b8-af59-0ea96b3e9f33">d7c66a58-a91e-48b8-af59-0ea96b3e9f33</a></td>
      <td>Q100315776</td>
      <td>4750497</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100450275">Q100450275</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/a1eec171-4baf-4e5f-8156-4fbc626f1ff8">a1eec171-4baf-4e5f-8156-4fbc626f1ff8</a></td>
      <td>Q100450275</td>
      <td>554436</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100995191">Q100995191</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/0c159e39-d25a-4d09-a33d-3d72c45f5324">0c159e39-d25a-4d09-a33d-3d72c45f5324</a></td>
      <td>Q100995191</td>
      <td>1625893</td>
    </tr>
  </tbody>
</table>


## Artists from MusicBrainz with wikidata links


```python
links_from_mb = sql("""
SELECT
    url.url AS wd,
    artist.gid AS mbid,
    artist.name
FROM 
    artist
    JOIN l_artist_url AS lau ON lau.entity0 = artist.id
    JOIN url                 ON lau.entity1 = url.id
WHERE
    url.url LIKE '%%wikidata.org%%'
ORDER BY
    artist.name
;
""")
links_from_mb.wd = links_from_mb.wd.apply(lambda s: s.split('/')[-1])
links_from_mb.mbid = links_from_mb.mbid.apply(str)

print('Count:', len(links_from_mb))
display_df(links_from_mb.head())
```

    Count: 200132



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q371">Q371</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/f26c72d3-e52c-467b-b651-679c73d8e1a7">f26c72d3-e52c-467b-b651-679c73d8e1a7</a></td>
      <td>!!!</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q343686">Q343686</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/8924ec2e-ff39-4968-a686-48effcb39d5e">8924ec2e-ff39-4968-a686-48effcb39d5e</a></td>
      <td>!Action Pact!</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1183824">Q1183824</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/55cc41c4-d527-4b1a-b45d-4c2ff718f000">55cc41c4-d527-4b1a-b45d-4c2ff718f000</a></td>
      <td>!DelaDap</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1622767">Q1622767</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/54a1dd0e-a535-46a9-9ad8-b49ebe1ce482">54a1dd0e-a535-46a9-9ad8-b49ebe1ce482</a></td>
      <td>!T.O.O.H.!</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q14565188">Q14565188</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/c60674c3-1cd8-4b2c-ada3-8f99d94c4aad">c60674c3-1cd8-4b2c-ada3-8f99d94c4aad</a></td>
      <td>!distain</td>
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

    Count: 4461



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1004132">Q1004132</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/98452b79-5c2b-4e1c-9bb8-ff9592c2a061">98452b79-5c2b-4e1c-9bb8-ff9592c2a061</a></td>
      <td>Bull City Red</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1004132">Q1004132</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/54143235-e5fb-4747-ae86-0433075a547d">54143235-e5fb-4747-ae86-0433075a547d</a></td>
      <td>George Washington</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100464">Q100464</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/661be230-f092-4e64-b5ef-196f4e5f53e7">661be230-f092-4e64-b5ef-196f4e5f53e7</a></td>
      <td>Wolfgang Roloff</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100464">Q100464</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/072f218c-da41-4a7a-b0aa-9aa816dc160c">072f218c-da41-4a7a-b0aa-9aa816dc160c</a></td>
      <td>Ronny</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q1005957">Q1005957</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/6054baf8-3a47-4c3a-8c51-eb976f69ecfc">6054baf8-3a47-4c3a-8c51-eb976f69ecfc</a></td>
      <td>Hobo</td>
    </tr>
  </tbody>
</table>



```python
duplicate_mb = links_from_mb[['wd', 'mbid', 'name']].groupby('mbid').filter(
    lambda row: len(row.mbid) > 1).sort_values('mbid')

print('Count:', len(duplicate_mb))
display_df(duplicate_mb.head())
```

    Count: 244



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q79048065">Q79048065</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/01793aba-0995-4df1-86f2-baa31b4e4cb7">01793aba-0995-4df1-86f2-baa31b4e4cb7</a></td>
      <td>STAXKK</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q79048066">Q79048066</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/01793aba-0995-4df1-86f2-baa31b4e4cb7">01793aba-0995-4df1-86f2-baa31b4e4cb7</a></td>
      <td>STAXKK</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q57314794">Q57314794</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/06783a0f-cf91-4fe6-97dc-5f303dcdb36c">06783a0f-cf91-4fe6-97dc-5f303dcdb36c</a></td>
      <td>梅田綾乃</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q15908991">Q15908991</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/06783a0f-cf91-4fe6-97dc-5f303dcdb36c">06783a0f-cf91-4fe6-97dc-5f303dcdb36c</a></td>
      <td>梅田綾乃</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q98443953">Q98443953</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/10d626a3-ce89-4fe7-b8e0-b502a9148d60">10d626a3-ce89-4fe7-b8e0-b502a9148d60</a></td>
      <td>Sebastian Barrera</td>
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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100147499">Q100147499</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/3a7d3219-41e1-4f5a-87f4-fbf5c7aed04d">3a7d3219-41e1-4f5a-87f4-fbf5c7aed04d</a></td>
      <td>Q100147499</td>
      <td>1642404</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100251627">Q100251627</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/a9639067-da3f-4747-b604-0269241d7494">a9639067-da3f-4747-b604-0269241d7494</a></td>
      <td>Q100251627</td>
      <td>5776203</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100315776">Q100315776</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/d7c66a58-a91e-48b8-af59-0ea96b3e9f33">d7c66a58-a91e-48b8-af59-0ea96b3e9f33</a></td>
      <td>Q100315776</td>
      <td>4750497</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100450275">Q100450275</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/a1eec171-4baf-4e5f-8156-4fbc626f1ff8">a1eec171-4baf-4e5f-8156-4fbc626f1ff8</a></td>
      <td>Q100450275</td>
      <td>554436</td>
      <td>Alistair Anderson</td>
      <td>both</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100995191">Q100995191</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/0c159e39-d25a-4d09-a33d-3d72c45f5324">0c159e39-d25a-4d09-a33d-3d72c45f5324</a></td>
      <td>Q100995191</td>
      <td>1625893</td>
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

    Count: 85896



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
      <td>"Kid" Prince Moore</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/72050802-74fe-46a8-b926-ff08740e1058">72050802-74fe-46a8-b926-ff08740e1058</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q28008608">Q28008608</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>"Mean" Gene Okerlund</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/44843557-35d0-4bd1-afae-bd162fb007fc">44843557-35d0-4bd1-afae-bd162fb007fc</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q955033">Q955033</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td>"a band called David"</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/f583f07d-c1e2-407d-b869-9d7c6a6a34af">f583f07d-c1e2-407d-b869-9d7c6a6a34af</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q4655343">Q4655343</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td>#1 Dads</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/7aaf9000-eceb-4290-b38d-8cb4242c7730">7aaf9000-eceb-4290-b38d-8cb4242c7730</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q22080866">Q22080866</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td>#2Маши</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/c352886d-fa34-4d6e-8c88-688c1c8c29d1">c352886d-fa34-4d6e-8c88-688c1c8c29d1</a></td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q62964320">Q62964320</a></td>
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

    Count: 21407



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
      <td>Q100147499</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100147499">Q100147499</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/3a7d3219-41e1-4f5a-87f4-fbf5c7aed04d">3a7d3219-41e1-4f5a-87f4-fbf5c7aed04d</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/3a7d3219-41e1-4f5a-87f4-fbf5c7aed04d/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q100147499">edit</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td>Q100251627</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100251627">Q100251627</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/a9639067-da3f-4747-b604-0269241d7494">a9639067-da3f-4747-b604-0269241d7494</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/a9639067-da3f-4747-b604-0269241d7494/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q100251627">edit</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td>Q100315776</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100315776">Q100315776</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/d7c66a58-a91e-48b8-af59-0ea96b3e9f33">d7c66a58-a91e-48b8-af59-0ea96b3e9f33</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/d7c66a58-a91e-48b8-af59-0ea96b3e9f33/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q100315776">edit</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td>Q100995191</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100995191">Q100995191</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/0c159e39-d25a-4d09-a33d-3d72c45f5324">0c159e39-d25a-4d09-a33d-3d72c45f5324</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/0c159e39-d25a-4d09-a33d-3d72c45f5324/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q100995191">edit</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td>Q101072266</td>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q101072266">Q101072266</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/b29c45fe-3e06-4736-9053-1cbe93f61691">b29c45fe-3e06-4736-9053-1cbe93f61691</a></td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/b29c45fe-3e06-4736-9053-1cbe93f61691/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q101072266">edit</a></td>
    </tr>
  </tbody>
</table>


## Data alignment through Discogs

TBD on wd entries with discogs links and no mb link


```python
# linked to Discogs artist
discogs_links_from_wd = sparql("""
SELECT (?artist AS ?wd) ?artistLabel ?discogs
WHERE {
  ?artist wdt:P1953 ?discogs .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
  MINUS {
    ?artist wdt:P434 ?mbid .  
  }
}
ORDER BY ASC(?artistLabel)
""")
discogs_links_from_wd.rename(columns={'artistLabel': 'name'}, inplace=True)

print('Count:', len(discogs_links_from_wd))
display_df(discogs_links_from_wd.head())
```

    Count: 37976



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100024805">Q100024805</a></td>
      <td>Q100024805</td>
      <td>3469656</td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100266269">Q100266269</a></td>
      <td>Q100266269</td>
      <td>5025860</td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100268968">Q100268968</a></td>
      <td>Q100268968</td>
      <td>2763300</td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100272130">Q100272130</a></td>
      <td>Q100272130</td>
      <td>1005141</td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100448674">Q100448674</a></td>
      <td>Q100448674</td>
      <td>3792973</td>
    </tr>
  </tbody>
</table>



```python
discogs_links_from_mb = sql("""
SELECT
    url.url AS discogs,
    artist.gid AS mbid,
    artist.name
FROM 
    artist
    JOIN l_artist_url AS lau ON lau.entity0 = artist.id
    JOIN url                 ON lau.entity1 = url.id
WHERE
    url.url LIKE '%%discogs.com%%'
    AND lau.entity0 IN (
        SELECT
            entity0
        FROM 
            l_artist_url
            JOIN url ON l_artist_url.entity1 = url.id
        WHERE
            url.url LIKE '%%discogs.com%%'
    EXCEPT
        SELECT
            entity0
        FROM 
            l_artist_url
            JOIN url ON l_artist_url.entity1 = url.id
        WHERE
            url.url LIKE '%%wikidata.org%%'
    )
ORDER BY
    artist.name
;
""")
discogs_links_from_mb.discogs = discogs_links_from_mb.discogs.apply(lambda s: s.split('/')[-1])
discogs_links_from_mb.mbid = discogs_links_from_mb.mbid.apply(str)

print('Count:', len(discogs_links_from_mb))
display_df(discogs_links_from_mb.head())
```

    Count: 575584



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
      <td>2738698</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/d0d9b2a4-c5f0-4407-90cd-44dfd513158b">d0d9b2a4-c5f0-4407-90cd-44dfd513158b</a></td>
      <td>! Obtain?</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1101118</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/ba813b0d-982a-491a-8648-3b2097b069dd">ba813b0d-982a-491a-8648-3b2097b069dd</a></td>
      <td>!!!</td>
    </tr>
    <tr>
      <th>2</th>
      <td>542719</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/a057fba4-ac0e-4745-88e7-6e89c586e9cb">a057fba4-ac0e-4745-88e7-6e89c586e9cb</a></td>
      <td>!!!</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1036695</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/19605e24-020f-4493-97b5-a4f9880a3ac5">19605e24-020f-4493-97b5-a4f9880a3ac5</a></td>
      <td>!!*</td>
    </tr>
    <tr>
      <th>4</th>
      <td>213060</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/acec84ff-c4cb-420c-96cf-982b651573bd">acec84ff-c4cb-420c-96cf-982b651573bd</a></td>
      <td>!!Swanhunter</td>
    </tr>
  </tbody>
</table>



```python
discogs_merge = pd.merge(discogs_links_from_wd, discogs_links_from_mb, 
                 on=['discogs'], suffixes=('_wd', '_mb'),
                 how='inner', indicator=False)
discogs_merge['edit_link'] = discogs_merge.apply(
    mb_artist_edit_wd_link, axis=1)

print('Count:', len(discogs_merge))
display_df(discogs_merge.head())
```

    Count: 8748



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
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q100268968">Q100268968</a></td>
      <td>Q100268968</td>
      <td>2763300</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/9df09077-c63d-45c0-bc60-114589f83996">9df09077-c63d-45c0-bc60-114589f83996</a></td>
      <td>Attilio Staffelli</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/9df09077-c63d-45c0-bc60-114589f83996/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q100268968">edit</a></td>
    </tr>
    <tr>
      <th>1</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q101158997">Q101158997</a></td>
      <td>Q101158997</td>
      <td>5487155</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/e4f25fd5-9e46-48b9-b5b8-cf3633a157a1">e4f25fd5-9e46-48b9-b5b8-cf3633a157a1</a></td>
      <td>Floating Sofa Quartet</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/e4f25fd5-9e46-48b9-b5b8-cf3633a157a1/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q101158997">edit</a></td>
    </tr>
    <tr>
      <th>2</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q101429533">Q101429533</a></td>
      <td>Q101429533</td>
      <td>2038099</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/7dd59664-0b60-4eef-9280-491e6c679d37">7dd59664-0b60-4eef-9280-491e6c679d37</a></td>
      <td>Robin Fincker</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/7dd59664-0b60-4eef-9280-491e6c679d37/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q101429533">edit</a></td>
    </tr>
    <tr>
      <th>3</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q101504558">Q101504558</a></td>
      <td>Q101504558</td>
      <td>601285</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/9554bc87-d985-4f73-a394-5c52fbca6449">9554bc87-d985-4f73-a394-5c52fbca6449</a></td>
      <td>Marius Beets</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/9554bc87-d985-4f73-a394-5c52fbca6449/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q101504558">edit</a></td>
    </tr>
    <tr>
      <th>4</th>
      <td><a target="_blank" href="https://www.wikidata.org/wiki/Q101935166">Q101935166</a></td>
      <td>Q101935166</td>
      <td>3201305</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/e6470441-2cc3-4b3f-b361-92c5f23f9707">e6470441-2cc3-4b3f-b361-92c5f23f9707</a></td>
      <td>Constantin Herzog</td>
      <td><a target="_blank" href="https://musicbrainz.org/artist/e6470441-2cc3-4b3f-b361-92c5f23f9707/edit?edit-artist.url.99.type=689870a4-a1e4-4912-b17f-7b2664215698&edit-artist.url.99.text=https://www.wikidata.org/wiki/Q101935166">edit</a></td>
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
    <title>Alignment of MusicBrainz and Wikidata Artists</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>

  <body style="margin: 20px;">
    <h1>Alignment of MusicBrainz and Wikidata Artists</h1>

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

with open('../docs/wd-artists-report.html', 'w') as f:
    f.write(template.render(**globals())
            .replace('&lt;', '<').replace('&gt;', '>')
            .replace('class="dataframe"', 'class="table table-striped table-hover table-sm"')
            .replace('thead', 'thead class="thead-light"'))
```
