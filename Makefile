# One command: regenerate public/legal/ from legal/*.md. The HTML is never hand-edited.
legal:
	python3 legal-site/build.py
.PHONY: legal
