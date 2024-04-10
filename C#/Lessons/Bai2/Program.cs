namespace Bai2;

class Program
{
    static void Main(string[] args)
    {
        //khởi tạo biến
        int soLuong = 0;
        float diemTrungBinh = 8.5f;
        string name = "son";
        byte tuoi;//khai báo biến
        System.Console.WriteLine("tên là {0} co diem trung binh la {1}",name,diemTrungBinh);

        int a=1;
        int b=2;
        float z=a/b;
        float z2=(float)a/b;
        System.Console.WriteLine("1/2={0}",z);
        System.Console.WriteLine("1/2={0}",z2);

        byte x=255;
        int y=x;

        int k=40000;
        System.Console.WriteLine("gia tri cua k:{0}",k);
        byte l=(byte)k;
        System.Console.WriteLine("gia tri cua l:{0}",l);
    }
}
