mal
===

**mal** is a console interface to GitHub.  It has both a curses based interface
and a command line repl.

**mal** is written using [RDD][rdd].  If this very paragraph is still present
when you read this, the RDD process is not yet complete and features described
in this README might not have been implemented yet.  There might be dragons.


## Features

* ncurses interface that mimics the experience of the GitHub web UI:
  * Start page similar to the activity feed
  * Repository and user browsing
  * Quickfast cloning and forking
  * Smooth tmux integration for dropping into own workspaces of repositories
  * Beautiful 256 color support
  * Configurable vi/emacs-style keybindings

* Command line repl for use inside repositories:
  * Interactive context aware prompt
  * Listing of issues and pull requests
  * Commenting, closing and merging said pull requests
  * Completion of all commands and most git objects

* Offline mode!  Browsing repositories will download GitHub centric metadata to
  them in full.  All the data can be browsed locally, and issues and pull
  requests can be modified locally and pushed to GitHub at a later time,
  allowing for the disconnected workflow that normal git encourages.

* Support for using both the GitHub main API and GitHub Enterprise APIs
* [tig][tig] support for browsing repository logs

## Installation

`python setup.py install`


## Invocation

`mal curses` will start the curses interface.

`mal` will start the repl.  Any valid subcommand (e.g. `mal issues`) can also
be in the invocation, and that will print the same thing as the repl would.

When started from within a directory that is a part of a git repository, both
the curses interface and the repl will start with the context of that
repository.


## Configuration

**mal** listens to a global and a local configuration file;
`/etc/xdg/mal/config.yml` and `$HOME/.config/mal/config.yml`, respectively.
All defaults are stored in the global file, and any values in the local one
will override them.

To avoid inevitable out-of-sync issues with this README, all configuration
values and their documentation are stored in `config/global.yml` in this
repository.


## Authentication

When `mal` is invoked and no OAuth token is stored at
`$HOME/.local/share/mal/oauth.key` the process of retrieving a token will
start.

It is not possible to use plain user/password authentication, because storing
passwords in plain text is *a bad thing*.


## License

**mal** is licensed under the MIT license.


[rdd]: http://tom.preston-werner.com/2010/08/23/readme-driven-development.html
[mal]: http://rpggamer.org/uploaded_images/MalcolmReynolds13.jpg
[tig]: https://github.com/jonas/tig
