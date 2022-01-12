from collections import Counter
import sys


with open("words_alpha.txt") as f:
    words = f.read().splitlines()
letter_cnt = Counter()
five_letter_candidates = set()
for w in words:
    if len(w) == 5 and len(set(w)) == 5:
        letter_cnt.update(set(w))
        five_letter_candidates.add(w)
candidates_weighted: dict[int, str] = {
    w: sum(letter_cnt[c] for c in w) for w in five_letter_candidates
}
candidates_weighted = dict(
    sorted(candidates_weighted.items(), key=lambda x: x[1], reverse=True)
)
candidates = list(candidates_weighted.keys())
print("Top candidates: ", list(candidates)[:20])
print(f"number of candidates left={len(candidates)}")
for _ in range(6):
    word = input("Enter a word: ")
    print("0 - no, 1 - yes, position is wrong, 2 - yes, position is right.")
    for i, letter in enumerate(word):
        answer = input(f"Is the letter {letter} present in word? Letter {letter}: ")
        match answer:
            case "0":  # letter not in the word
                candidates = {word for word in candidates if letter not in word}
            case "1":  # letter in the word, wrong position
                candidates = {
                    word for word in candidates if letter in word and word[i] != letter
                }
            case "2":  # letter in the word, right position
                candidates = {word for word in candidates if word[i] == letter}
            case _:
                print("Wrong input. Exiting...")
                sys.exit(1)
    print("Top candidates:", ", ".join(list(candidates)[:30]))
    print(f"number of candidates left={len(candidates)}")
    if len(candidates) < 2:
        break
