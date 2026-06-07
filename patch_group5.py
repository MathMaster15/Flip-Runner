import re

with open('index.html', 'r') as f:
    content = f.read()

def replace_func(func_name, new_body):
    global content
    pattern = r"function " + func_name + r"\(ctx,col,ch,sw,sh2,player,t,lv=0\)\{.*?(?=\nfunction draw[A-Za-z]+Char|\n// ── SHOP SYSTEM)"
    content = re.sub(pattern, new_body, content, flags=re.DOTALL)

# FROST
new_frost = """function drawFrostChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 20;
  
  // Freezing Mist
  ctx.fillStyle = 'rgba(0, 221, 255, 0.2)';
  ctx.beginPath();
  ctx.arc(0, ha, wa+10+Math.sin(t*3)*5, 0, Math.PI*2);
  ctx.fill();
  
  // Ice Crystal Body
  ctx.fillStyle = '#003355';
  ctx.beginPath();
  ctx.moveTo(0, -ha-10);
  ctx.lineTo(wa, 0);
  ctx.lineTo(0, ha+5);
  ctx.lineTo(-wa, 0);
  ctx.closePath();
  ctx.fill();
  
  // Crystalline Facets
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(0, -ha-10);
  ctx.lineTo(wa/2, 0);
  ctx.lineTo(0, ha+5);
  ctx.closePath();
  ctx.fill();
  
  ctx.fillStyle = '#fff';
  ctx.globalAlpha = 0.5;
  ctx.beginPath();
  ctx.moveTo(0, -ha-10);
  ctx.lineTo(-wa/4, -ha/2);
  ctx.lineTo(0, 0);
  ctx.closePath();
  ctx.fill();
  
  // Floating Shards
  ctx.globalAlpha = 1.0;
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(-wa-5, 0); ctx.lineTo(-wa-10, -5); ctx.lineTo(-wa-8, 5); ctx.fill();
  ctx.beginPath();
  ctx.moveTo(wa+5, 0); ctx.lineTo(wa+10, -5); ctx.lineTo(wa+8, 5); ctx.fill();

  if(lv>=2){
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.arc(0, -ha/2, wa, 0, Math.PI);
    ctx.stroke();
  }
  ctx.restore();
}"""

# GRAVITY
new_gravity = """function drawGravityChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 25;
  
  const hover = Math.sin(t*2)*6;
  ctx.translate(0, hover);
  
  // Orbital Rings
  ctx.strokeStyle = col;
  ctx.lineWidth = 2;
  ctx.save();
  ctx.rotate(t*1.5);
  ctx.beginPath(); ctx.ellipse(0,0, wa+10, ha/3, 0, 0, Math.PI*2); ctx.stroke();
  ctx.restore();
  
  ctx.save();
  ctx.rotate(-t*2);
  ctx.strokeStyle = '#fff';
  ctx.beginPath(); ctx.ellipse(0,0, ha/2, wa+12, 0, 0, Math.PI*2); ctx.stroke();
  ctx.restore();
  
  // Disembodied Geometric Core
  ctx.fillStyle = '#330066';
  ctx.beginPath();
  ctx.moveTo(0, -ha);
  ctx.lineTo(wa/2, -ha/2);
  ctx.lineTo(0, 0);
  ctx.lineTo(-wa/2, -ha/2);
  ctx.closePath();
  ctx.fill();
  
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(0, ha);
  ctx.lineTo(wa/2, ha/2);
  ctx.lineTo(0, 5);
  ctx.lineTo(-wa/2, ha/2);
  ctx.closePath();
  ctx.fill();
  
  // Gravity Sphere
  ctx.fillStyle = '#000';
  ctx.beginPath();
  ctx.arc(0, 0, 6, 0, Math.PI*2);
  ctx.fill();
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.arc(0, 0, 2, 0, Math.PI*2);
  ctx.fill();

  if(lv>=2){
    ctx.fillStyle = col;
    ctx.beginPath();
    ctx.arc(-wa-10, 0, 3, 0, Math.PI*2);
    ctx.arc(wa+10, 0, 3, 0, Math.PI*2);
    ctx.fill();
  }
  ctx.restore();
}"""

