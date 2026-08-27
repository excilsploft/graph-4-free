image := $(shell basename $$(pwd))
dot := $(addsuffix .dot, $(image))
svg := $(addsuffix .svg, $(image))
png := $(addsuffix .png, $(image))

default: build

.PHONY: build
build: $(svg) $(png)

$(svg): $(dot)
	@dot -Tsvg $< -o $@

$(png): $(dot)
	@dot -Tpng $< -o $@

.PHONY: nop
nop: $(dot)
	dot -Knop2 $<

.PHONY: clean
clean:
	-rm $(svg)
	-rm $(png)
