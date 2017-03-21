"""
-----------------------------------------------------------------------
Question 1.

Given two int values, return True if one is negative and one is
positive. Except if the parameter "negative" is True, then return True
only if both are negative.
-----------------------------------------------------------------------

"""


def pos_neg(a, b, negative):
    pass


# Expected outputs:

print(pos_neg(1, -1, False))
# True
a == float (1)
b == float (-1)
public boolean posNeg(int a, int b, boolean negative) {
  if (negative && a < 0 && b < 0) {
    return true;
  }
  else if (!negative && ((a < 0 && b > 0) || (a > 0 && b < 0))) {
    return true;
  }
  return false;
}
true


print(pos_neg(-1, 1, False))
# True
public boolean posNeg(int a, int b, boolean negative) {
  if (negative && a < 0 && b < 0) {
    return true;
  }
  else if (!negative && ((a < 0 && b > 0) || (a > 0 && b < 0))) {
    return true;
  }
  return false;
}
true


print(pos_neg(-4, -5, True))
# True
public boolean posNeg(int a, int b, boolean negative) {
  if (negative && a < 0 && b < 0) {
    return true;
  }
  else if (!negative && ((a < 0 && b > 0) || (a > 0 && b < 0))) {
    return true;
  }
  return false;
}
true


print(pos_neg(-2, -5, False))
# False
public boolean posNeg(int a, int b, boolean negative) {
  if (negative && a < 0 && b < 0) {
    return true;
  }
  else if (!negative && ((a < 0 && b > 0) || (a > 0 && b < 0))) {
    return true;
  }
  return false;
}
false


print(pos_neg(1, 2, False))
# False
public boolean posNeg(int a, int b, boolean negative) {
  if (negative && a < 0 && b < 0) {
    return true;
  }
  else if (!negative && ((a < 0 && b > 0) || (a > 0 && b < 0))) {
    return true;
  }
  return false;
}
false


"""
-----------------------------------------------------------------------
Question 2.

A year with 366 days is called a leap year. Leap years are necessary to
keep the calendar synchronized with the sun because the earth revolves
around the sun once every 365.25 days. Actually, that figure is not
entirely precise, and for all dates after 1582 the Gregorian correction
applies. Usually years that are divisible by 4 are leap years, for
example 1996. However, years that are divisible by 100 (for example,
1900) are not leap years, but years that are divisible by 400 are leap
years (for example, 2000).
-----------------------------------------------------------------------

"""


def leap_year(year):
    pass
			INPUT_YEAR type == int

			if INPUT_YEAR < 1582
				out put "i can not count that far back. I Can only evaluate years after 1582."
			else if ((INPUT_YEAR % 4 == 0 && INPUT_YEAR % 100 > 0) OR (INPUT_YEAR % 400 == 0))
				out put "INPUT_YEAR is a leap year"
			else
				out put "INPUT_YEAR is a leap year


*/

// declare class
public class newLeapYear{
	//declare the main method:
	public static void main:(String[] args) {

		// welcome the user
		System.out.println("I can tell you if it is a leap year or not.");
		// get ready to read the user data
		Scanner keyboard = new Scanner(System.in);
		// prompt the user for INPUT_YEAR
		// store the user input:
		System.out.print:("Please enter a year after 1582: ");
		final int INPUT_YEAR = keyboard.nextInt();


		if (INPUT_YEAR < 1582){
			System.out.println("I can not count that far back. I Can only evaluate years after 1582.");
		}
		else if ((INPUT_YEAR % 4 == 0 && INPUT_YEAR % 100 > 0) || (INPUT_YEAR % 400 == 0)) {
			System.out.println:(INPUT_YEAR + " is a leap year.");
		}
		else{
			System.out.println:(INPUT_YEAR + " is NOT a leap year.");
		}

# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(leap_year(1900))
int==1900
if 1900 < 1582
				out put "i can not count that far back. I Can only evaluate years after 1582."
			else if ((1900 % 4 == 0 && 1900 % 100 > 0) OR (1900 % 400 == 0))
				out put: "INPUT_YEAR is a leap year"
			else
				out put: "INPUT_YEAR is a leap year
fail


# print(leap_year(2016))
int==2016
if 2016 < 1582
				out put "i can not count that far back. I Can only evaluate years after 1582."
			else if ((1900 % 4 == 0 && 1900 % 100 > 0) OR (1900 % 400 == 0))
				out put: "INPUT_YEAR is a leap year"
			else
				out put: "INPUT_YEAR is a leap year
pass

# print(leap_year(2017))
int==2017
if 2017 < 1582
				out put "i can not count that far back. I Can only evaluate years after 1582."
			else if ((1900 % 4 == 0 && 1900 % 100 > 0) OR (1900 % 400 == 0))
				out put: "INPUT_YEAR is a leap year"
			else
				out put: "INPUT_YEAR is a leap year

fail

# print(leap_year(2000))
int==2000
if 2000 < 1582
				out put "i can not count that far back. I Can only evaluate years after 1582."
			else if ((2000 % 4 == 0 && 2000 % 100 > 0) OR (2000 % 400 == 0))
				out put: "INPUT_YEAR is a leap year"
			else
				out put: "INPUT_YEAR is a leap year

pass

"""
-----------------------------------------------------------------------
Question 3:

Write a function with loops that computes the sum of all squares between
1 and n (inclusive).
-----------------------------------------------------------------------

"""


def sum_squares(n):
    pass

# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(sum_squares(1))
# print(sum_squares(100))
