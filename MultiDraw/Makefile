target=libmultidraw.so
src=$(wildcard src/*.cc)
obj=$(patsubst src/%.cc,obj/%.o,$(src))
inc=$(patsubst src/%.cc,interface/%.h,$(src))

copts=-DGNU_GCC -D_GNU_SOURCE -Werror=main -Werror=pointer-arith -Werror=overlength-strings -Wno-vla -Werror=overflow -std=c++14 -ftree-vectorize -Wstrict-overflow -Werror=array-bounds -Werror=format-contains-nul -Werror=type-limits -fvisibility-inlines-hidden -fno-math-errno --param vect-max-version-for-alias-checks=50 -fipa-pta -Wa,--compress-debug-sections -msse3 -felide-constructors -fmessage-length=0 -Wall -Wno-non-template-friend -Wno-long-long -Wreturn-type -Wunused -Wparentheses -Wno-deprecated -Werror=return-type -Werror=missing-braces -Werror=unused-value -Werror=address -Werror=format -Werror=sign-compare -Werror=write-strings -Werror=delete-non-virtual-dtor -Werror=maybe-uninitialized -Werror=strict-aliasing -Werror=narrowing -Werror=uninitialized -Werror=unused-but-set-variable -Werror=reorder -Werror=unused-variable -Werror=conversion-null -Werror=return-local-addr -Werror=switch -fdiagnostics-show-option -Wno-unused-local-typedefs -Wno-attributes -Wno-psabi

$(target): $(obj) obj/dict.o
	g++ -std=c++14 -O2 -fPIC -shared $(shell root-config --libs) -o $@ $^

obj/dict.o: $(inc) obj/LinkDef.h
	mkdir -p obj
	rootcling -f obj/libmultidraw.cc $^
	mv obj/libmultidraw_rdict.pcm .
	g++ -std=c++14 -O2 -fPIC -c -o $@ -I$(shell root-config --incdir) -I$(shell pwd) obj/libmultidraw.cc

obj/LinkDef.h:
	mkdir -p obj
	./mkLinkDef.py

obj/%.o: src/%.cc $(inc)
	mkdir -p obj
	g++ $(copts) -O2 -fPIC -c -o $@ -I$(shell root-config --incdir) $<

.PHONY: clean

clean:
	rm -rf obj libmultidraw*
