fun main(args: Array<String>) {
    //ep kieu rong
    var soA:Int=35
    var soB:Long=soA.toLong()
    //ktr kieu loai
    println("kieu loai cua a la: "+(soA::class.java.typeName))
    println("kieu loai cua b la: "+(soB::class.java.typeName))
    println("a=$soA")
    println("b=$soB")

    //ep kieu hep
    var soC:Short=32767
    var soD:Byte=soC.toByte()
    println("c=$soC")
    println("d=$soD")

    var soE:Short=120
    var soF:Byte=soE.toByte()
    println("e=$soE")
    println("f=$soF")

    var soG:Float= 9.9F
    var soH:Int=soG.toInt()
    println("g=$soG")
    println("h=$soH")
}