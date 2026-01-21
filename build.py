#!/usr/bin/env python3
import subprocess
import sys

def main():
    print("Compiling LaTeX...")
    result = subprocess.run(["pdflatex", "-interaction=nonstopmode", "connolly-resume.tex"])
    if result.returncode != 0:
        print("LaTeX compilation failed. Check that deps are installed and on PATH.")
        sys.exit(1)

    print("Generating preview...")
    result = subprocess.run(["pdftoppm", "-png", "-r", "150", "-singlefile", "connolly-resume.pdf", "preview"])
    if result.returncode != 0:
        print("Preview generation failed. Ensure you have pdftoppm and it is on PATH.")
        sys.exit(1)

    print("Build complete, you may now commit and push")

if __name__ == "__main__":
    main()
