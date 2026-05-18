
def make_layer(value, size=300):
    return ["auto", "auto"] + [str(value)] * size

def make_layers(empty_count=300, value="0", filled_count=300, size=300):
    return ["auto", "auto"] + [""] * empty_count + [str(value)] * filled_count



# from tui to web
def tui_to_web(start, rot):
    d_transformed = {}
    starts = start.items()
    for row_i, row in starts:
        if (int(row_i) <= 3):
            if row_i == '2':
                if any(str(k) in row.keys()
                       for k in range(44)):
                    d_transformed['3'] = {}
                if any(str(k) in row.keys()
                       for k in range(45 ,75)):
                    d_transformed['2'] = {}
            if row_i == '0' or row_i == '1':
                d_transformed[row_i] = {}
            shot = rot.get(f"0-{row_i}", {})
            for col_i, col in row.items():
                you = int(col_i)
                if row_i == '2':
                    tor = you <= 44
                    tes = '3' if tor else '2'
                    ttts = d_transformed[tes]
                if row_i == '0' or row_i == '1':
                    tt = d_transformed[row_i]
                for cell_i, cell in col.items():
                    if row_i == '0':
                        rst = shot[you]
                        ust = int(cell_i)
                        bst = str(rst[ust])
                        tt[bst] = cell
                    if row_i == '1':
                        if col_i not in tt:
                            tt[col_i] = {}
                        tt[col_i][cell_i] = cell
                    if row_i == '2':
                        sht = str(shot[you])
                        if cell_i not in ttts:
                            ttts[cell_i] = {}
                        ttts[cell_i][sht] = cell
    return d_transformed

# from web to tui
def web_to_tui(start, rot):
    d_transformed = {}
    starts = start.items()
    for row_i, i in starts:
        if (row_i == "3"
            or row_i == "2"
            or row_i == "1"):
            l0 = row_i == '1'
            l1 = '1' if l0 else '2'
            d_transformed[l1] = {}
            l2 = d_transformed[l1]
            l3 = rot[f"00-{row_i}"]
            for col_i0, i0 in i.items():
                for cell_i1, i1 in i0.items():
                    l5 = l3[int(cell_i1)]
                    l6 = str(l5) or ""
                    if row_i == '1':
                        if col_i0 not in l2:
                            l2[col_i0] = {}
                        l2[col_i0][cell_i1] = i1
                    if (row_i == '2'
                        or row_i == '3'):
                        if l6 not in l2:
                            l2[l6] = {}
                        l2[l6][row_i] = i1
    return d_transformed
