# Vortex Java: common steps. Usage: make slides L=2   (L defaults to 1)
L ?= 1

status:
	python3 scripts/status.py

slides:
	python3 scripts/make_slides.py $(L)

video:
	python3 scripts/assemble.py $(L)

.PHONY: status slides video
