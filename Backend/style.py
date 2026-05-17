
import numpy as np
import cv2


def clamp(value, max_val, min_val):
    value = max(0, min(value, 100))
    range = max_val - min_val
    ranges = value / 100.0
    total = range * ranges
    return total + min_val

def opencv(args, args0):
    setting = args0['setting']
    setting0 = args0['setting0']
    setting1 = args0['setting1']
    setting2 = args0['setting2']

    img = cv2.imdecode(
        np.frombuffer(args,
        dtype=np.uint8),
        cv2.IMREAD_UNCHANGED)

    rgb = img[:, :, :3]
    alpha = img[:, :, 3]
    ys, xs = np.where(alpha > 0)
    y_min, y_max = ys.min(), ys.max()
    x_min, x_max = xs.min(), xs.max()
    sub_rgb = rgb[y_min:y_max + 1, x_min:x_max + 1]

    if setting == 0:
        return

    if setting == 1:


        enhanced = cv2.bitwise_not(sub_rgb)

    # if setting == 1:
    #    enhanced = cv2.Canny(img, 10, 20)

    if setting == 2:
        enhanced = cv2.stylization(sub_rgb,
            sigma_s=int(clamp(setting0, 30, 100)),
            sigma_r=float(clamp(setting1, 0.2, 0.7)))

    elif setting == 3:
        enhanced = cv2.detailEnhance(sub_rgb,
            sigma_s=float(clamp(setting0, 5, 100)),
            sigma_r=float(clamp(setting1, 0.1, 0.5)))

    elif setting == 4:
        _, enhanced = cv2.pencilSketch(sub_rgb,
            sigma_s=float(clamp(setting0, 30, 100)),
            sigma_r=float(clamp(setting1, 0.05, 0.3)),
            shade_factor=float(clamp(setting2, 0.02, 0.05)))

    elif setting == 5:
        adaptive_II = int(clamp(setting1, 0, 20))
        adaptive_I = int(clamp(setting0, 3, 51)) | 1
        medianBlur = int(clamp(setting2, 3, 15)) | 1

        gray = cv2.cvtColor(sub_rgb, cv2.COLOR_RGB2GRAY)
        gray_blur = cv2.medianBlur(gray, medianBlur)
        edges = cv2.adaptiveThreshold(
            gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY, adaptive_I, adaptive_II)
        color = cv2.bilateralFilter(sub_rgb, 24, 75, 75)
        enhanced = cv2.bitwise_and(color, color, mask=edges)

    rgb[y_min:y_max + 1, x_min:x_max + 1] = enhanced
    b, g, r = cv2.split(rgb)
    processed = cv2.merge([b, g, r, alpha])
    _, encoded_img = cv2.imencode('.png', processed)
    image_bytes = encoded_img.tobytes()
    return image_bytes


