// https://www.hackerrank.com/challenges/a-very-big-sum/problem

import math._
import io._

object Solution extends App {
	val line = Source.stdin.getLines.drop(1).take(1).toList.headOption
	val x = line match {
	    case Some(x) => x.split("\\s+").map(BigInt(_)).toList.foldLeft(BigInt(0))(_ + _)
		case _ => new Exception("aoeu")
	}
	println(x)

//	val big1 = BigInt("1111111111100000000")
//    val big2 = BigInt("2222222222200000000")
//
//	println(big1 + big2)
//
//	val bi1 = BigInt("111111111111111111111029837450928734509823740958720398457023984711")
//
//	println(bi1 * bi1)
//
//	val bi2: BigInt = big2 * big1
//
//	println(bi2)
}
