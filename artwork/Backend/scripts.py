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
        f14 = cv2.cvtColor(
            cv2.Canny(f13, 10, 20),
            cv2.COLOR_GRAY2BGR,
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

    f6[f9 : f10 + 1, f11 : f12 + 1] = f14
    f22, f23, f24 = cv2.split(f6)
    f25 = cv2.merge([f22, f23, f24, f5])
    _, f26 = cv2.imencode(".png", f25)
    f27 = f26.tobytes()
    return f27
