all: build/main.pdf

# hier Python-Skripte:
build/plot_countd24.pdf: plotd24-c.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plotd24-c.py

build/plot_E24.pdf: plotE24.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plotE24.py

build/plot_countd42.pdf: plotd42-c.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plotd42-c.py

build/plot_E42.pdf: plotE42.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plotE42.py

build/plot_gauss.pdf: gauss.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python gauss.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot_countd24.pdf build/plot_E24.pdf build/plot_countd42.pdf build/plot_E42.pdf build/plot_gauss.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
