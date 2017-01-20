## cookiecutter-pylibng

![cookies!](https://source.unsplash.com/Qx8xIXhyB5Q/888x300)

A poorly named [cookiecutter] for quickly scaffolding new Python
libraries.

Some of the batteries included:

* An [EditorConfig] file.
* A fairly complete `setup.py`, and versioning built-in with
  [setuptools_scm].
* Choice of MIT, Apache 2.0, and GPLv3 licenses.
* Best practices for Python distribution organization.
* Pre-configured [tox].ini, with [Tox-Travis] and `.travis.yml`.
* Requirements organized with [reqwire].
* Sphinx documentation.
* [Mypy] and typing support.

The generated distribution skeleton is compatible with Python 2.7 and
above.

[cookiecutter]: https://github.com/audreyr/cookiecutter
[EditorConfig]: http://editorconfig.org/
[Mypy]: http://mypy.readthedocs.io/en/latest/
[reqwire]: https://github.com/darvid/reqwire
[setuptools_scm]: https://github.com/pypa/setuptools_scm
[tox]: https://tox.readthedocs.io/en/latest/
[Tox-Travis]: http://tox-travis.readthedocs.io/en/stable/

### Usage

```shell
$ # If cookiecutter isn't already installed, install with:
$ pip install cookiecutter
$ cookiecutter gh:darvid/cookiecutter-pylibng
```

### Next Steps

*Detailed next steps and full configuration guide coming soon™...*

```shell
$ cd myproject/
$ # Using reqwire is optional, feel free to use a vanilla requirements.txt.
$ pip install reqwire
$ reqwire build -a
$ # You can now install requirements from requirements/lck/main.txt in
$ # your environment of choosing (i.e. virtualenv, pyenv)
$ pip install -r requirements/lck/main.txt
$ # Before installation, you must initialize a Git repo
$ git init
$ # Finally, install your library in development mode
$ python setup.py develop
```

