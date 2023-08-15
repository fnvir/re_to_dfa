# _Regex to DFA_ by direct method


A simple regex compiler in python which converts the regular expression into a dfa, which can then be simulated to check if a given string matches the pattern...

> See [main.py](/src/main.py) for usage examples


## Features
- Convert regex to dfa
- Match regex with a string
- Supports additional operators like + (kleene), ? (optional) in regex
- Supports additional symbols like \w, \s, \d, .

## How to Use
  - The program recognizes the following symbols and operators in the regex
    Symbol | Meaning
    ------------- | -------------
    $ | epsilon (empty string)
    \\s | Matches any whitespace characters
    \\w | Alphanumeric or underscore
    \\d | Digits (0-9)
    . | All except newline
    Any ascii/unicode character |
    
    Operator | Meaning
    -------- | -------
    \* | Kleene Star (zero or many)
    \+  | Kleene Plus (One or many)
    \?  | Optional (zero or one)
    \|  | OR 
    .  | Concat (for internal use)
    \( \) | brackets
   - **Note:** To use any character which is an operator/symbol like '+' or '?', append '\\' before it.
      - Like: **\\.** for '.', **\\+** for '+', **\\?** etc.
   
  

## How it works
1. Preprocess the regex
    1. Replace all the characters/token in the regex with a integer code (This makes it easier to support additional operators like +,?,\s,\d etc.)
    2. Support + and ? operators (Replace all instances of x+ with xx* and x? with (x | epsilon) \[epsilon=empty string\])
    3. Add concatenate operator in the regex and augment # in the end to indicate end: (a|b)abb -> (a|b).a.b.#
2. Convert the regex to postfix
3. Generate Syntax tree from postfix regex
    * Assign every leaf node an unique id
4. Calculate nullable, firstpost, lastpos, followpos
5. Generate DFA from Syntax tree using the following algorithm:
    * ![algo](/assets/algo.PNG?raw=true "DFA from Syntax tree")

