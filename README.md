# Deterministic Finite Automaton

Author: Luiz Paulo Grafetti Terres

cc: Linguagens Formais e Autômatos

Professor: BRAULIO ADRIANO DE MELLO

#  example:

`input_file.txt`:

```
¨ This is a comment !
¨ This files contains regular grammars and tokens.
¨ It is meant to guaranteed work with at most: 
¨	1 Regular grammar, with N rules
¨	N Tokens of any reasonable length

se
entao
senao

<S> ::= a<A> | e<A> | i<A> | o<A> | u<A>
<A> ::= a<A> | e<A> | i<A> | o<A> | u<A> | ε
```

# Outputs based on the example input_file.txt:

Note: ERROR state is actually `[0]`, but its output is represented by `-` for better understanding of the table;

## State Transition Table:

 | Accept State | 0 |s |e |n |t |a |o |i |u |
|-|-|-|-|-|-|-|-|-|-|
 |  | 1 |[2, 9] |[4, 14] |- |- |[14] |[14] |[14] |[14] |
 |  | 2 |- |[3] |- |- |- |- |- |- |
 | se | 3 |- |- |- |- |- |- |- |- |
 |  | 4 |- |- |[5] |- |- |- |- |- |
 |  | 5 |- |- |- |[6] |- |- |- |- |
 |  | 6 |- |- |- |- |[7] |- |- |- |
 |  | 7 |- |- |- |- |- |[8] |- |- |
 | entao | 8 |- |- |- |- |- |- |- |- |
 |  | 9 |- |[10] |- |- |- |- |- |- |
 |  | 10 |- |- |[11] |- |- |- |- |- |
 |  | 11 |- |- |- |- |[12] |- |- |- |
 |  | 12 |- |- |- |- |- |[13] |- |- |
 | senao | 13 |- |- |- |- |- |- |- |- |
 | _variable_A | 14 |- |[14] |- |- |[14] |[14] |[14] |[14] |

## Deterministic State Transition Table:

 | Accept State | - |s |e |n |t |a |o |i |u |
|-|-|-|-|-|-|-|-|-|-|
 |  | [1] |[2, 9] |[4, 14] |- |- |[14] |[14] |[14] |[14] |
 |  | [2, 9] |- |[3, 10] |- |- |- |- |- |- |
 | _variable_A | [4, 14] |- |[14] |[5] |- |[14] |[14] |[14] |[14] |
 | _variable_A | [14] |- |[14] |- |- |[14] |[14] |[14] |[14] |
 | se | [3, 10] |- |- |[11] |- |- |- |- |- |
 |  | [5] |- |- |- |[6] |- |- |- |- |
 |  | [11] |- |- |- |- |[12] |- |- |- |
 |  | [6] |- |- |- |- |[7] |- |- |- |
 |  | [12] |- |- |- |- |- |[13] |- |- |
 |  | [7] |- |- |- |- |- |[8] |- |- |
 | senao | [13] |- |- |- |- |- |- |- |- |
 | entao | [8] |- |- |- |- |- |- |- |- |
