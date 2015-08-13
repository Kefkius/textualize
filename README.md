# textualize

This package provides a tool for textualizing integers. 
In other words, a tool for getting the textual representation
of integers.

For example, the textual representation of 123 is 
'one hundred twenty-three'.

## Usage

```python
    import textualize
    print(textualize.textualize(5))
    # 'five' is printed
```

Instead of `textualize(num)`, you can also use the convenience 
function `i2s(num)`:

```python
    import textualize
    print(textualize.i2s(5))
    # 'five' is printed
```

or

```python
    from textualize import *
    print(i2s(5))
    # 'five' is printed
```

## Examples

```python
    >>> from textualize import i2s
    >>> i2s(5)
    'five'
    >>> i2s(104)
    'one hundred four'
    >>> i2s(8294)
    'eight thousand two hundred ninety-four'
    >>> i2s(10000)
    'ten thousand'
```

## License

This package is released under The MIT License. See LICENSE.txt for details.
