class TripleSumTest extends org.scalatest.FunSuite {

  test("basic") {
    assert(true)
  }

  test("countLessThanOrEqual") {
    assert(TripleSum.countLessThanOrEqual(Array(1,2,3,4,5), 3) === 3)
    assert(TripleSum.countLessThanOrEqual(Array(1,2,3,4,5), 0) === 0)
    assert(TripleSum.countLessThanOrEqual(Array(1,2,3,4,5), 1) === 1)
    assert(TripleSum.countLessThanOrEqual(Array(1,2,3,4,5), 33) === 5)

    assert(TripleSum.countLessThanOrEqual(Array(1,2,3,3,4,5), 3) === 4)
    assert(TripleSum.countLessThanOrEqual(Array(3,3,3,3,3,3), 3) === 6)
    assert(TripleSum.countLessThanOrEqual(Array(3,3,3,3,3,3), 4) === 6)
    assert(TripleSum.countLessThanOrEqual(Array(3,3,3,3,3,3), 2) === 0)

  }

  ignore("triplets") {
    val a = Array(1,3,5)
    val b = Array(2,3)
    val c = Array(1,2,3)

    assert(TripleSum.triplets(a, b, c) === 8)
  }

  test("triplets II") {
    val a = Array(1,4,5)
    val b = Array(2,3,3)
    val c = Array(1,2,3)

    assert(TripleSum.triplets(a, b, c) === 5)
  }

  ignore("triplets III") {
    val a = Array(1,3,5,7)
    val b = Array(5,7,9)
    val c = Array(7,9,11,13)

    assert(TripleSum.triplets(a, b, c) === 12)
  }

}
