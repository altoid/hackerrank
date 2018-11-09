object CamelCase {

  def camelcase(s: String): Int = {
    val uppers = s.filter(_.isUpper)
    println(uppers)
    uppers.length + 1
  }

  def main(args: Array[String]): Unit = {
    val tests = List("", "aoeu", "aBcDeFgHi")

    for (t <- tests) {
      println(camelcase(t))
    }
  }
}
