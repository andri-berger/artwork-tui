/** @type {string} */
/** * @param {number} x
* @param {number} y
* @returns {number} */
/** @typedef {{ name: string, age: number }} User */
/** @type {User} */
/** @type {string[]} */
/** @type {Map<string, number>} */
/** @type {import('./types.js').MyType} */
/** @param {Event} e */
/** @returns {Promise<void>} */

import { toCanvas } from 'html-to-image';
import * as filters from 'pixi-filters';
import * as PIXI from 'pixi.js';
import * as d3 from 'random';
import k from './script.js';

const k0 = {
    "3-0": [],
    "3-1": null,
    "4-0": {
    "l00-0": ["0",-10,10],
    "l00-1": ["-",60,100],
    "l00-2": ["0",-400,400],
    "l00-3": ["0",-300,100],
    "l00-4": ["0",-300,100],
    "l00-5": ["-",60,100],
    "l00-6": ["1-1",0,4],
    "l00-7": ["0-1",0,3],
    "l00-9": ["-",0,100],
    "l00-10": ["0",0,100],
    "l00-11": ["1",-50,50],
    "l00-12": ["1",-50,50],
    "l00-13": ["1",-50,50],
    "l00-14": ["1",-50,50],
    "l00-15": ["1",-50,50],
    "l00-16": ["1",-50,50],
    "l00-17": ["2",0,100],

    "k00-0": ["-",60,100],
    "k00-1": ["0",-400,400],
    "k00-2": ["0",-300,100],
    "k00-3": ["0",-300,100],
    "k00-4": ["-",60,100],
    "k00-5": ["0-1",0,3],
    "k00-6": ["0-1",0,3],
    "k00-8": ["0",0,100],
    "k00-9": ["0",0,100],
    "k00-10": ["1",-50,50],
    "k00-11": ["1",-50,50],
    "k00-12": ["1",-50,50],
    "k00-13": ["1",-50,50],
    "k00-14": ["1",-50,50],
    "k00-15": ["1",-50,50],
    "k00-16": ["2",0,100],

    "t00-0": ["-",60,100],
    "t00-1": ["0",-400,400],
    "t00-2": ["0",-300,100],
    "t00-3": ["0",-300,100],
    "t00-4": ["-",60,100],
    "t00-5": ["0-1",0,3],
    "t00-6": ["0-1",0,3],
    "t00-8": ["0",0,100],
    "t00-9": ["0",0,100],
    "t00-10": ["1",-50,50],
    "t00-11": ["1",-50,50],
    "t00-12": ["1",-50,50],
    "t00-13": ["1",-50,50],
    "t00-14": ["1",-50,50],
    "t00-15": ["1",-50,50],
    "t00-16": ["2",0,100]},
    "4-1": {
    "f0-0": ["0",-10,10],
    "f0-1": ["0",-10,10],
    "f0-2": ["0",-10,10],
    "f0-3": ["0",-10,10],
    "f0-4": ["0-2",0,3],
    "f0-5": ["0",0,10],
    "f0-6": ["0",-10,10],
    "f0-7": ["0",-10,10],
    "f0-8": ["0",-10,10],
    "f0-9": ["0-0",0,2],
    "f0-10": ["0",0,10],
    "f0-11": ["0",-10,10],
    "f0-12": ["0",-10,10],
    "f0-13": ["0",-10,10],
    "f0-14": ["0-0",0,2],
    "f0-15": ["0",0,10],
    "f0-16": ["0",0,10],
    "f0-17": ["0",0,10],
    "f0-18": ["0",0,10],
    "f0-19": ["0",0,10],
    "f0-20": ["0",-10,10],
    "f0-24": ["1",0,100],
    "f0-26": ["1",0,100],
    "f0-28": ["1",0,100],
    "f0-30": ["1",0,100],
    "f0-35": ["0",0,360],

    "f1-0": ["3",0,1],
    "f1-1": ["3",0,1],
    "f1-2": ["3",0,1],
    "f1-3": ["3",0,1],
    "f1-4": ["3",0,1],
    "f1-5": ["3",0,1],
    "f1-6": ["3",0,1],
    "f1-9": ["3-3",0,13],
    "f1-10": ["0-0",0,2],
    "f1-11": ["0-0",0,2],
    "f1-12": ["0",0,10],
    "f1-13": ["0",-10,10],
    "f1-14": ["0",-10,10],
    "f1-15": ["0",0,100],
    "f1-16": ["0",0,100],
    "f1-17": ["0",0,100],
    "f1-19": ["0",0,100],
    "f1-20": ["0",0,100],
    "f1-22": ["4-3",0,8],
    "f1-23": ["5-3",0,3],
    "f1-24": ["6-3",0,2],
    "f1-25": ["1",0,10],
    "f1-26": ["1",0,100],

    "f1-l00": ["3",14,40],
    "f1-k00": ["3",14,40],
    "f1-t00": ["3",14,40],
    "f0-t00": ["2",0,35],
    "f0-k00": ["2",0,35],
    "f0-l00": ["2",0,35],
    "l00": ["1",0,17,1],
    "k00": ["1",19,35,101],
    "t00": ["1",37,53,201]},
    "5-0": {
        "2-01": 20,
        "2-02": 30,
        "3-01": 20,
        "3-02": 30,
        "4-01": 20,
        "4-02": 30,
        "2-19": 100,
        "3-19": 100,
        "4-19": 100},
    "6-0": {
    "0-0": ["false","true"],
    "6-3": ["linear","radial"],
    "0-1": ["start","ends","center"],
    "1-3": ["both","axis x","axis y"],
    "2-3": ["none","hidden","visible"],
    "0-2": ["border","content","padding"],
    "5-3": ["circle","ellipse","conical"],
    "1-1": ["start","ends","center","stretch"],
    "1-2": ["inset","outset","dotted","dashed"],
    "3-2": ["start","ends","evenly","around","between"],
    "4-2": ["ends","center","stretch","evenly","around","between"],
    "2-2": ["top","left","right","bottom","angle nw","angle sw","angle ne","angle se"],
    "4-3": ["top","left","right","bottom","angle nw","angle sw","angle ne","angle se"],
    "3-3": ["hue","color","screen","lighten","darken","overlay","multiply","saturation","luminosity","color dodge","color burn","hard light","soft light"],
    "0-3": ["White","Transparent","Gainsboro","Wheat","Gold","Crimson","MediumVioletRed","MediumSeaGreen","SeaGreen","DeepSkyBlue","DodgerBlue","MediumSlateBlue","Black","Snow","HoneyDew","MintCream","Azure","AliceBlue","GhostWhite","WhiteSmoke","SeaShell","Beige","OldLace","FloralWhite","Ivory","AntiqueWhite","Linen","LavenderBlush","MistyRose","CornSilk","BlanchedAlmond","Bisque","NavajoWhite","BurlyWood","RosyBrown","SandyBrown","GoldenRod","DarkGoldenRod","Peru","Chocolate","SaddleBrown","Sienna","Brown","Maroon","LightGray","Silver","DarkGray","Gray","DimGray","LightSlateGray","SlateGray","DarkSlateGray","LightYellow","LemonChiffon","PapayaWhip","Moccasin","PeachPuff","PaleGoldenRod","Khaki","DarkKhaki","Coral","Tomato","OrangeRed","DarkOrange","IndianRed","LightCoral","Salmon","DarkSalmon","LightSalmon","FireBrick","DarkRed","Pink","LightPink","HotPink","DeepPink","PaleVioletRed","Lavender","Thistle","Plum","Violet","Orchid","Fuchsia","Magenta","MediumOrchid","MediumPurple","BlueViolet","DarkViolet","DarkOrchid","DarkMagenta","Purple","Indigo","SlateBlue","DarkSlateBlue","GreenYellow","Chartreuse","LimeGreen","PaleGreen","LightGreen","SpringGreen","ForestGreen","DarkGreen","YellowGreen","OliveDrab","Olive","DarkOliveGreen","MediumAquamarine","DarkSeaGreen","LightSeaGreen","DarkCyan","Teal","Aqua","Cyan","LightCyan","PaleTurquoise","AquaMarine","Turquoise","MediumTurquoise","DarkTurquoise","CadetBlue","SteelBlue","LightSteelBlue","PowderBlue","LightBlue","SkyBlue","LightSkyBlue","CornflowerBlue","RoyalBlue","MediumBlue","DarkBlue","MidnightBlue","Navy"]
    }};
