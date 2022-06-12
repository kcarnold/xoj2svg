.PHONY: install uninstall

DESTDIR=
PREFIX=/usr/local

CP=cp
INSTALL=install
LN=ln
MKDIR=mkdir -p
RM=rm -f -v

install:
	$(MKDIR) "$(DESTDIR)$(PREFIX)/share/xoj2svg"
	$(INSTALL) -m0755 xoj2svg.py "$(DESTDIR)$(PREFIX)/share/xoj2svg/xoj2svg.py"
	$(MKDIR) "$(DESTDIR)$(PREFIX)/bin"
	$(LN) -sf "$(PREFIX)/share/xoj2svg/xoj2svg.py" "$(DESTDIR)$(PREFIX)/bin/xoj2svg"

uninstall:
	$(RM) -R "$(DESTDIR)$(PREFIX)/bin/xoj2svg" "$(DESTDIR)$(PREFIX)/share/xoj2svg"
