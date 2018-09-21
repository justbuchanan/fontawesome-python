# Font Awesome icons for python [![PyPI version](https://badge.fury.io/py/fontawesome.svg)](https://badge.fury.io/py/fontawesome)

## Installation 

```{.sh}
pip install fontawesome
```

## Usage 

```{.py}
import fontawesome as fa

print(fa.icons['thumbs-up'])
>>> 
```

## Build 

```{.sh}
# Run the generate script to download font awesome's character mapping
# and generate a python-formatted version of it.  Save this file as icons.py
# in the fontawesome subdirectory.  Note that this pulls the latest revision
# on the master branch.  You can easily change this  with the --revision flag.
./fontawesome/generate.py > ./fontawesome/icons.py

python setup.py build

python setup.py install
```

## License

The code in this repository is licensed under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

The character codes included with this package are part of the [Font Awesome project](http://fontawesome.io/).