const k1 = {
    "110": "2-01",
    "111": "2-02",
    "112": "2-03",
    "113": "2-04",
    "114": "2-05",
    "115": "2-06",
    "116": "2-19",
    "117": "2-20",

    "118": "3-01",
    "119": "3-02",
    "120": "3-03",
    "121": "3-04",
    "122": "3-05",
    "123": "3-06",
    "124": "3-19",
    "125": "3-20",

    "126": "4-01",
    "127": "4-02",
    "128": "4-03",
    "129": "4-04",
    "130": "4-05",
    "131": "4-06",
    "132": "4-19",
    "133": "4-20",

    "134": "0-3",
    "135": "0-4",
    "136": "0-5",
    "137": "0-6",
    "138": "0-7",
    "139": "0-8",

    "106": "0-21",
    "107": "0-22",
    "108": "0-23",
    "142": "0-0",
    "143": "0-1",
    "144": "0-2"
};
const k2 = document.body;
const k3 = document.documentElement;
const k4 = _ => document.createElement(_);
const k5 = _ => document.querySelector(_);
const k6 = _ => document.querySelectorAll(_);
const k7 = _ => _.getBoundingClientRect();
const k8 = _ => _[0].getAttribute(_[1]);
const k9 = _ => _[0].removeAttribute(_[1]);
const k10 = _ => String(_).padStart(2,'0');
const k11 = _ => _[1]+(_[2]-_[1])*(_[0]/100);
const k12 = _ => [1,10,100,1000,10000][_[0]];
const k13 = _ => Math.round(_[1]*k12(_))/k12(_);
const k14 = document.createElement('canvas');
const k15 = k14.getContext(
    '2d',{ willReadFrequently: true });

