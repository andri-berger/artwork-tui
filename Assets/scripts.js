/* SPDX-License-Identifier: AGPL-3.0-or-later
SPDX-FileCopyrightText: 2024 Andri Berger

This file is part of layout-tui.

layout-tui is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. */

import * as d3 from 'random';

const h = new Object();
const k = new Object();
const k5 = _ => localStorage.getItem(_);
const k4 = _ => localStorage.setItem(..._);
const k15 = _ => String(_).padStart(2,'0');
const k17 = _ => [1,10,100,1000,10000][_[0]];
const k21 = _ => Math.round(_[1]*k17(_))/k17(_);

const h6 = l => {
let l0 = 'number';
let l1 = l[0] == 'IB';
let l2 = k5(l[0])||'{}';
let l3 = JSON.parse(l2);
let l4 = typeof l[2];
let l5 = l[2].length;
let l6 = l4 == l0||0;
let l7 = l6 && l[2];
let l8 = !l6 && l5;
if (l8 || l7) {
if (l1 == false) {
h[l[1]] = l[2]; }
l3[l[1]] = l[2]; }
if (!l8 && !l7) {
delete l3[l[1]];
if (l1 == false) {
delete h[l[1]]; }}
k4([l[0],JSON.
stringify(l3)]); };


const h19 = l => {
if (l[0] <= 1) {
let l0 = new Array();
let l1 = d3.randomUniform;
let l2 = d3.randomBernoulli;
let l3 = d3.randomLcg(l[4]);
let l4 = _ => Math.min(_,1);
let l5 = _ => Math.max(_,0);
if (l[0] == 1) {
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
if (l[0] == 0) {
l0 = Array.from(
l[3],l2.source(
l3)(l[2])); }
return l0 || []; }
if (l[0] == 2) {
let l0 = Object();
let l1 = f['4-1'];
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
let l15 = k21([0,l14]);
let l16 = k21([0,l12]);
if (l1.length >= 3) {
let l17 = l5.length-1;
let l18 = [0,_[0]*l17];
let l19 = k21(l18);
l9 = l5?.[l19]; }
if (l1 == '-' ||
l1 == '0') {
l9 = l15; }
if (l1 == '1') {
l9 = `${l15}`; }
if (l1 == '2') {
let l17 = ['k'];
if (_[1] >= 1) {
let l18 = Array.from(
{length:_[1]},(_,_0)=>
`${l0[0]}${k15(_0)}`);
l17.push(...l18||[]); }
let l19 = l17.length;
let l20 = l03 * _[0]||0;
let l21 = l20 * (l19-1);
let l22 = k21([0,l21]);
l9 = l17[l22]; }
if (l1 == '3') {
if (l[3].length) {
l9 = l[3][l16]; }}
return l9; };
for (let i in l[2]) {
let l12 = l[2][i];
let l13 = l[1][i];
let l14 = [l12,i];
let l15 = l11(l14);
if (l15 != null) {
if (l7 == true
|| l13 == 1) {
l8[i] = l15; }}}
return l8; };

const h21 = l => {
let l0 = f['4-0'];
let l1 = f['4-1'];
let l2 = {...l0,...l1};
let l3 = new Object();
let l4 = Number(l[1]);
let l5 = l2[l[0]||''];
let l6 = [l[4],l[5]];
let l8 = k21([0,l[2]]);
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
let l30 = l28 == '3';
let l31 = l28 == '2';
let l32 = l24 + l5[1];
let l33 = [l17[i],l[6]];
let l34 = l30? l13: l16[i];
let l35 = l30? l14[i]: l15[i];
if (l31 || l35 || l28 == '-') {
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

export default () => {
let l0 = [
'l00','k00','t00'];
let l1 = new Object();
l1['1'] = new Object();
l1['2'] = new Object();
l1['3'] = new Object();
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
if (h[l6] != null) {
for (let i0 in l8) {
let l10 = Number(i0);
let l11 = l10 >= 9;
let l12 = l10 >= 7;
let l13 = l12? 12: 0;
let l14 = l10 + l13||0;
let l15 = [0,2*l2+l10-6];
let l16 = [l2+2,k15(l14)];
let l17 = h[l16.join('-')];
let l18 = h[l15.join('-')];
let l19 = l11? l18: l17;
if (l10 == 0) {
let l20 = `0-2${l2+1}`;
let l21 = `0-${l2+0}`;
let l22 = h[`${l21}`];
let l23 = [l22,`${l3}`];
let l24 = [l21,`${l3}`];
let l25 = h[l20] && l22;
l8[0] = l23[l25?0:1];
if (l25 == null) {
h6(['ID',...l24]); }}
if (l10 == 1) {
l8[l10] = l19; }
if (l10 >= 2) {
if (l19 != null) {
let l20 = l19 / 100;
let l21 = k21([3,l20]);
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

