object army_game {
  def answer(m: Int, n: Int): Int = {
    def howmany(n: Int, k: Int): Int = {
      // how many intervals of size k are covered by n?
      (n + k - 1) / k
    }

    howmany(m, 2) * howmany(n, 2)
  }

  def main(args: Array[String]) = {
    val stdin = scala.io.StdIn
    val params = stdin.readLine.split(" ").map(_.trim.toInt)
    val arg1 = params(0)
    val arg2 = params(1)

    println(answer(arg1, arg2))
  }
}
