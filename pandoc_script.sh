for i in *.md; do
    pandoc "$i" --pdf-engine=xelatex -o "${i%.*}.pdf"
done
