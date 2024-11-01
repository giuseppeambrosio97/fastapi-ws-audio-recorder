import pathlib as pl

__version__ = "1.0.0"

PACKAGE_LOCATION = pl.Path(__file__).parent.resolve()
ROOT_LOCATION = PACKAGE_LOCATION.parent
RECORDINGS_LOCATION = ROOT_LOCATION / "recordings"
RECORDINGS_LOCATION.mkdir(exist_ok=True)
