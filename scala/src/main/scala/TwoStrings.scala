object TwoStrings {

  def twoStrings(s1: String, s2: String): String = {
    if ((s1 intersect s2).size == 0) "NO" else "YES"
  }

  def main(args: Array[String]): Unit = {
    println(twoStrings("hello", "world"))
    println(twoStrings("hi", "world"))
  }
}
