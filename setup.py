from setuptools import setup

APP = ["bandwidth_monitor.py"]
DATA_FILES = ["icon.icns"]
OPTIONS = {
    "argv_emulation": False,
    "plist": {
        "CFBundleIconFile": "icon",
        "CFBundleName": "Bandwidth Monitor",
        "CFBundleDisplayName": "Bandwidth Monitor",
        "CFBundleVersion": "1.0.0",
        "CFBundleShortVersionString": "1.0",
        "LSUIElement": True,
    },
    "packages": ["rumps", "psutil"],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
