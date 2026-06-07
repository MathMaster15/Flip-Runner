import re

with open('index.html', 'r') as f:
    content = f.read()

def replace_func(func_name, new_body):
    global content
    pattern = r"function " + func_name + r"\(ctx,col,ch,sw,sh2,player,t,lv=0\)\{.*?(?=\nfunction draw[A-Za-z]+Char|\n// ── SHOP SYSTEM)"
    content = re.sub(pattern, new_body, content, flags=re.DOTALL)

# TIMEBENDER (TimeChar)
new_time = """function drawTimeChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 20;
  
  // Floating mystic clockwork
  ctx.translate(0, Math.sin(t*2)*4);
  
  // Golden Clock dial behind
  ctx.strokeStyle = 'rgba(255, 224, 102, 0.4)';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.arc(0, 0, wa+10, 0, Math.PI*2);
  ctx.stroke();
  
  // Clock hands spinning
  ctx.save();
  ctx.rotate(t*3);
  ctx.beginPath(); ctx.moveTo(0,0); ctx.lineTo(0, -wa-5); ctx.stroke();
  ctx.restore();
  ctx.save();
  ctx.rotate(t*-0.5);
  ctx.lineWidth = 4;
  ctx.beginPath(); ctx.moveTo(0,0); ctx.lineTo(0, -wa+2); ctx.stroke();
  ctx.restore();
  
  // Temporal Suit
  ctx.fillStyle = '#1a1400';
  ctx.beginPath();
  ctx.moveTo(0, -ha);
  ctx.lineTo(wa, -ha/2);
  ctx.lineTo(wa/2, ha);
  ctx.lineTo(-wa/2, ha);
  ctx.lineTo(-wa, -ha/2);
  ctx.closePath();
  ctx.fill();
  
  // Golden Armor accents
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(0, -ha+4);
  ctx.lineTo(wa-4, -ha/2+2);
  ctx.lineTo(0, ha-8);
  ctx.lineTo(-wa+4, -ha/2+2);
  ctx.closePath();
  ctx.fill();
  
  // Glowing monocle/eye
  ctx.fillStyle = '#fff';
  ctx.shadowColor = '#fff';
  ctx.shadowBlur = 10;
  ctx.beginPath();
  ctx.arc(wa/2, -ha+10, 4, 0, Math.PI*2);
  ctx.fill();

  if(lv>=2){
    ctx.strokeStyle = col;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.arc(0,0, wa+15, Math.PI, 1.5*Math.PI);
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(0,0, wa+15, 0, 0.5*Math.PI);
    ctx.stroke();
  }
  ctx.restore();
}"""

# JUMPER
new_jumper = """function drawJumperChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 15;
  
  const squash = player.onGround ? 1.4 : 1.0;
  const stretch = player.onGround ? 0.7 : (player.dashing ? 1.0 : 1.1);
  ctx.scale(squash, stretch);
  
  // Spring Legs
  ctx.strokeStyle = '#aaa';
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(-wa/2, ha-10);
  ctx.lineTo(-wa/2-2, ha-5);
  ctx.lineTo(-wa/2+2, ha);
  ctx.lineTo(-wa/2, ha+5);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(wa/2, ha-10);
  ctx.lineTo(wa/2-2, ha-5);
  ctx.lineTo(wa/2+2, ha);
  ctx.lineTo(wa/2, ha+5);
  ctx.stroke();
  
  // Lunar spherical body
  ctx.fillStyle = '#223322';
  ctx.beginPath();
  ctx.arc(0, 0, wa, 0, Math.PI*2);
  ctx.fill();
  
  // Green cyber accents
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.arc(0, 0, wa-2, 0, Math.PI*2);
  ctx.fill();
  
  // Lunar craters
  ctx.fillStyle = 'rgba(0,0,0,0.3)';
  ctx.beginPath(); ctx.arc(-wa/2, -ha/2, 3, 0, Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(wa/3, -ha/4, 4, 0, Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(-wa/4, ha/3, 2, 0, Math.PI*2); ctx.fill();

  // Bouncy Visor
  ctx.fillStyle = '#0a1a00';
  ctx.fillRect(-wa+4, -ha/4, sw-8, 12);
  ctx.fillStyle = '#fff';
  ctx.fillRect(-wa+6, -ha/4+2, sw-12, 4);

  if(lv>=2){
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(0,0, wa+6, Math.PI/4, 3*Math.PI/4);
    ctx.stroke();
  }
  ctx.restore();
}"""

