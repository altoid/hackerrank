import scala.collection.mutable.ArrayBuffer

// max value for signed long is 9223372036854775807, which is > 10 ** 18.
// so 10 ** 18 fits in a long

// successor algorithm:
// find the number we have to add to n to result in a number that is kosher.
//
// need to find the next larger number that does not have consecutive 1 bits.
//
// to do this we need to add to the original number a value that causes its
// 1111 substrings to roll over to 10000:
//
// 000000000000000010010001100001111110011100101010000000000000
//                        ^^    ^^^^^^  ^^^
//                         1     11111   11
//
// we'll take n, shift it 1 to the left, then AND this with n
//
// 000000000000000010010001100001111110011100101010000000000000
// 000000000000000100100011000011111100111001010100000000000000   << shifted 1 to the left
// ------------------------------------------------------------
//                        1     11111   11                       << a
//                         1     11111   11                      << b
// take the & and then shift 1 position to right.  then do !a & b.
// this is what we add to the original number.  if the result still has
// consecutive 11 bits, do it again.


object chandrima_xor {

  def bitsToLong(bitstring: String): Long = (bitstring.toList.map(_.asDigit) foldLeft 0L)((b, a) => 2 * b + a)

  def longToBits(n: Long, fillTo: Int = 60): String = {
    // left pad with 0 until the string is fillTo long.  if fillTo is 0, do not pad.
    val bits = n.toBinaryString

    val padding = if (fillTo > 0) (fillTo - bits.length max 0) else 0
    Array.fill(padding)(0).mkString ++ bits
  }

  // return true iff n has no runs of consecutive 1 bits.
  def isKosher(n: Long): Boolean = (n & (n << 1)) == 0

  def successor(n: Long): Long = {
    def addend(n: Long): Long = {
      if (isKosher(n)) 1
      else {
        val shifted_n = n << 1
        val result = n & shifted_n
        val result_shifted = result >> 1
        val a = ~result & result_shifted
        a
      }
    }

//    println("------------------")
    var a = addend(n)
    var result = n + a
//    println(longToBits(n) + " << n")
    while (!isKosher(result)) {
      a = addend(result)
//      println(longToBits(a, 60) + " << a")
//      println(longToBits(result, 60) + " << result")

      result += a
    }
//    println(longToBits(a, 60) + " << a")
//    println(longToBits(result) + " << result")
    result
  }

  def solve(arr: Array[Long]): Long = {
    var filtered = arr.filter(isKosher(_))

//    println(arr.mkString(" "))

    var nremoved = arr.length - filtered.length
    var last = filtered.last
    while (nremoved > 0) {
      last = successor(last)
      filtered = filtered :+ last
      nremoved -= 1
    }
//    println(filtered.mkString(" "))
    (filtered foldLeft 0L)((b, a) => a ^ b)
  }


  def main(args: Array[String]): Unit = {
    val arr = ArrayBuffer[Long]()
    arr += math.pow(10, 18).toLong
    arr += math.pow(10, 13).toLong
    arr += math.pow(10, 11).toLong

    var n = math.pow(10, 13).toLong
//    val bits = n.toBinaryString.toArray.map(_.asDigit)
//    val n2 = bitsToLong(n.toBinaryString)
//
//    val morebits = "000000000000000010010001100001111110011100101010000000000000"
//    println(bits.mkString +": " + isKosher(n))
//    println(morebits +": " + isKosher(bitsToLong(morebits)))

//    println(bitsToLong("011001")) // 25
//    println(bitsToLong(morebits))
//    println(bitsToLong(morebits).toBinaryString.toArray.map(_.asDigit).mkString)

//    n = 1
//    println(longToBits(n))
//    while (n < 256) {
//      n = successor(n)
//    }
//
//    n = math.pow(10, 13).toLong
//    n = successor(n)

    var answer = solve(Array(1,2,3,4,5))
    println(answer)

    answer = solve(Array(1,2,3))
    println(answer)

    answer = solve(Array(1,3,4))
    println(answer)
  }
}
