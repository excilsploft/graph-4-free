image := $(shell basename $$(pwd))
dot := $(addsuffix .dot, $(image))
svg := $(addsuffix .svg, $(image))
png := $(addsuffix .png, $(image))
logos := $(wildcard **/*.png)

default: build

.PHONY: build
build: $(svg) $(png)

$(dot): $(logos)

$(svg): $(dot) $(logos)
	@dot -Tsvg $< -o $@

$(png): $(dot) $(logos)
	@dot -Tpng $< -o $@

.PHONY: clean
clean:
	-rm $(svg)
	-rm $(png)
