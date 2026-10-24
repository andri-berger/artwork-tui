import cv2
import numpy as np


def scripts_f0(h, h0, h1) -> float:
    f0 = min(h, 100)
    f1 = max(f0, 0)
    f2 = f1 / 100
    f3 = h0 - h1
    f4 = f3 * f2
    f5 = f4 + h1
    return f5


def scripts_f1(h, h0) -> bytes:
    f0 = max(h["h"], 1)
    f1 = h["h0"] or 0
    f2 = h["h1"] or 0
    f3 = h["h2"] or 0
    f15 = h["h3"] or 0

    f4 = cv2.imdecode(
        np.frombuffer(h0, dtype=np.uint8),
        cv2.IMREAD_UNCHANGED,
    )

    if f4.ndim != 3 or f4.shape[2] != 4:
        return h0

    f5 = f4[:, :, 3]
    f6 = f4[:, :, :3]
    f7, f8 = np.where(f5 > 0)
    if f7.size == 0:
        return h0
    f9, f10 = f7.min(), f7.max()
    f11, f12 = f8.min(), f8.max()
    f13 = f6[f9 : f10 + 1, f11 : f12 + 1]
    f14 = None

    if f0 == 1:
        f14 = cv2.bitwise_not(f13)

    if f0 == 2:
        # P1/P2 thresholds (empty = 10/20 as
        # before), P4 line thickness 1-9 px
        f14 = cv2.Canny(
            f13,
            scripts_f0(f1, 200, 10),
            scripts_f0(f2, 400, 20),
        )
        f16 = round(scripts_f0(f15, 9, 1))
        if f16 > 1:
            f14 = cv2.dilate(
                f14, np.ones((f16, f16), np.uint8)
            )
        f14 = cv2.cvtColor(
            f14, cv2.COLOR_GRAY2BGR
        )

    if f0 == 3:
        f14 = cv2.stylization(
            f13,
            sigma_s=int(scripts_f0(f1, 30, 100)),
            sigma_r=float(
                scripts_f0(f2, 0.2, 0.7)
            ),
        )

    elif f0 == 4:
        f14 = cv2.detailEnhance(
            f13,
            sigma_s=float(scripts_f0(f1, 5, 100)),
            sigma_r=float(
                scripts_f0(f2, 0.1, 0.5)
            ),
        )

    # P3 fades back to the original (0 = full
    # effect, 100 = original)
    if f3 > 0:
        f17 = scripts_f0(f3, 1, 0)
        f14 = cv2.addWeighted(
            f14, 1 - f17, f13, f17, 0
        )

    # f6 is a view: this writes into f4, alpha
    # untouched, so no split/merge copies
    f6[f9 : f10 + 1, f11 : f12 + 1] = f14
    _, f26 = cv2.imencode(".png", f4)
    f27 = f26.tobytes()
    return f27
