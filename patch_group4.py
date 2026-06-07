import re

with open('index.html', 'r') as f:
    content = f.read()

def replace_func(func_name, new_body):
    global content
    pattern = r"function " + func_name + r"\(ctx,col,ch,sw,sh2,player,t,lv=0\)\{.*?(?=\nfunction draw[A-Za-z]+Char|\n// ── SHOP SYSTEM)"
    content = re.sub(pattern, new_body, content, flags=re.DOTALL)

# CHRONO
new_chrono = """function drawChronoChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 25;
  const hover = Math.sin(t*2)*5;
  ctx.translate(0, hover);
  
  // Mystical Geometric Rings
  ctx.strokeStyle = 'rgba(255, 221, 0, 0.4)';
  ctx.lineWidth = 2;
  ctx.save();
  ctx.rotate(t);
  ctx.beginPath(); ctx.ellipse(0,0, wa+15, ha/2, 0, 0, Math.PI*2); ctx.stroke();
  ctx.restore();
  ctx.save();
  ctx.rotate(-t);
  ctx.beginPath(); ctx.ellipse(0,0, ha/2, wa+15, 0, 0, Math.PI*2); ctx.stroke();
  ctx.restore();
  
  // Hourglass Body
  ctx.fillStyle = '#2d2200';
  ctx.beginPath();
  ctx.moveTo(-wa+4, -ha);
  ctx.lineTo(wa-4, -ha);
  ctx.lineTo(4, 0);
  ctx.lineTo(wa-4, ha);
  ctx.lineTo(-wa+4, ha);
  ctx.lineTo(-4, 0);
  ctx.closePath();
  ctx.fill();
  
  // Glowing Sand
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(-wa+6, -ha+2);
  ctx.lineTo(wa-6, -ha+2);
  ctx.lineTo(0, -2);
  ctx.fill();
  
  ctx.fillStyle = col;
  const sandLevel = ha - (Math.abs(Math.sin(t))*ha*0.8);
  ctx.beginPath();
  ctx.moveTo(0, 2);
  ctx.lineTo(wa-6, ha-2);
  ctx.lineTo(-wa+6, ha-2);
  ctx.fill();
  
  // Sand Particles falling
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.arc(0, Math.sin(t*10)*10, 1, 0, Math.PI*2);
  ctx.fill();

  // Divine Crown
  ctx.fillStyle = '#ffaa00';
  ctx.beginPath();
  ctx.moveTo(-wa, -ha);
  ctx.lineTo(-wa/2, -ha-10);
  ctx.lineTo(0, -ha-4);
  ctx.lineTo(wa/2, -ha-10);
  ctx.lineTo(wa, -ha);
  ctx.fill();

  if(lv>=2){
    ctx.strokeStyle = '#fff';
    ctx.beginPath();
    ctx.arc(0,0, wa+25, 0, Math.PI*2);
    ctx.stroke();
  }
  ctx.restore();
}"""

