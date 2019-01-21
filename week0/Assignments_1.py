def fizz_buzz_sum(numbers):
    '''Sums all numbers in a list that are either a multiple of 3 or 5.

    Parameters
    ----------
    numbers: list
      A list of integers.

    Returns
    -------
    sum: int
      The sum of all the numeric data in the list, excluding those summands
      divisible by 3 or 5.
    '''
    new_numbers = [a for a in numbers if (a%3 == 0) or (a%5== 0)]
    return sum(new_numbers)

print(fizz_buzz_sum([1,2,3,4,5,555]))

import numpy as np
def transpose(matrix):
    '''Transpose a matrix.  That is, reverse the roles of rows and columns

    $ transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]

    Parameters
    ----------
    matrix: list of lists of numbers.

    Returns
    -------
    transposed: list of lists of numbers
      The transposed matrix.
    '''
    row_num = len(matrix)
    col_num = len(matrix[0])
    new_matrix = np.zeros((col_num,row_num))
    #new_matrix = [[0] * row_num] * col_num

    for i in range(col_num):
        for j in range(row_num):
            new_matrix[i][j] = matrix[j][i]
    return new_matrix

print(transpose([[1, 2, 3], [4, 5, 6]]))

import string
def split_vowel_consonant_punctuation(stri):
    '''Split a string into three strings: one containing vowels, one containing
    consonants, and one containing punctuation.

    $ s = "My cat's name is Moshi!  She is old, but friendly."
    $ split_vowel_consonant_punctuation(s)
    ["aaeioieiouie", "MyctsnmsMshShsldbtfrndly", " '   !    ,  ."]

    Hint: Look up the `.join` method on strings!

    Parameters
    ----------
    string: str

    Returns
    -------
    vowel_consonant_punctuation: list of three strings.
      The first element in the list contains only vowels, the second only
      consonants, and the third only punctuation. 
    '''
    all_letter = set(string.ascii_lowercase + string.ascii_lowercase.upper())
    vowels = {"a","e","i","o","u","A","E","I","O","U","S","s"}
    consonants = all_letter - vowels
    stri_vowels = []
    stri_consonants = []
    others = []
    for letter in stri:
        if letter in vowels:
            stri_vowels.append(letter)
        elif letter in consonants:
            stri_consonants.append(letter)
        else:
            others.append(letter)
    return ["".join(stri_vowels),"".join(stri_consonants),"".join(others)]
print(split_vowel_consonant_punctuation("xxflajdfajs;dlkfja;lsdjfals"))

def make_triangle(n):
    '''Make a triangle containing the integers from 0 to (n+1)*n / 2

    $ make_triangle(2)
    [[1], [2, 3]]
    $ make_triangle(3)
    [[1], [2, 3], [4, 5, 6]]

    Parameters
    ----------
    n: positive integer

    Returns
    -------
    triangle: list of lists of integers
      A triangle continaing the consecutive integers
    '''
    new_list = []
    for i in range(1,int((n+1)*n / 2)):
        new_list.append(list(range(i,2*i)))
        if i > n -1 :
            break 
    return new_list

print(make_triangle(3))

def triangle_sum(triangle):
    '''Sum the diagonals of a triangle of numbers.

    $ triangle_sum([[1], [2, 3]])
    [2, 4]

    Because:
    [1]
    [2, 3] <- sum the diagonals
     2  4

    $ triangle_sum([[1], [2, 3], [4, 5, 6]])
    [4, 7, 10]

    Because:
    [1]
    [2, 3]
    [4, 5, 6] <- sum the diagonals
     4  7  10

    Parameters
    ----------
    triangle: list of lists of numbers

    Returns
    -------
    diagonal_sums: list of numbers
      The diagonal sums of the triangle.
    '''
    result = [ [] for i in range(len(triangle))]#[[]] * len(triangle)
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            x = i - j
            result[x].append(triangle[i][j])
    result = [sum(a) for a in result]
    return result[::-1]
print(triangle_sum([[1], [2, 3], [4, 5, 6]]))

from string import ascii_lowercase
from string import ascii_uppercase 

def pangram(test):
    '''Detects if a string contains every letter in the alphabet at least once. E.g.
       
        $ pangram("The quick brown fox jumps over the lazy dog")
    True
        $ pangram("Welcome to the jungle, we've got fun and games") 
        False

    Parameters
    ----------
    string: str

    Returns
    -------
    bool: Is the string a pangram?
    '''
    test = set(list(test.upper()))
    #all_letters = ascii_lowercase + ascii_uppercase
    return (set(list(ascii_uppercase)) - test) == set() ## set() - set() were way more faster than list
        
    
test = "Welcome to the jungle, we've got fun and games"
print(pangram(test))