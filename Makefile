all: clean compile removetemporaries

compile:
	pdflatex bericht.tex
	bibtex8 -W bericht
	pdflatex bericht.tex
	pdflatex bericht.tex

clean:
	rm -f *pdf *dvi *aux *toc *log *blg *bbl
	
removetemporaries:
	rm -f *aux *toc *log *blg *bbl
