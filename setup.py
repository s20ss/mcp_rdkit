from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='mcp_rdkit',
    version='0.1.6',
    author='Shashank Shekhar Shukla',
    author_email='shukla20shashankshekhar@gmail.com',
    description='A package for RDKit integration with MCP',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    install_requires=[
        "rdkit",
        "mcp"
    ],
    project_urls={
        "Documentation": "https://github.com/s20ss/mcp_rdkit#readme",
        "Source": "https://github.com/s20ss/mcp_rdkit",
        "Issues": "https://github.com/s20ss/mcp_rdkit/issues"
    },
)