
# import jaconv
import convrules_onion
import re


with open("input_yo_so.txt",mode="r",encoding="utf-8") as infile:
    l1=infile.read()
#    l1=infile.readlines()
l1=l1.split('\n')
#print(l1)

# j1=re.compile(r'([あいうえおゐゑぁぃぅぇぉかきくけこがぎぐげごゕゖさしすせそざじずぜぞたちつてとだぢづでどっなにぬねのはひふへほばびぶべぼゔぱぴぷぺぽまみむめもやゆよゃゅょらりるれろわをんゎ])') #ー
# j2=re.compile(r'([アイウエオヰヱァィゥェォカキクケコガギグゲゴヵヶサシスセソザジズゼゾタチツテトダヂヅデドッナニヌネノハヒフヘホバビブベボヴパピプペポマミムメモヤユヨャュョラリルレロワヲンヮ])') #ー

for index, ii in enumerate(l1):

  ### 漢字促音 ###

  ii=re.sub(r"c([.,]chi)", r"q\1",ii)
  ii=re.sub(r"s([.,]shi)", r"q\1",ii)
  ii=re.sub(r"f([.,]fu)", r"q\1",ii)
  ii=re.sub(r"t([.,]tsu)", r"q\1",ii)
  ii=re.sub(r"j([.,]ji)", r"q\1",ii)

  ii=re.sub(r"k([.,]ky)(?=[auo])", r"q\1",ii)
  ii=re.sub(r"g([.,]gy)(?=[auo])", r"q\1",ii)
  ii=re.sub(r"s([.,]sh)(?=[auo])", r"q\1",ii)
  ii=re.sub(r"j([.,]j)(?=[auo])", r"q\1",ii)
  ii=re.sub(r"d([.,]dy)(?=[auo])", r"q\1",ii)
  ii=re.sub(r"c([.,]ch)(?=[auo])", r"q\1",ii)
  ii=re.sub(r"`n([.,])ny(?=[auo].*)", r"q\1`ny",ii)
  ii=re.sub(r"h([.,]hy)(?=[auo])", r"q\1",ii)
  ii=re.sub(r"b([.,]by)(?=[auo])", r"q\1",ii)
  ii=re.sub(r"p([.,]py)(?=[auo])", r"q\1",ii)
  ii=re.sub(r"m([.,]my)(?=[auo])", r"q\1",ii)
  ii=re.sub(r"r([.,]ry)(?=[auo])", r"q\1",ii)

  ii=re.sub(r"k([.,]k)(?=[auoie])", r"q\1",ii)
  ii=re.sub(r"s([.,]s)(?=[auoe])", r"q\1",ii)
  ii=re.sub(r"t([.,]t)(?=[aoe])", r"q\1",ii)
  # ii=re.sub(r"`n([.,]n)(?=[auoie])", r"q\1",ii)
  ii=re.sub(r"h([.,]h)(?=[aoie])", r"q\1",ii)
  ii=re.sub(r"f([.,]f)(?=[u])", r"q\1",ii)
  ii=re.sub(r"m([.,]m)(?=[auoie])", r"q\1",ii)
  ii=re.sub(r"y([.,]y)(?=[auoie])", r"q\1",ii)
  ii=re.sub(r"r([.,]r)(?=[auoie])", r"q\1",ii)
  # ii=re.sub(w([.,]w)(?=[auoie])", r"q\1",ii)

  ii=re.sub(r"g([.,]g)(?=[auoie])", r"q\1",ii)
  ii=re.sub(r"z([.,]z)(?=[auoie])", r"q\1",ii)
  ii=re.sub(r"d([.,]d)(?=[auoie])", r"q\1",ii)
  ii=re.sub(r"b([.,]b)(?=[auoie])", r"q\1",ii)
  ii=re.sub(r"p([.,]p)(?=[auoie])", r"q\1",ii)

  ii=re.sub(r"(q[.,])(?=[a-z])", r"\1 ",ii)
  ii=re.sub(r"q([ksptgchmrwdbzf][a-z]+)([.,])", r"q\2 \1\2",ii)

  ### 假名中促音 ###
  ii=re.sub(r"c(chi)([.,])", r"q\2 \1\2",ii)
  ii=re.sub(r"s(shi)([.,])", r"q\2 \1\2",ii)
  ii=re.sub(r"f(fu)([.,])", r"q\2 \1\2",ii)
  ii=re.sub(r"t(tsu)([.,])", r"q\2 \1\2",ii)
  ii=re.sub(r"j(ji)([.,])", r"q\2 \1\2",ii)

  ii=re.sub(r"k(ky)([auo])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"g(gy)([auo])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"s(sh)([auo])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"j(j)([auo])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"d(dy)([auo])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"c(ch)([auo])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"`nny([auo])([.,])", r"q\2 `ny\1\2",ii)
  ii=re.sub(r"h(hy)([auo])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"b(by)([auo])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"p(py)([auo])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"m(my)([auo])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"r(ry)([auo])([.,])", r"q\3 \1\2\3",ii)

  ii=re.sub(r"k(k)([auoie])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"s(s)([auoe])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"t(t)([aoe])([.,])", r"q\3 \1\2\3",ii)
  # ii=re.sub(r"`n(n)([auoie])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"h(h)([aoie])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"f(f)([u])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"m(m)([auoie])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"y(y)([auoie])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"r(r)([auoie])([.,])", r"q\3 \1\2\3",ii)
  # ii=re.sub(w(w)([auoie])([.,])", r"q\3 \1\2\3",ii)

  ii=re.sub(r"g(g)([auoie])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"z(z)([auoie])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"d(d)([auoie])([.,])", r"q\3 \1\2\3",ii)
  ii=re.sub(r"b(b)([auoie])([.,])", r"q\3 \1\2\3",ii)

  ### 假名中拗音 ###

  ii=re.sub(r"(ky)([auo])([.,])", r"ki\3 xy\2\3",ii)
  ii=re.sub(r"(gy)([auo])([.,])", r"gi\3 xy\2\3",ii)
  ii=re.sub(r"(sh)([auo])([.,])", r"shi\3 xy\2\3",ii)
  ii=re.sub(r"(j)([auo])([.,])", r"ji\3 xy\2\3",ii)
  ii=re.sub(r"(dy)([auo])([.,])", r"di\3 xy\2\3",ii)
  ii=re.sub(r"(ch)([auo])([.,])", r"chi\3 xy\2\3",ii)
  ii=re.sub(r"`(ny)([auoie])([.,])", r"ni\3 xy\2\3",ii)
  ii=re.sub(r"(hy)([auoie])([.,])", r"hi\3 xy\2\3",ii)
  ii=re.sub(r"(by)([auoe])([.,])", r"bi\3 xy\2\3",ii)
  ii=re.sub(r"(py)([auoie])([.,])", r"pi\3 xy\2\3",ii)
  ii=re.sub(r"(my)([auoie])([.,])", r"mi\3 xy\2\3",ii)
  ii=re.sub(r"(ry)([auoie])([.,])", r"ri\3 xy\2\3",ii)


  l1[index]=ii

#print(l1)
strout="\n".join(l1)

with open("output_yo_so.txt",mode="w",encoding="utf-8") as outfile:
    outfile.write(strout)

