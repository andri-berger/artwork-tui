
def make_layer(value, size=300):
    return ["auto", "auto"] + [str(value)] * size

def make_sparse_layer(empty_count=300, value="0", filled_count=300, size=300):
    return ["auto", "auto"] + [""] * empty_count + [str(value)] * filled_count


def hash_table(start, rot):
    d_transformed = {}
    for row_i, row in start:
        shot = rot[f"0-{row_i}"]
        if row_i == '2':
            if any(str(k) in row.keys()
                   for k in range(44)):
                d_transformed['3'] = {}
            if any(str(k) in row.keys()
                   for k in range(45 ,75)):
                d_transformed['2'] = {}
        if row_i == '0' or row_i == '1':
            d_transformed[row_i] = {}
        for col_i, col in row.items():
            if row_i == '2':
                tor = int(col_i) <= 44
                tes = '3' if tor else '2'
                ttts = d_transformed[tes]
            if row_i == '0' or row_i == '1':
                tt = d_transformed[row_i]
            for cell_i, cell in col.items():
                rst = shot[int(col_i)]
                sht = str(rst)
                if row_i == '0':
                    ust = int(cell_i)
                    bst = str(rst[ust])
                    tt[bst] = cell
                if row_i == '1':
                    if sht not in tt:
                        tt[sht] = {}
                    tt[sht][cell_i] = cell
                if row_i == '2':
                    if cell_i not in ttts:
                        ttts[cell_i] = {}
                    ttts[cell_i][sht] = cell
    return d_transformed