const h00 = l => {
    let l0 = k4('canvas');
    let l1 = l0.getContext('2d');
    l0.height = l.height;
    l0.width = l.width;
    l1.drawImage(l, 0, 0); console.log('togo',l0)
    k0['3-0'][0] = l0; };

const h0 = l => {
    let l0 = k3.style;
    let l1 = [l[1],'px'];
    let l2 = `--${l[0]}`;
    let l3 = l1.join('');
    if (l[1] !== 0) {
    let l4 = [l2,l3];
    l0.setProperty(...l4); }
    if (l[1] === 0) {
    l0.removeProperty(l2); }
    if (!k8([k3,'style'])) {
    k9([k3,'style']); }};

const h1 = l => {
    let l90 = k4('svg');
    let l91 = k4('div');
    let l92 = k4('style');
    let l93 = k4 ('style');
    k2.appendChild(l90);
    k2.appendChild(l91);
    k2.appendChild(l92);
    k2.appendChild(l93);
    let l4 = k5('body>svg');
    let l5 = k5('body>div');
    let l6 = k6('body>style');
    let l8 = k([l[0],l[2]]);
    l4.innerHTML = l8[0]||'';
    l5.innerHTML = l8[1]||'';
    l6[0].innerHTML = l8[2];
    l6[1].innerHTML = l8[3];
    return h2(l[1]); };

const h2 = l => {
    let l0 = 'body>div';
    let l1 = '.t00,.t000';
    let l2 = `.k00,${l1}`;
    let l3 = `.l00,${l2}`;
    let l4 = -Infinity;
    let l5 = -Infinity;
    let l6 = Infinity;
    let l7 = Infinity;
    h0(['f0',0||0]);
    h0(['f1',0||0]);
    k6(`${l0},${l3}`)
    .forEach(_ => {
    let l8 = k7(_);
    let l9 = l8.top;
    let l10 = l8.left;
    let l11 = l8.right;
    let l12 = l8.bottom;
    l7 = Math.min(l7,l9);
    l6 = Math.min(l6,l10);
    l5 = Math.max(l5,l11);
    l4 = Math.max(l4,l12); });
    let l8 = k3.scrollTop||0;
    let l9 = k3.scrollWidth||0;
    let l10 = k3.scrollLeft * 2;
    let l11 = l9 - l5 - l6 - l10;
    let l12 = Math.round(l-l7-l8);
    let l13 = Math.round(0.5*l11);
    let l14 = Math.round(l5-l6);
    let l15 = Math.round(l4-l7);
    let l16 = [l14||0,l15||0]
    h0(['f0',l13||0]);
    h0(['f1',l12||0]);
    return l16; };

