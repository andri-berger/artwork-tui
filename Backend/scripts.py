import numpy as np
import cv2

def scripts_f0(h, h0, h1) -> float:
    f0 = min(h, 100)
    f1 = max(f0,0)
    f2 = f1 / 100
    f3 = h0 - h1
    f4 = f3 * f2
    f5 = f4 + h1
    return f5

def scripts_f1(h, h0) -> bytes:
    f0 = max(h['h'],1)
    f1 = h['h0'] or 0
    f2 = h['h1'] or 0
    f3 = h['h2'] or 0

    f4 = cv2.imdecode(
        np.frombuffer(
            h0, dtype=np.uint8),
        cv2.IMREAD_UNCHANGED)

    f5 = f4[:, :, 3]
    f6 = f4[:, :, :3]
    f7, f8 = np.where(f5 > 0)
    f9, f10 = f7.min(), f7.max()
    f11, f12 = f8.min(), f8.max()
    f13 = f6[f9:f10+1, f11:f12+1]
    f14 = None

    if f0 == 1:
        f14 = cv2.bitwise_not(f13)

    if f0 == 2:
        f14 = cv2.Canny(f4, 10, 20)

    if f0 == 3:
        f14 = cv2.stylization(
            f13,sigma_s=int(scripts_f0(f1, 30, 100)),
            sigma_r=float(scripts_f0(f2, 0.2, 0.7)))

    elif f0 == 4:
        f14 = cv2.detailEnhance(
            f13, sigma_s=float(scripts_f0(f1, 5, 100)),
            sigma_r=float(scripts_f0(f2, 0.1, 0.5)))

    elif f0 == 5:
        _, f14 = cv2.pencilSketch(
            f13, sigma_s=float(scripts_f0(f1, 30, 100)),
            sigma_r=float(scripts_f0(f2, 0.05, 0.3)),
            shade_factor=float(scripts_f0(f3, 0.02, 0.05)))

    elif f0 == 6:
        f15 = int(scripts_f0(f2, 0, 20))
        f16 = int(scripts_f0(f1, 3, 51)) | 1
        f17 = int(scripts_f0(f3, 3, 15)) | 1

        f18 = cv2.cvtColor(f13, cv2.COLOR_RGB2GRAY)
        f19 = cv2.medianBlur(f18, f17)
        f20 = cv2.adaptiveThreshold(
            f19, 255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY, f16, f15)
        f21 = cv2.bilateralFilter(
            f13, 24, 75, 75)
        f14 = cv2.bitwise_and(
            f21, f21, mask=f20)

    f6[f9:f10+1, f11:f12+1] = f14
    f22, f23, f24 = cv2.split(f6)
    f25 = cv2.merge([f22, f23, f24, f5])
    _, f26 = cv2.imencode('.png', f25)
    f27 = f26.tobytes()
    return f27
