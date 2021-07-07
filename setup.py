import setuptools


with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()


setuptools.setup(
    name="pearson-pdf",
    version="1.0.5",
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
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=["requests", "pillow"],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["pearson_pdf=pearson_pdf.__main__:main"]},
)
