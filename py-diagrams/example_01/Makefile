image := example_01
src := $(addsuffix .py, $(image))
svg := $(addsuffix .svg, $(image))
png := $(addsuffix .png, $(image))

default: build
.PHONY: build
build: $(svg) $(png)

$(svg): $(src) $(png)

$(png): $(src)
	@python $< $@

.PHONY: clean
clean:
	-rm $(svg)
	-rm $(png)

