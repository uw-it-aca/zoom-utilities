import os
from setuptools import setup

README = """
See the README on `GitHub
<https://github.com/uw-it-aca/zoom-utilities>`_.
"""

# The VERSION file is created by travis-ci, based on the tag name
version_path = "zoom_utilities/VERSION"
print(os.path.join(os.path.dirname(__file__), version_path))
VERSION = open(os.path.join(os.path.dirname(__file__), version_path)).read()
VERSION = VERSION.replace("\n", "")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

url = "https://github.com/uw-it-aca/zoom-utilities"
setup(
    name="ZoomUtilities",
    version=VERSION,
    packages=[],
    author="UWIT Student & Educational Technology Services",
    author_email="aca-it@uw.edu",
    include_package_data=True,
    install_requires=[
        "django~=5.2",
        'django-storages[google]',
        'uw-restclients-core~=1.4',
        'uw-restclients-zoom~=0.1',
        'uw-restclients-gws~=2.3',
        'uw-memcached-clients~=1.0',
        'django-supporttools~=3.6',
        'uw-django-saml2~=1.8',
        'psycopg[c]',
    ],
    license="Apache License, Version 2.0",
    description="Zoom utilities",
    long_description=README,
    url=url,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
)
