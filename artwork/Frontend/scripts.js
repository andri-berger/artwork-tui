// Sync on purpose: a throw reaches the page as an
// error event (h13 rejects) instead of hanging
self.onmessage = (l) => {
	const l0 = l.data[2]
	const l1 = l.data[3]
	const l2 = [l.data[0], l.data[1]]
	const l3 = new OffscreenCanvas(...l2)
	const l4 = new Uint8ClampedArray(l0)
	const l5 = l3.getContext('2d')

	const l6 = l1[50] || 0
	const l7 = l1[51] * 2 + 3 || 3
	const l8 = l1[52] * 2 + 3 || 3
	const l9 = l1[53] / 30 || 0
	const l10 = l1[54] / 30 || 0
	const l11 = l1[55] / 30 || 0
	const l12 = l1[56] / 30 || 0
	const l13 = l1[57] / 30 || 0
	const l14 = l1[58] / 30 || 0
	const l15 = l1[59] / 30 || 0
	const l16 = l1[60] / 30 || 0
	const l17 = l1[61] / 2 || 0
	const l18 = l1[62] / 2 || 0
	const l19 = l1[63] / 50 || 0
	const l20 = l1[64] / 50 || 0
	const l21 = l1[65] / 50 || 0
	const l22 = l1[66] / 50 || 0
	const l23 = l1[67] / 50 || 0
	const l24 = l1[68] / 50 || 0
	const l25 = (l1[67] / 100) * 7 || 0
	const l26 = (l1[68] / 100) * 7 || 0
	const l27 = l1[69] / 30 || 0
	const l28 = l1[70] / 30 || 0
	const l29 = l1[71] / 30 || 0
	const l30 = l1[72] / 30 || 0
	const l31 = l1[73] / 30 || 0
	const l32 = l1[74] / 30 || 0

	const l33 = l9 <= 1 ? 1 - l9 : l9
	const l34 = l11 <= 1 ? 1 - l11 : l11
	const l35 = l13 <= 1 ? 1 - l13 : l13
	const l36 = l29 > 0 && l30 > 0
	const l37 = l17 > 0 || l18 > 0
	const l38 = l37 || l6 >= 2
	const l39 = !l11 ? l33 : l34
	const l40 = !l13 ? l33 : l35

	// Style only changes with the pixel color, line
	// cap once: per-pixel style strings were the cost
	const l41 = l38 ? 'strokeStyle' : 'fillStyle'
	let l42 = ''
	l5.lineCap = 'square'

	for (let x = 0; x < l.data[0]; x += l7) {
		for (let y = 0; y < l.data[1]; y += l8) {
			const l43 = (x + y * l.data[0]) * 4
			if (l4[l43 + 3] === 0) continue
			const l44 = (l4[l43 + 3] / 255).toFixed(2)
			const l45 = `rgba(${l4[l43]},${l4[l43 + 1]},${l4[l43 + 2]},${l44})`
			const l48 = Math.random()
			const l49 = Math.random()
			const l50 = Math.random()
			const l51 = Math.random()
			const l52 = Math.random()
			const l53 = Math.random()
			const l54 = Math.random()
			const l55 = Math.random()
			const l56 = Math.random()
			const l57 = Math.random()
			const l58 = Math.random()
			const l59 = Math.random()
			const l60 = Math.random()
			const l61 = Math.random()

			const l62 = l48 * l18 + l17
			const l85 = l59 * l10
			const l90 = !l12 ? l85 : l60 * l12
			const l91 = !l14 ? l85 : l61 * l14
			const l88 = (l57 - 0.5) * l15 * l7
			const l89 = (l58 - 0.5) * l16 * l8
			const l96 = Math.max(
				0,
				(l90 + l39) * l7 - l62,
			)
			const l97 = Math.max(
				0,
				(l91 + l40) * l8 - l62,
			)
			const l102 =
				x - (l96 - l7) / 2 + l88 - l7 / 2
			const l103 =
				y - (l97 - l8) / 2 + l89 - l8 / 2
			if (l45 !== l42) {
				l42 = l45
				l5[l41] = l45
			}
			if (l38) {
				l5.lineWidth = l62
			}
			l5.beginPath()

			if (l6 === 0) {
				l5.rect(l102, l103, l96, l97)
			}
			if (l6 === 1) {
				const l77 =
					2 - Math.min(2, l55 * l20 + l19)
				const l78 = Math.min(2, l54 * l22 + l21)
				l5.ellipse(
					x + l88,
					y + l89,
					l96 / 2,
					l97 / 2,
					(l56 * l24 + l23) * Math.PI,
					l78 * Math.PI,
					(l77 + l78) * Math.PI,
				)
			}
			if (l6 === 2 || l6 === 3) {
				// Direction 0-7, clamped (negative
				// values threw): start on the cell edge,
				// end on the opposite side
				const l73 = Math.round(
					Math.max(
						0,
						Math.min(7, l53 * l26 + l25),
					),
				)
				const l110 = l103 + l97 / 2
				const l111 = l102 + l96 / 2
				const l112 = l103 + l97
				const l113 = l102 + l96
				const l114 = [
					l102,
					l102,
					l102,
					l111,
					l113,
					l113,
					l113,
					l111,
				]
				const l115 = [
					l103,
					l110,
					l112,
					l112,
					l112,
					l110,
					l103,
					l103,
				]
				const l116 = l114[(l73 + 4) % 8]
				const l117 = l115[(l73 + 4) % 8]
				l5.moveTo(l114[l73], l115[l73])
				if (l6 === 2) {
					l5.lineTo(l116, l117)
				}
				if (l6 === 3) {
					const l118 =
						l102 -
						l96 +
						l96 * Math.min(3, l49 * l31 + l27)
					const l119 =
						l103 -
						l97 +
						l97 * Math.min(3, l50 * l32 + l28)
					if (l36 === false) {
						l5.quadraticCurveTo(
							l118,
							l119,
							l116,
							l117,
						)
					}
					if (l36 === true) {
						l5.bezierCurveTo(
							l118,
							l119,
							l102 -
								l96 +
								l96 *
									Math.min(3, l51 * l31 + l29),
							l103 -
								l97 +
								l97 *
									Math.min(3, l52 * l32 + l30),
							l116,
							l117,
						)
					}
				}
			}
			if (l38 === false) {
				l5.fill()
			}
			if (l38 === true) {
				l5.stroke()
			}
		}
	}
	const l120 = l3.transferToImageBitmap()
	self.postMessage(l120, [l120])
}
