import sys
import random

import click

from .worddata import wordle_dict


def _invalidLetters(word, green, yellow):
    return (
        set(word) - set([l.lower() for l in yellow]) - set([l.lower() for l in green])
    )


def _filterByInvalidLetters(word, wordlist, green, yellow):
    invalidLetters = _invalidLetters(word, green, yellow)
    return list(
        filter(
            lambda word: not any(letter in word for letter in invalidLetters), wordlist
        )
    )


def _indices(mixedCaseWord):
    return [
        (index, letter)
        for index, letter in enumerate(mixedCaseWord)
        if letter.isupper()
    ]


def _filterByIndices(wordlist, indices, invalidComp):
    invalid = []
    for index in indices:
        for word in wordlist:
            if invalidComp(index, word):
                invalid.append(word)
    return list(set(wordlist) - set(invalid))


def _filterByGreenIndices(wordlist, indices):
    return _filterByIndices(
        wordlist,
        indices,
        lambda index, word: word[index[0]].lower() != index[1].lower(),
    )


def _filterByYellowIndices(wordlist, indices):
    # First, filter out the words that don't have the letter in them at all
    remaining = _filterByIndices(
        wordlist, indices, lambda index, word: index[1].lower() not in word
    )
    # Then filter words where the letter is in the known wrong position
    return _filterByIndices(
        remaining,
        indices,
        lambda index, word: word[index[0]].lower() == index[1].lower(),
    )


def _determineRemaining(word, wordlist, green, yellow):
    greenIndicies = _indices(green)
    yellowIndices = _indices(yellow)
    remaining = _filterByInvalidLetters(
        word, wordlist, [x[1] for x in greenIndicies], [x[1] for x in yellowIndices]
    )
    remaining = _filterByGreenIndices(remaining, greenIndicies)
    remaining = _filterByYellowIndices(remaining, yellowIndices)

    # don't forget to remove the initial word from the list
    return list(set(remaining) - set([word]))


def _runCycle(word, wordlist):
    click.echo(f"Word: {word.upper()}")
    if click.confirm("Did I guess correctly?"):
        click.echo("Wonderful, I knew I would")
        sys.exit(0)

    greenWord = ""
    while greenWord.lower() != word.lower():
        greenWord = click.prompt(f"Type {word}, but only capitalize the GREEN letters", default=word, show_default=True)

    yellowWord = ""
    while yellowWord.lower() != word.lower():
        yellowWord = click.prompt(f"Type {word}, but only capitlize the YELLOW letters", default=word, show_default=True)

    return _determineRemaining(word, wordlist, greenWord, yellowWord)

@click.command()
@click.option("--start-with", default="aesir", help="Word to start with")
def solve(start_with):
    remainingWords = wordle_dict
    startingWord = start_with 
    iterator = 0

    click.echo(f"Searching through {len(remainingWords)} for the answer...")

    while iterator <= 6 and len(remainingWords) != 0:
        remainingWords = _runCycle(startingWord, remainingWords)
        iterator = iterator + 1

        click.echo(f"Hmm... well, only {len(remainingWords)} words left to try!")
        #TODO - a good optimization would be to use letter_freq to choose the next word
        #For now, choose a random word from the remaining words...
        startingWord = random.choice(remainingWords)

    if iterator == 7:
        click.echo("Sorry, I tried my best!")


if __name__ == "__main__":
    solve()


