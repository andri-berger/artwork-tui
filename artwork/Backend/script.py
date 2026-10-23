import shutil
from pathlib import Path

from platformdirs import (
    user_data_dir,
    user_state_dir,
)


def script_f02(h) -> Path:
    f0 = Path(h("artwork-tui"))
    f0.mkdir(parents=True, exist_ok=True)
    return f0


def script_f01() -> Path:
    return script_f02(user_state_dir)


def script_f00() -> Path:
    return script_f02(user_data_dir)


def script_f0(h) -> list:
    return ["auto", "auto"] + [str(h)] * 300


def script_f1(h) -> list:
    return (
        ["auto", "auto"]
        + [""] * 300
        + [str(h)] * 300
    )


def script_f2() -> list:
    return [
        [
            [""],
            [f"{h}{h0:02d}", "px", "10"],
            [f"{h}{h0:02d}", "px", "10"],
            [f"{h}{h0:02d}", "px", "10"],
            [f"{h}{h0:02d}", "px", "10"],
            [f"{h}{h0:02d}", "boolean", "false"],
            [f"{h}{h0:02d}", "list 3", "cover"],
            [f"{h}{h0:02d}", "list 8", "center"],
            [f"{h}{h0:02d}", "px,px", ""],
            [f"{h}{h0:02d}", "%,%", ""],
            [f"{h}{h0:02d}", "px,px", ""],
            [f"{h}{h0:02d}", "%,%", ""],
            [f"{h}{h0:02d}", "image", ""],
        ]
        for h in "ABCDEF"
        for h0 in range(100)
    ]


def script_f3() -> list:
    return [
        [
            [""],
            [f"{h}{h0:02d}", "px", "10"],
            [f"{h}{h0:02d}", "px", "10"],
            [f"{h}{h0:02d}", "px", "10"],
            [f"{h}{h0:02d}", "px", "10"],
            [f"{h}{h0:02d}", "#hex", ""],
            [f"{h}{h0:02d}", "#hex", ""],
            [f"{h}{h0:02d}", "list 4", "auto"],
            [f"{h}{h0:02d}", "list 4", "auto"],
            [f"{h}{h0:02d}", "list 3", "none"],
            [f"{h}{h0:02d}", "1-9", "4"],
            [f"{h}{h0:02d}", "px,px", "16"],
            [f"{h}{h0:02d}", "otf", ""],
            [f"{h}{h0:02d}", "text", ""],
        ]
        for h in "ABCDEF"
        for h0 in range(100)
    ]


def script_f4(h) -> list:
    f0 = f" {['Image', 'Text'][h]}"
    return [
        [f"{h1}{h0:02d}{f0}"]
        for h1 in "ABCDEF"
        for h0 in range(100)
    ]


def script_f8(self, h, h0="") -> None:
    # Feedback toast; label-0 keeps its text
    self.notify(h, title=h0, timeout=3)


def script_f5(self, h) -> None:
    f0 = self.app.store["4-2"]
    script_f8(self, f0.get(h, ""))


def script_f6(self, h, h0, h1="") -> None:
    f0 = self.app.store["4-1"].get(h, "")
    script_f8(self, f0.format(f3=h0.upper()), h1)


def script_f7(h, h0, h1, h2) -> None:
    # PNG IHDR: width @16, height @20
    f1 = int.from_bytes(h2[20:24])
    f2 = int.from_bytes(h2[16:20])
    f4 = h0.get("2", 0)
    f3 = h0.get("3")
    f5 = h.height
    f6 = h.width
    f7 = h1.styles
    f8 = f2 / f1 / 1
    f9 = f6 / f8 / 2
    f10 = f5 * f8 * 2

    f11 = f9 - f5
    f12 = f10 - f6
    f13 = f11 * f4
    f14 = f12 * f4
    f15 = f13 / 100
    f16 = f14 / 100
    f17 = round(f15)
    f18 = round(f16)
    f19 = max(f17, 0)
    f20 = max(f18, 0)
    f21 = f3 == "true"
    f7.height = "100%"
    f7.width = "auto"

    if f4 != 0:
        f22 = (-f20, 0)
        f23 = (0, -f19)
        f7.offset = f23 if f21 else f22


def script_f15(h, h0=int) -> int | float:
    # Cell value -> number; 0 for text or
    # an empty cell (hand-edited saves)
    try:
        return h0(h)
    except TypeError, ValueError:
        return 0


