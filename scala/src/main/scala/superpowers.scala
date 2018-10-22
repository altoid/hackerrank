object superpowers {
  def solve(exp: Int, modulus: Int): Int = {
    var result: Long = 2
    for (i <- 1 to exp) {
      result = scala.math.pow(result, 2).toLong % modulus
    }
    result.toInt
  }

  def main(args: Array[String]): Unit = {
    println(solve(290, 443))
    println(solve(1000000, 2699))
    println(solve(261887, 573440))
  }
}
