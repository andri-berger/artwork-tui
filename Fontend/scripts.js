self.onmessage = async (l) => {
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

	for (let x = 0; x < l.data[0]; x += l7) {
		for (let y = 0; y < l.data[1]; y += l8) {
			const l41 = (x + y * l.data[0]) * 4
			const l42 = l4[l41 + 0]
			const l43 = l4[l41 + 1]
			const l44 = l4[l41 + 2]
			const l45 = l4[l41 + 3] / 255
			const l46 = l45.toFixed(0 || 2)
			const l47 = [0 || l42, l43, l44, l46]
			if (l4[l41 + 3] === 0) continue
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
			const l63 = l49 * l31 + l27
			const l64 = l50 * l32 + l28
			const l65 = l51 * l31 + l29
			const l66 = l52 * l32 + l30
			const l71 = l53 * l26 + l25
			const l74 = l54 * l22 + l21
			const l75 = l55 * l20 + l19
			const l76 = l56 * l24 + l23
			const l67 = Math.min(3, l63)
			const l68 = Math.min(3, l64)
			const l69 = Math.min(3, l65)
			const l70 = Math.min(3, l66)
			const l72 = Math.min(7, l71)
			const l73 = Math.round(l72)
			const l77 = 2 - Math.min(2, l75)
			const l78 = Math.min(2, l74)
			const l83 = l57 - 0.5
			const l84 = l58 - 0.5
			const l85 = l59 * l10
			const l86 = l60 * l12
			const l87 = l61 * l14
			const l88 = l83 * l15 * l7
			const l89 = l84 * l16 * l8
			const l90 = !l12 ? l85 : l86
			const l91 = !l14 ? l85 : l87
			const l92 = (l90 + l39) * l7
			const l93 = (l91 + l40) * l8
			const l96 = Math.max(0, l92 - l62)
			const l97 = Math.max(0, l93 - l62)
			const l82 = (l77 + l78) * Math.PI
			const l80 = l78 * Math.PI
			const l81 = l76 * Math.PI
			const l98 = (l96 - l7) / 2
			const l99 = (l97 - l8) / 2
			const l100 = x - l98 + l88
			const l101 = y - l99 + l89
			const l102 = l100 - l7 / 2
			const l103 = l101 - l8 / 2
			const l104 = [l81, l80, l82]
			const l105 = [l96 / 2, l97 / 2]
			const l106 = [x + l88, y + l89]
			const l107 = [...l105, ...l104]
			const l108 = [...l106, ...l107]
			const l109 = [l102, l103, l96, l97]
			const l110 = l103 + l97 / 2
			const l111 = l102 + l96 / 2
			const l112 = l103 + l97
			const l113 = l102 + l96
			const l114 = [
				[l102, l103, l113, l112],
				[l102, l110, l113, l110],
				[l102, l112, l113, l103],
				[l111, l112, l111, l103],
				[l113, l112, l102, l103],
				[l113, l110, l102, l110],
				[l113, l103, l102, l112],
				[l111, l103, l111, l112],
			]

			const l115 = l114[l73]
			const l116 = l115.slice(0, 2)
			const l117 = l115.slice(2, 4)
			const l118 = l102 - l96 + l96 * l67
			const l119 = l103 - l97 + l97 * l68
			const l120 = l102 - l96 + l96 * l69
			const l121 = l103 - l97 + l97 * l70
			l5.strokeStyle = `rgba(${l47})`
			l5.fillStyle = `rgba(${l47})`
			l5.lineCap = `square`
			l5.lineWidth = l62
			l5.beginPath()

			if (l6 === 0) {
				l5.rect(...l109)
			}
			if (l6 === 1) {
				l5.ellipse(...l108)
			}
			if (l6 === 2) {
				l5.moveTo(...l116)
				l5.lineTo(...l117)
			}
			if (l6 === 3) {
				if (l36 === false) {
					l5.moveTo(...l116)
					l5.quadraticCurveTo(l118, l119, ...l117)
				}
				if (l36 === true) {
					l5.moveTo(...l116)
					l5.bezierCurveTo(l118, l119, l120, l121, ...l117)
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
	const l41 = await createImageBitmap(l3)
	self.postMessage(l41, [l41])
}
