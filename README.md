TestCalculator project - created in order to show QA automation skills and approaches with python language usage.

Task description:

"""
•Chose one of tools that has +, -, * and / operations on
numbers:
•expr 1 + 2
•echo "3 * 4" | bc
•awk 'BEGIN {print 5 / 7}'
•python3 -c 'print(7-9)'
•bash -c 'echo $((5 + 10 * 2))'
•Write unit tests for +, -, * and / operations on numbers
•Tests has to run on Linux command line
•Test can be written in: Bash, Python, Java or Kotlin
•You can use any form of communication with tested
software
•using directly if your language allows
•using some interposes communication if needed
•Find the limits of given software
•Check error reporting
"""

Leveraged pytest, allure-pytest tools.
Used test design techniques:

- Equivalence partitioning (EP)
- Boundary Value Analysis (BVA)
  Created positive and negative scenarios.

In order to run the project and get reports:

1. pip install requirements.txt
2. pytest --alluredir <report_dir>
3. allure serve <report_dir>