const h3 = l => {
    if (l[0] <= 1) {
    let l0 = new Array();
    let l1 = d3.randomUniform;
    let l2 = d3.randomBernoulli;
    let l3 = d3.randomLcg(l[4]);
    let l4 = _ => Math.min(_,1);
    let l5 = _ => Math.max(_,0);
    if (l[0] === 1) {
    let l6 = l[1] >= 0.5;
    let l7 = [l[1],1-l[1]];
    let l8 = l7[!l6? 1: 0];
    let l9 = (1-l[2]) * l8;
    let l10 = l[1] - l9;
    let l11 = l[1] + l9;
    let l12 = l5(l10);
    let l13 = l4(l11);
    l0 = Array.from(
    l[3],l1.source(
    l3)(l12,l13)); }
    if (l[0] === 0) {
    l0 = Array.from(
    l[3],l2.source(
    l3)(l[2])); }
    return l0 || []; }
    if (l[0] === 2) {
    let l0 = Object();
    let l1 = k0['4-1'];
    let l2 = l1[l[1]];
    for (let i in l[2]) {
    let l3 = l[2][0||i];
    for (let i0 in l3) {
    let l4 = Number(i0);
    let l5 = l4 + l2[3];
    let l6 = l3[i0];
    l0[l5] ??= {};
    l0[l5][i] = l6; }}
    return l0 || {}; }};

const h4 = l => {
    let l0 = l[0][0];
    let l1 = l[0][1];
    let l2 = l[0][2];
    let l3 = l[0][3];
    let l03 = 1-l[0][4];
    let l4 = ['-','2'];
    let l5 = k0['6-0'][l1];
    let l6 = l[3].length-1;
    let l7 = l4.includes(l1);
    let l8 = new Object();
    let l9 = undefined;
    let l10 = l3 - l2;
    let l11 = _ => {
    let l12 = _[0] * l6;
    let l13 = _[0] * l10;
    let l14 = 0||l13 + l2;
    let l15 = k13([0,l14]);
    let l16 = k13([0,l12]);
    if (l1.length >= 3) {
    let l17 = l5.length-1;
    let l18 = [0,_[0]*l17];
    let l19 = k13(l18);
    l9 = l5?.[l19]; }
    if (l1 === '-' ||
    l1 === '0') {
    l9 = l15; }
    if (l1 === '1') {
    l9 = `${l15}`; }
    if (l1 === '2') {
    let l17 = ['k'];
    if (_[1] >= 1) {
    let l18 = Array.from(
    {length:_[1]},(_,_0)=>
    `${l0[0]}${k10(_0)}`);
    l17.push(...l18||[]); }
    let l19 = l17.length;
    let l20 = l03 * _[0]||0;
    let l21 = l20 * (l19-1);
    let l22 = k13([0,l21]);
    l9 = l17[l22]; }
    if (l1 === '3') {
    if (l[3].length) {
    l9 = l[3][l16]; }}
    return l9; };
    for (let i in l[2]) {
    let l12 = l[2][i];
    let l13 = l[1][i];
    let l14 = [l12,i];
    let l15 = l11(l14);
    if (l15 != null) {
    if (l7 === true
    || l13 === 1) {
    l8[i] = l15; }}}
    return l8; };

