object LoveLetterMystery {

  // idea - from the outside in, compute the abs of the difference between the two characters.
  // answer is the total.

  def theLoveLetterMystery(s: String): Int = {
    if (s.length == 0) 0
    else {
      var total = 0
      for (i <- 0 until s.length / 2) {
        val l = s(i)
        val r = s(s.length - i - 1)
        total += math.abs(l - r)
      }
      total
    }
  }

  def main(args: Array[String]): Unit = {
    println(theLoveLetterMystery("")) // 0
    println(theLoveLetterMystery("abcba")) // 0
    println(theLoveLetterMystery("abcdef")) // 5 + 3 + 1 = 9
    println(theLoveLetterMystery("abcxdef")) // 5 + 3 + 1 = 9
  }
}
