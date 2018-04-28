// https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

//
// rotation is 1 <= r <= 10^9
//

import scala.collection.mutable.ArrayBuffer

object Solution {

    // x0, y0 - upper right of matrix
    // x1, y1 - lower left of matrix

    def getRing(y0: Int, x0: Int,
                y1: Int, x1: Int, matrix: Array[Array[Int]]): ArrayBuffer[Int]  =  {

//      println(s"x0 y0 = ($x0 $y0)")
//      println(s"x1 y1 = ($x1 $y1)")
        val leg1 = ArrayBuffer[Int]()
        val leg2 = ArrayBuffer[Int]()
        val leg3 = ArrayBuffer[Int]()
        val leg4 = ArrayBuffer[Int]()

        val xd = x1 - x0
        val yd = y1 - y0

        for (i <- 0 until xd) {
            leg1 += matrix(y0)(x0 + i)
            leg3 += matrix(y1)(x1 - i)
        }

        for (j <- 0 until yd) {
            leg2 += matrix(y0 + j)(x1)
            leg4 += matrix(y1 - j)(x0)
        }

//      println(leg1)
//      println(leg2)
//      println(leg3)
//      println(leg4)
        return leg1 ++ leg2 ++ leg3 ++ leg4
    }

    def applyRing(y0: Int, x0: Int,
                  y1: Int, x1: Int,
                  ring: ArrayBuffer[Int],
                  matrix: Array[Array[Int]]): Unit = {
        
        val rows = matrix.length
        val cols = matrix(0).length
        val xd = x1 - x0
        val yd = y1 - y0
        

        for (i <- 0 until xd) {
            matrix(y0)(x0 + i) = ring(i)
            matrix(y1)(x1 - i) = ring(xd + yd + i)
        }

        for (j <- 0 until yd) {
            matrix(y0 + j)(x1) = ring(xd + j)
            matrix(y1 - j)(x0) = ring(xd + yd + xd + j)
        }
    }

    // beware, original implementation did not have r parameter
    def matrixRotation(r: Int, matrix: Array[Array[Int]])  =  {
        // problem statement says r >= 1, so don't worry about r == 0
        val rows = matrix.length
        val cols = matrix(0).length
        val nrings = math.min(rows, cols) / 2
//      println(s"rows $rows, cols $cols, nrings $nrings")

        for (nring <- 0 until nrings) {
            var ring = getRing(nring, nring, rows - (nring + 1), cols - (nring + 1), matrix)
//          println(ring)
            var rfactor = r % ring.length
            // if rfactor == 0 skip entirely
            if (rfactor > 0) {
                ring = ring.drop(rfactor) ++ ring.take(rfactor)
//              println(ring)
                applyRing(nring, nring, rows - (nring + 1), cols - (nring + 1), ring, matrix)
            }
        }

        printMatrix(matrix)     
    }

    def printMatrix(matrix: Array[Array[Int]]): Unit = {
        val rows = matrix.length
        val cols = matrix(0).length
        for (j <- 0 until rows) {
            println(matrix(j).mkString(" "))
        }
    }

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var m = sc.nextInt();
        var n = sc.nextInt();
        var r = sc.nextInt();
        var matrix = Array.ofDim[Int](m,n);
        for(matrix_i <- 0 to m-1) {
           for(matrix_j <- 0 to n-1){
              matrix(matrix_i)(matrix_j) = sc.nextInt();
           }
        }
        matrixRotation(r, matrix);
    }
}
