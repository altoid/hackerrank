object DayOfTheProgrammer {
  // in a leap year, day 256 is 12 sep
  // in non-leap year, day 256 is 13 sep
  // in 1918, day 256 is 26 sep

  def isLeapYear(year: Int): Boolean = {
    if (year < 1918) {
      year % 4 == 0
    }
    else if (year % 400 == 0) true
    else if (year % 100 == 0) false
    else year % 4 == 0
  }

  def dayOfProgrammer(year: Int): String = {
    if (year == 1918) s"26.09.$year"
    else if (isLeapYear(year)) s"12.09.$year"
    else s"13.09.$year"
  }

  def test(year: Int): Unit = {
    println(year + " " + dayOfProgrammer(year))
  }

  def main(args: Array[String]): Unit = {
//    println(isLeapYear(1700))
//    println(isLeapYear(1704))
//    println(isLeapYear(1964))
//    println(isLeapYear(2000))
//    println(isLeapYear(2001))
//    println(isLeapYear(1800))

    test(1965)
    test(1918)
    test(2000)
    test(1800)
  }
}
