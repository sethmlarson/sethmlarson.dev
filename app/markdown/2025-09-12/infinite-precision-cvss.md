# Infinite* Precision CVSS Calculator

[CVSS](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System) is a scoring system for the severity of a software vulnerability.
The scores range from 0 to 10, but that doesn't mean it's a “10-point system”.
A single value after a decimal (“8.7”) is allowed too, meaning there are 100 potential CVSS scores.
**But what if we need more precision?**

<!-- more -->

Look no further than the “Infinite Precision CVSS Calculator”:

<blockquote>
<form>
<label for="av">Attack Vector (P=0.2, L=0.55, A=0.62, N=0.85)</label><br>
<input name="av" id="av" type="number" value="0.2" min="0.2" max="0.85" step="0.000000000000001"/><br> 
<label for="ac">Attack Complexity (H=0.44, L=0.77)</label><br>
<input name="ac" id="ac" type="number" value="0.44" min="0.44" max="0.77" step="0.000000000000001"/><br> 
<label for="pr">Privileges Required (H=0.27, L=0.62, N=0.85)</label><br>
<input name="pr" id="pr" type="number" value="0.27" min="0.27" max="0.85" step="0.000000000000001"/><br> 
<label for="ui">User Interaction (R=0.62, N=0.85)</label><br>
<input name="ui" id="ui" type="number" value="0.62" min="0.62" max="0.85" step="0.000000000000001"/><br> 
<label for="sc">Scope (U=0.0, C=1.0)</label><br>
<input name="sc" id="sc" type="number" value="0.0" min="0.0" max="1.0" step="0.000000000000001"/><br>
<label for="ci">Confidentiality Impact (N=0.0, L=0.22, H=0.56)</label><br>
<input name="ci" id="ci" type="number" value="0.0" min="0.0" max="0.56" step="0.000000000000001"/><br> 
<label for="ii">Integrity Impact (N=0.0, L=0.22, H=0.56)</label><br>
<input name="ii" id="ii" type="number" value="0.0" min="0.0" max="0.56" step="0.000000000000001"/><br> 
<label for="ai">Availability Impact (N=0.0, L=0.22, H=0.56)</label><br>
<input name="ai" id="ai" type="number" value="0.0" min="0.0" max="0.56" step="0.000000000000001"/><br> 
<hr>
<label for="cvss">CVSS:</label>
<input name="cvss" id="cvss" value="0.0"/>
</form>
</blockquote>

> **NOTE:** This page is a joke, do not use for actual software vulnerability
CVSS calculations.

<script>
function calculateScore() {
  var ac = Number.parseFloat(document.querySelector("#ac").value);
  var av = Number.parseFloat(document.querySelector("#av").value);
  var pr = Number.parseFloat(document.querySelector("#pr").value);
  var ui = Number.parseFloat(document.querySelector("#ui").value);
  var ci = Number.parseFloat(document.querySelector("#ci").value);
  var ii = Number.parseFloat(document.querySelector("#ii").value);
  var ai = Number.parseFloat(document.querySelector("#ai").value);
  var sc = Number.parseFloat(document.querySelector("#sc").value);
  sc = Math.min(1, Math.max(0, sc));
  var impactBaseScore = 1 - ((1 - ci) * (1 - ii) * (1 - ai));
  var impactSubScoreChanged = (7.52 * (impactBaseScore - 0.029)) - (3.25 * ((impactBaseScore - 0.02) ** 15));
  var impactSubScoreUnchanged = 6.42 * impactBaseScore;
  var impactSubScore = (impactSubScoreUnchanged * (1 - sc)) + (impactSubScoreChanged * sc);
  var environmentSubScore = 8.22 * ac * av * pr * ui;
  var totalScoreChanged = 1.08 * (impactSubScore + environmentSubScore);
  var totalScoreUnchanged = impactSubScore + environmentSubScore;
  var totalScore = (totalScoreUnchanged * (1 - sc)) + (totalScoreChanged * sc);
  var cvss = Math.min(10.0, Math.max(0, totalScore));
  document.querySelector("#cvss").value = cvss.toString();
};

document.getElementById("av").addEventListener("input", (event) => {calculateScore();});
document.getElementById("ac").addEventListener("input", (event) => {calculateScore();});
document.getElementById("pr").addEventListener("input", (event) => {calculateScore();});
document.getElementById("ui").addEventListener("input", (event) => {calculateScore();});
document.getElementById("sc").addEventListener("input", (event) => {calculateScore();});
document.getElementById("ci").addEventListener("input", (event) => {calculateScore();});
document.getElementById("ii").addEventListener("input", (event) => {calculateScore();});
document.getElementById("ai").addEventListener("input", (event) => {calculateScore();});
calculateScore();
</script>