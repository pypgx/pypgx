from setuptools import setup, find_packages

exec(open("pypgx/version.py").read())

setup(
    name="pypgx",
    version=__version__,
    author='Seung-been "Steven" Lee',
    author_email="sbstevenlee@gmail.com",
    description="A Python package for pharmacogenomics research",
    url="https://github.com/sbslee/pypgx",
    packages=find_packages(exclude=["tests"]),
    package_data={
        "pypgx.resources": [
            "gene_table.tsv",
            "snp_table.tsv",
            "star_table.tsv",
        ],
    },
    entry_points={"console_scripts": ["pypgx=pypgx.__main__:main"]}
)
