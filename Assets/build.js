/* SPDX-License-Identifier: A




GPL-3.0-or-later
SPDX-FileCopyrightText: 2024 Andri Berger

This file is part of layout-tui.

layout-tui is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. */


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
import k from  './scripts.js';
import k0 from './model.js';

const k1 = document.body;
const k2 = document.documentElement;
const k3 = _ => document.createElement(_);
const k4 = _ => document.querySelector(_);
const k5 = _ => document.querySelectorAll(_);
const k6 = _ => _.getBoundingClientRect();
const k7 = _ => _[0].getAttribute(_[1]);
const k8 = _ => _[0].removeAttribute(_[1]);
const k9 = _ => _[1]+(_[2]-_[1])*(_[0]/100);

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
let l8 = k0([0,l||{}]); console.log('l8',l,l8)
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
let l16 = Math.round(30-l8-l9);
let l15 = Math.round(0.5*l12);
let l13 = Math.round(l6-l7);
let l14 = Math.round(l5-l8);
k10(['f0',l15||Number()]);
k10(['f1',l16||Number()]);
k0[2] ??= new Array();
k0[2][1] = l13;
k0[2][2] = l14; };


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

// OK [resolution,[padding]]
const k19 = async l => {

let l1 = k3('canvas');

let l3 = k0[2][1] + 60;
let l4 = k0[2][2] + 60;


let l6 = k2.scrollWidth;	// OK
let l7 = k2.scrollHeight;	// OK

let l8 = l1.getContext('2d',
{willReadFrequently:true});	// OK


let l10 = l[1][0] * l[0];

let l11 = l[1][0] * l[0];
let l12 = l[0] * l3;
let l13 = l[0] * l4;

let l14 = {
width: l6,
height: l7,
canvasWidth: l6,
canvasHeight: l7,
pixelRatio: l[0]};

let l15 =
await toCanvas(k1,l14);
let l16 = l[0] * 2;
let l17 = l15.width;
let l18 = l17 - l12;
let l19 = l10 * l16;
let l20 = l11 * l16;
let l21 = l13 + l20;
let l22 = l12 + l19;
l1.width = l22;
l1.height = l21;
l8.drawImage(
l15,l18/2,0,
l12,l13,l19/2,
l20/2,l12,l13);
k15([l[0],l1,l[2]]);
};

window.testlaufs = (config) => {
    window.k0 = [];
    window.k1 = {};
    // k10(['f0',0||0]);
    // k10(['f1',0||0]);
    // k10(['f2',0||0]);
    // k10(['f3',0||0]);
    document.body.innerHTML = '';
    return new Promise(resolve => {
        window.resolveCapture = resolve;
        k12(config[2]);
        k19(config);
});
}

testlaufs([3, [0, 0], {"1": {"1": {"1": 20, "3": 30}}}])
