
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

import { toCanvas } from 'html-to-image';
import * as filters from 'pixi-filters';
import * as PIXI from 'pixi-core';
import * as d3 from 'random';
import k0 from './model.js';




const k1 = document.body;
const k2 = document.documentElement;
const k3 = _ => document.createElement(_);
const k4 = _ => document.querySelector(_);
const k5 = _ => document.querySelectorAll(_);
const k6 = _ => _.getBoundingClientRect();
const k7 = _ => _[0].getAttribute(_[1]);
const k8 = _ => _[0].removeAttribute(_[1]);
const xk15 = _ => String(_).padStart(2,'0');
const k9 = _ => _[1]+(_[2]-_[1])*(_[0]/100);
const xk17 = _ => [1,10,100,1000,10000][_[0]];
const xk21 = _ => Math.round(_[1]*xk17(_))/xk17(_);

const f = {
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
    "0-4": ["pk_test_51NxxzcERfj72s6CFVpAcJDo68hN1WeHWfqhRJyvxC1Yw7u9KRZc4jUqCfJKxx0yBx177dZIUDafhPJNWSufRkxbv0032KRCTGD"],
    "3-3": ["hue","color","screen","lighten","darken","overlay","multiply","saturation","luminosity","color dodge","color burn","hard light","soft light"],
    "0-3": ["White","Transparent","Gainsboro","Wheat","Gold","Crimson","MediumVioletRed","MediumSeaGreen","SeaGreen","DeepSkyBlue","DodgerBlue","MediumSlateBlue","Black","Snow","HoneyDew","MintCream","Azure","AliceBlue","GhostWhite","WhiteSmoke","SeaShell","Beige","OldLace","FloralWhite","Ivory","AntiqueWhite","Linen","LavenderBlush","MistyRose","CornSilk","BlanchedAlmond","Bisque","NavajoWhite","BurlyWood","RosyBrown","SandyBrown","GoldenRod","DarkGoldenRod","Peru","Chocolate","SaddleBrown","Sienna","Brown","Maroon","LightGray","Silver","DarkGray","Gray","DimGray","LightSlateGray","SlateGray","DarkSlateGray","LightYellow","LemonChiffon","PapayaWhip","Moccasin","PeachPuff","PaleGoldenRod","Khaki","DarkKhaki","Coral","Tomato","OrangeRed","DarkOrange","IndianRed","LightCoral","Salmon","DarkSalmon","LightSalmon","FireBrick","DarkRed","Pink","LightPink","HotPink","DeepPink","PaleVioletRed","Lavender","Thistle","Plum","Violet","Orchid","Fuchsia","Magenta","MediumOrchid","MediumPurple","BlueViolet","DarkViolet","DarkOrchid","DarkMagenta","Purple","Indigo","SlateBlue","DarkSlateBlue","GreenYellow","Chartreuse","LimeGreen","PaleGreen","LightGreen","SpringGreen","ForestGreen","DarkGreen","YellowGreen","OliveDrab","Olive","DarkOliveGreen","MediumAquamarine","DarkSeaGreen","LightSeaGreen","DarkCyan","Teal","Aqua","Cyan","LightCyan","PaleTurquoise","AquaMarine","Turquoise","MediumTurquoise","DarkTurquoise","CadetBlue","SteelBlue","LightSteelBlue","PowderBlue","LightBlue","SkyBlue","LightSkyBlue","CornflowerBlue","RoyalBlue","MediumBlue","DarkBlue","MidnightBlue","Navy"]}};
