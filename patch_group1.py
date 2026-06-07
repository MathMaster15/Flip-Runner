import re

with open('index.html', 'r') as f:
    content = f.read()

def replace_func(func_name, new_body):
    global content
    pattern = r"function " + func_name + r"\(ctx,col,ch,sw,sh2,player,t,lv=0\)\{.*?(?=\nfunction draw[A-Za-z]+Char|\n// ── SHOP SYSTEM)"
    # We use re.DOTALL to match across newlines
    content = re.sub(pattern, new_body, content, flags=re.DOTALL)

# RUNNER
new_runner = """function drawRunnerChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = player.dashing ? '#00ffff' : ch.glow;
  ctx.shadowBlur = player.dashing ? 30 : 15;
  const bounce = player.onGround ? Math.sin(t*10)*2 : 0;
  ctx.translate(0, bounce);
  
  // Sleek Aerodynamic Suit
  ctx.fillStyle = '#111';
  ctx.beginPath();
  ctx.moveTo(-wa+4, -ha+4);
  ctx.lineTo(wa-4, -ha+2);
  ctx.lineTo(wa, ha-2);
  ctx.lineTo(-wa, ha);
  ctx.closePath();
  ctx.fill();
  
  // Cybernetic Armor Plates (Cyan)
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(-wa+2, -ha+10);
  ctx.lineTo(wa-2, -ha+6);
  ctx.lineTo(wa+2, 0);
  ctx.lineTo(-wa-2, 4);
  ctx.closePath();
  ctx.fill();
  
  // Energy Backpack / Thruster
  ctx.fillStyle = '#222';
  ctx.fillRect(-wa-6, -ha+12, 6, 14);
  ctx.fillStyle = '#00f5a0';
  ctx.fillRect(-wa-8, -ha+14, 4, 10);
  
  // Visor
  ctx.fillStyle = '#0a0a0f';
  ctx.beginPath();
  ctx.moveTo(-wa+4, -ha+8);
  ctx.lineTo(wa+2, -ha+4);
  ctx.lineTo(wa+1, -ha+12);
  ctx.lineTo(-wa+2, -ha+14);
  ctx.closePath();
  ctx.fill();
  
  // Visor Glow Trail
  ctx.strokeStyle = '#00f5a0';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(wa-2, -ha+8);
  ctx.lineTo(wa+8, -ha+8 + Math.sin(t*15)*2);
  ctx.stroke();

  // Energy Core
  ctx.fillStyle = '#fff';
  ctx.shadowBlur = 20;
  ctx.beginPath();
  ctx.arc(0, ha-6, 4, 0, Math.PI*2);
  ctx.fill();

  if(lv>=2) {
    ctx.strokeStyle = '#00ffff';
    ctx.setLineDash([2, 2]);
    ctx.beginPath();
    ctx.moveTo(0, -ha+15);
    ctx.lineTo(0, ha-10);
    ctx.stroke();
    ctx.setLineDash([]);
  }
  ctx.restore();
}"""

