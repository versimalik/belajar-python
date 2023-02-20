import hashlib

m = hashlib.sha256()
m.update(b"selamatpagi123")

print(m.hexdigest())