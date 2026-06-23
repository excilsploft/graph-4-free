image := $(shell basename $$(pwd))
src := $(addsuffix .d2, $(image))
svg := $(addsuffix .svg, $(image))
png := $(addsuffix .png, $(image))

default: build

.PHONY: build
build: $(svg) $(png)

$(src): $(lastword $(MAKEFILE_LIST))
	@test -f $@ && rm $@ || touch $@
	@printf "'%s' -> '%s': make\n" $< $@ >> $@
	@printf "'%s' -> '%s': d2\n" $@ $(svg) >> $@
	@printf "'%s' -> '%s': d2\n" $@ $(png) >> $@
	
$(svg): $(src)
	@d2 -t 101 $< $@

$(png): $(src)
	@d2 -t 101 $< $@

.PHONY: print
print: $(src)
	@d2 fmt $<
	@cat $<

.PHONY: clean
clean:
	-@rm $(src)
	-@rm $(svg)
	-@rm $(png)
