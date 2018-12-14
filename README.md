# get-wayback-machine [![Build Status](https://travis-ci.com/jfilter/get-wayback-machine.svg?branch=master)](https://travis-ci.com/jfilter/get-wayback-machine) [![PyPI](https://img.shields.io/pypi/v/get-wayback-machine.svg)](https://pypi.org/project/get-wayback-machine/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/get-wayback-machine.svg)](https://pypi.org/project/get-wayback-machine/)

Fetch a URL via the latest Wayback Machine Snapshot.

## Why?

Occasionally, you have a given URL that it is not online anymore. You may still access it's content via the Internet Archive's [Wayback Machine](https://archive.org/web/).

## Install

```bash
pip install get_wayback_machine
```

## Usage

```python
import get_wayback_machine

response = get_wayback_machine.get('https://en.wikipedia.org')
if response:
    print(response.status_code)
```

The response is either `None` (for fails) or a [Requests](http://docs.python-requests.org/en/master/) response.

## Related

-   https://github.com/hartator/wayback-machine-downloader
-   https://github.com/sangaline/wayback-machine-scraper
-   https://github.com/jsvine/waybackpack

## License

MIT.
