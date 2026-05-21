
/** @type {string} */
/**
* @param {number} x
* @param {number} y
* @returns {number}
*/

/** @typedef {{ name: string, age: number }} User */
/** @type {User} */

/** @type {string[]} */
/** @type {Map<string, number>} */
/** @type {import('./types.js').MyType} */   // import types from another file
/** @param {Event} e */
/** @returns {Promise<void>} */

import * as filters from 'pixi-filters';
import { toCanvas } from 'html-to-image';
import * as PIXI from 'pixi.js';
import * as d3 from 'random';
import k from './script.js';
const k0 = Array();

const k1 = {
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
const k2 = {
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
const k3 = document.body;
const k4 = document.documentElement;
const k5 = _ => document.createElement(_);
const k6 = _ => document.querySelector(_);
const k7 = _ => document.querySelectorAll(_);
const k8 = _ => _.getBoundingClientRect();
const k9 = _ => _[0].getAttribute(_[1]);
const k10 = _ => _[0].removeAttribute(_[1]);
const k11 = _ => String(_).padStart(2,'0');
const k12 = _ => _[1]+(_[2]-_[1])*(_[0]/100);
const k13 = _ => [1,10,100,1000,10000][_[0]];
const k14 = _ => Math.round(_[1]*k13(_))/k13(_);
const k15 = document.createElement('canvas');
const k16 = k15.getContext('2d',
{ willReadFrequently: true});


const h0 = l => {
let l0 = k4.style;
let l1 = [l[1],'px'];
let l2 = `--${l[0]}`;
let l3 = l1.join('');
if (l[1] !== 0) {
let l4 = [l2,l3];
l0.setProperty(...l4); }
if (l[1] === 0) {
l0.removeProperty(l2); }
if (!k9([k4,'style'])) {
k10([k4,'style']); }};

const h1 = l => {
    /* let l82 = k6('canvas')
 if (l82) {
k3.removeChild(l82); } */
let l90 = k5('svg');
let l91 = k5('div');
let l92 = k5('style');
let l93 = k5 ('style');
k3.appendChild(l90);
k3.appendChild(l91);
k3.appendChild(l92);
k3.appendChild(l93);
let l4 = k6('body>svg');
let l5 = k6('body>div');
let l6 = k7('body>style');
let l8 = k([l[0],l[1]]);
l5.innerHTML = l8[1];
l6[0].innerHTML = l8[2];
l6[1].innerHTML = l8[3]; };

const h2 = l => {
let l0 = 'body>div';
let l1 = '.t00,.t000';
let l2 = `.k00,${l1}`;
let l3 = `.l00,${l2}`;
let l5 = -Infinity;
let l6 = -Infinity;
let l7 = Infinity;
let l8 = Infinity;
h0(['f0',0||0]);
h0(['f1',0||0]);
k7(`${l0},${l3}`)
.forEach(_ => {
let l10 = k8(_);
let l11 = l10.top;
let l12 = l10.left;
let l13 = l10.right;
let l14 = l10.bottom;
l8 = Math.min(l8,l11);
l7 = Math.min(l7,l12);
l6 = Math.max(l6,l13);
l5 = Math.max(l5,l14); });
let l9 = k4.scrollTop||0;
let l10 = k4.scrollWidth||0;
let l11 = k4.scrollLeft * 2;
let l12 = l10 - l6 - l7 - l11;
let l16 = Math.round(l-l8-l9);
let l15 = Math.round(0.5*l12);
let l13 = Math.round(l6-l7);
let l14 = Math.round(l5-l8);
h0(['f0',l15||0]);
h0(['f1',l16||0]);
f0[1] = l13||0;
f0[2] = l14||0; };

// prefix, canvas, data
const h3 = l => { console.log('h3',l)
    let l07 = l[2]['0']||{};
    let l80 = l07['89']||10;
    let l91 = Object.keys(l07);
    let l0 =  l91.some(
    _ => _ >= 51 && _ <= 74);
    let l81 = f0[1] + (l80 * 2);
    let l82 = f0[2] + (l80 * 2);

    let l00 = _ => {
    h0(['f2',l81]);
    h0(['f3',l82]);
    k3.innerHTML = '';
    k3.appendChild(_);
    let l200 = '';
    let l90 = ""


        let testr = [_.toDataURL()]; // make conditional
        if (l[0] === 3) {
            delete l[2]['0']
            testr.push(l[2])
        }
    window.resolveCapture(testr); };


if (l0 === true) {
let l2 = k5('canvas');
let l3 = '/styles.js';
let l4 = l[1].getContext('2d',
{ willReadFrequently: true });
l2.width = l[1].width || Number();
l2.height = l[1].height || Number();
let l5 = [0,0,l[1].width,l[1].height];
let l6 = l2.transferControlToOffscreen();
let l7 = l4.getImageData(...l5||[]);
let l8 = [l7.width,l7.height];
let l9 = [l7.data.buffer,l6];
let l10 = new Worker(l3);
l10.postMessage([...l8,
...l9,l[2]['0']],l9||[]);
l10.onmessage = _ => {
l00(_.data[0]); }; }
if (l0 === false) {
l00(l[1]); }};

const h4 = l => { console.log('h4',l)
    let l0 = l['75']||0;
    let l1 = l['76']||0;
    let l2 = l['77']||0;
    let l3 = l['78']||0;
    let l4 = l['79']||0;
    let l5 = l['89']||10;
    let l6 = f0[1] + (l5 * 2);
    let l7 = f0[2] + (l5 * 2);
    let l8 = l7.height;
    let l9 = l6.width;
    let l10 = filters;
    let l11 = {};
    switch (l0) {
        case 9: l11 = new
        l10.ZoomBlurFilter({
            strength: k12([l1,0.2,2]),
            innerRadius:k12([l2,100,1000]),
            radius: k12([l3,100,1000]),
            centerY: l8 * k12([l4,0,1]),
            centerX: l9 * 0.5});
        break;
        case 10: l11 = new
        l10.TwistFilter({
            offset: [l9 / 2,
            20 + k12([l1,100,900])
            + l8 * k12([l1,0,1])],
            radius: k12([l2,100,900]),
            angle: k12([l3,0,100])});
        break;
        case 11: l11 = new
        l10.BulgePinchFilter({
            radius: k12([l2,200,2000]),
            strength: k12([l3,-1,1]),
            center:{x: 0.5,
            y: k12([l1,0,1])}});
        break;
        case 12: l11 = new
        l10.GlitchFilter({
            slices: k12([l1,0,100]),
            offset: k12([l2,-400,400]),
            direction:k12([l3,0,360]),
            sampleSize: k12([l4,512,1024])});
        break;
        case 13: l11 = new
        l10.ReflectionFilter({
            boundary: k12([l1,0,0.9]),
            amplitudeEnd: k12([l3,2,200]),
            amplitudeStart: k12([l2,2,200]),
            wavelengthStart: k12([l4,2,200])/*,
            wavelengthEnd: k10([l4,2,200]),
            alphaStart: k10([l5,0.2,1]),
            alphaEnd: k10([l6,0.2,1]),
            mirror: k10([l6,0,1]) */}); }
    return l11; };


const h5 = l => { console.log('h5',l)
    let l0 = l['75']||0;
    let l1 = l['76']||0;
    let l2 = l['77']||0;
    let l3 = l['78']||0;
    let l4 = l['79']||0;
    let l7 = filters;
    let l6 = {};
    switch(l0) {
        case 1: l6 = new
        l7.AsciiFilter({
                size: k12(
                    [l1, 1, 200])});
        break;
        case 2: l6 = new
        PIXI.NoiseFilter({
            noise: k12([l1, 0.2, 2]),
            seed: k12([l2, 0.01, 100])});
        break;
        case 3: l6 = new
        l7.DotFilter({
            scale: k12([l1, 0, 2]),
            angle: k12([l2, 0, 10]),
            grayscale: false});
        break;
        case 4: l6 = new
        l7.CRTFilter({
            lineContrast: k12([l2, 0.25, 10]),
            lineWidth: k12([l1, 1, 100]),
            curvature: k12([l3, 1, 100]),
            verticalLine: k12([l4, 0, 1])
            > 0.5 ? true : false});
        break;
        case 5: l6 = new
        l7.SimplexNoiseFilter({
            strength: k12([l1, 0.3, 0.9]),
            noiseScale: k12([l2, 1, 90]),
            offsetX: k12([l3, 0, 100]),
            offsetY: k12([l4, 0, 100])/*,
            offsetZ: k10([l4,0,100]),
            step: k10([l5,-1,1]) */});
        break;
        case 6: l6 = new
        l7.GlowFilter({
            distance: k12([l1, 1, 100]),
            innerStrength: k12([l2, 0.1, 20]),
            outerStrength: k12([l3, 0.1, 20]),
            alpha: k12([l4, 0.1, 10])});
        break;
        case 7: l6 = new
        l7.KawaseBlurFilter({
            strength: k12([l1, 0, 20]),
            quality: k12([l4, 1, 3]),
            pixelSize: {
                x: k12([l2, 1, 10]),
                y: k12([l3, 1, 10])}});
        break;
        case 8: l6 = new
        l7.AdvancedBloomFilter({
                threshold: k12([l1, 0.1, 1]),
                bloomScale: k12([l2, 0, 2]),
                quality: k12([l3, 0, 10]),
                pixelSizeX: k12([l4, 0, 10]),
                /* pixelSizeY: k10([l4,0,10]),
                blur: k10([l5,0,10]) */}); }
    if (l0 >= 9) {
    return h4(l); }
    if (l0 <= 8) {
    return l6; }};







const h7 = l => {
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
let l1 = k1['4-1'];                  // metadata ok
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

const h8 = l => {
let l0 = l[0][0];
let l1 = l[0][1];
let l2 = l[0][2];
let l3 = l[0][3];
let l03 = 1-l[0][4];
let l4 = ['-','2'];
let l5 = k1['6-0'][l1];
let l6 = l[3].length-1;
let l7 = l4.includes(l1);
let l8 = new Object();
let l9 = undefined;
let l10 = l3 - l2;
let l11 = _ => {
let l12 = _[0] * l6;
let l13 = _[0] * l10;
let l14 = 0||l13 + l2;
let l15 = k14([0,l14]);
let l16 = k14([0,l12]);
if (l1.length >= 3) {
let l17 = l5.length-1;
let l18 = [0,_[0]*l17];
let l19 = k14(l18);
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
`${l0[0]}${k11(_0)}`);
l17.push(...l18||[]); }
let l19 = l17.length;
let l20 = l03 * _[0]||0;
let l21 = l20 * (l19-1);
let l22 = k14([0,l21]);
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

const h9 = l => {
let l0 = k1['4-0'];                          // metadata ok
let l1 = k1['4-1'];                          // metadata ok
let l2 = {...l0,...l1};
let l3 = {};
let l4 = Number(l[1]);
let l5 = l2[l[0]||''];
let l6 = [l[4],l[5]];
let l8 = k14([0,l[2]]);
let l9 = l5[2] - l5[1];
let l10 = {length:l9+1};
let l11 = {length:l8+0};
let l12 = 0.1 + 0.9 * l[9];
let l13 = 0.1 + 0.9 * l[8];
let l14 = h7([0,0,l12,l10,l4]);
let l15 = h7([0,0,l[3],l10,l4+1]);
let l16 = h7([1,...l6,l10,l4+2]);
let l17 = h7([1,0,0,l10,l4+3]);
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
let l36 = h7([1,...l33,l11,l26]);
let l37 = h7([0,0,l34,l11,l26]);
let l38 = h7([1,0,0,l11,l26]);
let l39 = [l[0],...l27,l[7]];
let l40 = !l31? l36: l38;
let l41 = [l37,l40,l22];
let l42 = [l39,...l41];
let l43 = h8(l42);
let l44 = l19(l43);
if (l44.length) {
l3[l32] = l43 }}}}
return l3; };

const h10 = () => {
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
if (f1[l6] != null) {
for (let i0 in l8) {
let l10 = Number(i0);
let l11 = l10 >= 9;
let l12 = l10 >= 7;
let l13 = l12? 12: 0;
let l14 = l10 + l13||0;
let l15 = [0,2*l2+l10-6];
let l16 = [l2+2,k11(l14)];
let l17 = f1[l16.join('-')];
let l18 = f1[l15.join('-')];
let l19 = l11? l18: l17;
if (l10 === 0) {
let l21 = `0-${l2}`;
l8[0] = f1[l21] || `${l3}`;
if (f1[l21] == null) {
f1[l21] = `${l3}`; }}
if (l10 === 1) {
l8[l10] = l19; }
if (l10 >= 2) {
if (l19 != null) {
let l20 = l19 / 100;
let l21 = k14([3,l20]);
l8[l10] = l11? l19: l21; }}}
let l10 = h9([l4,...l8]);
let l11 = h9([l5,...l8]);
let l12 = h7([2,l0[i],l11]);
let l13 = h7([2,l0[i],l10]);
let l14 = h9([l0[i],...l8]);
l1['1'] = {...l1['1'],...l14};
l1['2'] = {...l1['2'],...l13};
l1['3'] = {...l1['3'],...l12}; }}
return l1; };





