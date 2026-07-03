import os, sys, json, random,datetime
from pathlib import Path

from typing import List, Tuple, Dict, Any, Union

from threading import Thread


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

class ThreadWithReturnValue(Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def json_to_html(payload: List[Dict[str, Any]],
                 jsonFilePath: Path, 
                 htmlFilePath: Path, 
                 cssFilePath: Path = defaultCssPath) -> None:
    '''Converts a JSON file to an HTML file'''
    def create_tr(item: Dict[str, Any], counter: int) -> dominate.tags.tr:
        '''Creates a table row for the HTML file'''
        tr = dominate.tags.tr()
        columnCount = 1
        col_line = []

        with tr:
            dominate.tags.td(counter, _class="column-0")
            for key, value in item.items():
                if columnCount == 2:
                    if value == 'girl':
                        dominate.tags.td(value, _class="column-{}-g".format(columnCount))
                    elif value == 'boy':
                        dominate.tags.td(value, _class="column-{}-b".format(columnCount))
                else:
                    dominate.tags.td(value, _class="column-{}".format(columnCount))
                col_line.append(value)
                columnCount += 1
                
        print(f"Row {counter}: <generated> {col_line}")
        del col_line 
        return tr
    with open(jsonFilePath, 'r') as f:
        data = json.load(f)
    
    # Gen Document
    doc_name = "jTh-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    doc = dominate.document(title='JSON to HTML')
    # Append Header and CSS
    with doc.head:
        dominate.tags.style(type='text/css').add_raw_string(cssFilePath.read_text()) 

    # Create Table
    table_name = "json-table"
    with doc:

        rows : List[dominate.tags.tr] = []
        table = dominate.tags.table(id=table_name)
        with table:
            counter = 0
            headers_count = 0
            dominate.tags.th("No.", _class="header-0")
            for key in data[0].keys():
                headers_count += 1
                dominate.tags.th(key, _class="header-0")
            threads : List[ThreadWithReturnValue] = []
            for item in data:
                threads.append(ThreadWithReturnValue(name=f"thread-{counter}", target=create_tr, args=(item, counter)))
                counter += 1
            
            for thread in threads:
                thread.start()
            
            for thread in threads:
                rows.append(thread.join())
            # rows.sort(key=lambda x: int(x.children[0].text))  # Sort rows based on the first column (No.)
        for row in rows:
            table.add(row)
        print(f"HTML file created at: {htmlFilePath}")


    print(doc.render(), file=open(htmlFilePath, 'w'))

for p in paths:
    if not p.exists():
        p.mkdir(parents=True, exist_ok=True)

