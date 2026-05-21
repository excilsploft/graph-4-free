image := example_01
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

.PHONY: clean
clean:
	-rm $(svg)
	-rm $(png)
