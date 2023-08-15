# Build

To get Debug messages printed from DistUtils/Setuptools, we need to set an ENV var to any (non-blank) value

    let $DISTUTILS_DEBUG = '1'
    unlet $DISTUTILS_DEBUG


Build and examine the contents of the Wheel:

    pip install wheel

    setup.py bdist_wheel
    for %w in (.\dist\*.whl) do @(7z x -bb1 -y -o%~nw %w)

# Install Locally

Editable install:

    py -3 -m pip install --editable .
    dir /b /s /a C:\Python39\Lib\site-packages\jayminizip*

Direct WHEEL instal:

    for %w in (.\dist\*.whl) do @(py -3 -m pip install %w)
    dir /b /s /a-d C:\Python39\Lib\site-packages\jayminizip

# Uninstall

    py -3 -m pip uninstall -y jayminizip


# Clean

    setup.py clean --all
    echo Now performing manual clean steps...
    rm -rf .eggs
    rm -rf build
    rm -rf dist
    for /f "tokens=*" %d in ('dir /b /s /ad jayminizip-*-*-*-* 2^>nul') do @(echo removing %d&rmdir /s /q "%~d")
    for /f "tokens=*" %d in ('dir /b /s /ad *.egg-info 2^>nul') do @(echo removing %d&rmdir /s /q "%~d")
    for /f "tokens=*" %d in ('dir /b /s /ad __pycache__ 2^>nul') do @(echo removing %d&rmdir /s /q "%~d")


---

