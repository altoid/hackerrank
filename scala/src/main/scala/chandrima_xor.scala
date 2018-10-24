import scala.collection.mutable.ArrayBuffer

object chandrima_xor {

  def solve(arr: Array[Long]): Int = {
    // for each number in arr, turn it into a list of bits.
    val a2 = arr.map(x => x.toBinaryString.toList.map(_.asDigit))
    val maxlength = (a2 foldLeft 0)((b, a) => a.length max b)

    // pad on the left with 0s
    val a3 = a2.map(x => {
      val padding = List.fill(maxlength - x.length)(0)
      padding ++ x
    })

    a3 foreach println

    0
  }

  def main(args: Array[String]): Unit = {
    val arr = ArrayBuffer[Long]()
    arr += math.pow(10, 18).toLong
    arr += math.pow(10, 13).toLong
    arr += math.pow(10, 11).toLong

    val result = solve(arr.toArray)
  }

}
