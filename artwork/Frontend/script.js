import { toCanvas } from 'html-to-image'
import * as filters from 'pixi-filters'
import * as PIXI from 'pixi.js'
import * as d3 from 'random'
import k from './model.js'

const k0 = {
	'02': {
		'2-01': 20,
		'2-02': 30,
		'3-01': 20,
		'3-02': 30,
		'4-01': 20,
		'4-02': 30,
		'2-19': 100,
		'3-19': 100,
		'4-19': 100,
	},
	'00': {
		'l00-0': ['0', -10, 10],
		'l00-1': ['-', 60, 100],
		'l00-2': ['0', -400, 400],
		'l00-3': ['0', -300, 100],
		'l00-4': ['0', -300, 100],
		'l00-5': ['-', 60, 100],
		'l00-6': ['1-1', 0, 4],
		'l00-7': ['0-1', 0, 3],
		'l00-9': ['-', 0, 100],
		'l00-10': ['0', 0, 100],
		'l00-11': ['1', -50, 50],
		'l00-12': ['1', -50, 50],
		'l00-13': ['1', -50, 50],
		'l00-14': ['1', -50, 50],
		'l00-15': ['1', -50, 50],
		'l00-16': ['1', -50, 50],
		'l00-17': ['2', 0, 100],

		'k00-0': ['-', 60, 100],
		'k00-1': ['0', -400, 400],
		'k00-2': ['0', -300, 100],
		'k00-3': ['0', -300, 100],
		'k00-4': ['-', 60, 100],
		'k00-5': ['0-1', 0, 3],
		'k00-6': ['0-1', 0, 3],
		'k00-8': ['0', 0, 100],
		'k00-9': ['0', 0, 100],
		'k00-10': ['1', -50, 50],
		'k00-11': ['1', -50, 50],
		'k00-12': ['1', -50, 50],
		'k00-13': ['1', -50, 50],
		'k00-14': ['1', -50, 50],
		'k00-15': ['1', -50, 50],
		'k00-16': ['2', 0, 100],

		't00-0': ['-', 60, 100],
		't00-1': ['0', -400, 400],
		't00-2': ['0', -300, 100],
		't00-3': ['0', -300, 100],
		't00-4': ['-', 60, 100],
		't00-5': ['0-1', 0, 3],
		't00-6': ['0-1', 0, 3],
		't00-8': ['0', 0, 100],
		't00-9': ['0', 0, 100],
		't00-10': ['1', -50, 50],
		't00-11': ['1', -50, 50],
		't00-12': ['1', -50, 50],
		't00-13': ['1', -50, 50],
		't00-14': ['1', -50, 50],
		't00-15': ['1', -50, 50],
		't00-16': ['2', 0, 100],
	},
	'01': {
		'f0-0': ['0', -10, 10],
		'f0-1': ['0', -10, 10],
		'f0-2': ['0', -10, 10],
		'f0-3': ['0', -10, 10],
		'f0-4': ['0-2', 0, 3],
		'f0-5': ['0', 0, 10],
		'f0-6': ['0', -10, 10],
		'f0-7': ['0', -10, 10],
		'f0-8': ['0', -10, 10],
		'f0-9': ['0-0', 0, 2],
		'f0-10': ['0', 0, 10],
		'f0-11': ['0', -10, 10],
		'f0-12': ['0', -10, 10],
		'f0-13': ['0', -10, 10],
		'f0-14': ['0-0', 0, 2],
		'f0-15': ['0', 0, 10],
		'f0-16': ['0', 0, 10],
		'f0-17': ['0', 0, 10],
		'f0-18': ['0', 0, 10],
		'f0-19': ['0', 0, 10],
		'f0-20': ['0', -10, 10],
		'f0-24': ['1', 0, 100],
		'f0-26': ['1', 0, 100],
		'f0-28': ['1', 0, 100],
		'f0-30': ['1', 0, 100],
		'f0-35': ['0', 0, 360],

		'f1-0': ['3', 0, 1],
		'f1-1': ['3', 0, 1],
		'f1-2': ['3', 0, 1],
		'f1-3': ['3', 0, 1],
		'f1-4': ['3', 0, 1],
		'f1-5': ['3', 0, 1],
		'f1-6': ['3', 0, 1],
		'f1-9': ['3-3', 0, 13],
		'f1-10': ['0-0', 0, 2],
		'f1-11': ['0-0', 0, 2],
		'f1-12': ['0', 0, 10],
		'f1-13': ['0', -10, 10],
		'f1-14': ['0', -10, 10],
		'f1-15': ['0', 0, 100],
		'f1-16': ['0', 0, 100],
		'f1-17': ['0', 0, 100],
		'f1-19': ['0', 0, 100],
		'f1-20': ['0', 0, 100],
		'f1-22': ['4-3', 0, 8],
		'f1-23': ['5-3', 0, 3],
		'f1-24': ['6-3', 0, 2],
		'f1-25': ['1', 0, 10],
		'f1-26': ['1', 0, 100],

		'f1-l00': ['3', 14, 40],
		'f1-k00': ['3', 14, 40],
		'f1-t00': ['3', 14, 40],
		'f0-t00': ['2', 0, 35],
		'f0-k00': ['2', 0, 35],
		'f0-l00': ['2', 0, 35],
		l00: ['1', 0, 17, 1],
		k00: ['1', 19, 35, 101],
		t00: ['1', 37, 53, 201],
	},
	'03': {
		'0-0': ['false', 'true'],
		'6-3': ['linear', 'radial'],
		'0-1': ['start', 'ends', 'center'],
		'1-3': ['both', 'axis x', 'axis y'],
		'2-3': ['none', 'hidden', 'visible'],
		'3-3': [
			0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
		],
		'0-2': ['border', 'content', 'padding'],
		'5-3': ['circle', 'ellipse', 'conical'],
		'1-1': ['start', 'ends', 'center', 'stretch'],
		'1-2': [
			'inset',
			'outset',
			'dotted',
			'dashed',
		],
		'3-2': [
			'start',
			'ends',
			'evenly',
			'around',
			'between',
		],
		'4-2': [
			'ends',
			'center',
			'stretch',
			'evenly',
			'around',
			'between',
		],
		'2-2': [
			'top',
			'left',
			'right',
			'bottom',
			'angle nw',
			'angle sw',
			'angle ne',
			'angle se',
		],
		'4-3': [
			'top',
			'left',
			'right',
			'bottom',
			'angle nw',
			'angle sw',
			'angle ne',
			'angle se',
		],
	},
}
const k1 = {
	110: '2-01',
	111: '2-02',
	112: '2-03',
	113: '2-04',
	114: '2-05',
	115: '2-06',
	116: '2-19',
	117: '2-20',

	118: '3-01',
	119: '3-02',
	120: '3-03',
	121: '3-04',
	122: '3-05',
	123: '3-06',
	124: '3-19',
	125: '3-20',

	126: '4-01',
	127: '4-02',
	128: '4-03',
	129: '4-04',
	130: '4-05',
	131: '4-06',
	132: '4-19',
	133: '4-20',

	134: '0-3',
	135: '0-4',
	136: '0-5',
	137: '0-6',
	138: '0-7',
	139: '0-8',

	101: '0-21',
	102: '0-22',
	103: '0-23',
	104: '0-0',
	105: '0-1',
	106: '0-2',
}
const k2 = document.body
const k3 = document.documentElement
const k4 = (_) => document.createElement(_)
const k5 = (_) => document.querySelector(_)
const k6 = (_) => document.querySelectorAll(_)
const k7 = (_) => _.getBoundingClientRect()
const k8 = (_) => _[0].getAttribute(_[1])
const k9 = (_) => _[0].removeAttribute(_[1])
const k10 = (_) => String(_).padStart(2, '0')
const k11 = (_) => String(_).padStart(3, '0')
const k12 = (_) =>
	_[1] + (_[2] - _[1]) * (_[0] / 100)
