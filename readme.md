# PyWordleSolver

## Motivation
I hate word puzzles, because I'm dumb at words (seriously- scrabble is my achilles heel).  So when everyone starts sharing how smart they are all over social media, I get jealous and do what I am smart at.  I'm pretty sure this will solve any Wordle, so you too can look smart.

## Installation
Look- this isn't really a serious repository.  If you don't know how to install a python module outside of ```pip```, it probably isn't for you.  If you do know how to install a python module outside of ```pip``` you probably don't need my help.  But here goes:

1. Clone the repository to a local directory: ```git clone https://github.com/harriscm/PyWordleSolver.git```
2. Change to the newly created directory: ```cd PyWordleSolver```
3. Install as a python module: ```pip install .```
4. There is no step 4.

## Usage
Run the application, it will print a starting word. The default starting word is AESIR, but you can change the behavior with the --start-with flag.  Put that word into your app, then follow the on screen prompts to tell the solver what your green and yellow letters are.  It will then eliminate words that don't fit the rules and print a new word.  There are 12972 5-letter words, but this whittles it down pretty quickly.  One caveat, different Wordle implementations apparently use different lists of valid words.  This is the largest list I have found, but that means sometimes your implementation may complain about an invalid word.  The best thing you can do in that instance is stop play, and restart using the last word you put in the app as the starting word.

```
$ pywordle
Searching through 12972 for the answer...
Word: AESIR
Did I guess correctly? [y/N]: n
Type aesir, but only capitalize the GREEN letters [aesir]: aesir
Type aesir, but only capitlize the YELLOW letters [aesir]: AEsir
Hmm... well, only 364 words left to try!
Word: ZOEAE
Did I guess correctly? [y/N]: n
Type zoeae, but only capitalize the GREEN letters [zoeae]: zoeaE
Type zoeae, but only capitlize the YELLOW letters [zoeae]: zoeAe
Hmm... well, only 107 words left to try!
Word: DALLE
Did I guess correctly? [y/N]: n
Type dalle, but only capitalize the GREEN letters [dalle]: dAllE
Type dalle, but only capitlize the YELLOW letters [dalle]: daLle
Hmm... well, only 19 words left to try!
Word: BAYLE
Did I guess correctly? [y/N]: n
Type bayle, but only capitalize the GREEN letters [bayle]: bAylE
Type bayle, but only capitlize the YELLOW letters [bayle]: bayLe
Hmm... well, only 5 words left to try!
Word: LATHE
Did I guess correctly? [y/N]: y
Wonderful, I knew I would
```

## Known Issues
Known is a bit harsh- but there are some corner cases I suspect may be issues.  I'm somewhat convinced a situation where you have two identical vowels and 1 is in a green and 1 is in a yellow could cause some problems.  But I haven't seen it yet, and according to the Quantum Theory of Code Testing, a bug cannot exist until it is observed.

I have no plans to fix this though, because again the only reason I did this was so I can feel smarter than the smart word people :)
