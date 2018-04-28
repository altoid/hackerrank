import math.abs
import io._

object Solution {
  // initialize 2d array; canonical 3x3 magic square
  val square = Array(
    Array(2,7,6),
    Array(9,5,1),
    Array(4,3,8)
  )

  val permutations = List(
    square,
    transpose(square),
    rotate(square),
    transpose(rotate(square)),
    rotate(rotate(square)),
    transpose(rotate(rotate(square))),
    rotate(rotate(rotate(square))),
    transpose(rotate(rotate(rotate(square)))),
  )

  def printmatrix(arr: Array[Array[Int]]): Unit = {
    for (i <- 0 until arr.length) {
      arr(i).map(x => print(x + " "))
      println
    }
  }

  // rotate the matrix clockwise
  def rotate(arr: Array[Array[Int]]): Array[Array[Int]] = {
    val m = arr.length  // rows
    val n = arr(0).length  // columns

    val result = Array.ofDim[Int](n, m)

    for (i <- 0 until n) {
      for (j <- 0 until m) {
        result(j)((arr(0).length - 1) - i) = arr(i)(j)
      }
    }
    result
  }

  def transpose(arr: Array[Array[Int]]): Array[Array[Int]] = {
    val m = arr.length  // rows
    val n = arr(0).length  // columns

    val result = Array.ofDim[Int](n, m)

    for (i <- 0 until n) {
      for (j <- 0 until m) {
        result(i)(j) = arr(j)(i)
      }
    }
    result
  }

  def cost(a: Array[Array[Int]], b: Array[Array[Int]]): Int = {
    // assumes a and b have same dimensions
    val m = a.length  // rows
    val n = a(0).length  // columns

    var cost = 0
    for (i <- 0 until n) {
      for (j <- 0 until m) {
        cost += math.abs(a(i)(j) - b(i)(j))
      }
    }
    cost
  }

  def formingMagicSquare(sample: Array[Array[Int]]): Int = {
    permutations.map(cost(_, sample)).toList.min
  }

  def main(args: Array[String]) {
    var sample = Array[Array[Int]]()
    for (line <- Source.stdin.getLines) {
      val a = line.split("\\s+").map(_.toInt).toArray
      sample = sample :+ a
    }

    //    printmatrix(square)
    //
    //    println("<<<<<<<<<<<")
    //    printmatrix(sample)
    //    println(">>>>>>>>>>>")

    println(formingMagicSquare(sample))
  }
}