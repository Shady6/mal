# Lispreter
Lispreter is an (incomplete) implementation of the Lisp language in Python based on the mal guide. To give it a try you can run the `main.py` file. If you'd like to check some test cases from the root directory run `make 'test^lispreter^step{step_number}'`. You can view the test cases for each step in `/impls/tests/`.

### What is the minimal set of funcionalities that makes this language Turing Complete?
For a language to be Turing Complete it has to be able to simulate Turing Machine or recreate another system which is considered to be Turing Complete.

1. Turing Machine scans the infinite memory tape and it's able to read the contents of the cell - Lispreter is able to read input and parse it into abstract syntax tree.
2. Turing Machine based on cell content from memory tape, machine own state, or specific user instuctions writes to the cell - Lispreter is able to define some state by using it's environment and declaring variables with for example `def!` or `let*`. Based on the current instruction like `+` it can perform opertion on given arguments and save information about the result. Simple example would be:      
`(def! a 1)`   
`(def! b 2)`   
`(def! c (+ a b))`   
`c ;3`
3. Turing machine based on the result of operation will move to the left cell or right cell on the memory tape - Lispreter implements if statements   
`(if true 1 3) ;1`
4. Turing Machine Based on the content of cell can halt or move to the next instruction - Lispreter will halt if it will evaluate all tokens or prematurely when exception is thrown else it will move to the next instruction.

To summarize minimal set of funcionalities are: ability to read and parse tokens, environment state, basic operators like `+ - / * < > <= >= ==`, if statements and functions.