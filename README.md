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
with filename as f:
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
