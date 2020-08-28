import setuptools

NAME = "screening-report-tool"
AUTHOR = "Rudy Williams"
AUTHOR_EMAIL = "rudysw05@knights.ucf.edu"
SHORT_DESCRIPTION = "A cli tool for creating useful plots from screening data"
URL = "https://github.com/RudyWilliams/screening-report"

with open("screening_report_tool/VERSION") as v:
    VERSION = v.read().strip()


def list_reqs(fname="requirements.txt"):
    with open(fname) as f:
        return f.read().splitlines()


setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=SHORT_DESCRIPTION,
    url=URL,
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["screen=screening_report_tool.run:run_cli"]},
    install_requires=list_reqs(),
    include_package_data=True,
    python_requires=">=3.6",
)
