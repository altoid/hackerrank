object CamelCase {

  def camelcase(s: String): Int = {
    val uppers = s.filter(_.isUpper)
    println(uppers)

    0
  }

  def main(args: Array[String]): Unit = {
    camelcase("")
    camelcase("aoeu")
    camelcase("aAaAaAa")
  }
}
