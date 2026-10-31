# Contributing

Thank you for helping improve this curriculum. Errors in a training course cost real time, so corrections are especially welcome.

## Report a problem

Open an issue. The most useful reports say:

- which lesson or lab, and which step;
- your BrailleBlaster **version** and operating system;
- what the book says, what you saw, and what you expected.

Menu paths and shortcuts change between releases, so the version matters.

## Change the book

1. Edit files in `my-book/src`. Never edit `my-book/docs`.
2. Follow the lesson pattern in the README.
3. Run the checks before you open a pull request:

   ```bash
   python3 tools/check_book.py
   mdbook build my-book
   ```

4. If you change a menu path or shortcut, say **which BrailleBlaster version you verified it with** in the pull request.
5. If you change the sample files, edit `tools/build_samples.py` and re-run it. Do not edit the generated files by hand.

## Standards for content

- Cite *Braille Formats 2016* sections where a rule is stated.
- Use plain language, and write for learners who may be using a screen reader or a braille display. Do not rely on color or position to carry meaning.
- Give every image a text alternative.
- Write original sample text, or record its source and license.
- Do not copy passages from copyrighted works. Link and summarize instead.
- Describe behaviors you have not verified as expectations, and say so.

## Conduct

Be kind, assume good faith, and remember that the people who read this book include learners who are new to braille.
