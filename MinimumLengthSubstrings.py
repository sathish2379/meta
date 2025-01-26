'''
Minimum Length Substrings
You are given two strings s and t. You can select any substring of string s and rearrange the characters of the selected substring. Determine the minimum length of the substring of s such that string t is a substring of the selected substring.
Signature
int minLengthSubstring(String s, String t)
Input
s and t are non-empty strings that contain less than 1,000,000 characters each
Output
Return the minimum length of the substring of s. If it is not possible, return -1
Example
s = "dcbefebce"
t = "fd"
output = 5
Explanation:
Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb". Thus, the minimum length required is 5.
'''
import math
# Add any extra import statements you may need here

from collections import Counter
# Add any helper functions you may need here


def min_length_substring(s, t):
  # Write your code here
  t_freq = Counter(t)
    
  # Step 2: Sliding window setup
  left = 0
  min_len = float('inf')
  required_chars = len(t_freq)
  window_freq = Counter()
  formed = 0

  # Step 3: Expand the window with right pointer
  for right in range(len(s)):
      # Add current character to the window
      char = s[right]
      window_freq[char] += 1

      # If current window contains all characters from t, update formed
      if char in t_freq and window_freq[char] == t_freq[char]:
          formed += 1

      # Step 4: Shrink the window from the left while valid
      while left <= right and formed == required_chars:
          # Update minimum length of valid substring
          min_len = min(min_len, right - left + 1)

          # Remove leftmost character from the window
          char = s[left]
          window_freq[char] -= 1
          if char in t_freq and window_freq[char] < t_freq[char]:
              formed -= 1

          # Move left pointer to shrink the window
          left += 1

  # Step 5: Return the result
  return min_len if min_len != float('inf') else -1 
  
  











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  