const h = {
"0-21": 0,      // 0: 100
"0-22": 0,      // 0: 101
"0-23": 0,      // 0: 102

"2-01": 10,     // 0: 103
"2-02": 30,     // 0: 104
"2-03": null,   // 0: 105
"2-04": null,   // 0: 106
"2-05": null,   // 0: 107
"2-06": null,   // 0: 108
"2-19": null,   // 0: 109
"2-20": null,   // 0: 110

"3-01": null,     // 0: 111
"3-02": null,     // 0: 112
"3-03": null,   // 0: 113
"3-04": null,   // 0: 114
"3-05": null,   // 0: 115
"3-06": null,   // 0: 116
"3-19": null,   // 0: 117
"3-20": null,   // 0: 118

"4-01": null,     // 0: 119
"4-02": null,     // 0: 120
"4-03": null,   // 0: 121
"4-04": null,   // 0: 122
"4-05": null,   // 0: 123
"4-06": null,   // 0: 124
"4-19": null,   // 0: 125
"4-20": null,   // 0: 126

"0-0": null,    // 0: 127
"0-1": null,    // 0: 128
"0-2": null,    // 0: 129
};




const k10 = l => {
let l0 = k2.style;
let l1 = [l[1],'px'];
let l2 = `--${l[0]}`;
let l3 = l1.join('');
if (l[1] !== 0) {
let l4 = [l2,l3];
l0.setProperty(...l4); }
if (l[1] === 0) {
l0.removeProperty(l2); }
if (!k7([k2,'style'])) {
k8([k2,'style']); }};

/// OK
const k11 = l => {
let l0 = _ => Math.floor(_);
let l1 = Object.keys(l||{});
let l3 = l1.some(
    _ => _ >= 58 && _ <= 81);
let l4 = l[102] || 0;
let l5 = l[50] / 7.143;
let l6 = l[82] / 16.667;
let l7 = [l0(l5),l0(l6)];
return [l3,...l7,l4]; };

