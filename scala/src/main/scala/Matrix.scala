
class Matrix private(val nrows: Int, val ncolumns: Int, val matrix: Array[Int]) {
  require(nrows > 0)
  require(ncolumns > 0)

  // public constructor
  def this(nrows: Int, ncolumns: Int) = this(nrows, ncolumns, new Array[Int](nrows * ncolumns))

  def copy(): Matrix = {
    new Matrix(nrows, ncolumns, matrix.clone())
  }

  def set(row: Int, column: Int, value: Int): Unit = {
    matrix(row * ncolumns + column) = value
  }

  def get(row: Int, column: Int): Int = matrix(row * ncolumns + column)

  def display(): Unit = {
    for (r <- 0 until nrows) {
      for (c <- 0 until ncolumns) {
        print(" " + get(r, c))
      }
      println()
    }
  }

  def * (other: Matrix): Matrix = {
    // number of columns in me must match number of rows in other
    require(ncolumns == other.nrows)

    val result = new Matrix(nrows, other.ncolumns)

    for (r <- 0 until nrows) {
      for (c <- 0 until other.ncolumns) {
        var n = 0
        for (k <- 0 until ncolumns) {
          n += get(r, k) * other.get(k, c)
        }
        result.set(r, c, n)
      }
    }
    result
  }

  def pow(exp: Int): Matrix = {
    require(exp > 0)

    var calls = 0
    var multiplies = 0

    def pow_helper(exp: Int): Matrix = {
      calls += 1
      if (exp == 1) this.copy()
      else if (exp % 2 == 1) {
        multiplies += 1
        this * pow_helper(exp - 1)
      }
      else {
        val m = pow_helper(exp / 2)
        multiplies += 1
        m * m
      }
    }

    var result = pow_helper(exp)
    println(s"calls = $calls")
    println(s"multiplies = $multiplies")
    result
  }
}

object Sandbox {
  def main(args: Array[String]): Unit = {
    val nrows = 2
    val ncolumns = 2

    val matrix = new Matrix(nrows, ncolumns)

    for (r <- 0 until nrows) {
      for (c <- 0 until ncolumns) {
        matrix.set(r, c, 1)
      }
    }

    matrix.display()

    val product = matrix * matrix

    val product_copy = product.copy()
    product_copy.set(0, 0, 444)
    product.display()
    product_copy.display()

    val fibonacci = new Matrix(2, 2)
    for (r <- 0 until fibonacci.nrows) {
      for (c <- 0 until fibonacci.ncolumns) {
        fibonacci.set(r, c, 1)
      }
    }
    fibonacci.set(0, 0, 0)
//    for (i <- 1 to 5) {
//      println(s"----- pow = $i")
//      fibonacci.pow(i).display()
//    }
    println("----- pow = 23")
    fibonacci.pow(23).display()
    println("----- pow = 233")
    fibonacci.pow(233).display()
  }
}