const k13 = (_) => [1, 10, 100, 1000, 10000][_[0]]
const k14 = (_) =>
	Math.round(_[1] * k13(_)) / k13(_)
const k15 = document.createElement('canvas')
const k16 = document.createElement('canvas')
const k17 = k16.getContext('2d')
const k18 = k15.getContext('2d')

const h0 = (l) => {
	let l0 = k3.style
	let l1 = [l[1], 'px']
	let l2 = `--${l[0]}`
	let l3 = l1.join('')
	if (l[1] !== 0) {
		let l4 = [l2, l3]
		l0.setProperty(...l4)
	}
	if (l[1] === 0) {
		l0.removeProperty(l2)
	}
	if (!k8([k3, 'style'])) {
		k9([k3, 'style'])
	}
}

const h1 = (l) => {
	let l0 = k4('svg')
	let l1 = k4('div')
	let l2 = k4('style')
	let l3 = k4('style')
	k2.appendChild(l0)
	k2.appendChild(l1)
	k2.appendChild(l2)
	k2.appendChild(l3)
	let l7 = k5('body>svg')
	let l8 = k5('body>div')
	let l9 = k6('body>style')
	let l10 = k([l[0], l[2]])
	l7.innerHTML = l10[0] || ''
	l8.innerHTML = l10[1] || ''
	l9[0].innerHTML = l10[2]
	l9[1].innerHTML = l10[3]
	return h2(l[1])
}

