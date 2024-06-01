fun main(args: Array<String>) {
    //khởi tạo biến
    var a:Byte=20
    var b:Short=1000
    println("giá trị của a là: "+a)
    println("giá trị của b là: $b")

    //khai báo biến
    var c:Double

    //đặt tên biến
    var diemToan:Float
    var diemVan:Float
    var giáThuốc:Double

    //khai báo số thực
    var y:Double=8.5
    var x=9.5
    println("kieu loai cua y la: "+(y::class.java.typeName))
    println("kieu loai cua x la: "+(x::class.java.typeName))

    var k:Float = 9.2F
    println("kieu loai cua k la: "+(k::class.java.typeName))

    //khai báo số nguyên
    var soB:Int=14
    var soA=13

    //khai báo long
    var soG:Long=100
    var soH=101L
    println("kieu loai cua h la: "+(soH::class.java.typeName))

    //kiểu short
    var soS:Short=32767

    //khai bao ky tu
    var kyTu:Char='a'

    //kieu string
    var str1:String="abc"
    var str2:String="1"
    var str3="khai bao tat"

    //khai bao doan
    var str4="""-Cay không?
-Có.
-Làm được gì không?
-Không."""
    println(str4)

    //khai bao bool
    var check:Boolean=true
    var check2:Boolean=false

    //khai bao mang
    var mangSoThuc:FloatArray= floatArrayOf(0.5F, 7.5F, 8.8F)
    var mangKyTu:CharArray= charArrayOf('a','b','c')

    //khai bao hang so
    val nhietDoSoi:Int=100
    val nhietDoDonng:Int=0
    val soPi=3.14
}