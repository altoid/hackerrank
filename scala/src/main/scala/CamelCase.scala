object CamelCase {

  def camelcase(s: String): Int = {
    s.filter(_.isUpper).length + 1
  }

  def main(args: Array[String]): Unit = {
    val tests = List("", "aoeu", "aBcDeFgHi")

    for (t <- tests) {
      println(camelcase(t))
    }
  }
}
