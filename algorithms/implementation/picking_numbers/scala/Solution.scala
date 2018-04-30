import io._

object Solution {

    def pickingNumbers(a: Array[Int]): Int =  {

        // idea: map each integer to its count.  look for two
        // consecutive integers with the largest total count or else
        // the integer with the largest count by itself.  bigger of
        // these wins.

        val m = a.groupBy(identity).mapValues(_.size)
        val k = m.keys.toArray.sorted
        // cases
        // there are consecutive keys
        // there are no consecutive keys

        val pairs = k.zip(k.tail).filter(p => p._2 - p._1 == 1)
        val maxsolo = m.values.max
		val maxpair = pairs match {
		    case Array() => 0
            case p => p.map(x => m(x._1) + m(x._2)).max
			}
        maxsolo max maxpair
    }

    def main(args: Array[String]) {
        val line = Source.stdin.getLines.drop(1).take(1).toList.head.split("\\s+").map(_.toInt).toArray

        val result = pickingNumbers(line)
        println(result)
    }
}
