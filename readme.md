# PyWordleSolver

## Motivation
I hate word puzzles, because I'm dumb at words (seriously- scrabble is my achilles heel).  So when everyone starts sharing how smart they are all over social media, I get jealous and do what I am smart at.  I'm pretty sure this will solve any Wordle, so you too can look smart.

## Installation
Look- this isn't really a serious repository.  If you don't know how to install a python module outside of ```pip```, it probably isn't for you.  If you do know how to install a python module outside of ```pip``` you probably don't need my help.  But here goes:

1. Clone the repository to a local directory: ```git clone https://github.com/harriscm/PyWordleSolver.git```
2. Change to the newly created directory: ```cd PyWordleSolver```
3. Install as a python module: ```python install .```
4. There is no step 4.

## Usage
Run the application, it will print a word (it will use AUDIO, because that is a good first word- it immediately solves your vowel issue).  Put that word into your app, then follow the on screen prompts to tell the solver what your green and yellow letters are.  It will then eliminate words that don't fit the rules and print a new word.  There are 2500 (ish) 5-letter words, but this whittles it down pretty quickly.

```
$ pywordle
Word: AUDIO
Did I guess correctly? [y/N]: n
Type audio, but only capitalize the GREEN letters: audio
Type audio, but only capitlize the YELLOW letters: audiO
Hmm... well, only 282 words left to try!
Word: SLOOP
Did I guess correctly? [y/N]: n
Type sloop, but only capitalize the GREEN letters: slOop
Type sloop, but only capitlize the YELLOW letters: slooP
Hmm... well, only 13 words left to try!
Word: PROVE
Did I guess correctly? [y/N]: n
Type prove, but only capitalize the GREEN letters: prOve
Type prove, but only capitlize the YELLOW letters: ProvE
Hmm... well, only 2 words left to try!
Word: EPOXY
Did I guess correctly? [y/N]: n
Type epoxy, but only capitalize the GREEN letters: EPOxy
Type epoxy, but only capitlize the YELLOW letters: epoxy
Hmm... well, only 1 words left to try!
Word: EPOCH
Did I guess correctly? [y/N]: y
Wonderful, I knew I would
```

## Known Issues
Known is a bit harsh- but there are some corner cases I suspect may be issues.  I'm somewhat convinced a situation where you have two identical vowels and 1 is in a green and 1 is in a yellow could cause some problems.  But I haven't seen it yet, and according to the Quantum Theory of Code Testing, a bug cannot exist until it is observed.

I have no plans to fix this though, because again the only reason I did this was so I can feel smarter than the smart word people :)
