image := example_02
src := $(addsuffix .d2, $(image))
svg := $(addsuffix .svg, $(image))
png := $(addsuffix .png, $(image))

default: build

.PHONY: build
build: $(svg) $(png)

$(svg): $(src) 
	@d2 --layout=Dagre $< $@

$(png): $(src)
	@d2 --layout=Dagre $< $@

.PHONY: clean
clean:
	-rm $(svg)
	-rm $(png)
