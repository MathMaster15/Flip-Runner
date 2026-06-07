import re

with open('index.html', 'r') as f:
    content = f.read()

def replace_func(func_name, new_body):
    global content
    pattern = r"function " + func_name + r"\(ctx,col,ch,sw,sh2,player,t,lv=0\)\{.*?(?=\nfunction draw[A-Za-z]+Char|\n// ── SHOP SYSTEM)"
    content = re.sub(pattern, new_body, content, flags=re.DOTALL)

# STORM
new_storm = """function drawStormChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 25;
  const float = Math.sin(t*4)*3;
  ctx.translate(0, float);
  
  // Cloud Trail / Base
  ctx.fillStyle = 'rgba(200, 220, 255, 0.4)';
  ctx.beginPath();
  ctx.arc(0, ha, 15, 0, Math.PI*2);
  ctx.arc(-10, ha+5, 10, 0, Math.PI*2);
  ctx.arc(10, ha+5, 10, 0, Math.PI*2);
  ctx.fill();
  
  // Crystal Armor Body
  ctx.fillStyle = '#001122';
  ctx.beginPath();
  ctx.moveTo(0, -ha-4);
  ctx.lineTo(wa, -ha/2);
  ctx.lineTo(wa-4, ha);
  ctx.lineTo(-wa+4, ha);
  ctx.lineTo(-wa, -ha/2);
  ctx.closePath();
  ctx.fill();
  
  // Thunder Crown
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(-wa-4, -ha);
  ctx.lineTo(-wa/2, -ha-12);
  ctx.lineTo(0, -ha-4);
  ctx.lineTo(wa/2, -ha-12);
  ctx.lineTo(wa+4, -ha);
  ctx.fill();
  
  // Crackling Energy Bolts
  ctx.strokeStyle = '#fff';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(-wa+4, ha-10);
  ctx.lineTo(0, ha-4+Math.random()*4);
  ctx.lineTo(wa-4, ha-10);
  ctx.stroke();

  // Divine Eyes
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.arc(-6, -ha+8, 2, 0, Math.PI*2);
  ctx.arc(6, -ha+8, 2, 0, Math.PI*2);
  ctx.fill();

  if(lv>=2){
    ctx.strokeStyle = col;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.arc(0,0, wa+10, 0, Math.PI*2);
    ctx.stroke();
  }
  ctx.restore();
}"""

# SPECTER
new_specter = """function drawSpecterChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 20;
  
  // Holographic Wireframe
  ctx.strokeStyle = col;
  ctx.lineWidth = 1;
  ctx.setLineDash([2, 2]);
  ctx.beginPath();
  ctx.moveTo(0, -ha);
  ctx.lineTo(wa, 0);
  ctx.lineTo(0, ha);
  ctx.lineTo(-wa, 0);
  ctx.closePath();
  ctx.stroke();
  
  ctx.beginPath();
  ctx.moveTo(0, -ha);
  ctx.lineTo(wa/2, 0);
  ctx.lineTo(0, ha);
  ctx.lineTo(-wa/2, 0);
  ctx.closePath();
  ctx.stroke();
  
  // Core Data Stream
  ctx.fillStyle = 'rgba(0, 68, 51, 0.8)';
  ctx.fillRect(-wa/2, -ha/2, wa, ha);
  
  // Glitching segments
  ctx.fillStyle = '#fff';
  if(Math.random()>0.8){
    ctx.fillRect(-wa/2+Math.random()*wa, -ha/2+Math.random()*ha, 8, 2);
  }
  
  // Cyber Eyes
  ctx.fillStyle = '#44ffcc';
  ctx.fillRect(-wa/2+2, -ha/4, 6, 4);
  ctx.fillRect(wa/2-8, -ha/4, 6, 4);

  if(lv>=2){
    ctx.setLineDash([]);
    ctx.strokeStyle = '#fff';
    ctx.beginPath();
    ctx.arc(0,0, wa, 0, Math.PI*2);
    ctx.stroke();
  }
  ctx.restore();
}"""

