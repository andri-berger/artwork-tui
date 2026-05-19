
def make_layer(value):
    return ["auto", "auto"] + [str(value)] * 300

def make_layers(value="0"):
    return ["auto", "auto"] + [""] * 300 + [str(value)] * 300

def make_new(value):
    return ([[""]] + [[f"00 {value}"]]
    + [[f"A{i:02d} {value}"] for i in range(100)]
    + [[f"B{i:02d} {value}"] for i in range(100)]
    + [[f"C{i:02d} {value}"] for i in range(100)]
    + [[f"D{i:02d} {value}"] for i in range(100)]
    + [[f"E{i:02d} {value}"] for i in range(100)]
    + [[f"F{i:02d} {value}"] for i in range(100)])


def make_news(value):
    if value == "Image":
        return ([["VARIOUS PROPERTIES. Lorem ipsum dolor sit amet.",
        "CSS PADDING. Lorem ipsum dolor sit amet.",
        "CSS PADDING. Lorem ipsum dolor sit amet.",
        "CSS BACKGROUND. Lorem ipsum dolor sit amet.",
        "CSS BACKGROUND-SIZE. Lorem ipsum dolor sit amet.",
        "CSS BACKGROUND-POSITION. Lorem ipsum dolor sit amet.",
        "CSS BACKGROUND-IMAGE. Lorem ipsum dolor sit amet."]] * 601)
    elif value == "Content":
        return ([[
        "VARIOUS PROPERTIES. Lorem ipsum dolor sit amet.",
        "CSS POSITION. Lorem ipsum dolor sit amet.",
        "CSS COLOR. Lorem ipsum dolor sit amet.",
        "CSS TEXT-DECORATION. Lorem ipsum dolor sit amet.",
        "CSS FONT-WEIGHT. Lorem ipsum dolor sit amet.",
        "CSS FONT-SIZE. Lorem ipsum dolor sit amet.",
        "CSS FONT-FACE. Lorem ipsum dolor sit amet."]] * 601)

def make_news_0(value):
    if value == "Image":
        return ([[[""],
                  ["00","px",""],
                  ["00","px",""],
                  ["00","unclear",""],
                  ["00","list 6","cover"],
                  ["00","list 3","contain"],
                  ["00","path",""]]]
                    + [[[""],
                  [f"{i0}{i:02d}","px",""],
                  [f"{i0}{i:02d}","px",""],
                  [f"{i0}{i:02d}","unclear",""],
                  [f"{i0}{i:02d}","list 6","cover"],
                  [f"{i0}{i:02d}","list 3","contain"],
                  [f"{i0}{i:02d}","path",""]]
                    for i0 in "ABCDEF"
                    for i in range(100)])
    elif value == "Content":
        return ([[[""],
                  ["00","px",""],
                  ["00","px",""],
                  ["00","unclear",""],
                  ["00","list 6","cover"],
                  ["00","list 3","contain"],
                  ["00","path",""]]]
                    + [[[""],
                  [f"{i0}{i:02d}","px",""],
                  [f"{i0}{i:02d}","px",""],
                  [f"{i0}{i:02d}","unclear",""],
                  [f"{i0}{i:02d}","list 6","cover"],
                  [f"{i0}{i:02d}","list 3","contain"],
                  [f"{i0}{i:02d}","path",""]]
                    for i0 in "ABCDEF"
                    for i in range(100)])


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
            l3 = rot.get(f"00-{row_i}",{})
            for col_i0, i0 in i.items():
                for cell_i1, i1 in i0.items():
                    if row_i == '1':
                        if col_i0 not in l2:
                            l2[col_i0] = {}
                        l2[col_i0][cell_i1] = i1
                    if (row_i == '2'
                        or row_i == '3'):
                        l4 = int(cell_i1)
                        l5 = str(l3[l4])
                        if l5 not in l2:
                            l2[l5] = {}
                        l2[l5][row_i] = i1
    return d_transformed

def tui_to_web(start, rot):
    d_transformed = {}
    starts = start.items()
    for row_i, i in starts:
        if (int(row_i) <= 3):
            if row_i == '2':
                if any(str(k) in i.keys()
                       for k in range(45)):
                    d_transformed['3'] = {}
                if any(str(k) in i.keys()
                       for k in range(45,75)):
                    d_transformed['2'] = {}
            if row_i == '0' or row_i == '1':
                d_transformed[row_i] = {}
            l0 = rot.get(f"0-{row_i}", {})
            for col_i0, i0 in i.items():
                l1 = int(col_i0)
                if row_i == '2':
                    l2 = l1 <= 44
                    l3 = '3' if l2 else '2'
                    l4 = d_transformed[l3]
                if row_i == '0' or row_i == '1':
                    l5 = d_transformed[row_i]
                for cell_i1, i1 in i0.items():
                    if (row_i == '1'
                        or row_i == '4'
                        or row_i == '5'):
                        if col_i0 not in l5:
                            l5[col_i0] = {}
                        l5[col_i0][cell_i1] = i1
                    if (row_i == '2'
                        or row_i == '3'):
                        l6 = row_i == '3'
                        l7 = str(l0[l1])
                        l8 = int(cell_i1)
                        l9 = 301 if l6 else 0
                        if l0[l1] is not None:
                            lss = str(l9 + l8)
                            if lss not in l4:
                                l4[lss] = {}
                            l4[lss][l7] = i1
                    if row_i == '0':
                        l6 = l0[l1]
                        l7 = int(cell_i1)
                        l8 = str(l6[l7])
                        l5[l8] = i1
    return d_transformed



def testlauf(self,image_outs,Image,cv2):
    size = self.size
    cell_w, cell_h = 9, 18
    target_w = size.width * cell_w
    target_h = size.height * cell_h
    container_ratio = target_w / target_h

    img = cv2.imread(str(image_outs))
    height, width = img.shape[:2]
    img_ratio = width / height

    if img_ratio > container_ratio:
        self.query_one(Image).styles.width = "100%"
        self.query_one(Image).styles.height = "auto"
    else:
        self.query_one(Image).styles.width = "auto"
        self.query_one(Image).styles.height = "100%"