const h2 = (l) => {
	let l0 = 'body>div'
	let l1 = '.t00,.t000'
	let l2 = `.k00,${l1}`
	let l3 = `.l00,${l2}`
	let l4 = -Infinity
	let l5 = -Infinity
	let l6 = Infinity
	let l7 = Infinity
	h0(['f0', 0 || 0])
	h0(['f1', 0 || 0])
	k6(`${l0},${l3}`).forEach((_) => {
		let l8 = k7(_)
		let l9 = l8.top
		let l10 = l8.left
		let l11 = l8.right
		let l12 = l8.bottom
		l7 = Math.min(l7, l9)
		l6 = Math.min(l6, l10)
		l5 = Math.max(l5, l11)
		l4 = Math.max(l4, l12)
	})
	let l8 = k3.scrollTop || 0
	let l9 = k3.scrollWidth || 0
	let l10 = k3.scrollLeft * 2
	let l11 = l9 - l5 - l6 - l10
	let l12 = Math.round(l - l7 - l8)
	let l13 = Math.round(0.5 * l11)
	let l14 = Math.round(l5 - l6)
	let l15 = Math.round(l4 - l7)
	let l16 = [l14 || 0, l15 || 0]
	h0(['f0', l13 || 0])
	h0(['f1', l12 || 0])
	return l16
}

const h3 = (l) => {
	if (l[0] <= 1) {
		let l0 = []
		let l1 = d3.randomUniform
		let l2 = d3.randomBernoulli
		let l3 = d3.randomLcg(l[4])
		let l4 = (_) => Math.min(_, 1)
		let l5 = (_) => Math.max(_, 0)
		if (l[0] === 1) {
			let l6 = l[1] >= 0.5
			let l7 = [l[1], 1 - l[1]]
			let l8 = l7[!l6 ? 1 : 0]
			let l9 = (1 - l[2]) * l8
			let l10 = l[1] - l9
			let l11 = l[1] + l9
			let l12 = l5(l10)
			let l13 = l4(l11)
			l0 = Array.from(
				l[3],
				l1.source(l3)(l12, l13),
			)
		}
		if (l[0] === 0) {
			l0 = Array.from(l[3], l2.source(l3)(l[2]))
		}
		return l0 || []
	}
	if (l[0] === 2) {
		let l0 = Object()
		let l1 = k0['01']
		let l2 = l1[l[1]]
		for (let i in l[2]) {
			let l3 = l[2][0 || i]
			for (let i0 in l3) {
				let l4 = Number(i0)
				let l5 = l4 + l2[3]
				let l6 = l3[i0]
				l0[l5] ??= {}
				l0[l5][i] = l6
			}
		}
		return l0 || {}
	}
}

