
def make_layer(value):
    return ["auto", "auto"] + [str(value)] * 300

def make_layers(value="0"):
    return ["auto", "auto"] + [""] * 300 + [str(value)] * 300

def make_new(value):
    return (
    [[f"A{i:02d} {value}"] for i in range(100)]
    + [[f"B{i:02d} {value}"] for i in range(100)]
    + [[f"C{i:02d} {value}"] for i in range(100)]
    + [[f"D{i:02d} {value}"] for i in range(100)]
    + [[f"E{i:02d} {value}"] for i in range(100)]
    + [[f"F{i:02d} {value}"] for i in range(100)])


def make_news(value):
    if value == "Image":
        return ([[
        "VARIOUS PROPERTIES. Lorem ipsum dolor sit amet.",
        "CSS PADDING-LEFT. Lorem ipsum dolor sit amet.",
        "CSS PADDING-RIGHT. Lorem ipsum dolor sit amet.",
        "CSS PADDING-TOP. Lorem ipsum dolor sit amet.",
        "CSS PADDING-BOTTOM. Lorem ipsum dolor sit amet.",
        "CSS BACKGROUND-ORIGIN. Lorem ipsum dolor sit amet.",
        "CSS BACKGROUND-SIZE. Lorem ipsum dolor sit amet. => contain, auto, 100%",
        "CSS BACKGROUND-POSITION. Lorem ipsum dolor sit amet. => top, left, right, bottom, angle nw, angle sw, angle ne, angle se",
        "CSS BACKGROUND-POSITION. Lorem ipsum dolor sit amet.",
        "CSS BACKGROUND-POSITION. Lorem ipsum dolor sit amet.",
        "CSS BACKGROUND-SIZE. Lorem ipsum dolor sit amet.",
        "CSS BACKGROUND-SIZE. Lorem ipsum dolor sit amet.",
        "CSS BACKGROUND-IMAGE. Lorem ipsum dolor sit amet."]] * 601)
    elif value == "Text":
        return ([[
        "VARIOUS PROPERTIES. Lorem ipsum dolor sit amet.",
        "CSS PADDING-LEFT. Lorem ipsum dolor sit amet.",
        "CSS PADDING-RIGHT. Lorem ipsum dolor sit amet.",
        "CSS PADDING-TOP. Lorem ipsum dolor sit amet.",
        "CSS PADDING-BOTTOM. Lorem ipsum dolor sit amet.",
        "CSS BACKGROUND-COLOR. Lorem ipsum dolor sit amet.",
        "CSS STYLE COLOR. Lorem ipsum dolor sit amet.",
        "CSS ALIGN-SELF. Lorem ipsum dolor sit amet. => start, end, center, stretch",
        "CSS TEXT-ALIGN. Lorem ipsum dolor sit amet. => left, center, right, justify",
        "CSS TEXT-DECORATION. Lorem ipsum dolor sit amet. => both, over, under",
        "CSS FONT-WEIGHT. Lorem ipsum dolor sit amet.",
        "CSS FONT-SIZE LINE-HEIGHT. Lorem ipsum dolor sit amet.",
        "CSS FONT-FACE. Lorem ipsum dolor sit amet.",
        "HTML SPAN ENTITY. Lorem ipsum dolor sit amet."]] * 601)

def make_news_0(value):
    if value == "Image":
        return ([[[""],
                  [f"{i0}{i:02d}","px","10"],
                    [f"{i0}{i:02d}","px","10"],
                    [f"{i0}{i:02d}","px","10"],
                    [f"{i0}{i:02d}","px","10"],
                    [f"{i0}{i:02d}","boolean","false"],
                    [f"{i0}{i:02d}","list 3","cover"],
                    [f"{i0}{i:02d}","list 8","center"],
                    [f"{i0}{i:02d}","px,px",""],
                    [f"{i0}{i:02d}","%,%",""],
                    [f"{i0}{i:02d}","px,px",""],
                    [f"{i0}{i:02d}","%,%", ""],
                    [f"{i0}{i:02d}","png",""]]
                    for i0 in "ABCDEF"
                    for i in range(100)])
    elif value == "Text":
        return ([[[""],
                    [f"{i0}{i:02d}","px","10"],
                    [f"{i0}{i:02d}","px","10"],
                    [f"{i0}{i:02d}","px","10"],
                    [f"{i0}{i:02d}","px","10"],
                    [f"{i0}{i:02d}","#hex",""],
                    [f"{i0}{i:02d}","#hex",""],
                    [f"{i0}{i:02d}","list 4","auto"],
                    [f"{i0}{i:02d}","list 4","auto"],
                    [f"{i0}{i:02d}","list 3","none"],
                    [f"{i0}{i:02d}","1-9","4"],
                    [f"{i0}{i:02d}","px,px","16"],
                    [f"{i0}{i:02d}","otf",""],
                    [f"{i0}{i:02d}","text",""]]
                    for i0 in "ABCDEF"
                    for i in range(100)])


def web_to_tui(start, rot):
    d_transformed = {}
    starts = start.items()
    for row_i, i in starts:
        l0 = row_i == '1'
        l1 = '1' if l0 else '2'
        if l1 not in d_transformed:
            d_transformed[l1] = {}
        l2 = d_transformed[l1]
        l3 = rot.get(f"00-{row_i}")
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
                    l2[l5][col_i0] = i1
    return d_transformed

def tui_to_web(start, rot):
    d_transformed = {}
    starts = start.items()
    for row_i, i in starts:
      if row_i == '2':
          if any(str(k) in i.keys()
                 for k in range(45)):
              d_transformed['2'] = {}
          if any(str(k) in i.keys()
                 for k in range(45,75)):
              d_transformed['3'] = {}
      elif int(row_i) in [0,1,4,5]:
          d_transformed[row_i] = {}
      l0 = rot.get(f"0-{row_i}", {})
      for col_i0, i0 in i.items():
          l1 = int(col_i0)
          if row_i == '2':
              l2 = l1 <= 44
              l3 = '2' if l2 else '3'
              l4 = d_transformed[l3]
          elif int(row_i) in [0,1,4,5]:
              l5 = d_transformed[row_i]
          for cell_i1, i1 in i0.items():
              if int(row_i) in [1,4,5]:
                  if col_i0 not in l5:
                      l5[col_i0] = {}
                  l5[col_i0][cell_i1] = i1
              if int(row_i) in [2,3]:
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

