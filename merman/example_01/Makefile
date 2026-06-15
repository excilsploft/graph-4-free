image := example_01
src := $(addsuffix .mmd, $(image))
svg := $(addsuffix .svg, $(image))
png := $(addsuffix .png, $(image))

default: build

.PHONY: build
build:  $(svg) $(png)

$(svg): $(src) 
	@merman-cli -i $< -o $@

$(png): $(src)
	@merman-cli -i $< -o $@

.PHONY: clean
clean:
	-rm $(svg)
	-rm $(png)