const h4 = (l) => {
	let l0 = {
		l00: 'a',
		k00: 'b',
		t00: 'c',
	}
	let l1 = l[0][0]
	let l2 = l[0][1]
	let l3 = l[0][2]
	let l4 = l[0][3]
	let l5 = 1 - l[0][4]
	let l6 = ['-', '2']
	let l7 = ['00'] || []
	let l8 = k0['03'][l2]
	let l9 = l[3].length - 1
	let l10 = l6.includes(l2)
	let l11 = new Object()
	let l12 = undefined
	let l13 = l4 - l3
	let l14 = (_) => {
		let l16 = _[0] * l9
		let l17 = _[0] * l13
		let l18 = 0 || l17 + l3
		let l19 = k14([0, l18])
		let l20 = k14([0, l16])
		if (l2.length >= 3) {
			let l21 = l8.length - 1
			let l22 = [0, _[0] * l21]
			let l23 = k14(l22)
			l12 = l8?.[l23]
		}
		if (l2 === '-' || l2 === '0') {
			l12 = l19
		}
		if (l2 === '1') {
			l12 = `${l19}`
		}
		if (l2 === '2') {
			if (_[1] >= 1) {
				let l21 = Array.from(
					{ length: _[1] },
					(_, _0) => `${l0[l1]}${k10(_0)}`,
				)
				l7.push(...(l21 || []))
			}
			let l22 = l7.length
			let l23 = l5 * _[0] || 0
			let l24 = l23 * (l22 - 1)
			let l25 = k14([0, l24])
			l12 = l7[l25]
		}
		if (l2 === '3') {
			if (l[3].length) {
				l12 = l[3][l20]
			}
		}
		return l12
	}
	for (let i in l[2]) {
		let l15 = l[2][i]
		let l16 = l[1][i]
		let l17 = [l15, i]
		let l18 = l14(l17)
		if (l18 != null) {
			if (l10 === true || l16 === 1) {
				l11[i] = l18
			}
		}
	}
	return l11
}

const h5 = (l) => {
	let l0 = {}
	let l1 = k0['00']
	let l2 = k0['01']
	let l3 = { ...l1, ...l2 }
	let l4 = Number(l[1])
	let l5 = l3[l[0] || '']
	let l6 = [l[4], l[5]]
	let l8 = k14([0, l[2]])
	let l9 = l5[2] - l5[1]
	let l10 = { length: l9 + 1 }
	let l11 = { length: l8 + 0 }
	let l12 = 0.1 + 0.9 * l[9]
	let l13 = 0.1 + 0.9 * l[8]
	let l14 = h3([0, 0, l12, l10, l4])
	let l15 = h3([0, 0, l[3], l10, l4 + 1])
	let l16 = h3([1, ...l6, l10, l4 + 2])
	let l17 = h3([1, 0, 0, l10, l4 + 3])
	let l18 = l
		.slice(10)
		.map((_) => _.split('.').filter(Boolean))
	let l19 = (_) => Object.keys(_)
	let l20 = (_) => _.join('-')
	let l21 = l[0].split('-')
	let l22 = l18.flat()
	for (let i in l15) {
		let l23 = [l21[0], i]
		let l24 = Number(i)
		let l25 = l20(l23)
		let l26 = l24 + l4
		let l27 = l3[l25]
		if (l27 != null) {
			let l28 = l27[0]
			let l30 = l28 === '3'
			let l31 = l28 === '2'
			let l32 = l24 + l5[1]
			let l33 = [l17[i], l[6]]
			let l34 = l30 ? l13 : l16[i]
			let l35 = l30 ? l14[i] : l15[i]
			if (l31 || l35 || l28 === '-') {
				let l36 = h3([1, ...l33, l11, l26])
				let l37 = h3([0, 0, l34, l11, l26])
				let l38 = h3([1, 0, 0, l11, l26])
				let l39 = [l[0], ...l27, l[7]]
				let l40 = !l31 ? l36 : l38
				let l41 = [l37, l40, l22]
				let l42 = [l39, ...l41]
				let l43 = h4(l42)
				let l44 = l19(l43)
				if (l44.length) {
					l0[l32] = l43
				}
			}
		}
	}
	return l0
}