# MECH
new_mech = """function drawMechChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 10;
  
  // Hydraulic Legs
  ctx.fillStyle = '#222';
  ctx.fillRect(-wa-4, ha-6, 12, 12);
  ctx.fillRect(wa-8, ha-6, 12, 12);
  ctx.fillStyle = '#444';
  ctx.fillRect(-wa-2, ha-2, 8, 8);
  ctx.fillRect(wa-6, ha-2, 8, 8);
  
  // Boxy Iron Chassis
  ctx.fillStyle = col;
  ctx.fillRect(-wa-6, -ha+6, sw+12, sh2-12);
  
  // Central Gear/Reactor
  ctx.fillStyle = '#1a2200';
  ctx.beginPath();
  ctx.arc(0, 0, 10, 0, Math.PI*2);
  ctx.fill();
  ctx.save();
  ctx.rotate(t);
  ctx.strokeStyle = '#bbcc66';
  ctx.lineWidth = 3;
  ctx.beginPath(); ctx.moveTo(0,0); ctx.lineTo(10,0); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(0,0); ctx.lineTo(-10,0); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(0,0); ctx.lineTo(0,10); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(0,0); ctx.lineTo(0,-10); ctx.stroke();
  ctx.restore();
  
  // Visor / Mono-eye
  ctx.fillStyle = '#000';
  ctx.fillRect(-wa+2, -ha-2, sw-4, 8);
  ctx.fillStyle = '#ff0000';
  const scanX = Math.sin(t*3)*(wa-6);
  ctx.beginPath();
  ctx.arc(scanX, -ha+2, 3, 0, Math.PI*2);
  ctx.fill();
  
  if(lv>=2){
    ctx.fillStyle = '#ffcc00';
    ctx.fillRect(-wa-8, -ha+10, 4, 14);
    ctx.fillRect(wa+4, -ha+10, 4, 14);
  }
  ctx.restore();
}"""

# BUBBLE
new_bubble = """function drawBubbleChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 20;
  
  // Wobbly Bubble
  const wobble = Math.sin(t*5)*2;
  ctx.scale(1.0 + wobble/20, 1.0 - wobble/20);
  
  // Liquid Body
  ctx.fillStyle = 'rgba(102, 221, 255, 0.4)';
  ctx.beginPath();
  ctx.arc(0, 0, wa+4, 0, Math.PI*2);
  ctx.fill();
  
  // Reflection Highlights
  ctx.fillStyle = 'rgba(255, 255, 255, 0.6)';
  ctx.beginPath();
  ctx.ellipse(-wa/2, -ha/2, 6, 3, -Math.PI/4, 0, Math.PI*2);
  ctx.fill();
  ctx.beginPath();
  ctx.arc(wa/2, ha/2, 2, 0, Math.PI*2);
  ctx.fill();
  
  // Inner Core (Cute Protector)
  ctx.fillStyle = '#002233';
  ctx.beginPath();
  ctx.arc(0, 0, 8, 0, Math.PI*2);
  ctx.fill();
  
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.arc(-3, -2, 2, 0, Math.PI*2);
  ctx.arc(3, -2, 2, 0, Math.PI*2);
  ctx.fill();

  if(lv>=2){
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.arc(0,0, wa+8, 0, Math.PI*2);
    ctx.stroke();
  }
  ctx.restore();
}"""

# VORTEX
new_vortex = """function drawVortexChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 25;
  
  // Void Core
  ctx.fillStyle = '#1a0a2d';
  ctx.beginPath();
  ctx.arc(0, 0, 10, 0, Math.PI*2);
  ctx.fill();
  
  // Spinning Energy Tornado
  const rot = t*15;
  ctx.rotate(rot);
  
  ctx.strokeStyle = col;
  ctx.lineWidth = 3;
  ctx.beginPath();
  for(let i=0; i<3; i++){
    const ang = i*(Math.PI*2/3);
    ctx.moveTo(Math.cos(ang)*10, Math.sin(ang)*10);
    ctx.quadraticCurveTo(Math.cos(ang+1)*25, Math.sin(ang+1)*25, Math.cos(ang+2)*35, Math.sin(ang+2)*35);
  }
  ctx.stroke();
  
  // Debris
  ctx.fillStyle = '#fff';
  for(let i=0; i<4; i++){
    const dang = i*(Math.PI/2) + t*5;
    const drad = 15 + Math.sin(t*2+i)*5;
    ctx.beginPath();
    ctx.arc(Math.cos(dang)*drad, Math.sin(dang)*drad, 2, 0, Math.PI*2);
    ctx.fill();
  }
  
  // Eye in the storm
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.arc(0, 0, 3, 0, Math.PI*2);
  ctx.fill();

  if(lv>=2){
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.arc(0,0, 35, 0, Math.PI*2);
    ctx.stroke();
  }
  ctx.restore();
}"""

replace_func('drawStormChar', new_storm)
replace_func('drawSpecterChar', new_specter)
replace_func('drawMechChar', new_mech)
replace_func('drawBubbleChar', new_bubble)
replace_func('drawVortexChar', new_vortex)

with open('index.html', 'w') as f:
    f.write(content)
