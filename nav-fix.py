import os
import re

pages = [
    'index.html',
    'services-managed-foundation.html',
    'services-process-intelligence.html',
    'services-strategic-intelligence.html',
    'academy.html',
    'community.html'
]

# CSS to inject before </style>
mobile_css = """
    .hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:4px;border:none;background:transparent;}
    .hamburger span{display:block;width:22px;height:2px;background:var(--t2);border-radius:2px;transition:all .2s;}
    .hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg);}
    .hamburger.open span:nth-child(2){opacity:0;}
    .hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg);}
    @media(max-width:680px){
      .hamburger{display:flex;}
      .snl{display:none;flex-direction:column;gap:0;position:absolute;top:48px;left:0;right:0;background:#FFFFFF;border-bottom:0.5px solid var(--b1);z-index:100;padding:8px 0;}
      .snl.open{display:flex;}
      .snl a{padding:10px 24px;font-size:14px;border-bottom:0.5px solid var(--b1);}
      .snl li:last-child a{border-bottom:none;}
      .sncta{display:none;}
      .sn{position:relative;}
    }"""

# JS to inject before </body>
mobile_js = """<script>
  document.querySelector('.hamburger').addEventListener('click',function(){
    this.classList.toggle('open');
    document.querySelector('.snl').classList.toggle('open');
  });
</script>"""

# Hamburger HTML to inject after <ul class="snl"...></ul> block
hamburger_html = '\n      <button class="hamburger" aria-label="Toggle menu"><span></span><span></span><span></span></button>'

for page in pages:
    path = f'/home/claude/merlyn-site/{page}'
    with open(path, 'r') as f:
        html = f.read()
    
    # Inject mobile CSS before </style>
    html = html.replace('  </style>', mobile_css + '\n  </style>', 1)
    
    # Inject hamburger button after the closing </ul> inside nav
    html = html.replace('      <a href="mailto:hello@merlynailabs.com" class="sncta">Get started</a>\n    </div>\n  </nav>', 
                        '      <a href="mailto:hello@merlynailabs.com" class="sncta">Get started</a>' + hamburger_html + '\n    </div>\n  </nav>', 1)
    
    # Inject JS before </body>
    html = html.replace('</body>', mobile_js + '\n</body>', 1)
    
    with open(path, 'w') as f:
        f.write(html)
    print(f'Updated {page}')