# CYBER
new_cyber = """function drawCyberChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 20;
  
  // Holographic Base
  ctx.fillStyle = 'rgba(0, 255, 204, 0.15)';
  ctx.beginPath();
  ctx.arc(0, 0, wa+5, 0, Math.PI*2);
  ctx.fill();
  
  // Tech Body
  ctx.fillStyle = '#003344';
  ctx.beginPath();
  ctx.moveTo(-wa+4, -ha);
  ctx.lineTo(wa-4, -ha);
  ctx.lineTo(wa, ha);
  ctx.lineTo(-wa, ha);
  ctx.closePath();
  ctx.fill();
  
  // Data Rings
  ctx.strokeStyle = col;
  ctx.lineWidth = 1.5;
  ctx.setLineDash([4, 4]);
  ctx.beginPath();
  ctx.arc(0, 0, wa+8, t*2, t*2 + Math.PI);
  ctx.stroke();
  ctx.setLineDash([]);
  
  // Oracle Eye
  ctx.fillStyle = '#00ffcc';
  ctx.beginPath();
  ctx.arc(0, -ha/2, 6, 0, Math.PI*2);
  ctx.fill();
  ctx.fillStyle = '#fff';
  ctx.fillRect(-8, -ha/2-1, 16, 2);
  
  // Runes
  ctx.fillStyle = col;
  ctx.fillRect(-wa/2, ha/2, 4, 4);
  ctx.fillRect(wa/2-4, ha/2, 4, 4);

  if(lv>=2){
    ctx.strokeStyle = '#fff';
    ctx.beginPath();
    ctx.arc(0, -ha/2, 10, 0, Math.PI*2);
    ctx.stroke();
  }
  ctx.restore();
}"""

# STORM_HUNT
new_stormhunt = """function drawStormHuntChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 25;
  
  const shake = player.dashing ? Math.sin(t*20)*2 : 0;
  ctx.translate(shake, 0);
  
  // Electric Wings
  ctx.strokeStyle = 'rgba(170, 187, 255, 0.6)';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(0, 0);
  ctx.lineTo(-wa-15, -ha-5+Math.sin(t*15)*5);
  ctx.lineTo(-wa-10, 0);
  ctx.stroke();
  
  ctx.beginPath();
  ctx.moveTo(0, 0);
  ctx.lineTo(wa+15, -ha-5+Math.sin(t*15)*5);
  ctx.lineTo(wa+10, 0);
  ctx.stroke();
  
  // Aerodynamic Arrow Body
  ctx.fillStyle = '#112244';
  ctx.beginPath();
  ctx.moveTo(0, -ha-8);
  ctx.lineTo(wa+4, ha);
  ctx.lineTo(0, ha-6);
  ctx.lineTo(-wa-4, ha);
  ctx.closePath();
  ctx.fill();
  
  // Energy Veins
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(0, -ha-2);
  ctx.lineTo(wa-2, ha-2);
  ctx.lineTo(0, ha-8);
  ctx.lineTo(-wa+2, ha-2);
  ctx.closePath();
  ctx.fill();
  
  // Visor
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.moveTo(0, -ha+6);
  ctx.lineTo(wa/2, -ha+10);
  ctx.lineTo(0, -ha+14);
  ctx.lineTo(-wa/2, -ha+10);
  ctx.closePath();
  ctx.fill();

  if(lv>=2){
    ctx.fillStyle = '#fff';
    ctx.beginPath();
    ctx.arc(0, ha+5, 4, 0, Math.PI*2);
    ctx.fill();
  }
  ctx.restore();
}"""

# VENOM
new_venom = """function drawVenomChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 20;
  
  // Toxic Slime Base
  const pulse = Math.sin(t*3)*3;
  ctx.fillStyle = 'rgba(0, 221, 136, 0.4)';
  ctx.beginPath();
  ctx.ellipse(0, ha, wa+pulse, 8, 0, 0, Math.PI*2);
  ctx.fill();
  
  // Predatory Slime Body
  ctx.fillStyle = '#004422';
  ctx.beginPath();
  ctx.moveTo(0, -ha);
  ctx.quadraticCurveTo(wa+5, -ha/2, wa-2, ha);
  ctx.quadraticCurveTo(0, ha+5, -wa+2, ha);
  ctx.quadraticCurveTo(-wa-5, -ha/2, 0, -ha);
  ctx.closePath();
  ctx.fill();
  
  // Dripping Tentacles
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(-wa/2, ha);
  ctx.quadraticCurveTo(-wa/2, ha+10, -wa/2+2, ha+15+Math.sin(t*4)*5);
  ctx.quadraticCurveTo(-wa/2+4, ha+10, -wa/2+6, ha);
  ctx.fill();
  
  ctx.beginPath();
  ctx.moveTo(wa/2, ha);
  ctx.quadraticCurveTo(wa/2, ha+8, wa/2-2, ha+12+Math.cos(t*5)*5);
  ctx.quadraticCurveTo(wa/2-4, ha+8, wa/2-6, ha);
  ctx.fill();
  
  // Compound Eyes
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.ellipse(-4, -ha+10, 4, 6, -0.2, 0, Math.PI*2);
  ctx.ellipse(4, -ha+10, 4, 6, 0.2, 0, Math.PI*2);
  ctx.fill();
  ctx.fillStyle = '#000';
  ctx.beginPath();
  ctx.arc(-4, -ha+12, 1.5, 0, Math.PI*2);
  ctx.arc(4, -ha+12, 1.5, 0, Math.PI*2);
  ctx.fill();

  if(lv>=2){
    ctx.strokeStyle = col;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(0, -ha, 6, 0, Math.PI);
    ctx.stroke();
  }
  ctx.restore();
}"""