const h6 = (l) => {
	let l0 = ['l00', 'k00', 't00']
	let l1 = {}
	l1['1'] = {}
	l1['2'] = {}
	l1['3'] = {}
	let l2 = Date.now()
	for (let i in l0) {
		let l3 = Number(i)
		let l4 = `f0-${l0[i]}`
		let l5 = `f1-${l0[i]}`
		let l6 = `${l3 + 2}-01`
		let l7 = new Array(9)
		let l8 = l7.fill(0)
		l8.push(String())
		l8.push(String())
		if (l[l6] != null) {
			for (let i0 in l8) {
				let l10 = Number(i0)
				let l11 = l10 >= 9
				let l12 = l10 >= 7
				let l13 = l12 ? 12 : 0
				let l14 = l10 + l13 || 0
				let l15 = [0, 2 * l3 + l10 - 6]
				let l16 = [l3 + 2, k10(l14)]
				let l17 = l[l16.join('-')]
				let l18 = l[l15.join('-')]
				let l19 = l11 ? l18 : l17
				if (l10 === 0) {
					let l21 = `0-${l3}`
					l8[0] = l[l21] || `${l2}`
					if (l[l21] == null) {
						l[l21] = `${l2}`
					}
				}
				if (l10 === 1) {
					l8[l10] = l19
				}
				if (l10 >= 2) {
					if (l19 != null) {
						let l20 = l19 / 100
						let l21 = k14([3, l20])
						l8[l10] = l11 ? l19 : l21
					}
				}
			}
			let l10 = h5([l4, ...l8])
			let l11 = h5([l5, ...l8])
			let l12 = h3([2, l0[i], l11])
			let l13 = h3([2, l0[i], l10])
			let l14 = h5([l0[i], ...l8])
			l1['1'] = { ...l1['1'], ...l14 }
			l1['2'] = { ...l1['2'], ...l13 }
			l1['3'] = { ...l1['3'], ...l12 }
		}
	}
	return l1
}

const h7 = (l) => {
	let l0 = l[2]['75'] || 0
	let l1 = l[2]['76'] || 0
	let l2 = l[2]['77'] || 0
	let l3 = l[2]['78'] || 0
	let l4 = l[2]['79'] || 0
	let l5 = l[2]['92'] || 10
	let l6 = l[0] + l5 * 2
	let l7 = l[1] + l5 * 2
	let l8 = filters
	let l9 = {}
	if (l0 === 8) {
		l9 = new l8.AdvancedBloomFilter({
			threshold: k12([l1, 0.1, 1]),
			bloomScale: k12([l2, 0, 2]),
			quality: k12([l3, 0, 10]),
			pixelSizeX: k12([l4, 0, 10]),
			pixelSizeY: k10([l4, 0, 10]),
		})
	}
	if (l0 === 9) {
		l9 = new l8.ZoomBlurFilter({
			strength: k12([l1, 0.2, 2]),
			innerRadius: k12([l2, 100, 1000]),
			radius: k12([l3, 100, 1000]),
			centerY: l6 * k12([l4, 0, 1]),
			centerX: l7 * 0.5,
		})
	} else if (l0 === 10) {
		l9 = new l8.TwistFilter({
			offset: [
				l7 / 2,
				20 +
					k12([l1, 100, 900]) +
					l6 * k12([l1, 0, 1]),
			],
			radius: k12([l2, 100, 900]),
			angle: k12([l3, 0, 100]),
		})
	} else if (l0 === 11) {
		l9 = new l8.BulgePinchFilter({
			radius: k12([l2, 200, 2000]),
			strength: k12([l3, -1, 1]),
			center: { x: 0.5, y: k12([l1, 0, 1]) },
		})
	} else if (l0 === 12) {
		l9 = new l8.GlitchFilter({
			slices: k12([l1, 0, 100]),
			offset: k12([l2, -400, 400]),
			direction: k12([l3, 0, 360]),
			sampleSize: k12([l4, 512, 1024]),
		})
	} else if (l0 === 13) {
		l9 = new l8.ReflectionFilter({
			boundary: k12([l1, 0, 0.9]),
			amplitudeEnd: k12([l3, 2, 200]),
			amplitudeStart: k12([l2, 2, 200]),
			wavelengthStart: k12([l4, 2, 200]),
			wavelengthEnd: k10([l4, 2, 200]),
		})
	}
	return l9
}

