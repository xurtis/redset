pkgpython_PYTHON = __init__.py redshift.py
nodist_pkgpython_PYTHON = defs.py

dist_bin_SCRIPTS = redset

EXTRA_DIST = defs.py.in redset.in
CLEANFILES = defs.py redset

# Local python definitions
defs.py: defs.py.in
	sed -e "s|\@bindir\@|$(bindir)|g" \
		-e "s|\@localedir\@|$(localedir)|g" $< > $@

# Python path for binary
redset: redset.in
	sed -e "s|\@pythondir\@|$(pythondir)|g" $< > $@
