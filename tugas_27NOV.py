#A
penumpang = ["wiliam","Kate","Anderson", "Jame", "Mady"]
print("A.", penumpang)
#B
penumpang.append("Jones")
print("b.", penumpang)
#C
penumpang[penumpang.index("Anderson")] = "Grace"
print("C.", penumpang)
#D
print("D.", "Thompson" in penumpang)
#E
penumpang.sort()
print("E.", penumpang)
#F
print("f. Penumpang yang sampai di Yogyakarta:")
for orang in penumpang:
     print("-", orang)
#G
penumpang.clear()
print("G.", penumpang)