const h8 = (l) => {
	let l0 = l[2]['75'] || 0
	let l1 = l[2]['76'] || 0
	let l2 = l[2]['77'] || 0
	let l3 = l[2]['78'] || 0
	let l4 = l[2]['79'] || 0
	let l5 = filters
	let l6 = {}
	if (l0 === 1) {
		l6 = new l5.AsciiFilter({
			size: k12([l1, 1, 200]),
		})
	} else if (l0 === 3) {
		l6 = new l5.DotFilter({
			scale: k12([l1, 0, 2]),
			angle: k12([l2, 0, 10]),
			grayscale: false,
		})
	} else if (l0 === 4) {
		l6 = new l5.CRTFilter({
			lineContrast: k12([l2, 0.25, 10]),
			lineWidth: k12([l1, 1, 100]),
			curvature: k12([l3, 1, 100]),
			verticalLine: k12([l4, 0, 1]) > 0.5,
		})
	} else if (l0 === 5) {
		l6 = new l5.SimplexNoiseFilter({
			strength: k12([l1, 0.3, 0.9]),
			noiseScale: k12([l2, 1, 90]),
			offsetZ: k10([l3, 0, 100]),
			step: k10([l4, -1, 1]),
		})
	} else if (l0 === 6) {
		l6 = new l5.GlowFilter({
			distance: k12([l1, 1, 100]),
			innerStrength: k12([l2, 0.1, 20]),
			outerStrength: k12([l3, 0.1, 20]),
			alpha: k12([l4, 0.1, 10]),
		})
	} else if (l0 === 7) {
		l6 = new l5.KawaseBlurFilter({
			strength: k12([l1, 0, 20]),
			quality: k12([l4, 1, 3]),
			pixelSize: {
				x: k12([l2, 1, 10]),
				y: k12([l3, 1, 10]),
			},
		})
	}
	if (l0 >= 8) {
		return h7(l)
	}
	if (l0 <= 7) {
		return l6
	}
}

const h9 = async (l) => {
	let l0 = () => {
		return new PIXI.NoiseFilter({
			noise: k12([l8, 0.2, 2]),
			seed: k12([l9, 0.01, 100]),
		})
	}
	let l1 = PIXI.Texture.from(k16)
	let l2 = k16.height
	let l3 = k16.width
	let l4 = [l[0], l3, l2]
	let l5 = l[75] === 2
	let l6 = k0['00']
	let l7 = l6['00']
	let l8 = l[76] || 0
	let l9 = l[77] || 0
	if (!l7[0]) {
		l7[0] = new PIXI.Application()
		await l7[0].init({
			preference: 'webgl',
			backgroundAlpha: 0,
			antialias: true,
		})
	}
	if (!l7[1]) {
		l7[1] = new PIXI.Sprite(l1)
		l7[0].stage.addChild(l7[1])
	} else if (l7[1]) {
		l7[1].texture = l1
		l7[1].texture.update()
	}
	let l10 = l5 ? l0() : h8(l4)
	let l11 = l7[0].renderer
	l11.resize(l3, l2)
	l7[1].width = l3
	l7[1].height = l2
	l7[1].filters = [l10]
	l7[0].render() || null
	let l12 = l7[0].view || null
	k18.clearRect(0, 0, l3, l2)
	k18.drawImage(l12, 0, 0)
}

