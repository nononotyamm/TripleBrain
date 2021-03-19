question = []
stock = []
while True:
    _q = input().split()
    if len(_q) == 1 and _q[0] == "eof":
        if stock:
            question.append(''.join(stock))
        break
    if _q == []:
        question.append(''.join(stock))
        question.append('\n')
        stock = []
        continue
    stock.append(''.join(_q))

res_text = ""
tex_stock = []
alp_continue = False
for i, sentence in enumerate(question):
    for c in sentence:

        if alp_continue and not c.isascii():
            tex_stock.append('$')
            if len(tex_stock) == 4 and tex_stock[-2] in ['i', 'j', 'k']:
                tex_stock.insert(2, '_')
            res_text += ''.join(tex_stock)
            tex_stock = []
            res_text += c
            alp_continue = False
            continue

        if c.isascii() and c != '\n':
            if not alp_continue:
                alp_continue = True
                tex_stock.append('$')
            tex_stock.append(c)
            continue

        res_text += c
if tex_stock:
    tex_stock.append('$')
    if len(tex_stock) == 4 and tex_stock[-2] in ['i', 'j', 'k']:
        tex_stock.insert(2, '_')
    res_text += ''.join(tex_stock)

print(res_text)