# APEX
new_apex = """function drawApexChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 35;
  const float = Math.sin(t*3)*5;
  ctx.translate(0, float);
  
  // Magenta Halo / Mandala
  ctx.strokeStyle = col;
  ctx.lineWidth = 2;
  ctx.save();
  ctx.rotate(t*0.5);
  for(let i=0; i<8; i++){
    ctx.beginPath();
    ctx.moveTo(0,0);
    ctx.lineTo(0, -wa-20);
    ctx.stroke();
    ctx.rotate(Math.PI/4);
  }
  ctx.restore();
  
  // Multiple floating arms (golden)
  ctx.strokeStyle = '#ffaa00';
  ctx.lineWidth = 3;
  ctx.lineCap = 'round';
  for(let i=-1; i<=1; i+=2){
    ctx.beginPath();
    ctx.moveTo(i*wa, 0);
    ctx.quadraticCurveTo(i*(wa+15), -ha+Math.sin(t*4)*10, i*(wa+25), -ha);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(i*wa, 0);
    ctx.quadraticCurveTo(i*(wa+15), ha+Math.cos(t*4)*10, i*(wa+20), ha+10);
    ctx.stroke();
  }
  
  // Ultimate Body
  ctx.fillStyle = '#330033';
  ctx.beginPath();
  ctx.moveTo(0, -ha-5);
  ctx.lineTo(wa+5, 0);
  ctx.lineTo(0, ha+5);
  ctx.lineTo(-wa-5, 0);
  ctx.closePath();
  ctx.fill();
  
  // Inner Radiant Core
  ctx.fillStyle = '#fff';
  ctx.shadowColor = '#fff';
  ctx.shadowBlur = 20;
  ctx.beginPath();
  ctx.moveTo(0, -ha+5);
  ctx.lineTo(wa-5, 0);
  ctx.lineTo(0, ha-5);
  ctx.lineTo(-wa+5, 0);
  ctx.closePath();
  ctx.fill();
  
  // Crown Eye
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.arc(0, -ha+5, 3, 0, Math.PI*2);
  ctx.fill();

  if(lv>=2){
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.arc(0,0, wa+30, 0, Math.PI*2);
    ctx.stroke();
  }
  ctx.restore();
}"""

# VOLT
new_volt = """function drawVoltChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = player.dashing ? 40 : 25;
  const shake = player.dashing ? Math.random()*4-2 : 0;
  ctx.translate(shake, 0);
  
  // Static Discharge Particles
  ctx.fillStyle = '#fff';
  for(let i=0; i<3; i++){
    if(Math.random()>0.5){
      ctx.fillRect(-wa + Math.random()*sw, -ha + Math.random()*sh2, 2, 6);
    }
  }
  
  // Lightning Zig-Zag Body
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(-wa/2, -ha);
  ctx.lineTo(wa, -ha);
  ctx.lineTo(0, 0);
  ctx.lineTo(wa/2, 0);
  ctx.lineTo(-wa, ha);
  ctx.lineTo(-wa/4, ha);
  ctx.lineTo(wa/4, ha/2);
  ctx.lineTo(-wa/2, ha/2);
  ctx.closePath();
  ctx.fill();
  
  // Speed Goggles
  ctx.fillStyle = '#1a1a00';
  ctx.beginPath();
  ctx.moveTo(-wa/4, -ha+4);
  ctx.lineTo(wa-4, -ha+4);
  ctx.lineTo(wa-8, -ha+10);
  ctx.lineTo(-wa/4-2, -ha+10);
  ctx.closePath();
  ctx.fill();
  
  // Glowing Eyes
  ctx.fillStyle = '#fff';
  ctx.fillRect(0, -ha+6, 6, 2);

  // Electrical Aura lines
  ctx.strokeStyle = '#fff';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(-wa-5, -ha+Math.random()*10);
  ctx.lineTo(-wa-15, -ha+Math.random()*20);
  ctx.stroke();

  if(lv>=2){
    ctx.fillStyle = '#ffaa00';
    ctx.beginPath();
    ctx.moveTo(0, ha);
    ctx.lineTo(wa, ha+10);
    ctx.lineTo(wa/2, ha+15);
    ctx.fill();
  }
  ctx.restore();
}"""