const h10 = async (l) => {
	let l0 = l[1][3]
	let l1 = l[1][0]
	let l2 = l[0][0] + l1 * 2
	let l3 = l[0][1] + l1 * 2
	let l4 = l2 + l[1][1] * 2
	let l5 = l3 + l[1][2] * 2
	let l6 = l0 * l[1][1] * 2
	let l7 = l0 * l[1][2] * 2
	let l8 = k3.scrollWidth
	let l9 = k3.scrollHeight
	let l10 = l0 * l2
	let l11 = l0 * l3
	let l12 = l0 * l8
	let l13 = l12 - l10
	let l14 = l10 + l6
	let l15 = l11 + l7
	let l16 = await toCanvas(k2, {
		width: l8,
		height: l9,
		canvasWidth: l8,
		canvasHeight: l9,
		pixelRatio: l0,
	})
	k16.height = l15
	k16.width = l14
	k15.width = l14
	k15.height = l15
	k18.drawImage(
		l16,
		l13 / 2,
		0,
		l10,
		l11,
		l6 / 2,
		l7 / 2,
		l10,
		l11,
	)
	h0(['f2', l4])
	h0(['f3', l5])
	k17.drawImage(k15, 0, 0)
}

window.h11 = async (l) => {
	k2.innerHTML = ''
	let l0 = k0['02']
	let l1 = l[1] || {}
	let l2 = l1['0'] || {}
	if (l[0] === 2) {
		for (let i in l2) {
			if (k1[i] != null) {
				l0[k1[i]] = l2[i]
			}
		}
	}
	let l3 = l2['75'] || 0
	let l4 = l2['90'] || 0
	let l5 = l2['91'] || 0
	let l6 = l2['94'] || 4 // 94
	let l7 = l2['93'] || 5
	let l8 = l2['92'] || 10 // 92
	let l9 = Math.min(l6, 10)
	let l10 = Math.min(l7, 10)
	let l11 = l[0] === 4 ? l10 : l9
	let l12 = Object.keys(l2)
	if (l[0] === 2) {
		l1 = { ...l1, ...h6(l0) }
	}
	if (l[0] >= 1) {
		let l15 = [l8, l4, l5, l11]
		let l16 = [l[0], l8, l1]
		l1[1] = h12(l1[1] || {})
		let l17 = await h1(l16)
		await h10([l17, l15])
	}
	if (l12.some((_) => _ >= 51 && _ <= 74)) {
		await h13([l3, l2])
	}
	if (l3 >= 1) {
		await h9(l2)
	}
	k2.innerHTML = ''
	k2.appendChild(k15)
	return [k15.toDataURL(), l1]
}

window.h12 = (l) => {
	let l0 = [17, 35, 53]
	let l1 = { '00': 'k' }
	let l2 = 'abc'.split('')
	let l3 = 'def'.split('')
	for (let i = 0; i < l2.length; i++) {
		for (let i0 = 0; i0 < 100; i0++) {
			let l4 = `${k10(i0)}`
			let l5 = `${l2[i]}`
			let l6 = `${l5}${l4}`
			l1[l6] = `${'lkt'[i]}${l4}`
		}
	}
	for (let i = 0; i < l3.length; i++) {
		for (let i0 = 0; i0 < 100; i0++) {
			let l4 = i * 100 + i0
			let l5 = `${l3[i]}`
			let l6 = `${k10(i0)}`
			let l7 = `${l5}${l6}`
			l1[l7] = `t${k11(l4)}`
		}
	}
	for (let i in l) {
		let l4 = Number(i)
		if (l0.includes(l4)) {
			for (let i0 in l[i]) {
				let l5 = l[i][i0]
				if (l1[l5] != null) {
					l[i][i0] = l1[l5]
				}
			}
		}
	}
	return l || {}
}

window.h13 = (l) => {
	return new Promise((resolve) => {
		let l0 = l[0] ? k17 : k18
		let l1 = [k16.width, k16.height]
		let l2 = k17.getImageData(0, 0, ...l1)
		let l3 = new Worker('/scripts.js')
		let l4 = [...l1, l2.data.buffer, l[1]]
		l3.postMessage(l4, [l2.data.buffer])
		l3.onmessage = async (_) => {
			l0.clearRect(0, 0, ...l1)
			l0.drawImage(_.data, 0, 0)
			_.data.close()
			resolve()
		}
	})
}
