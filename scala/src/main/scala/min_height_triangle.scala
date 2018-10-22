object min_height_triangle {

  def main(args: Array[String]) = {
    val stdin = scala.io.StdIn
    val params = stdin.readLine.split(" ").map(_.trim.toInt)
    val base = params(0)
    val area = params(1)
    val height = math.ceil((2 * area) / base.toDouble).toInt
    println(height)
  }
}
