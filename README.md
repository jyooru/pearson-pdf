# pearson-pdf

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
pearson_pdf xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx output.pdf

# with a url
pearson_pdf -u https://example.com/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx output.pdf
```

More information on usage is in the help page:

```bash
pearson_pdf -h
```

## License

See [LICENSE](LICENSE) for details.
