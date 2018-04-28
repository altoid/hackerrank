// https://www.hackerrank.com/challenges/simple-array-sum/problem

import io._

object Solution extends App {
	val line = Source.stdin.getLines.drop(1).take(1).toList.headOption
	val x = line match {
		case Some(x) => x.split("\\s+").map(_.toInt).toList.foldLeft(0)(_ + _)
		case _ => new Exception("aoeu")
	}
	println(x)
}
