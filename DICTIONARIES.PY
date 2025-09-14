d1 = {"Adam Smith":"A","Judy Paxton":"B+"}
d2 = {"Mary Louis":"A","Patrick White":"C"}
d1.update(d2)
print(d1)

A = {"Tamil":92,"English":56,"Maths":88,"Science":97,"Social":89}
B = {"Tamil":78,"English":68,"Maths":88,"Science":97,"Social":56}
for score in A.values():
    if score in B.values():
        print("Maths: 88 is present in both A and B")