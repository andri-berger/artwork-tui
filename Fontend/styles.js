self.onmessage = async l => {
let l0 = l.data[2];
let l1 = l.data[3];
let l2 = l.data[4];
let l29 = l2[50] || 0;
let l3 = l2[51]*2+3||3;
let l4 = l2[52]*2+3||3;
let l5 = l2[53]/30||0;
let l6 = l2[54]/30||0;
let l7 = l2[55]/30||0;
let l8 = l2[56]/30||0;
let l9 = l2[57]/30||0;
let l10 = l2[58]/30||0;
let l11 = l2[59]/30||0;
let l12 = l2[60]/30||0;
let l13 = l2[61]/2||0;
let l14 = l2[62]/2||0;
let l15 = l2[63]/50||0;
let l16 = l2[64]/50||0;
let l17 = l2[65]/50||0;
let l18 = l2[66]/50||0;
let l19 = l2[67]/50||0;
let l20 = l2[68]/50||0;
let l21 = l2[67]/100*7||0;
let l22 = l2[68]/100*7||0;
let l23 = l2[69]/30||0;
let l24 = l2[70]/30||0;
let l25 = l2[71]/30||0;
let l26 = l2[72]/30||0;
let l27 = l2[73]/30||0;
let l28 = l2[74]/30||0;
let l31 = new Uint8ClampedArray(l0);
let l32 = l5 <= 1? (1 - l5): l5;
let l33 = l7 <= 1? (1 - l7): l7;
let l34 = l9 <= 1? (1 - l9): l9;
let l35 = l25 > 0 && l26 > 0;
let l36 = l13 > 0 || l14 > 0
let l37 = l36 || l29 >= 2;
let l38 = !l7? l32: l33;
let l39 = !l9? l32: l34;
l1.width = l.data[0];
l1.height = l.data[1];

let l40 = l1.getContext('2d');
for (let x=0;x<l.data[0];x+=l3) {
for (let y=0;y<l.data[1];y+=l4) {
let l41 = (x+y*l.data[0]) * 4;
let l42 = l31[l41+0];
let l43 = l31[l41+1];
let l44 = l31[l41+2];
let l45 = l31[l41+3] / 255;
let l46 = l45.toFixed(0||2);
let l47 = [0||l42,l43,l44,l46];
if (l31[l41+3] === 0) continue;
let l48 = Math.random();
let l49 = Math.random();
let l50 = Math.random();
let l51 = Math.random();
let l52 = Math.random();
let l53 = Math.random();
let l54 = Math.random();
let l55 = Math.random();
let l56 = Math.random();
let l57 = Math.random();
let l58 = Math.random();
let l59 = Math.random();
let l60 = Math.random();
let l61 = Math.random();

let l62 = l48 * l14 + l13;
let l63 = l49 * l27 + l23;
let l64 = l50 * l28 + l24;
let l65 = l51 * l27 + l25;
let l66 = l52 * l28 + l26;
let l71 = l53 * l22 + l21;
let l74 = l54 * l18 + l17;
let l75 = l55 * l16 + l15;
let l76 = l56 * l20 + l19;
let l67 = Math.min(3,l63);
let l68 = Math.min(3,l64);
let l69 = Math.min(3,l65);
let l70 = Math.min(3,l66);
let l72 = Math.min(7,l71);
let l73 = Math.round(l72);
let l77 = 2-Math.min(2,l75);
let l78 = Math.min(2,l74);
let l83 = l57 - 0.5;
let l84 = l58 - 0.5;
let l85 = l59 * l6;
let l86 = l60 * l8;
let l87 = l61 * l10;
let l88 = l83 * l11 * l3;
let l89 = l84 * l12 * l4;
let l90 = !l8? l85: l86;
let l91 = !l10? l85: l87;
let l92 = (l90 + l38) * l3;
let l93 = (l91 + l39) * l4;
let l96 = Math.max(0,l92-l62);
let l97 = Math.max(0,l93-l62);
let l82 = (l77+l78) * Math.PI;
let l80 = l78 * Math.PI;
let l81 = l76 * Math.PI;
let l98 = (l96 - l3) / 2;
let l99 = (l97 - l4) / 2;
let l100 = x - l98 + l88;
let l101 = y - l99 + l89;
let l102 = l100 - l3 / 2;
let l103 = l101 - l4 / 2;
let l104 = [l81,l80,l82];
let l105 = [l96/2,l97/2];
let l106 = [x+l88,y+l89];
let l107 = [...l105,...l104];
let l108 = [...l106,...l107];
let l109 = [l102,l103,l96,l97];
let l110 = l103 + l97 / 2;
let l111 = l102 + l96 / 2;
let l112 = l103 + l97;
let l113 = l102 + l96;
let l114 = [
[l102,l103,l113,l112],
[l102,l110,l113,l110],
[l102,l112,l113,l103],
[l111,l112,l111,l103],
[l113,l112,l102,l103],
[l113,l110,l102,l110],
[l113,l103,l102,l112],
[l111,l103,l111,l112]];
let l115 = l114[l73];
let l116 = l115.slice(0,2);
let l117 = l115.slice(2,4);
let l118 = l102 - l96 + l96 * l67;
let l119 = l103 - l97 + l97 * l68;
let l120 = l102 - l96 + l96 * l69;
let l121 = l103 - l97 + l97 * l70;
l40.strokeStyle = `rgba(${l47})`;
l40.fillStyle = `rgba(${l47})`;
l40.lineCap = `square`;
l40.lineWidth = l62;
l40.beginPath();

if (l29 === 0) {
l40.rect(...l109); }
if (l29 === 1) {
l40.ellipse(...l108); }
if (l29 === 2) {
l40.moveTo(...l116);
l40.lineTo(...l117); }
if (l29 === 3) {
if (l35 === false) {
l40.moveTo(...l116);
l40.quadraticCurveTo(
l118, l119,...l117); }
if (l35 === true) {
l40.moveTo(...l116);
l40.bezierCurveTo(
l118,l119,l120,
l121,...l117); }}
if (l37 === false) {
l40.fill(); }
if (l37 === true) {
l40.stroke(); }}}
let l99 = await l1.
convertToBlob()||null;
self.postMessage([l99]); };

