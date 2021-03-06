# JSONobj -- manipulate JSON objects in python

**JSONobj** aims at manipulation of JSON somewhat like [https://jsonpath.com/][jsonpath]

# Installation

Clone this repository, then

```bash
pip install .
```

from within the folder

# Examples

Start by importing JSONobj:

```python
from jsonobj import JSONobj
```

## Read a JSON file:

```python
with open(filename) as f:
    js = JSONobj(f)
```

## Access elements

```python
js['users']
```

returns a JSONobj if


```python
js['users/0/name']
```

returns ```"John Smith"```

The same result is obtained with


```python
js['users'][0]['name']
```

## Transform into the normal json python output

```python
js.to_python()
```

returns

```python
{'users':
    [
        {'name': 'John Smith',
         'email': 'john.smith@email.com'},
        {'name': 'Brian Smith',
         'email': 'brian.smith@email.com'},
    ]
}
```
## Assignment

Strings, numbers or booleans can be assigned to leaf nodes:

```python
js['users/0/email'] = 'j.smith@email.com'
```

JSON objects or python dicts can be assigned to branch nodes:


```python
js['users/2'] = js['users/0'] 

js['users/3'] = {'name': 'Mary Smith', 'email': 'mary@smith.com'}
```

## Iteration

Iterate through all leaf nodes of JSON:


```python
for k, v in js.iter_tree():
    print(k,v)
```
Prints:
```
'users/0/name': 'John Smith'
'users/0/email': 'john.smith@email.com'
'users/1/email': 'Brian Smith'
...
```

Alternatively, one can iterate over all nodes at a particular level with:

```python
for k,v in js.items():
    print(k,v)
```

Or apply a function to all values in tree with:

```python
js.vistitems(len)
```

returns the length of all strings in js tree

## Object copy

obtain a copy of `js` with:

```python
jsn = js.copy()
```

or


```python
jsn = js['/']
```

## Popping

As in a python dictionary, nodes can be popped:


```python
user0 = js.pop('users/0')
```