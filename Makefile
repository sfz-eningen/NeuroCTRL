PKGNAME=NeuroCTRL_Cyton
PRINT=@echo
I_OPT=Ateempting to install
LEND=.
CC=pyinstaller
COPT=-y

install:
	$(PRINT) $(I_OPT) $(PKGNAME)$(LEND)
	# $(CC) $(COPT) ./