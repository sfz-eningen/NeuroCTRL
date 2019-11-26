PKGNAME=NeuroCTRL_Cyton
PRINT=@echo
I_OPT=Ateempting to install
LEND=.
CC=pyinstaller
COPT=-y -F
PATH=./Cyton/graphics/
install:
	$(PRINT) $(I_OPT) $(PKGNAME)$(LEND)
	$(CC) $(COPT) $(PATH)

GIT_RESET=git reset HEAD --hard
GIT_CLEAN=git clean -fd
clean:
	$(GIT_RESET)
	$(GIT_CLEAN)
	