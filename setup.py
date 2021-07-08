from setuptools import setup, find_packages
import codecs
import os.path


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()


setup(
    name="pearson-pdf",
    version=get_version("pearson_pdf/__init__.py"),
    author="jyooru",
    license="MIT",
    description="Tool to download Pearson books as PDFs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jyooru/pearson-pdf",
    project_urls={
        "Source": "https://github.com/jyooru/pearson-pdf",
        "Issues": "https://github.com/jyooru/pearson-pdf/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="pearson, ebook, pearson-ebook, pdf, pearson-pdf",
    packages=find_packages(exclude=["tests"]),
    install_requires=["requests", "pillow"],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["pearson_pdf=pearson_pdf.__main__:main"]},
)