# TANK
new_tank = """function drawTankChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 10;
  
  // Massive Bulky Frame
  ctx.fillStyle = '#001022';
  ctx.beginPath();
  ctx.moveTo(-wa-8, -ha+10);
  ctx.lineTo(wa+8, -ha+10);
  ctx.lineTo(wa+4, ha+4);
  ctx.lineTo(-wa-4, ha+4);
  ctx.closePath();
  ctx.fill();
  
  // Plated Steel Armor
  ctx.fillStyle = col;
  // Shoulders
  ctx.fillRect(-wa-10, -ha+6, 12, 14);
  ctx.fillRect(wa-2, -ha+6, 12, 14);
  // Chest plate
  ctx.beginPath();
  ctx.moveTo(-wa, -ha+8);
  ctx.lineTo(wa, -ha+8);
  ctx.lineTo(wa-2, ha);
  ctx.lineTo(-wa+2, ha);
  ctx.closePath();
  ctx.fill();
  
  // Shield Generator Core
  ctx.fillStyle = '#fff';
  ctx.shadowBlur = 20;
  ctx.shadowColor = '#00ffff';
  ctx.beginPath();
  ctx.moveTo(0, -ha+18);
  ctx.lineTo(8, -ha+26);
  ctx.lineTo(0, -ha+34);
  ctx.lineTo(-8, -ha+26);
  ctx.closePath();
  ctx.fill();
  
  // Heavy Helmet Visor
  ctx.fillStyle = '#000';
  ctx.fillRect(-wa+4, -ha-2, sw-8, 8);
  ctx.fillStyle = '#66aaff';
  ctx.fillRect(-wa+6, -ha, sw-12, 4);

  if(lv>=2){
    ctx.strokeStyle = col;
    ctx.lineWidth = 3;
    ctx.globalAlpha = 0.5;
    ctx.beginPath();
    ctx.arc(0,0, wa+15, 0, Math.PI*2);
    ctx.stroke();
  }
  ctx.restore();
}"""

# NINJA
new_ninja = """function drawNinjaChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = player.dashing ? 30 : 15;
  
  // Sleek Ninja Body
  ctx.fillStyle = '#111';
  ctx.beginPath();
  ctx.moveTo(-wa+6, -ha);
  ctx.lineTo(wa-6, -ha);
  ctx.lineTo(wa-2, ha);
  ctx.lineTo(-wa+2, ha);
  ctx.closePath();
  ctx.fill();
  
  // Purple Accents / Wrap
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(-wa+2, -ha+14);
  ctx.lineTo(wa-2, -ha+14);
  ctx.lineTo(wa-4, -ha+20);
  ctx.lineTo(-wa+4, -ha+20);
  ctx.closePath();
  ctx.fill();
  
  // Mask & Eyes
  ctx.fillStyle = '#222';
  ctx.beginPath();
  ctx.arc(0, -ha+8, 10, 0, Math.PI*2);
  ctx.fill();
  
  ctx.fillStyle = '#e0e0ff';
  ctx.shadowColor = '#fff';
  ctx.shadowBlur = 8;
  ctx.beginPath();
  ctx.ellipse(-4, -ha+8, 4, 2, 0.2, 0, Math.PI*2);
  ctx.ellipse(4, -ha+8, 4, 2, -0.2, 0, Math.PI*2);
  ctx.fill();
  
  // Dual Katanas on Back
  ctx.strokeStyle = '#555';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(-wa-4, -ha-4);
  ctx.lineTo(wa+8, ha-8);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(wa+4, -ha-4);
  ctx.lineTo(-wa-8, ha-8);
  ctx.stroke();

  if(lv>=2){
    ctx.fillStyle = col;
    ctx.globalAlpha = 0.5;
    ctx.fillRect(-wa-4, Math.sin(t*10)*ha, sw+8, 2);
  }
  ctx.restore();
}"""

# PHOENIX
new_phoenix = """function drawPhoenixChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 35;
  const floatY = Math.sin(t*5)*4;
  ctx.translate(0, floatY);
  
  // Burning Wings
  ctx.fillStyle = 'rgba(255, 68, 0, 0.6)';
  const wingFlap = Math.sin(t*12)*15;
  ctx.beginPath();
  ctx.moveTo(-4, 0);
  ctx.quadraticCurveTo(-wa-30, -ha-wingFlap, -wa-20, ha-wingFlap);
  ctx.closePath();
  ctx.fill();
  ctx.beginPath();
  ctx.moveTo(4, 0);
  ctx.quadraticCurveTo(wa+30, -ha-wingFlap, wa+20, ha-wingFlap);
  ctx.closePath();
  ctx.fill();
  
  // Angelic / Fire Body
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(0, -ha);
  ctx.lineTo(wa, -ha/2);
  ctx.lineTo(wa/2, ha+10);
  ctx.lineTo(0, ha+20);
  ctx.lineTo(-wa/2, ha+10);
  ctx.lineTo(-wa, -ha/2);
  ctx.closePath();
  ctx.fill();
  
  // Inner Core (White Hot)
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.moveTo(0, -ha+6);
  ctx.lineTo(6, -ha+16);
  ctx.lineTo(0, ha);
  ctx.lineTo(-6, -ha+16);
  ctx.closePath();
  ctx.fill();

  // Halo
  ctx.strokeStyle = '#ffff00';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.ellipse(0, -ha-8, 12, 4, 0, 0, Math.PI*2);
  ctx.stroke();

  if(lv>=2){
    ctx.fillStyle = '#ffcc00';
    ctx.globalAlpha = 0.5;
    ctx.beginPath();
    ctx.arc(0, ha+20, 8, 0, Math.PI*2);
    ctx.fill();
  }
  ctx.restore();
}"""

replace_func('drawTimeChar', new_time)
replace_func('drawJumperChar', new_jumper)
replace_func('drawTankChar', new_tank)
replace_func('drawNinjaChar', new_ninja)
replace_func('drawPhoenixChar', new_phoenix)

with open('index.html', 'w') as f:
    f.write(content)
