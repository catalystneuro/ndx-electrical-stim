# Next Steps for ndx-electrical-stim Extension for NWB:N

## Creating Your Extension

1. In a terminal, change directory into the new ndx-electrical-stim directory.

2. Add any packages required by your extension to `requirements.txt` and `setup.py`.

3. Run `python -m pip install -r requirements.txt` to install the `pynwb` package
and any other packages required by your extension.

4. Modify `src/create_extension_spec.py` to define your extension.

    - If you want to create any custom classes for interacting with the extension,
      add them to the `src/pynwb`.
      - If present, the `src/pynwb` folder MUST contain the following:
        - `ndx-electrical-stim` - Folder with the sources of the NWB extension
        - `ndx-electrical-stim/__init__.py` - Python file that may be empty
        - `requirements.txt` - Text file listing the Python package requirements for the extension
        - `README.md` - Markdown file describing the NWB extension
      - If present, the `src/pynwb` folder MAY contain the following files/folders:
        - `test` - Folder for unit tests for the extensions
        - `jupyter-widgets` - Optional package with custom widgets for use with Jupyter

5. Run `python src/spec/create_extension_spec.py` to generate the
`spec/ndx-electrical-stim.namespace.yaml` and
`spec/ndx-electrical-stim.extensions.yaml` files.

6. You may need to modify `setup.py` and re-run `python setup.py install` if you
use any dependencies.


## Documenting and Publishing Your Extension to the Community

1. Clone the latest nwb-docutils repository https://github.com/nwb-extensions-test/ndx-template.git
or install the latest release:
`python -m pip install nwb-docutils`
    - If you cloned the latest version, run `python setup.py install` to install nwb-docutils locally.

2. Start a git repository for your extension directory ndx-electrical-stim
 and push it to GitHub. You will need a GitHub account.
    - Follow these directions:
  https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line

3. Change directory into `docs`.

4. Run `make html` to generate documentation for your extension based on the YAML files.

5. Read `docs/README.md` for instructions on how to customize documentation for
your extension.

6. Modify `README.md` to describe this extension for interested developers.

7. Add a license file. Permissive licenses should be used if possible. **A [BSD license](https://opensource.org/licenses/BSD-3-Clause) is recommended.**

8. Make a release for the extension on GitHub with the version number specified. e.g. if version is 0.1.0, then this page should exist: https://github.com/jrliu95/ndx-electrical-stim/releases/tag/0.1.0

9. Publish your updated extension on PyPi.
    - Follow these directions: https://packaging.python.org/tutorials/packaging-projects/
    - You may need to modify `setup.py`
    - If your extension version is 0.1.0, then this page should exist: https://pypi.org/project/ndx-electrical-stim/0.1.0

10. Go to https://github.com/nwb-extensions/staged-extensions and fork the
repository.

10. Clone the fork onto your local filesystem.

10. Copy the directory `staged-extensions/example` to a new directory
`staged-extensions/ndx-electrical-stim`:

    ```bash
cp -r staged-extensions/example staged-extensions/ndx-electrical-stim
```

11. Edit `staged-extensions/ndx-electrical-stim/ndx-meta.yaml`
with information on where to find your NWB extension.
    - The YAML file MUST contain a dict with the following keys:
      - name: extension namespace name
      - version: extension version
      - src: URL for the main page of the public repository (e.g. on GitHub, BitBucket, GitLab) that contains the sources of the extension
      - pip: URL for the main page of the extension on PyPI
      - license: name of the license of the extension
      - maintainers: list of GitHub
      usernames of those who will reliably maintain the extension
    -

  You may copy and modify the following YAML that was auto-generated:
```yaml
name: ndx-electrical-stim
version: 0.1.0
src: https://github.com/jrliu95/ndx-electrical-stim
pip: https://pypi.org/project/ndx-electrical-stim/
license: BSD 3-Clause
maintainers:
  - jrliu95
```

12. Edit `staged-extensions/ndx-electrical-stim/README.md`
to add information about your extension. You may copy it from
`ndx-electrical-stim/README.md`.

  ```bash
cp ndx-electrical-stim/README.md staged-extensions/ndx-electrical-stim/README.md
```

13. Git commit and push your changes to GitHub.

14. Open a pull request. Building of your extension will be tested on Windows,
Mac, and Linux. The technical team will review your extension shortly after
and provide feedback and request changes, if any.

15. When your pull request is merged, a new repository, called
ndx-electrical-stim-feedstock will be created in the nwb-extensions
GitHub organization and you will be added as a maintainer for that repository.


## Updating Your Published Extension

1. Update your ndx-electrical-stim GitHub repository.

2. Publish your updated extension on PyPi.

3. Fork the ndx-electrical-stim-feedstock repository on GitHub.

4. Open a pull request to test the changes automatically. The technical team
will review your changes shortly after and provide feedback and request changes,
 if any.

5. Your updated extension is approved.