def script_f9(h, h0) -> dict:
    # Tables -> JS store. Tables 2/3 flip
    # to element -> property: rows 0-45 go
    # to "2", rows 46-74 to "3" (build.json
    # "0-2"/"0-3" = row -> property)
    f0 = {}
    f1 = h.items()
    for h1, h2 in f1:
        if h1 in ("2", "3"):
            if any(
                str(k) in h2.keys()
                for k in range(46)
            ):
                f0.setdefault("2", {})
            if any(
                str(k) in h2.keys()
                for k in range(46, 75)
            ):
                f0.setdefault("3", {})
        elif int(h1) in [0, 1, 4, 5]:
            f0[h1] = {}
        f2 = h0.get(f"0-{h1}", {})
        for h3, h4 in h2.items():
            f3 = int(h3)
            if h1 in ("2", "3"):
                f4 = f3 <= 45
                f5 = "2" if f4 else "3"
                f6 = f0[f5]
            elif int(h1) in [0, 1, 4, 5]:
                f7 = f0[h1]
            for h5, h6 in h4.items():
                if int(h1) in [1, 4, 5]:
                    if h3 not in f7:
                        f7[h3] = {}
                    f7[h3][h5] = h6
                if int(h1) in [2, 3]:
                    f8 = h1 == "3"
                    f9 = str(f2[f3])
                    f10 = int(h5)
                    f11 = 301 if f8 else 0
                    if f2[f3] is not None:
                        f12 = str(f11 + f10)
                        if f12 not in f6:
                            f6[f12] = {}
                        f6[f12][f9] = h6
                # Table 0: cells without a key
                # (past a row's columns) stay out
                if h1 == "0":
                    f13 = f2[f3]
                    f14 = int(h5)
                    if f14 < len(f13):
                        f15 = str(f13[f14])
                        f7[f15] = h6
    return f0


def script_f10(h, h0) -> dict:
    # CREATE result -> tables: JS "2"/"3"
    # (element -> property) flip back into
    # table 2 rows via build.json "00-2"/"00-3"
    f0 = {}
    f1 = h.items()
    for h1, h2 in f1:
        if h1 not in ("1", "2", "3"):
            continue
        f2 = h1 == "1"
        f3 = "1" if f2 else "2"
        if f3 not in f0:
            f0[f3] = {}
        f4 = f0[f3]
        f5 = h0.get(f"00-{h1}")
        for h3, h4 in h2.items():
            for h5, h6 in h4.items():
                if h1 == "1":
                    if h3 not in f4:
                        f4[h3] = {}
                    f4[h3][h5] = h6
                if h1 == "2" or h1 == "3":
                    f6 = int(h5)
                    f7 = str(f5[f6])
                    if f7 not in f4:
                        f4[f7] = {}
                    f4[f7][h3] = h6
    return f0


def script_f13(h, h0) -> str:
    # Picked file h -> stored name: images
    # keep their suffix, fonts store the stem
    f0 = h.suffix.lower()
    return h.stem if h0 else h.stem + f0


def script_f14(h, h0) -> str:
    # Stored name -> file name; a bare stem
    # means .png (older saves) or .otf;
    # v0.1.0 stored base fonts as x.otf
    f0 = str(h)
    if h0:
        f1 = f0.lower().endswith(".otf")
        return f0 if f1 else f"{f0}.otf"
    return f0 if Path(f0).suffix else f"{f0}.png"


def script_f16(h, h0) -> set:
    # File names store h uses (h0: 0 image,
    # 1 otf): "0"/"37"/"3"|"4" = base
    # image/otf (JS key 144/145 via
    # build.json "0-0"[37]) and
    # "4"|"5"/row/"11" = column 12 of
    # tables 4/5
    f0 = h.get("0", {}).get("37", {})
    f1 = h.get(str(h0 + 4), {}).values()
    f2 = [f0.get(str(h0 + 3))]
    f2 += [h1.get("11") for h1 in f1]
    return {script_f14(h1, h0) for h1 in f2 if h1}


def script_f17(h) -> list:
    # Assets store h uses that are not
    # in the state dir
    return sorted(
        f"{f0}/{h1}"
        for h0, f0 in enumerate(
            ("module", "modules")
        )
        for h1 in script_f16(h, h0)
        if not (script_f01() / f0 / h1).exists()
    )


def script_f12(h, h0, h1, h2) -> None:
    # Copy picked asset h (h0: 0 image, 1 otf)
    # into the state dir; drop the replaced
    # name h2 unless a store h1 still uses it
    f1 = ["module", "modules"][h0]
    f2 = script_f01() / f1
    f2.mkdir(exist_ok=True)
    f3 = f2 / script_f14(script_f13(h, h0), h0)
    f4 = f2 / script_f14(h2, h0)
    f8 = script_f16(h1, h0)
    if h2 and f4.name not in f8 and f4 != f3:
        f4.unlink(missing_ok=True)
    if h.resolve() != f3.resolve():
        shutil.copy2(h, f3)
