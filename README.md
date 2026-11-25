### 2.14 LAB: Longest common subsequence

#### Overview

The longest common substring algorithm is presented elsewhere in this book.  The longest common subsequence algorithm is similar.  Unlike a substring, a subsequence ned not be continuous.  Ex: "ARTS" is a subsequence of ALGORITHMS, but is not a substring.

A dynamic programming matrix can be used to solve the longest common subsequence (LCS) problem.  Rules for populating the matrix differ sligthly from the longest common substring algorithm.  Both algorithms populate rows from top to bottom, and left to right accross a row.  Each entry matrix[R][C] is computed as follows:

* if characters match, both algorithms assign matrix[R][C] with 1 + matrix[R - 1][C - 1].
* if characters do not match, the longest common....
    * substring: algorithm assigns matrix[R][C] with 0
    * subsequence: algorithm assigns matrix[R][C] with max(matrix[R - 1][C], matrix[R][C - 1])

Each algorithm uses 0 for out of bounds entries.  Ex: When computing matrix[0][0] for a character match, 0 is used instead of trying to access matrix[-1][-1].