// OK [resolution,canvas,data]
const h6 = async l => {
    let l0 = PIXI.
    Texture.from(k15);
    let l1 = k15.height;
    let l2 = k15.width;
    if (!k0[1]) {
        k0[1] = new PIXI.
        Application();
        await k0[1].init({
            width: l2 || 0,
            height: l1 || 0,
            preference: 'canvas',
            backgroundAlpha: 0,
            antialias: true
        }); }
   if (!k0[2]) {
        k0[2] = new
        PIXI.Sprite(l0);
        k0[1].stage.
        addChild(k0[2]);     }
   else if (k0[2]) {
        k0[2].texture = l0; }
        k0[2].width = l2;
        k0[2].height = l1;
        let l6 = h5(l);
        k0[2].filters = [l6];
        k0[1].render() || null;
        console.log('suri',k15.width,k0[1].renderer.width)

        k15.width = k0[1].renderer.width;
        k15.height = k0[1].renderer.height;

        k16.drawImage(k0[1].view,0,0);

};

const h11 = async l => {
    let l90 = l[1]['89']||10;
    let l00 = l[1]['90']||0;
    let l01 = l[1]['91']||0;
    let l09 = l[1]['92']||6;
    let l08 = l[1]['93']||5;
    let l1 = f0[1] + (l90 * 2);
    let l2 = f0[2] + (l90 * 2);
    let l5 = k4.scrollWidth;
    let l6 = k4.scrollHeight;
    let l0 = l[0]? l08: l09;
    let l7 = l0 * l00;
    let l8 = l0 * l01;
    let l14 = l0 * l7 * 2;
    let l15 = l0 * l8 * 2;
    let l10 = l0 * l1;
    let l11 = l0 * l2;
    let l12 = l0 * l5;
    let l13 = l12 - l10;
    let l16 = await toCanvas(
    k3,{ width: l5,
    height: l6,
    canvasWidth: l5,
    canvasHeight: l6,
    pixelRatio: l0});
    k15.width = l10 + l14;
    k15.height = l11 + l15;
    k16.drawImage(
    l16,l13/2,0,
    l10,l11,l14/2,
    l15/2,l10,l11); };