const k15 = async l => {

    let l00 = _ => {
        let l01 = _.width;
        let l02 = _.height;
        k10(['f2',l01/l[0]]);
        k10(['f3',l02/l[0]]);
        k1.innerHTML = '';
        k1.appendChild(_);
        window.resolveCapture(_.toDataURL());
    };
let l0 = k11(l[2]['0']||{});
if (l0[0] === true) {
let l2 = k3('canvas');
let l3 = '/script.js';
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
if (l0[0] === false) {
l00(l[1]); }};

const k16 = l => {
let l0 = l[2][51]||0;
let l1 = l[2][52]||0;
let l2 = l[2][53]||0;
let l3 = l[2][54]||0;
let l4 = l[2][55]||0;
let l5 = l[2][56]||0;
let l6 = l[2][57]||0;
let l7 = new Object();
let l8 = filters;
let l9 = l[1].height;
let l10 = l[1].width;
if (l[0] === 9) {
l7 = new l8.
ZoomBlurFilter({
strength: k9([l0,0.2,2]),
innerRadius:k9([l1,100,1000]),
radius: k9([l2,100,1000]),
centerY: l9 * k9([l3,0,1]),
centerX: l10 * 0.5}); }
if (l[0] === 10) {
l7 = new l8.
TwistFilter({
offset: [l10 / 2,
20 + k9([l0,100,900])
+ l9 * k9([l0,0,1])],
radius: k9([l1,100,900]),
angle: k9([l2,0,100])}); }
if (l[0] === 11) {
l7 = new l8.
BulgePinchFilter({
radius: k9([l1,200,2000]),
strength: k9([l2,-1,1]),
center:{x: 0.5,
y: k9([l0,0,1])}}); }
if (l[0] === 12) {
l7 = new l8.GlitchFilter({
slices: k9([l0,0,100]),
offset: k9([l1,-400,400]),
direction:k9([l2,0,360]),
sampleSize: k9([l3,512,1024])}); }
if (l[0] === 13) {
l7 = new l8.
ReflectionFilter({
boundary: k9([l0,0,0.9]),
amplitudeEnd: k9([l2,2,200]),
amplitudeStart: k9([l1,2,200]),
wavelengthStart: k9([l3,2,200]),
wavelengthEnd: k9([l4,2,200]),
alphaStart: k9([l5,0.2,1]),
alphaEnd: k9([l6,0.2,1]),
mirror: k9([l6,0,1])}); }
return l7; };

const k17 = l => {
let l0 = l[2][51]||0;
let l1 = l[2][52]||0;
let l2 = l[2][53]||0;
let l3 = l[2][54]||0;
let l4 = l[2][55]||0;
let l5 = l[2][56]||0;
let l6 = new Object();
let l7 = filters;
if (l[0] === 1) {
l6 = new l7.
AsciiFilter({
size: k9(
[l0,1,200])}); }
if (l[0] === 2) {
l6 = new PIXI.
NoiseFilter({
noise: k9([l0,0.2,2]),
seed: k9([l1,0.01,100])}); }
if (l[0] === 3) {
l6 = new l7.DotFilter({
scale: k9([l0,0,2]),
angle: k9([l1,0,10]),
grayscale: false}); }
if (l[0] === 4) {
l6 = new l7.CRTFilter({
lineContrast: k9([l1,0.25,10]),
lineWidth: k9([l0,1,100]),
curvature: k9([l2,1,100]),
verticalLine: k9([l3,0,1])
 > 0.5? true: false}); }
if (l[0] === 5) {
l6 = new l7.
SimplexNoiseFilter({
strength: k9([l0,0.3,0.9]),
noiseScale: k9([l1,1,90]),
offsetX: k9([l2,0,100]),
offsetY: k9([l3,0,100]),
offsetZ: k9([l4,0,100]),
step: k9([l5,-1,1])}); }
if (l[0] == 6) {
l6 = new l7.GlowFilter({
distance: k9([l0,1,100]),
innerStrength: k9([l1,0.1,20]),
outerStrength: k9([l2,0.1,20]),
alpha: k9([l3,0.1,10])}); }
if (l[0] === 7) {
l6 = new l7.KawaseBlurFilter({
strength: k9([l0,0,20]),
quality: k9([l3,1,3]),
pixelSize: {
x:k9([l1,1,10]),
y:k9([l2,1,10])}}); }
if (l[0] === 8) {
l6 = new l7.AdvancedBloomFilter({
threshold: k9([l0,0.1,1]),
bloomScale: k9([l1,0,2]),
quality: k9([l2,0,10]),
pixelSizeX: k9([l3,0,10]),
pixelSizeY: k9([l4,0,10]),
blur: k9([l5,0,10])}); }
if (l[0] >= 9) {
return k16(l); }
if (l[0] <= 8) {
return l6; }};


// OK [resolution,canvas,data]
const k18 = async l => {

let l0 = k11(l[2]['0']||{});
let l1 = [l0[1],l[1]];
let l2 = l0[1] >= 1;
let l3 = l[2]['0'];
let l4 = [...l1,l3];
let l5 = l[1].height;
let l6 = l[1].width;
k0[10] = new PIXI.
Application({
width: l6||Number(),
height: l5||Number(),
preference: 'webgl',
backgroundAlpha: 0,
antialias: true});

// PIXI.utils.clearTextureCache();

let l7 = PIXI.
Texture.from(l[1]);



// k0[9] = new PIXI.
// Sprite(0||0||l7);



if (!k0[9]) {console.log('first')
k0[9] = new PIXI.Sprite(l7);
k0[9].width = l6;
k0[9].height = l5;
k0[10].stage.addChild(k0[9]);}
else { console.log('second')
k0[9].texture = l7;
k0[9].width = l6;
k0[9].height = l5;
}

if (l2 === true) {
let l8 = k17(0||l4);
k0[9].filters = [l8];
k0[10].render() || null;
let l9 = k3(0||'canvas');
let l10 = l9.getContext('2d',
{ willReadFrequently: true });
l9.width = k0[10].renderer.width;
l9.height = k0[10].renderer.height;
l10.drawImage(k0[10].view,0,0);
k15([0,l9,l[2]]);
k0[5] = l9||{}; }

if (l2 === false) {
k15([l[0],l[1],l[2]]);
}};


const k19 = async l => {
let l1 = k0[2][1] + 20;
let l2 = k0[2][2] + 20;
let l3 = k3('canvas');
let l4 = l3.getContext('2d',
{willReadFrequently: true});
let l5 = k2.scrollWidth;
let l6 = k2.scrollHeight;
let l7 = l[0] * l[1][0];
let l8 = l[0] * l[1][1];
let l14 = l[0] * l7 * 2;
let l15 = l[0] * l8 * 2;
let l10 = l[0] * l1;
let l11 = l[0] * l2;
let l12 = l[0] * l5;
let l13 = l12 - l10;
let l16 =
await toCanvas(k1,{
width: l5,
height: l6,
canvasWidth: l5,
canvasHeight: l6,
pixelRatio: l[0]});
l3.width = l10 + l14;
l3.height = l11 + l15;
l4.drawImage(
l16,l13/2,0,
l10,l11,l14/2,
l15/2,l10,l11);

k15([l[0],l3,l[2]]);
};







///////////////////////////////////////////////////////////////////
 /////////////////////////////////////////////////////////////////
 /////////////////////////////////////////////////////////////////







const h19 = l => {
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
let l1 = f['4-1'];                  // metadata ok
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

const h20 = l => {
let l0 = l[0][0];
let l1 = l[0][1];
let l2 = l[0][2];
let l3 = l[0][3];
let l03 = 1-l[0][4];
let l4 = ['-','2'];
let l5 = f['6-0'][l1];
let l6 = l[3].length-1;
let l7 = l4.includes(l1);
let l8 = new Object();
let l9 = undefined;
let l10 = l3 - l2;
let l11 = _ => {
let l12 = _[0] * l6;
let l13 = _[0] * l10;
let l14 = 0||l13 + l2;
let l15 = xk21([0,l14]);
let l16 = xk21([0,l12]);
if (l1.length >= 3) {
let l17 = l5.length-1;
let l18 = [0,_[0]*l17];
let l19 = xk21(l18);
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
`${l0[0]}${xk15(_0)}`);
l17.push(...l18||[]); }
let l19 = l17.length;
let l20 = l03 * _[0]||0;
let l21 = l20 * (l19-1);
let l22 = xk21([0,l21]);
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

const h21 = l => {
let l0 = f['4-0'];                          // metadata ok
let l1 = f['4-1'];                          // metadata ok
let l2 = {...l0,...l1};
let l3 = {};
let l4 = Number(l[1]);
let l5 = l2[l[0]||''];
let l6 = [l[4],l[5]];
let l8 = xk21([0,l[2]]);
let l9 = l5[2] - l5[1];
let l10 = {length:l9+1};
let l11 = {length:l8+0};
let l12 = 0.1 + 0.9 * l[9];
let l13 = 0.1 + 0.9 * l[8];
let l14 = h19([0,0,l12,l10,l4]);
let l15 = h19([0,0,l[3],l10,l4+1]);
let l16 = h19([1,...l6,l10,l4+2]);
let l17 = h19([1,0,0,l10,l4+3]);
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
let l36 = h19([1,...l33,l11,l26]);
let l37 = h19([0,0,l34,l11,l26]);
let l38 = h19([1,0,0,l11,l26]);
let l39 = [l[0],...l27,l[7]];
let l40 = !l31? l36: l38;
let l41 = [l37,l40,l22];
let l42 = [l39,...l41];
let l43 = h20(l42);
let l44 = l19(l43);
if (l44.length) {
l3[l32] = l43 }}}}
return l3; };

