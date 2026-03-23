#what does this test do? 
# It tests the add function from the app module to ensure it correctly adds two numbers together. 
# It includes three test cases: adding 2 and 3 to get 5, adding -1 and 1 to get 0, and adding 0 and 0 to get 0.
# can this be similar concept to PHPUnit test?
# Yes, this is similar to a PHPUnit test in that it is testing a specific function (in this case, the add function) to ensure it behaves as expected.
#  In PHPUnit, you would typically create a test class that extends PHPUnit's TestCase class and write test methods that assert the expected outcomes of the function being tested. 
# The concept of writing tests to validate code functionality is common across different testing frameworks and languages.
# What are the other similar concepts in other languages?
# Similar concepts in other languages include:
# - JUnit for Java: A popular testing framework for Java applications that allows you to write test cases to validate your code.
# - NUnit for C#: A testing framework for .NET applications that provides a way to write and run tests.
# - RSpec for Ruby: A testing framework for Ruby applications that allows you to write human-readable tests.
# - Mocha for JavaScript: A testing framework for JavaScript applications that provides a way to write and run tests, often used in conjunction with assertion libraries like Chai.

from app import add
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0