window.testlaufs = async l => {
    window.f0 = [];
    window.f1 = {
        "2-01": 20,
        "2-02": 30,
        "3-01": 20,
        "3-02": 30,
        "4-01": 20,
        "4-02": 30,
        "2-19": 100,
        "3-19": 100,
        "4-19": 100};
        let l0 = l[1]||{};
        let l1 = l0['0']||{};
        let l02 = l1['75']||0;
        let l2 = l1['89']||10;
        let l3 = l1['92']||6;
        let l4 = l1['93']||5;
        let l5 = l3 === l4;
    document.body.innerHTML = '';
    return new Promise(async resolve => {
        window.resolveCapture = resolve;
        if (l[0] === 3) {
            let l6 = h10()
            for (let i in l1) {
            f1[k2[i]] = l1[i]; }
            h1([l[0],l6]);
            h2([l2,'_']);
            h11([l[0],l6]); }

        if (l[0] === 2 || l[0] === 1) {
            let l90 = [l[0],l1];
            let l91 = [l[0],l[1]];
            let l92 = []
            await h1(l91);                    // OK
            await h2(l2);                     // OK
            await h11(l90);                   // OK


            if (l02 >= 1) {
                 await h6(l1); }
            /* if (1 === 1) {
            h3([l[0],l20,l[1]]); } */


            console.log('yes!!!')
            k3.innerHTML = '';
            k3.appendChild(k15);
            window.resolveCapture(
        [k15.toDataURL(),l[1]]);

        }

}); }


// first params
testlaufs([2,
    {"0":{"75":2,"76":20},
        "1":{"1":{"1":20,"2":80}}}
])





/*        if (l[0] === 0) {
            if (l5 === false) {
                h1([l[0],l[1]]);
                h2([l2,'_']);
                h11([l[0],l[1]]); }
            if (l5 === true) {
                let l4 = f0[0].toDataURL()
                window.resolveCapture([l4,{}]); }
        }*/

