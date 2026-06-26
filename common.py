import os, sys, json, random,datetime
from pathlib import Path

from typing import List, Tuple, Dict, Any, Union

import dominate


root = Path(os.path.dirname( __file__ ))
temp = root/"temp"

jsonDataPath = temp/"json"
htmlDataPath = temp/"html"
defaultCssPath = root/"style.css"

paths = [
    root,
    temp,
    jsonDataPath,
    htmlDataPath
]

def json_to_html(payload: List[Dict[str, Any]],
                 jsonFilePath: Path, 
                 htmlFilePath: Path, 
                 cssFilePath: Path = defaultCssPath) -> None:
    '''Converts a JSON file to an HTML file'''
    with open(jsonFilePath, 'r') as f:
        data = json.load(f)
    
    doc = dominate.document(title='JSON to HTML')

    with doc.head:
        dominate.tags.style(type='text/css').add_raw_string(cssFilePath.read_text()) 

    with doc:
        with dominate.tags.table( ):
            counter = 1
            headers_count = 0
            dominate.tags.th("No.", _class="header-0")
            for key in data[0].keys():
                headers_count += 1
                dominate.tags.th(key, _class="header-0")
            for item in data:
                with dominate.tags.tr():
                    
                    columnCount = 0
                    dominate.tags.td(counter, _class="column-{}".format(columnCount))
                    for key, value in item.items():
                        columnCount += 1
                        dominate.tags.td(value, _class="column-{}".format(columnCount))
                        

                    counter  += 1
    print(doc.render(), file=open(htmlFilePath, 'w'))

for p in paths:
    if not p.exists():
        p.mkdir(parents=True, exist_ok=True)

