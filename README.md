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
4. Copy that URL.
5. Download your URL as a PDF to `output.pdf` using pearson-pdf:
   ```bash
   pearson-pdf https://example.com/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/foxit-assets output.pdf
   ```

More information on usage is in the help page:

```bash
pearson-pdf -h
```

## License

See [LICENSE](LICENSE) for details.