# SHADOW NINJA
new_shadow = """function drawShadowChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = player.dashing ? 30 : 15;
  
  // Shadow Trail
  ctx.fillStyle = 'rgba(68, 51, 170, 0.3)';
  ctx.beginPath();
  ctx.moveTo(-wa+4, 0);
  ctx.quadraticCurveTo(-wa-20, ha, -wa-5, ha+20);
  ctx.lineTo(0, ha);
  ctx.fill();
  
  // Pure Darkness Silhouette
  ctx.fillStyle = '#110522';
  ctx.beginPath();
  ctx.moveTo(0, -ha-4);
  ctx.lineTo(wa-4, -ha+8);
  ctx.lineTo(wa, ha);
  ctx.lineTo(-wa, ha);
  ctx.lineTo(-wa+4, -ha+8);
  ctx.closePath();
  ctx.fill();
  
  // Glowing Purple Accents (Kunai/Dagger)
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(wa+2, 0);
  ctx.lineTo(wa+15, -10);
  ctx.lineTo(wa+8, 5);
  ctx.fill();
  
  // Assassin Eyes
  ctx.fillStyle = col;
  ctx.beginPath();
  ctx.moveTo(-wa+6, -ha+10);
  ctx.lineTo(0, -ha+14);
  ctx.lineTo(-wa+6, -ha+12);
  ctx.fill();
  ctx.beginPath();
  ctx.moveTo(wa-6, -ha+10);
  ctx.lineTo(0, -ha+14);
  ctx.lineTo(wa-6, -ha+12);
  ctx.fill();
  
  // Ethereal Smoke
  ctx.fillStyle = 'rgba(136, 68, 255, 0.5)';
  ctx.beginPath();
  ctx.arc(wa, -ha, 3, 0, Math.PI*2);
  ctx.arc(-wa, ha, 4, 0, Math.PI*2);
  ctx.fill();

  if(lv>=2){
    ctx.strokeStyle = col;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(-wa-10, 0);
    ctx.lineTo(-wa-25, 10);
    ctx.stroke();
  }
  ctx.restore();
}"""

# BLAZE
new_blaze = """function drawBlazeChar(ctx,col,ch,sw,sh2,player,t,lv=0){
  const ha=sh2/2, wa=sw/2;
  ctx.save();
  ctx.shadowColor = ch.glow;
  ctx.shadowBlur = 30;
  
  // Molten Aura
  const pulse = Math.sin(t*6)*5;
  ctx.fillStyle = 'rgba(255, 68, 0, 0.4)';
  ctx.beginPath();
  ctx.arc(0, 0, wa+10+pulse, 0, Math.PI*2);
  ctx.fill();
  
  // Heavy Obsidian Rock Body
  ctx.fillStyle = '#221111';
  ctx.beginPath();
  ctx.moveTo(-wa-10, -ha+10);
  ctx.lineTo(wa+10, -ha+10);
  ctx.lineTo(wa+4, ha);
  ctx.lineTo(-wa-4, ha);
  ctx.closePath();
  ctx.fill();
  
  // Lava Veins
  ctx.strokeStyle = col;
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(-wa, -ha+10);
  ctx.lineTo(-wa/2, 0);
  ctx.lineTo(0, -ha+20);
  ctx.lineTo(wa/2, 0);
  ctx.lineTo(wa, -ha+10);
  ctx.stroke();
  
  // Burning Shoulders
  ctx.fillStyle = '#ffaa00';
  ctx.beginPath();
  ctx.moveTo(-wa-12, -ha+10);
  ctx.lineTo(-wa-6, -ha-4);
  ctx.lineTo(-wa, -ha+10);
  ctx.fill();
  ctx.beginPath();
  ctx.moveTo(wa+12, -ha+10);
  ctx.lineTo(wa+6, -ha-4);
  ctx.lineTo(wa, -ha+10);
  ctx.fill();
  
  // Fiery Eyes
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.moveTo(-4, -ha+12);
  ctx.lineTo(0, -ha+16);
  ctx.lineTo(4, -ha+12);
  ctx.fill();

  if(lv>=2){
    ctx.fillStyle = col;
    ctx.beginPath();
    ctx.arc(0, -ha-10, 6, 0, Math.PI*2);
    ctx.fill();
  }
  ctx.restore();
}"""

replace_func('drawChronoChar', new_chrono)
replace_func('drawApexChar', new_apex)
replace_func('drawVoltChar', new_volt)
replace_func('drawShadowChar', new_shadow)
replace_func('drawBlazeChar', new_blaze)

with open('index.html', 'w') as f:
    f.write(content)