const h22 = () => {
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
let l6 = `${l2+2}-01`;              // Limit 2-01, 3-01, 4-01
let l7 = new Array(9);
let l8 = l7.fill(0);
l8.push(String());
l8.push(String());
if (h[l6] != null) {
for (let i0 in l8) {
let l10 = Number(i0);
let l11 = l10 >= 9;
let l12 = l10 >= 7;
let l13 = l12? 12: 0;
let l14 = l10 + l13||0;
let l15 = [0,2*l2+l10-6];
let l16 = [l2+2,xk15(l14)];
let l17 = h[l16.join('-')];                 // all others
let l18 = h[l15.join('-')];                 // all others
let l19 = l11? l18: l17;
if (l10 === 0) {
let l20 = `0-2${l2+1}`;             // l/k/t-seed 0-21/0-22/0-23
let l21 = `0-${l2+0}`;              // ID-Seed 0-0/0-1/0-2
let l22 = h[`${l21}`];
let l23 = [l22,`${l3}`];
let l25 = h[l20] && l22;
l8[0] = l23[l25?0:1];
if (l25 == null) {
    h[l21] = `${l3}`; }}
if (l10 === 1) {
l8[l10] = l19; }
if (l10 >= 2) {
if (l19 != null) {
let l20 = l19 / 100;
let l21 = xk21([3,l20]);
l8[l10] = l11? l19: l21; }}}
let l10 = h21([l4,...l8]);
let l11 = h21([l5,...l8]);
let l12 = h19([2,l0[i],l11]);
let l13 = h19([2,l0[i],l10]);
let l14 = h21([l0[i],...l8]);
l1['1'] = {...l1['1'],...l14};
l1['2'] = {...l1['2'],...l13};
l1['3'] = {...l1['3'],...l12}; }}
return l1; };












