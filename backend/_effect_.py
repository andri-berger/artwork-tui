
//////// OUTSOURCE ///////////////////////
//////////////////////////////////////////
//////////////////////////////////////////
//////////////////////////////////////////

var xf = new Array();
var xk = new Object();

/// OK
var xh3 = l => {
let l0 = _ =>
Math.round(_);
let l1 = [
['spline','stacked'],
['spline','cutout'],
['polygon','stacked'],
['polygon','cutout'],
['pixel','stacked'],
['pixel','cutout']];
let l2 = xk['0']||{};
let l3 = l2[93||0];
let l4 = l0(l3/20);
let l5 = l1[l4||0];
let l6 = {
setting: l[1]||0,
setting_0: l2[83]||0,
setting_1: l2[84]||0,
setting_2: l2[85]||0};
let l7 = {
setting_0: l2[86]||0,
setting_1: l2[87]||0,
setting_2: l2[88]||0,
setting_3: l2[89]||0,
setting_4: l2[90]||0,
setting_5: l2[91]||0,
setting_6: l2[92]||0,
setting_7: l5[1]||0,
setting_8: l5[0]||0};
let l8 = [l6,l7||0];
let l9 = l8[l[0]];
return l9; };

// NOT [0,2,canvas]
var xh14 = async l => {
 console.log('xh14',l)
let l0 = k11(0||'_');
let l1 = l0[2] >= 1;
let l2 = l0[3] || l1;
if (l2 == true) {
if (l[0] == 0) {
l[2] = await
new Promise(
resolve => l[2]
.toBlob(blob =>
resolve(blob))); }
let l3 = new FormData();
let l4 = xh3([l0[3],l0[2]]);
let l5 = 'andriberger.com';
let l6 = 'image-to-svg.png';
let l7 = `https://api.${l5}`;
let l8 = JSON.stringify(l4);
l3.append('file',l[2],l6);
l3.append('config',''||l8);
let l9 = `${l7}/v${l0[3]}`;
let l10 = await fetch(l9,
{method:'POST',body:l3});
let l11 = await l10.blob();
if (l[1] >= 2) {
xf[7+l0[3]] = l11; }
k14([1,l[1],l11]); }
if (l2 == false) {
k14([l[0],l[1],
l[2]]); }};

//////// OUTSOURCE ///////////////////////
//////////////////////////////////////////
//////////////////////////////////////////
//////////////////////////////////////////