const h5 = l => {
    let l3 = {};
    let l0 = k0['4-0'];
    let l1 = k0['4-1'];
    let l2 = {...l0,...l1};
    let l4 = Number(l[1]);
    let l5 = l2[l[0]||''];
    let l6 = [l[4],l[5]];
    let l8 = k13([0,l[2]]);
    let l9 = l5[2] - l5[1];
    let l10 = {length:l9+1};
    let l11 = {length:l8+0};
    let l12 = 0.1 + 0.9 * l[9];
    let l13 = 0.1 + 0.9 * l[8];
    let l14 = h3([0,0,l12,l10,l4]);
    let l15 = h3([0,0,l[3],l10,l4+1]);
    let l16 = h3([1,...l6,l10,l4+2]);
    let l17 = h3([1,0,0,l10,l4+3]);
    let l18 = l.slice(10).map(_ =>
    _.split('.').filter(Boolean));
    let l19 = _ => Object.keys(_);
    let l20 = _ => _.join('-');
    let l21 = l[0].split('-');
    let l22 = l18.flat();
    for (let i in l15) {
    let l23 = [l21[0],i];
    let l24 = Number(i);
    let l25 = l20(l23);
    let l26 = l24 + l4;
    let l27 = l2[l25];
    if (l27 != null) {
    let l28 = l27[0];
    let l30 = l28 === '3';
    let l31 = l28 === '2';
    let l32 = l24 + l5[1];
    let l33 = [l17[i],l[6]];
    let l34 = l30? l13: l16[i];
    let l35 = l30? l14[i]: l15[i];
    if (l31 || l35 || l28 === '-') {
    let l36 = h3([1,...l33,l11,l26]);
    let l37 = h3([0,0,l34,l11,l26]);
    let l38 = h3([1,0,0,l11,l26]);
    let l39 = [l[0],...l27,l[7]];
    let l40 = !l31? l36: l38;
    let l41 = [l37,l40,l22];
    let l42 = [l39,...l41];
    let l43 = h4(l42);
    let l44 = l19(l43);
    if (l44.length) {
    l3[l32] = l43 }}}}
    return l3; };

const h6 = l => {
    let l0 = [
    'l00','k00','t00'];
    let l1 = {};
    l1['1'] = {};
    l1['2'] = {};
    l1['3'] = {};
    for (let i in l0) {
    let l2 = Number(i);
    let l3 = Date.now();
    let l4 = `f0-${l0[i]}`;
    let l5 = `f1-${l0[i]}`;
    let l6 = `${l2+2}-01`;
    let l7 = new Array(9);
    let l8 = l7.fill(0);
    l8.push(String());
    l8.push(String());
    if (l[l6] != null) {
    for (let i0 in l8) {
    let l10 = Number(i0);
    let l11 = l10 >= 9;
    let l12 = l10 >= 7;
    let l13 = l12? 12: 0;
    let l14 = l10 + l13||0;
    let l15 = [0,2*l2+l10-6];
    let l16 = [l2+2,k10(l14)];
    let l17 = l[l16.join('-')];
    let l18 = l[l15.join('-')];
    let l19 = l11? l18: l17;
    if (l10 === 0) {
    let l21 = `0-${l2}`;
    l8[0] = l[l21] || `${l3}`;
    if (l[l21] == null) {
    l[l21] = `${l3}`; }}
    if (l10 === 1) {
    l8[l10] = l19; }
    if (l10 >= 2) {
    if (l19 != null) {
    let l20 = l19 / 100;
    let l21 = k13([3,l20]);
    l8[l10] = l11? l19: l21; }}}
    let l10 = h5([l4,...l8]);
    let l11 = h5([l5,...l8]);
    let l12 = h3([2,l0[i],l11]);
    let l13 = h3([2,l0[i],l10]);
    let l14 = h5([l0[i],...l8]);
    l1['1'] = {...l1['1'],...l14};
    l1['2'] = {...l1['2'],...l13};
    l1['3'] = {...l1['3'],...l12}; }}
    return l1; };

