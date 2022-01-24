# wordle-solver
Helps to solve [Wordle](https://www.powerlanguage.co.uk/wordle/).

Twitter thread with an explanation https://twitter.com/smirnoffs/status/1481381667126325250

And yes, it is Python 3.10, because I wanted to try match cases somewhere. I think I like match cases!

Example output:

```
❯ python main.py
Top candidates:  ['raise', 'aesir', 'serai', 'arise', 'oreas', 'arose', 'arsle', 'reals', 'lears', 'slare', 'earls', 'seral', 'laser', 'arles', 'rales', 'lares', 'resat', 'treas', 'arest', 'teras']
number of candidates left=10171
Enter a word: arise
0 - no, 1 - yes, position is wrong, 2 - yes, position is right.
Is the letter a present in word? Letter a: 1
Is the letter r present in word? Letter r: 1
Is the letter i present in word? Letter i: 0
Is the letter s present in word? Letter s: 0
Is the letter e present in word? Letter e: 0
Top candidates: pargo, rhamn, payor, volar, labor, poral, uparm, lyart, carum, thrax, nagor, mohar, marok, kurta, tardy, korma, garum, lunar, cumar, tarok, marco, harpy, favor, doura, nacry, knarl, murat, roman, rogan, royal
number of candidates left=324
Enter a word: rotal
0 - no, 1 - yes, position is wrong, 2 - yes, position is right.
Is the letter r present in word? Letter r: 1
Is the letter o present in word? Letter o: 1
Is the letter t present in word? Letter t: 0
Is the letter a present in word? Letter a: 1
Is the letter l present in word? Letter l: 0
Top candidates: narco, karou, ozark, pargo, cardo, payor, dargo, carbo, nahor, pharo, pardo, carom, baron, manor, garon, fardo, marko, nagor, marok, bardo, jarmo, ovary, vapor, marco, carob, cargo, phora, major, chora, garbo
number of candidates left=33
Enter a word: baron
0 - no, 1 - yes, position is wrong, 2 - yes, position is right.
Is the letter b present in word? Letter b: 0
Is the letter a present in word? Letter a: 2
Is the letter r present in word? Letter r: 1
Is the letter o present in word? Letter o: 2
Is the letter n present in word? Letter n: 0
Top candidates: payor, major, favor, vapor, mayor
number of candidates left=5
Enter a word: favor
0 - no, 1 - yes, position is wrong, 2 - yes, position is right.
Is the letter f present in word? Letter f: 2
Is the letter a present in word? Letter a: 2
Is the letter v present in word? Letter v: 2
Is the letter o present in word? Letter o: 2
Is the letter r present in word? Letter r: 2
Top candidates: favor
number of candidates left=1
```

24.01.2022
Today the word was `knoll` and the solver didn't work!!! (╯°□°）╯︵ ┻━┻
