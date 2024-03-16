import segno

s = input("Chuỗi:")

resp = segno.make_qr(s)
resp.save(
    "result.png",
    scale=10,
    light="white"
)