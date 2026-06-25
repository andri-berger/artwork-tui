import cv2

def script_f0(h) -> list:
    return (["auto", "auto"] +
            [str(h)] * 300)

def script_f1(h) -> list:
    return (["auto", "auto"] +
            [""] * 300 +
            [str(h)] * 300)

def script_f2() -> list:
    return ([[[""],
              [f"{h}{h0:02d}","px","10"],
              [f"{h}{h0:02d}","px","10"],
              [f"{h}{h0:02d}","px","10"],
              [f"{h}{h0:02d}","px","10"],
              [f"{h}{h0:02d}","boolean","false"],
              [f"{h}{h0:02d}","list 3","cover"],
              [f"{h}{h0:02d}","list 8","center"],
              [f"{h}{h0:02d}","px,px",""],
              [f"{h}{h0:02d}","%,%",""],
              [f"{h}{h0:02d}","px,px",""],
              [f"{h}{h0:02d}","%,%", ""],
              [f"{h}{h0:02d}","png",""]]
             for h in "ABCDEF"
             for h0 in range(100)])

def script_f3() -> list:
    return ([[[""],
              [f"{h}{h0:02d}","px","10"],
              [f"{h}{h0:02d}","px","10"],
              [f"{h}{h0:02d}","px","10"],
              [f"{h}{h0:02d}","px","10"],
              [f"{h}{h0:02d}","#hex",""],
              [f"{h}{h0:02d}","#hex",""],
              [f"{h}{h0:02d}","list 4","auto"],
              [f"{h}{h0:02d}","list 4","auto"],
              [f"{h}{h0:02d}","list 3","none"],
              [f"{h}{h0:02d}","1-9","4"],
              [f"{h}{h0:02d}","px,px","16"],
              [f"{h}{h0:02d}","otf",""],
              [f"{h}{h0:02d}","text",""]]
             for h in "ABCDEF"
             for h0 in range(100)])

def script_f4(h) -> list:
    f0 = f" {["Text","Image"][h]}"
    f1 = ([[f"A{h0:02d}{f0}"] for h0 in range(100)]
    + [[f"B{h0:02d}{f0}"] for h0 in range(100)]
    + [[f"C{h0:02d}{f0}"] for h0 in range(100)]
    + [[f"D{h0:02d}{f0}"] for h0 in range(100)]
    + [[f"E{h0:02d}{f0}"] for h0 in range(100)]
    + [[f"F{h0:02d}{f0}"] for h0 in range(100)])
    return f1

def script_f5(self, h) -> None:
    f0 = self.query_one("#label-0")
    f1 = self.app.store["4-1"]
    f2 = self.app.textfield
    f0.update(f1.get(h, ""))
    self.app.textfields = (
        self.set_timer(
            3, lambda:
            f0.update(f2)))

def script_f6(self, h, h0) -> None:
    f0 = self.query_one("#label-0")
    f1 = self.app.store["4-2"]
    f2 = self.app.textfield
    f3 = f1.get(h, "")
    f0.update(f3.format(
        f3=h0.upper()))
    self.app.textfields = (
        self.set_timer(
            3, lambda:
            f0.update(f2)))

def script_f7(self, h, h0) -> None:
    f0 = cv2.imread(str(h))
    f1 = self.query_one(h0)
    f2 = self.size.width * 9
    f3 = self.size.height * 18
    f4, f5 = f0.shape[:2]
    f6 = f1.styles
    f7 = f5 / f4
    if f7 > (f2 / f3):
        f6.width = "100%"
        f6.height = "auto"
    elif f7 <= (f2 / f3):
        f6.width = "auto"
        f6.height = "100%"

def script_f8(h, h0) -> dict:
    f0 = {}
    f1 = h.items()
    for h1, h2 in f1:
        f2 = h1 == '1'
        f3 = '1' if f2 else '2'
        if f3 not in f0:
            f0[f3] = {}
        f4 = f0[f3]
        f5 = h0.get(f"00-{h1}")
        for h3, h4 in h2.items():
            for h5, h6 in h4.items():
                if h1 == '1':
                    if h3 not in f4:
                        f4[h3] = {}
                    f4[h3][h5] = h6
                if (h1 == '2'
                    or h1 == '3'):
                    f6 = int(h5)
                    f7 = str(f5[f6])
                    if f7 not in f4:
                        f4[f7] = {}
                    f4[f7][h3] = h6
    return f0

def script_f9(h, h0) -> dict:
    f0 = {}
    f1 = h.items()
    for h1, h2 in f1:
      if h1 == '2':
          if any(str(k) in h2.keys()
                 for k in range(45)):
              f0['2'] = {}
          if any(str(k) in h2.keys()
                 for k in range(45,75)):
              f0['3'] = {}
      elif int(h1) in [0,1,4,5]:
          f0[h1] = {}
      f2 = h0.get(f"0-{h1}", {})
      for h3, h4 in h2.items():
          f3 = int(h3)
          if h1 == '2':
              f4 = f3 <= 44
              f5 = '2' if f4 else '3'
              f6 = f0[f5]
          elif int(h1) in [0,1,4,5]:
              f7 = f0[h1]
          for h5, h6 in h4.items():
              if int(h1) in [1,4,5]:
                  if h3 not in f7:
                      f7[h3] = {}
                  f7[h3][h5] = h6
              if int(h1) in [2,3]:
                  f8 = h1 == '3'
                  f9 = str(f2[f3])
                  f10 = int(h5)
                  f11 = 301 if f8 else 0
                  if f2[f3] is not None:
                      f12 = str(f11 + f10)
                      if f12 not in f6:
                          f6[f12] = {}
                      f6[f12][f9] = h6
              if h1 == '0':
                  f13 = f2[f3]
                  f14 = int(h5)
                  f15 = str(f13[f14])
                  f7[f15] = h6
    return f0
