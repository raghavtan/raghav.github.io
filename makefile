ifneq ($(shell command -v tput 2> /dev/null),)
    YELLOW := $(shell tput setaf 3)
    GREEN := $(shell tput setaf 2)
    RED := $(shell tput setaf 1)
    BLUE := $(shell tput setaf 4)
    RESET := $(shell tput sgr0)
else
    YELLOW := ""
    GREEN := ""
    RED := ""
    BLUE := ""
    RESET := ""
endif

# Virtual environment directory
VENV := venv

# Python commands
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

# Docker image name
IMAGE_NAME := simple-service
PORT := $(or $(PORT),8000)

.PHONY: help virtualenv clean install activate setup generate lint

help:  ## Show this help message
	@echo "$(YELLOW)Available commands:$(RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-20s$(RESET) %s\n", $$1, $$2}'

# Setup virtual environment
virtualenv:  ## Setup the python virtual environment
	@echo "$(BLUE)Setting up virtual environment...$(RESET)"
	@python3 -m venv $(VENV)
	@echo "$(GREEN)Virtual environment created.$(RESET)"

clean:  ## Clean up virtual environment and all temporary files
	@echo "$(RED)Cleaning up...$(RESET)"
	@rm -rf $(VENV) __pycache__ *.pyc *.pyo .pytest_cache .mypy_cache
	@rm -rf resume.md resume.pdf resume.html
	@echo "$(GREEN)Cleanup done.$(RESET)"

install:   ## Install requirements in the virtual environment
	@echo "$(BLUE)Installing requirements...$(RESET)"
	@$(PIP) install -r requirements.txt
	@echo "$(GREEN)Requirements installed.$(RESET)"

activate:  ## Activate the virtual environment
	@echo "$(YELLOW)To activate the virtual environment, run:$(RESET)"
	@echo "source $(VENV)/bin/activate"

generate: ## Run the generate script
	@echo "$(BLUE)Running the generate script...$(RESET)"
	@$(PYTHON) main.py
	@echo "$(GREEN)Generate script complete.$(RESET)"

lint:  ## Lint the application with flake8
	@echo "$(BLUE)Linting the application...$(RESET)"
	@$(VENV)/bin/flake8 . --exclude=$(VENV)
	@echo "$(GREEN)Linting complete.$(RESET)"

# Setup and run for new developers
setup: virtualenv activate install