import java.io.PrintWriter

object Solution {

    /*
     * Complete the nonDivisibleSubset function below.
     */
	def lookup(mymap: Map[Int, Int], key: Int) = {
        mymap.get(key) match {
            case Some(x) => x
		    case None => 0
        }
    }

    def nonDivisibleSubset(k: Int, arr: Array[Int]): Int = {
		// group the array by remainders
		val classes = arr.toList.groupBy(x => x % k)
//		println(classes)
		val counts = classes.mapValues(x => x.size)
//		println(counts)
		val upto = {
			if (k % 2 == 0) (k - 1) / 2
			else k / 2
		}

		var result = 0
		for (i <- 1 to upto) {
			result += math.max(lookup(counts, i), lookup(counts, k - i))
		}
		if (lookup(counts, 0) > 0) {
		   result += 1
	    }
		if (k % 2 == 0 && lookup(counts, k / 2) > 0) {
		   result += 1
        }
        result
    }

    def main(args: Array[String]) {
        val stdin = scala.io.StdIn

        val nk = stdin.readLine.split(" ")

        val n = nk(0).trim.toInt

        val k = nk(1).trim.toInt

        val S = stdin.readLine.split(" ").map(_.trim.toInt)
        val result = nonDivisibleSubset(k, S)

		println(result)
    }
}
