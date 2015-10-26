~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Woolworths Money plugin for  ofxstatement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is an ofxstatement plugin for Woolworths Money.

`ofxstatement`_ is a tool to convert proprietary bank statement to OFX format,
suitable for importing to GnuCash. Plugin for ofxstatement parses a
particular proprietary bank statement format and produces common data
structure, that is then formatted into an OFX file.

.. _ofxstatement: https://github.com/kedder/ofxstatement


Setting up development environment
==================================

It is recommended to use ``virtualenv`` make a clean development environment.
Setting up dev environment for writing a plugin is easy::

  $ git clone https://github.com/shenki/ofxstatement-woolworthsmoney
  $ cd ofxstatement-woolworthsmoney
  $ virtualenv -p python3 --no-site-packages .venv
  $ . .venv/bin/activate
  (.venv)$ python setup.py develop

This will download all the dependencies and install them into your virtual
environment. After this, you should be able to do::

  (.venv)$ ofxstatement list-plugins
  The following plugins are available:

    woolworthsmoney           Plugin for Woolworths Money (Australia)
