from setuptools import setup, find_packages

setup(
    name='mcp_rdkit',
    version='0.1.4',
    author='Shashank Shekhar Shukla',
    author_email='shukla20shashankshekhar@gmail.com',
    description='A package for RDKit integration with MCP',
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
)