# GLIDER
new_glider = """function drawGliderChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 20;
  
  const wingFlap = player.onGround ? 0 : Math.sin(t*8)*10;
  
  // Energy Wings
  ctx.fillStyle = 'rgba(0, 207, 255, 0.4)';
  ctx.beginPath();
  ctx.moveTo(-wa, 0);
  ctx.quadraticCurveTo(-wa-20, -ha-wingFlap, -wa-30, -ha+10-wingFlap);
  ctx.lineTo(-wa, 10);
  ctx.closePath();
  ctx.fill();
  
  ctx.beginPath();
  ctx.moveTo(wa, 0);
  ctx.quadraticCurveTo(wa+20, -ha-wingFlap, wa+30, -ha+10-wingFlap);
  ctx.lineTo(wa, 10);
  ctx.closePath();
  ctx.fill();

  // Aviator Body
  ctx.fillStyle = '#001a2e';
  ctx.beginPath();
  ctx.moveTo(0, -ha-4);
  ctx.lineTo(wa, 0);
  ctx.lineTo(wa-4, ha);
  ctx.lineTo(-wa+4, ha);
  ctx.lineTo(-wa, 0);
  ctx.closePath();
  ctx.fill();
  
  // Metallic plating
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(0, -ha+2);
  ctx.lineTo(wa-2, 0);
  ctx.lineTo(0, ha-4);
  ctx.lineTo(-wa+2, 0);
  ctx.closePath();
  ctx.fill();

  // Pilot Goggles
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.ellipse(-4, -ha+10, 4, 3, 0, 0, Math.PI*2);
  ctx.ellipse(4, -ha+10, 4, 3, 0, 0, Math.PI*2);
  ctx.fill();
  ctx.fillStyle = '#000';
  ctx.beginPath();
  ctx.arc(-4, -ha+10, 1.5, 0, Math.PI*2);
  ctx.arc(4, -ha+10, 1.5, 0, Math.PI*2);
  ctx.fill();
  
  // Thruster
  ctx.fillStyle = '#00cfff';
  ctx.globalAlpha = 0.6 + Math.sin(t*20)*0.4;
  ctx.beginPath();
  ctx.moveTo(-6, ha);
  ctx.lineTo(0, ha+15);
  ctx.lineTo(6, ha);
  ctx.fill();
  
  if(lv>=2){
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(-wa-30, -ha+10-wingFlap);
    ctx.lineTo(-wa-35, -ha-wingFlap);
    ctx.stroke();
  }
  ctx.restore();
}"""

# DASHER
new_dasher = """function drawDasherChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = '#ff3300';
  ctx.shadowBlur = 25;
  const shake = player.dashing ? Math.sin(t*30)*2 : 0;
  ctx.translate(shake, 0);
  
  // Flame Trail
  ctx.fillStyle = 'rgba(255, 68, 0, 0.5)';
  ctx.beginPath();
  ctx.moveTo(-wa, ha);
  ctx.lineTo(-wa-15, ha-10+Math.sin(t*10)*5);
  ctx.lineTo(-wa, ha-20);
  ctx.fill();
  
  // Spiked Armor Body
  ctx.fillStyle = '#1a0500';
  ctx.beginPath();
  ctx.moveTo(wa+4, -ha+8);
  ctx.lineTo(wa, ha);
  ctx.lineTo(-wa, ha);
  ctx.lineTo(-wa-4, -ha+8);
  ctx.lineTo(0, -ha-8);
  ctx.closePath();
  ctx.fill();
  
  // Magma Core & Veins
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(wa+2, -ha+10);
  ctx.lineTo(0, ha-4);
  ctx.lineTo(-wa-2, -ha+10);
  ctx.lineTo(0, -ha);
  ctx.closePath();
  ctx.fill();
  
  // Furious Eyes
  ctx.fillStyle = '#ffff00';
  ctx.beginPath();
  ctx.moveTo(-wa+4, -ha+8);
  ctx.lineTo(0, -ha+12);
  ctx.lineTo(-wa+4, -ha+14);
  ctx.fill();
  ctx.beginPath();
  ctx.moveTo(wa-4, -ha+8);
  ctx.lineTo(0, -ha+12);
  ctx.lineTo(wa-4, -ha+14);
  ctx.fill();

  // Exhaust Vents
  ctx.fillStyle = '#ffcc00';
  ctx.fillRect(-wa, ha-10, 4, 8);
  ctx.fillRect(wa-4, ha-10, 4, 8);

  if(lv>=2){
    ctx.strokeStyle = '#ff0000';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(0, ha, 10, Math.PI, 0);
    ctx.stroke();
  }
  ctx.restore();
}"""