# NEON
new_neon = """function drawNeonChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 30;
  
  // Chromatic Aberration & Glitch
  const glitch = Math.sin(t*20) > 0.8 ? 5 : 0;
  
  // Cyan layer
  ctx.fillStyle = '#00ffff';
  ctx.globalAlpha = 0.6;
  ctx.fillRect(-wa-glitch, -ha, sw, sh2);
  
  // Magenta layer
  ctx.fillStyle = '#ff00ff';
  ctx.fillRect(-wa+glitch, -ha, sw, sh2);
  
  // Main Body
  ctx.globalAlpha = 1.0;
  ctx.fillStyle = '#220022';
  ctx.fillRect(-wa+2, -ha+2, sw-4, sh2-4);
  
  // Data Lines
  ctx.fillStyle = col;
  ctx.fillRect(-wa+2, -ha+8, sw-4, 2);
  ctx.fillRect(-wa+2, ha-10, sw-4, 2);
  
  // Pixel Eyes
  ctx.fillStyle = '#fff';
  ctx.fillRect(-wa+6, -ha+12, 4, 4);
  ctx.fillRect(wa-10, -ha+12, 4, 4);
  
  // Glitch Blocks
  if(Math.random()>0.5){
    ctx.fillStyle = '#00ffff';
    ctx.fillRect(wa, -ha+Math.random()*sh2, 6, 4);
  }

  if(lv>=2){
    ctx.strokeStyle = '#ff00ff';
    ctx.beginPath();
    ctx.moveTo(-wa-10, ha);
    ctx.lineTo(wa+10, ha);
    ctx.stroke();
  }
  ctx.restore();
}"""

# SOLAR
new_solar = """function drawSolarChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = '#ffff00';
  ctx.shadowBlur = 40;
  
  // Sunburst
  ctx.save();
  ctx.rotate(t);
  ctx.fillStyle = 'rgba(255, 221, 0, 0.3)';
  for(let i=0; i<12; i++){
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(-4, -wa-15);
    ctx.lineTo(4, -wa-15);
    ctx.fill();
    ctx.rotate(Math.PI*2 / 12);
  }
  ctx.restore();
  
  // Divine Armor
  ctx.fillStyle = '#ffdd00';
  ctx.beginPath();
  ctx.moveTo(0, -ha-5);
  ctx.lineTo(wa+5, 0);
  ctx.lineTo(0, ha+10);
  ctx.lineTo(-wa-5, 0);
  ctx.closePath();
  ctx.fill();
  
  // Inner Core (White Hot)
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.moveTo(0, -ha+2);
  ctx.lineTo(wa-2, 0);
  ctx.lineTo(0, ha);
  ctx.lineTo(-wa+2, 0);
  ctx.closePath();
  ctx.fill();
  
  // Royal Crown
  ctx.fillStyle = '#ff6600';
  ctx.beginPath();
  ctx.moveTo(-wa, -ha-4);
  ctx.lineTo(-wa/2, -ha-15);
  ctx.lineTo(0, -ha-8);
  ctx.lineTo(wa/2, -ha-15);
  ctx.lineTo(wa, -ha-4);
  ctx.fill();
  
  // Majestic Eye
  ctx.fillStyle = '#000';
  ctx.beginPath();
  ctx.arc(0, 0, 3, 0, Math.PI*2);
  ctx.fill();

  if(lv>=2){
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(0,0, wa+12, 0, Math.PI*2);
    ctx.stroke();
  }
  ctx.restore();
}"""

replace_func('drawFrostChar', new_frost)
replace_func('drawGravityChar', new_gravity)
replace_func('drawCyberChar', new_cyber)
replace_func('drawStormHuntChar', new_stormhunt)
replace_func('drawVenomChar', new_venom)
replace_func('drawNeonChar', new_neon)
replace_func('drawSolarChar', new_solar)

with open('index.html', 'w') as f:
    f.write(content)
