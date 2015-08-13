from setuptools import setup

setup(
    name = 'textualize',
    version = '0.1',
    description = 'Tool for textualizing integers.',
    long_description = 'Tool for getting the textual representations of integers.',
    author = 'Tyler Willis',
    author_email = 'kefkius@mail.com',
    url = 'https://github.com/kefkius/textualize',
    keywords = ['textualize'],
    classifiers = [
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License'
    ],
    package_dir = {
        'textualize': 'textualize'
    },
    py_modules = [
        'textualize.__init__',
        'textualize.textualize'
    ]
)