# GHOST
new_ghost = """function drawGhostChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  const floatY = Math.sin(t*3)*5;
  ctx.translate(0, floatY);
  
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 30;
  
  // Ethereal Cape / Body
  ctx.globalAlpha = 0.7;
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(0, -ha-8);
  ctx.quadraticCurveTo(wa+10, -ha, wa+4, ha-10);
  // Wavy bottom
  ctx.quadraticCurveTo(wa, ha+10, wa/2, ha);
  ctx.quadraticCurveTo(0, ha+15, -wa/2, ha);
  ctx.quadraticCurveTo(-wa, ha+10, -wa-4, ha-10);
  ctx.quadraticCurveTo(-wa-10, -ha, 0, -ha-8);
  ctx.closePath();
  ctx.fill();
  
  // Dark inner hood
  ctx.globalAlpha = 1.0;
  ctx.fillStyle = '#110022';
  ctx.beginPath();
  ctx.arc(0, -ha+8, 12, 0, Math.PI*2);
  ctx.fill();
  
  // Hollow Glowing Eyes
  ctx.fillStyle = '#e0d0ff';
  ctx.shadowBlur = 10;
  ctx.shadowColor = '#fff';
  ctx.beginPath();
  ctx.ellipse(-4, -ha+8, 3, 5, -0.2, 0, Math.PI*2);
  ctx.ellipse(4, -ha+8, 3, 5, 0.2, 0, Math.PI*2);
  ctx.fill();
  
  // Spectral Orbs
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.arc(-wa-10, 0 + Math.sin(t*4)*4, 3, 0, Math.PI*2);
  ctx.arc(wa+10, 5 + Math.cos(t*4)*4, 4, 0, Math.PI*2);
  ctx.fill();

  if(lv>=2){
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0, -ha-15);
    ctx.lineTo(0, -ha-8);
    ctx.stroke();
  }
  ctx.restore();
}"""

# MAGNET
new_magnet = """function drawMagnetChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 15;
  
  // Heavy Cyber Boots
  ctx.fillStyle = '#333';
  ctx.fillRect(-wa, ha-4, wa-2, 8);
  ctx.fillRect(2, ha-4, wa-2, 8);
  
  // Bulky Torso
  ctx.fillStyle = '#1a0010';
  ctx.beginPath();
  ctx.roundRect(-wa-2, -ha+8, sw+4, sh2-12, 4);
  ctx.fill();
  
  // Magnetic Core
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.arc(0, 0, 10, 0, Math.PI*2);
  ctx.fill();
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.arc(0, 0, 4, 0, Math.PI*2);
  ctx.fill();
  
  // Floating Magnets on Shoulders
  const spin = t*2;
  ctx.save();
  ctx.translate(-wa-8, -ha+8);
  ctx.rotate(spin);
  ctx.fillStyle = '#ff0055'; // Red pole
  ctx.fillRect(-6, -6, 6, 12);
  ctx.fillStyle = '#0055ff'; // Blue pole
  ctx.fillRect(0, -6, 6, 12);
  ctx.restore();
  
  ctx.save();
  ctx.translate(wa+8, -ha+8);
  ctx.rotate(-spin);
  ctx.fillStyle = '#ff0055';
  ctx.fillRect(-6, -6, 6, 12);
  ctx.fillStyle = '#0055ff';
  ctx.fillRect(0, -6, 6, 12);
  ctx.restore();
  
  // Cyber Scanner Eye
  ctx.fillStyle = '#fff';
  ctx.fillRect(-wa+4, -ha, sw-8, 6);
  ctx.fillStyle = col;
  const scanX = Math.sin(t*5) * (wa-6);
  ctx.fillRect(scanX-2, -ha, 4, 6);

  if(lv>=2){
    ctx.strokeStyle = col;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(0,0, 18, -Math.PI/4, Math.PI/4);
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(0,0, 18, Math.PI - Math.PI/4, Math.PI + Math.PI/4);
    ctx.stroke();
  }
  ctx.restore();
}"""

replace_func('drawRunnerChar', new_runner)
replace_func('drawGliderChar', new_glider)
replace_func('drawDasherChar', new_dasher)
replace_func('drawGhostChar', new_ghost)
replace_func('drawMagnetChar', new_magnet)

with open('index.html', 'w') as f:
    f.write(content)
