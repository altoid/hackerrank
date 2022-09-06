// convert hh:mm:ss[AP]M to 24-hour time

/*
 test cases

07:00:00AM
07:00:00PM

12:01:02AM
12:01:02PM

13:00:00AM -- error

00:00:00AM -- error

01:67:00AM -- error

01:23:92AM -- error

1:02:03AM -- error
01:2:03AM -- error
01:02:3AM -- error

*/

object Solution extends App {
  val tpattern = "(\\d{2}):(\\d{2}):(\\d{2})([AP]M)".r

  def convert(h: Int, m: Int, s: Int, d: String): String = {
    if (h < 1 || h > 12) throw new IllegalArgumentException("bad hour:  " + h)
    else if (m < 0 || m > 59) throw new IllegalArgumentException("bad minute: " + m)
    else if (s < 0 || s > 59) throw new IllegalArgumentException("bad second: " + s)
    else {
      val hh = if (h == 12) 0 else h
      "%02d:%02d:%02d".format(if (d == "PM") hh + 12 else hh, m, s)
    }
  }

  def test(tstring: String): String = {
    val x1 = tstring match {
  	  case tpattern(h, m, s, d) => convert(h.toInt, m.toInt, s.toInt, d)
      case _ => throw new IllegalArgumentException(tstring + " is bogus")
  	}	 
	  x1
  }

  println(test("07:00:00AM"))
  println(test("12:00:00AM"))
  println(test("12:00:00PM"))
  try {
    println(test("00:00:00AM"))
  }
  catch {
    case e: IllegalArgumentException => println(e)
  }
  println(test("01:00:00AM"))
  try {
    println(test("aoeuaeou"))
  }
  catch {
    case e: IllegalArgumentException => println(e)
  }
  println(test("01:00:00PM"))
  try {
    println(test("00:00:00AM"))
  }
  catch {
    case e: IllegalArgumentException => println(e)
  }
  try {
    println(test("10:66:00AM"))
  }
  catch {
    case e: IllegalArgumentException => println(e)
  }
  try {
    println(test("10:00:66AM"))
  }
  catch {
    case e: IllegalArgumentException => println(e)
  }
}
