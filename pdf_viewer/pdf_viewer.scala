object Solution {

    def designerPdfViewer(h: Array[Int], word: String): Int =  {
        // Complete this function
		val sizes = word.toList.map(x => x.toInt).map(x => x - 'a'.toInt).map(i => h(i))
//		println(sizes)
//		println(sizes.max)
		sizes.max * word.length
    }

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var h = new Array[Int](26);
        for(h_i <- 0 to 26-1) {
           h(h_i) = sc.nextInt();
        }
        var word = sc.next();
        val result = designerPdfViewer(h, word);
        println(result)
    }
}