const h7 = l => {
    let l0 = l[1]['75']||0;
    let l1 = l[1]['76']||0;
    let l2 = l[1]['77']||0;
    let l3 = l[1]['78']||0;
    let l4 = l[1]['79']||0;
    let l5 = l[1]['89']||10;
    let l6 = l[0][1] + (l5 * 2);
    let l7 = l[0][2] + (l5 * 2);
    let l8 = filters;
    let l9 = {};
    if (l0 === 8) {
        l9 = new l8.AdvancedBloomFilter({
            threshold: k11([l1, 0.1, 1]),
            bloomScale: k11([l2, 0, 2]),
            quality: k11([l3, 0, 10]),
            pixelSizeX: k11([l4, 0, 10]),
            pixelSizeY: k10([l4,0,10])}); }
    if (l0 === 9) {
        l9 = new l8.ZoomBlurFilter({
            strength: k11([l1,0.2,2]),
            innerRadius:k11([l2,100,1000]),
            radius: k11([l3,100,1000]),
            centerY: l6 * k11([l4,0,1]),
            centerX: l7 * 0.5}); }
    else if (l0 === 10) {
        l9 = new l8.TwistFilter({
            offset: [l7 / 2,
            20 + k11([l1,100,900])
            + l6 * k11([l1,0,1])],
            radius: k11([l2,100,900]),
            angle: k11([l3,0,100])}); }
    else if (l0 === 11) {
        l9 = new l8.BulgePinchFilter({
            radius: k11([l2,200,2000]),
            strength: k11([l3,-1,1]),
            center:{x: 0.5,
            y: k11([l1,0,1])}}); }
    else if (l0 === 12) {
    l9 = new l8.GlitchFilter({
            slices: k11([l1,0,100]),
            offset: k11([l2,-400,400]),
            direction:k11([l3,0,360]),
            sampleSize: k11([l4,512,1024])}); }
    else if (l0 === 13) {
    l9 = new l8.ReflectionFilter({
            boundary: k11([l1,0,0.9]),
            amplitudeEnd: k11([l3,2,200]),
            amplitudeStart: k11([l2,2,200]),
            wavelengthStart: k11([l4,2,200]),
            wavelengthEnd: k10([l4,2,200])}); }
    return l9; };

const h8 = l => {
    let l0 = l[1]['75']||0;
    let l1 = l[1]['76']||0;
    let l2 = l[1]['77']||0;
    let l3 = l[1]['78']||0;
    let l4 = l[1]['79']||0;
    let l5 = filters;
    let l6 = {};
    if (l0 === 1) {/* OK */
    l6 = new l5.AsciiFilter({
        size: k11([l1, 1, 200])}); }
    else if (l0 === 2) {
    l6 = new PIXI.NoiseFilter({
        noise: k11([l1, 0.2, 2]),
        seed: k11([l2, 0.01, 100])}); }
    else if (l0 === 3) {
    l6 = new l5.DotFilter({
        scale: k11([l1, 0, 2]),
        angle: k11([l2, 0, 10]),
        grayscale: false}); }
    else if (l0 === 4) {
    l6 = new l5.CRTFilter({
        lineContrast: k11([l2, 0.25, 10]),
        lineWidth: k11([l1, 1, 100]),
        curvature: k11([l3, 1, 100]),
        verticalLine: k11([l4, 0, 1])
        > 0.5 ? true : false}); }
    else if (l0 === 5) {
    l6 = new l5.SimplexNoiseFilter({
        strength: k11([l1, 0.3, 0.9]),
        noiseScale: k11([l2, 1, 90]),
        offsetZ: k10([l3,0,100]),
        step: k10([l4,-1,1])}); }
    else if (l0 === 6) {
    l6 = new l5.GlowFilter({
        distance: k11([l1, 1, 100]),
        innerStrength: k11([l2, 0.1, 20]),
        outerStrength: k11([l3, 0.1, 20]),
        alpha: k11([l4, 0.1, 10])}); }
    else if (l0 === 7) {
    l6 = new l5.KawaseBlurFilter({
        strength: k11([l1, 0, 20]),
        quality: k11([l4, 1, 3]),
        pixelSize: {
            x: k11([l2, 1, 10]),
            y: k11([l3, 1, 10])}}); }
    if (l0 >= 8) { return h7(l); }
    if (l0 <= 7) { return l6; }};

