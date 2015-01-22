armin-build
-----------

### Build package frm Gitlab

### Usage:

    $ armin-build [OPTIONS] PROJECT_ID NAME PATH --src --out

### Arguments:

* `PROJECT_ID`: gitlab namespace with project name, eg. 'tonic/marco'
* `NAME`: package name
* `PATH`: /etc,/usr/bin,/usr/local/bin ...
* `src`: target folder to clone code, if not set, temp folder will be created and used
* `out`: folder where package will be placed, if not set, /tmp will be used

Good luck!
