PY = python3

SRC_DIR = src
BIN_DIR = $(SRC_DIR)/__pycache__

SRC = $(wildcard $(SRC_DIR)/*.py)

_MAIN = main.py
MAIN = $(SRC_DIR)/$(_MAIN)

run: $(SRC)
	@$(PY) $(MAIN)

.PHONY: clean
clean:
	@sudo rm -rf $(BIN_DIR)
