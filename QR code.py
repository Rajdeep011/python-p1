import qrcode as qr
img = qr.make("https://www.youtube.com/@souravjoshivlogs7028")
img.save("souravjoshi_youtube.png")
