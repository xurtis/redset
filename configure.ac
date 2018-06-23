AC_INIT([redset], [0.1], [curtis@curtism.me])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AC_CONFIG_FILES([
	Makefile
	src/Makefile
])

# Optional bundled redshift
AC_ARG_WITH(
	[redshift],
	[AS_HELP_STRING(
		[--without-redshift],
		[Do not install redshift (default is yes)]
	)],
	[use_redshift=no],
	[enable_redshift=yes]
)

# Install a local copy of redshift
if test "x$enable_redshift" = "xyes"; then
	AC_CONFIG_SUBDIRS([redshift])
fi
AM_CONDITIONAL([ENABLE_REDSHIFT], [test "x$enable_redshift" = "xyes"])

# Check for Python
AM_PATH_PYTHON([2.7])

AC_OUTPUT
