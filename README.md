# pearson-pdf

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pearson-pdf)](https://pypi.org/project/pearson-pdf/)
[![PyPI](https://img.shields.io/pypi/v/pearson-pdf)](https://pypi.org/project/pearson-pdf/)
[![Downloads](https://pepy.tech/badge/pearson-pdf)](https://pepy.tech/project/pearson-pdf)
[![ci](https://github.com/jyooru/pearson-pdf/actions/workflows/ci.yml/badge.svg)](https://github.com/jyooru/pearson-pdf/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/jyooru/pearson-pdf/branch/main/graph/badge.svg?token=SRK5RPLHN0)](https://codecov.io/gh/jyooru/pearson-pdf)
[![License](https://img.shields.io/github/license/jyooru/pearson-pdf)](LICENSE)

Tool to download Pearson books as PDFs.

## Installation

Install `pearson-pdf` using pip.

```bash
pip install pearson-pdf
```

## Usage

To download a PDF, you'll need to get the book's ID:

1. Open up DevTools in your browser.
2. Navigate to Console.
3. Type in:
   ```js
   window.foxitAssetURL;
   ```
4. Copy that URL. pearson-pdf will parse the ID from that URL.

Now you can download your PDF:

```bash
# with an id
pearson_pdf xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

# with a url
pearson_pdf https://example.com/generated/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/foxit-assets
```

More information on usage is in the help page:

```bash
pearson_pdf -h
```

## License

See [LICENSE](LICENSE) for details.