const k12 = l => {
let l82 = k4('canvas')
 if (l82) {
k1.removeChild(l82); }
let l90 = k3('svg');
let l91 = k3('div');
let l92 = k3('style');
let l93 = k3 ('style');
k1.appendChild(l90);
k1.appendChild(l91);
k1.appendChild(l92);
k1.appendChild(l93);
let l4 = k4('body>svg');
let l5 = k4('body>div');
let l6 = k5('body>style');
let l8 = k0([0,l||{}]);
l4.innerHTML = l8[0];
l5.innerHTML = l8[1];
l6[0].innerHTML = l8[2];
l6[1].innerHTML = l8[3];
k13(0||'_'); };

const k13 = () => {
let l0 = 'body>div';
let l1 = '.t00,.t000';
let l2 = `.k00,${l1}`;
let l3 = `.l00,${l2}`;
let l5 = -Infinity;
let l6 = -Infinity;
let l7 = Infinity;
let l8 = Infinity;
k10(['f0',0||0]);
k10(['f1',0||0]);
k5(`${l0},${l3}`)
.forEach(_ => {
let l10 = k6(_);
let l11 = l10.top;
let l12 = l10.left;
let l13 = l10.right;
let l14 = l10.bottom;
l8 = Math.min(l8,l11);
l7 = Math.min(l7,l12);
l6 = Math.max(l6,l13);
l5 = Math.max(l5,l14); });
let l9 = k2.scrollTop||0;
let l10 = k2.scrollWidth||0;
let l11 = k2.scrollLeft * 2;
let l12 = l10 - l6 - l7 - l11;
let l16 = Math.round(10-l8-l9);
let l15 = Math.round(0.5*l12);
let l13 = Math.round(l6-l7);
let l14 = Math.round(l5-l8);
k10(['f0',l15||Number()]);
k10(['f1',l16||Number()]);
k0[2] ??= new Array();
k0[2][1] = l13;
k0[2][2] = l14; };

////////////////////////////////////////////////
 ///////////////////////////////////////////////
 ///////////////////////////////////////////////




window.testlaufs = (config) => {
    window.k0 = [];
    window.k1 = {};
    document.body.innerHTML = '';
    return new Promise(resolve => {
        window.resolveCapture = resolve;
        let aris = h22()
        k12(aris);
        // k12(config[2])
        k19(config);
});
}
console.time('time')
console.log('this-time',h22())
 console.timeEnd('time')
testlaufs([5, [0, 0], {"1": {"1": {"1": 20, "3": 80}}}])






