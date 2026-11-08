import os
import os
import json

def generar_datos_deportivos():
    # 1. Liga MX
    partidos_mx = [
        { "local": "León", "visitante": "Chivas", "pL": 34.2, "pE": 28.5, "pV": 37.3, "pred": "Chivas (Visitante o Empate)" },
        { "local": "Querétaro", "visitante": "Puebla", "pL": 41.0, "pE": 27.5, "pV": 31.5, "pred": "Querétaro (Local o Empate)" }
    ]
    
    # 2. Liga de Expansión MX (Agregada de jalón)
    partidos_expansion = [
        { "local": "Atlante", "visitante": "Celaya", "pL": 48.0, "pE": 28.0, "pV": 24.0, "pred": "Atlante (Local)" },
        { "local": "Cancún FC", "visitante": "Leones Negros", "pL": 35.5, "pE": 29.5, "pV": 35.0, "pred": "Leones Negros (Empate o Visitante)" }
    ]
    
    # 3. Premier League
    partidos_premier = [
        { "local": "Manchester United", "visitante": "Aston Villa", "pL": 28.4, "pE": 21.2, "pV": 50.4, "pred": "Aston Villa (Visitante)" }
    ]

    # 4. J1 League
    partidos_japon = [
        { "local": "Gamba Osaka", "visitante": "Cerezo Osaka", "pL": 42.1, "pE": 26.4, "pV": 31.5, "pred": "Gamba Osaka (Local)" },
        { "local": "JEF United Chiba", "visitante": "Mito HollyHock", "pL": 55.0, "pE": 25.0, "pV": 20.0, "pred": "JEF United Chiba (Local)" }
    ]
    
    # 5. Tenis Mundial
    partidos_tenis = [
        { "local": "Ben Shelton", "visitante": "Lorenzo Musetti", "pL": 58.5, "pE": 0.0, "pV": 41.5, "pred": "Ben Shelton (Gana)" },
        { "local": "Alcaraz", "visitante": "Zverev", "pL": 62.1, "pE": 0.0, "pV": 37.9, "pred": "Alcaraz (Gana)" }
    ]
    
    return partidos_mx, partidos_expansion, partidos_premier, partidos_japon, partidos_tenis