const h9 = async l => {
    let l0 = PIXI.
    Texture.from(k14);
    let l1 = k0['3-0'];
    let l2 = k14.height;
    let l3 = k14.width;
    if (!l1[1]) {
        l1[1] = new PIXI.
        Application();
        await l1[1].init({
            preference: 'webgl',
            backgroundAlpha: 0,
            antialias: true}); }
   if (!l1[2]) {
        l1[2] = new
        PIXI.Sprite(l0);
        l1[1].stage.
        addChild(l1[2]); }
   else if (l1[2]) {
        l1[2].texture = l0;
        l1[2].texture.update(); }
   let l4 = l1[1].renderer;
   let l5 = [h8(l)];
   l4.resize(l3, l2)
   l1[2].width = l3;
   l1[2].height = l2;
   l1[2].filters = l5;
   l1[1].render() || null;
   let tt = l1[1].view || null;
   k15.clearRect(0, 0, l3,l2)
   k15.drawImage(tt,0,0); };

const h10 = async l => {
    let l5 = l[1][0] + l[2][0] * 2;
    let l6 = l[1][1] + l[2][0] * 2;
    let l7 = k3.scrollWidth;
    let l8 = k3.scrollHeight;
    let l3 = [l[2][3],l[2][4]];
    let l9 = l3[l[0]? 1: 0];
    let l10 = l9 * l[2][1] * 2;
    let l11 = l9 * l[2][2] * 2;
    let l12 = l9 * l5;
    let l13 = l9 * l6;
    let l14 = l9 * l7;
    let l15 = l14 - l12;
    let l16 = l12 + l10;
    let l17 = l13 + l11;
    let l18 = l5 + l[2][1] * 2;
    let l19 = l6 + l[2][2] * 2;
    let l20 = await toCanvas(
    k2,{ width: l7,
    height: l8,
    canvasWidth: l7,
    canvasHeight: l8,
    pixelRatio: l9});
    k14.width = l16;
    k14.height = l17;
    k15.drawImage(
    l20,l15/2,0,
    l12,l13,l10/2,
    l11/2,l12,l13);
    h0(['f2',l18]);
    h0(['f3',l19]);
    h00(k14); };


// rewrite A-F => assignments

window.h11 = async l => {
    k2.innerHTML = '';
    let l0 = l[1]||{};
    let l1 = l0['0']||{};
    let l2 = k0['3-0'];
    let l3 = k0['5-0'];
    let l02 = l2[0]||k14;
    let l4 = l[0] === 1;
    if (l[0] === 3) {
        for (let i in l1) {
        l3[k1[i]] = l1[i]; }}
    let l5 = l[0] <= 2;
    let l6 = l1['75']||0;
    let l7 = l1['89']||10;
    let l8 = l1['90']||0;
    let l9 = l1['91']||0;
    let l10 = l1['92']||6;
    let l11 = l1['93']||5;
    let l12 = Object.keys(l1);
    let l13 =  l12.some(
        _ => _ >= 51 && _ <= 74);
    let l14 = l5? l[1]: h6(l3);
    let l15 = l4? l02: k14;
    let l16 = [l7,l8,l9,l10,l11];
    let l17 = _ => [l[0],_,l16];
    let l18 = [l[0],l7,l14];
    let l19 = Array();
    if (l4 == false) {
        l19 = await h1(l18);
        await h10(l17(l19)); }
    if (l13 === true) {
        console.log('cool!')
        await h12(l1); }
    if (l6 >= 1) {
        await h9(
            [l19,l1]); }
    console.log('yesh',l15);
        k2.innerHTML = '';
        k2.appendChild(l15);
    return [l15.toDataURL(),l[1]]};

window.h12 = l => {
    return new Promise(resolve => {
        let l0 = [k14.width,k14.height];
        let l1 = k15.getImageData(0,0,...l0);
        let l2 = new Worker('/styles.js');
        let l3 = [...l0,l1.data.buffer,l]
        l2.postMessage(l3,[l1.data.buffer]);
        l2.onmessage = async _ => {
            k15.clearRect(0, 0, ...l0)
            k15.drawImage(_.data, 0, 0)
            _.data.close()
            resolve(); }; }); };

// h11([1, {"0":{"51":20,"52":20},"1":{"1":{"1":20,"2":80}}}])

h11([2, {"1":{"1":{"1":20,"2":80}}}])