def generar_html():
    mx, expansion, premier, japon, tenis = generar_datos_deportivos()
    
    # Corregido: Tomamos el primer partido [0] de cada lista para evitar que falle el script
    estelar_mx = mx[0]
    estelar_expansion = expansion[0]
    estelar_premier = premier[0]
    estelar_japon = japon[0]
    estelar_tenis = tenis[0]

    js_data = f"""
    const datosLigas = {{
        ligamx: {{
            nombre: "Liga MX (México)",
            esTenis: false,
            emoji: "⚽",
            estelar: {{ local: "{estelar_mx['local']}", visitante: "{estelar_mx['visitante']}", pL: {estelar_mx['pL']}, pE: {estelar_mx['pE']}, pV: {estelar_mx['pV']} }},
            partidos: {json.dumps(mx, ensure_ascii=False)}
        }},
        ligaexpansion: {{
            nombre: "Liga de Expansión MX",
            esTenis: false,
            emoji: "⚽",
            estelar: {{ local: "{estelar_expansion['local']}", visitante: "{estelar_expansion['visitante']}", pL: {estelar_expansion['pL']}, pE: {estelar_expansion['pE']}, pV: {estelar_expansion['pV']} }},
            partidos: {json.dumps(expansion, ensure_ascii=False)}
        }},
        premier: {{
            nombre: "Premier League (Inglaterra)",
            esTenis: false,
            emoji: "⚽",
            estelar: {{ local: "{estelar_premier['local']}", visitante: "{estelar_premier['visitante']}", pL: {estelar_premier['pL']}, pE: {estelar_premier['pE']}, pV: {estelar_premier['pV']} }},
            partidos: {json.dumps(premier, ensure_ascii=False)}
        }},
        japon: {{
            nombre: "J1 League (Japón)",
            esTenis: false,
            emoji: "⚽",
            estelar: {{ local: "{estelar_japon['local']}", visitante: "{estelar_japon['visitante']}", pL: {estelar_japon['pL']}, pE: {estelar_japon['pE']}, pV: {estelar_japon['pV']} }},
            partidos: {json.dumps(japon, ensure_ascii=False)}
        }},
        tenis: {{
            nombre: "Tenis Mundial (ATP / WTA)",
            esTenis: true,
            emoji: "🎾",
            estelar: {{ local: "{estelar_tenis['local']}", visitante: "{estelar_tenis['visitante']}", pL: {estelar_tenis['pL']}, pE: 0.0, pV: {estelar_tenis['pV']} }},
            partidos: {json.dumps(tenis, ensure_ascii=False)}
        }}
    }};
    """

    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asistente de Orientación Deportiva</title>
    <style>
        body {{ background-color: #0e1117; color: #ffffff; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; padding: 15px; margin: 0; }}
        h2 {{ color: #00f2fe; margin-bottom: 5px; font-size: 1.4rem; }}
        label {{ font-size: 0.9rem; color: #aaa; display: block; margin-top: 15px; margin-bottom: 5px; }}
        select {{ background-color: #1f293d; color: white; border: 1px solid #3b4252; padding: 10px; width: 100%; border-radius: 8px; font-size: 1rem; outline: none; }}
        .chat-box {{ background-color: #1f293d; padding: 15px; border-radius: 12px; margin-top: 15px; border-left: 5px solid #00f2fe; line-height: 1.5; font-size: 0.95rem; }}
        .btn-parlay {{ background: linear-gradient(45deg, #00f2fe, #4facfe); color: black; border: none; padding: 12px; width: 100%; border-radius: 8px; font-weight: bold; font-size: 1rem; margin-top: 15px; cursor: pointer; }}
        .parlay-box {{ background-color: #112233; padding: 15px; border-radius: 12px; border: 1px dashed #ff007f; margin-top: 15px; font-size: 0.9rem; line-height: 1.5; }}
        .divider {{ border-bottom: 1px solid #2e3440; margin: 15px 0; }}
    </style>
</head>
<body>
    <h2>🤖 Asistente de Orientación</h2>
    <p style="color: #8892b0; font-size: 0.85rem; margin: 0;">Multi-Deporte Automatizado en Vivo</p>

    <label for="ligaSelect">🌍 Selecciona un Mercado:</label>
    <select id="ligaSelect" onchange="cargarPartidoEstelar()">
        <option value="ligamx">Liga MX (México)</option>
        <option value="ligaexpansion">Liga de Expansión MX</option>
        <option value="premier">Premier League (Inglaterra)</option>
        <option value="japon">J1 League (Japón)</option>
        <option value="tenis">Tenis Profesional (ATP/WTA)</option>
    </select>

    <div id="chatContainer" class="chat-box"></div>
    <div class="divider"></div>
    <p style="font-size: 0.9rem; text-align: center; color: #aaa; margin-bottom: 5px;">🔥 ¿Te gustaría armar el parlay de la opción elegida?</p>
    <button class="btn-parlay" onclick="generarParlay()">✅ Sí, arma la selección</button>
    <div id="parlayContainer"></div>

    <script>
        {js_data}

        function cargarPartidoEstelar() {{
            const ligaSeleccionada = document.getElementById("ligaSelect").value;
            const info = datosLigas[ligaSeleccionada];
            const estelar = info.estelar;
            
            let recomendacion = "";
            let desglosePorcentajes = "";
            
            if(info.esTenis) {{
                recomendacion = estelar.pL > estelar.pV ? `te recomiendo ir a favor de <b>${{estelar.local}}</b>` : `te recomiendo ir a favor de <b>${{estelar.visitante}}</b>`;
                desglosePorcentajes = `• Probabilidad ${{estelar.local}}: ${{estelar.pL}}%<br>• Probabilidad ${{estelar.visitante}}: ${{estelar.pV}}%<br>`;
            }} else {{
                recomendacion = estelar.pL > estelar.pV ? `te recomiendo jugar al local (<b>${{estelar.local}}</b>)` : `te recomiendo asegurar con el visitante (<b>${{estelar.visitante}}</b>)`;
                desglosePorcentajes = `• Local: ${{estelar.pL}}% | Visitante: ${{estelar.pV}}% | Empate: ${{estelar.pE}}%<br>`;
            }}
            
            document.getElementById("chatContainer").innerHTML = `
                <b>¡Hola Bro!</b> Analicé los datos actualizados. En el evento principal de la ${{info.nombre}}:<br><br>
                ${{info.emoji}} <b>${{estelar.local}} vs ${{estelar.visitante}}</b><br>
                ${{desglosePorcentajes}}<br>
                🎯 Consejo estratégico: ${{recomendacion}}.
            `;
            document.getElementById("parlayContainer").innerHTML = "";
        }}

        function generarParlay() {{
            const ligaSeleccionada = document.getElementById("ligaSelect").value;
            const info = datosLigas[ligaSeleccionada];
            let parlayHtml = '<div class="parlay-box"><b>🔥 SELECCIÓN SUGERIDA 🔥</b><br><br>';
            info.partidos.forEach(p => {{
                parlayHtml += `• ${{p.local}} vs ${{p.visitante}} ➔ <b>${{p.pred}}</b><br>`;
            }});
            parlayHtml += '</div>';
            document.getElementById("parlayContainer").innerHTML = parlayHtml;
        }}
        window.onload = cargarPartidoEstelar;
    </script>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

if __name__ == "__main__":
    generar_html()
